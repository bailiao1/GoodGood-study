# 安装ray
# pip install -U "ray[default]"

# 最小可运行模板
import ray 

ray.init()

@ray.remote
def square(x):
  return x * x

ref = square.remote(10)
result = ray.get(ref)

print(x)    # 100

# 对应关系
# suqare(10)            # 普通同步调用
# squaare.remote(10)    # 提交给 Ray worker 算
# ray.get(ref)          # 等结果回来

# 并行跑多个任务（开始像多进程）
import ray
import time

ray.init()
@ray.remote
def work(x):
    time.sleep(1)
    return x * x

refs = []

for i in range(10):      # 如果是普通循环10个任务每个sleep 1 秒, 大约10秒。
    refs.append(work.remote(i))    # 用Ray后，它会并行调度到多个worker，实际耗时接近：任务数/可用cpu核心数
    
result = ray.get(refs)    # 可以接收单个object ref ，也可以接收一组refs；如果对象不在本地object store，Ray 会把它传回来
print(result)    # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


# ticker 分发
import ray
import time

ray.init()

@ray.remote
def calc_one_ticker(ticker):
  # 模拟计算
  time.sleep(1)

  return {"ticker": ticker,
          "status": "ok",
          "store": len(ticker)}

tickers = {"A", "B", "C"}
refs = []
for ticker in tickers:
  refs.append(calc_one_ticker.remote(ticker))

rows = ray.get(refs)
for row in rows::
  print(row)


# chunk 版本（减少碎任务频繁通信）
# tickers
#   → 切成 chunks
#   → 每个 chunk 交给一个 worker
#   → 每个 worker 返回 list[dict]
#   → 主程序合并
# ray.init()

def chunk_list(xs,size):
  return [xs[i:i + size] for i in range(0, len(xs), size)]

@ray.remote
def calc_ticker_chunk(tickers):
    rows = []

    for ticker in tickers:
        # 模拟单 ticker 计算
        time.sleep(0.2)

        rows.append({
            "ticker": ticker,
            "status": "ok",
            "score": len(ticker),
        })

    return rows

tickers = [
    "A", "B", "C", "D", "E",
    "F", "G", "H", "I", "J",
]

chunks = chunk_list(tickers, size=3)

refs = []

for chunk in chunks:
    refs.append(calc_ticker_chunk.remote(chunk))

nested_rows = ray.get(refs)

rows = []
for part in nested_rows:
    rows.extend(part)

for row in rows:
    print(row)


# 错误保护
# worker 内部捕获异常
# 不要让单个 ticker 炸掉全局
# 主程序最后检查 ok / error

ray.init()
@ray.remote
def calc_one_ticker(ticker):
    try:
        if ticker == "BAD":
            raise ValueError("mock error")

        time.sleep(0.5)

        return {
            "ticker": ticker,
            "ok": True,
            "score": len(ticker),
            "error": "",
        }

    except Exception as e:
        return {
            "ticker": ticker,
            "ok": False,
            "score": None,
            "error": repr(e),
        }

tickers = ["A", "B", "C", "D"]

refs = [calc_one_ticker.remote(t) for t in tickers]
rows = ray.get(refs)

for row in rows:
    print(row)

# 限制每个任务占几个 CPU
# 如一个任务比较重，希望每个任务占 2 个 CPU
ray.init()
@ray.remote(num_cpus=2)    # num_cpus 是 Ray 的资源调度参数；任务只有在集群有足够 CPU 资源时才会被调度。
def heavy_work(x):
    time.sleep(1)
    return x * x

refs = [heavy_work.remote(i) for i in range(10)]
results = ray.get(refs)

print(results)


# 从单机切到多机器
# 这个模板可以看出任务到底跑在哪台机器上

# 多机器启动方式：
# 假设 head 机器 (调度本机) IP 是 192.168.1.10
# head 机器运行：ray start --head --port=6379 --daashboard=0.0.0.0

# worker node 用 ray start --address=<head-node-address:port> 加入 head。
# worker 机器（计算节点）运行: ray start --address=192.168.1.10:6379

# 然后在head机器运行python: python ray_test.py  
# python 里 ray.init(address="auto")

import ray
import socket
import time

ray.init(address="auto")

@ray.remote
def work(x):
  time.sleep(1)

  return {
    "x" : x,
    "result": x * x,
    "machine": socket.gethostname(),
  }

refs = [work.remote(i) for i in range(20)]
rows = ray.get(refs)

for row in rows:
  print(row)

# {'x': 0, 'result': 0, 'machine': 'PC-1'}
# {'x': 1, 'result': 1, 'machine': 'PC-2'}
# {'x': 2, 'result': 4, 'machine': 'linux-box'} ...
