import numpy as np
import matplotlib.pyplot as plt

# x 값의 범위 설정
x = np.linspace(-2, 2, 500)  # -2부터 2까지 500개의 점

# 함수 정의
f_x = np.exp(x)  # f(x) = e^x
g_x = np.exp(x) - 1 - x  # g(x) = e^x - 1 - x

# 그래프 그리기
plt.figure(figsize=(8, 6))
plt.plot(x, f_x, label=r"$f(x) = e^x$", color="blue")
plt.plot(x, g_x, label=r"$g(x) = e^x - 1 - x$", color="orange")

# 그래프 설정
plt.axhline(0, color='black', linewidth=0.8, linestyle="--")
plt.axvline(0, color='black', linewidth=0.8, linestyle="--")
plt.title("Graphs of $f(x)$ and $g(x)$")
plt.xlabel("$x$")
plt.ylabel("$y$")
plt.legend()
plt.grid(True)

# 그래프 출력
plt.show()
