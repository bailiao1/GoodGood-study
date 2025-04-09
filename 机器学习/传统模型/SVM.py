import numpy as np

class SVM:
    def __init__(self,C=1.0, tol=1e-3, max_iter=100):
        self.C = C
        self.tol = tol
        self.max_iter = max_iter

    def fit(self,X,y):
        m,n = X.shape
        self.alpha = np.zeros(m)
        self.b = 0
        self.w = np.zeros(n)
        self.X = X
        self.y = y
        self.K = X @ X.T

        iter_count = 0
        while iter_count < self.max_iter:
            alpha_prev = np.copy(self.alpha)
            for i in range(m):
                Ei = self._decision_function(X[i])-y[i]
                if (y[i] * Ei < -self.tol and self.alpha[i]<self.C) or (y[i] *Ei > self.tol and self.alpha[i] > 0):
                    j = self._select_second_alpha(i,m)
                    Ej = self._decision_function(X[j])-y[j]

                    alpha_i_old,alpha_j_old = self.alpha[i],self.alpha[j]

                    if y[i] != y[j]:
                        L = max(0,alpha_j_old - alpha_i_old)
                        H = min(self.C,self.C + alpha_j_old - alpha_i_old)
                    else:
                        L = max(0,alpha_i_old + alpha_j_old - self.C)
                        H = min(self.C,alpha_i_old,alpha_j_old)
                    if L == H:
                        continue

                    eta = 2.0 * self.K[i,j] - self.K[i,j] - self.K[j,i]
                    if eta >= 0:
                        continue

                    self.alpha[j] -= (y[j]*(Ei - Ej)) .eta
                    self.alpha[j] = np.clip(self.alpha[j],L,H)

                    if abs(self.alpha[j] - alpha_j_old) < 1e-5:
                        continue

                    self.alpha[i] += y[i] * y[j] * (alpha_j_old - self.alpha[j])

                    b1 = self.b - Ei - y[i] * (self.alpha[i] - alpha_i_old) * self.K[i,i] - y[j] * (self.alpha[j] - alpha_j_old) * self.K[i,j]
                    b2 = self.b - Ej - y[i] * (self.alpha[i] - alpha_i_old) * self.K[i,j] - y[j] * (self.alpha[j] - alpha_j_old) * self.K[j,j]
                    if 0 < self.alpha[i] < self.C:
                        self.b = b1
                    elif 0 < self.alpha[j] < self.C:
                        self.b = b2
                    else:
                        self.b = (b1 + b2)/2.0

            iter_count += 1

            if np.linalg.norm(self.alpha - alpha_prev) < self.tol:
                break

        self.w = (self.alpha * y) @ X

    def predict(self,X):
        return np.sign(self._decision_function(X))

    def _decision_function(self,X):
        return X @ self.w + self.b

    def _select_second_alpha(self, i, m):
        j = i  # 初始化 j 为 i，以确保 while 循环至少执行一次
        while j == i:  # 不停地随机选取，直到 j 与 i 不同
            j = np.random.randint(0, m)
        return j

