# model = DecisionTreeClassifier(depth=5)                          # 决策树  depth(树的深度)
import numpy as np

# 计算基尼指数
def gini_index(groups, classes):                                        # 定义方法
    n_samples = sum([len(group) for group in groups])                   # 计算样本总数
    gini = 0.0                                                          # 初始化基尼指数
    for group in groups:                                                # 设置迭代器,处理各group
        size = len(group)                                               # 计算各组长度
        if size == 0:                                                   # 如果为0，直接跳过，防止除零报错
            continue
        score = 0.0                                                               # 初始化score
        for class_val in classes:                                                 # 设置迭代器,迭代各类别标签
            proportion = [row[-1] for row in group].count(class_val) / size       # count计算当前类别在 group 中的占比
            score += proportion ** 2                                              # 计算该类别的纯度贡献，并累加到 score
        gini += (1 - score) * (size / n_samples)                                  # 计算该 group 对整体基尼指数的贡献，并累加
    return gini                                                                   # 返回最终基尼指数

# 示例数据
dataset = [[1, 'A'], [2, 'A'], [3, 'B'], [4, 'B']]

# 寻找最佳分裂点
def best_split(dataset):
    best_feature, best_value, best_score, best_groups = None, None, float('inf'), None      # best_score设置为无限大
    classes = list(set(row[-1] for row in dataset))         # 提取数据集(dataset)中所有类别标签，使用 set 去重，得到唯一类别列表

    for feature in range(len(dataset[0]) - 1):              # 遍历每个特征,次数-1略过标签列
        for row in dataset:                                 # 外循环，遍历数据集中的每一行 row，尝试用 row[feature] 作为分裂点
            left, right = [], []                            # 初始化left, right
            for r in dataset:                               # 内循环，遍历数据集
                if r[feature] < row[feature]:               # 轮流与row[feature]进行对比
                    left.append(r)                                  # 分类
                else:
                    right.append(r)                                 # 分类
            gini = gini_index([left, right], classes)        # 计算gini指数
            if gini < best_score:                                   # 指数越低越纯，如果更纯，进行优化
                best_feature, best_value, best_score, best_groups = feature, row[feature], gini, (left, right)

    return {'feature': best_feature, 'value': best_value, 'groups': best_groups}       # 返回最终分类

# 递归构建决策树
def build_tree(dataset, max_depth, depth=0):                        # 定义决策树类
    node = best_split(dataset)                                      # 导入best_split
    left, right = node['groups']                                    # 使用best_split分割数据集
    del node['groups']                                              # 删除残留数据

    if depth >= max_depth or len(left) == 0 or len(right) == 0:                             # 终止递归条件
        node['left'] = node['right'] = max(set(row[-1] for row in left + right),
                                           key=[row[-1] for row in left + right].count)
        return node

    node['left'] = build_tree(left, max_depth, depth + 1)                       # 递归左
    node['right'] = build_tree(right, max_depth, depth + 1)                     # 递归右

    return node                                                                 # 返回值

# 示例数据
dataset = [[2.5, 'A'], [1.5, 'A'], [3.5, 'B'], [4.5, 'B']]

# 训练决策树
tree = build_tree(dataset, max_depth=2)
print(tree)


# 随机森林 RandomForestClassifier(n_estimators=100)
# n_estimators(树的数量)
# XGBoot  XGBClassifier(n_estimators=200,learning_rate=0.03,depth=5,random=42)
# learning_rate(学习率),random(随机种子)
