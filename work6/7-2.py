import sympy as sym
import matplotlib.pyplot as plt
import numpy as np

# 접선의 방정식을 구하는 함수
def cal_tangent_line(func_f, x_val):
    import sympy as sym
    x = sym.Symbol('x')
    diff_func_f = func_f.diff()
    y_val = func_f.subs({x:x_val})
    x_tangent = diff_func_f.subs({x:x_val})
    tangent_line_f = x_tangent*(x - x_val) + y_val
    return tangent_line_f

# 문제 (a)
# 함수 f(x) 정의
x = sym.Symbol('x')
f = x**3-x**2+x+2
a_val = -3
tan_line_f = cal_tangent_line(f, a_val)
print("문제 (a)")
print("접선의 방정식 = ", tan_line_f)

# 문제 (a)의 그래프 그리기
x = sym.Symbol('x')
my_f_func = sym.lambdify(x, f, "numpy")
my_tan_line_f_func = sym.lambdify(x, tan_line_f, "numpy")

# 함수에 입력되는 x 값의 범위
x = np.arange(-5, 5, 0.1)
tan_x = np.arange(-4.5, -1, 0.1)

# 축 레이블 넣기
plt.xlabel('x axis')
plt.ylabel('y axis')

# 그리드
plt.grid(color = "black", alpha=0.5, linestyle='--')

# 그리고자 하는 식
plt.plot(x, my_f_func(x), label='$x^3-x^2+x+2$')
plt.plot(tan_x, my_tan_line_f_func(tan_x), label='$34x+65$')
# 범례
plt.legend()
plt.show()

# 문제 (b)
# 함수 f(x) 정의
x = sym.Symbol('x')
f = sym.exp(x)*sym.cos(x)+sym.sin(x)
a_val = 0
tan_line_f = cal_tangent_line(f, a_val)
print("문제 (b)")
print("접선의 방정식 = ", tan_line_f)

# 문제 (b)의 그래프 그리기
x = sym.Symbol('x')
my_f_func = sym.lambdify(x, f, "numpy")
my_tan_line_f_func = sym.lambdify(x, tan_line_f, "numpy")

# 함수에 입력되는 x 값의 범위
x = np.arange(-2, 2, 0.1)
tan_x = np.arange(-1, 1, 0.1)

# 축 레이블 넣기
plt.xlabel('x axis')
plt.ylabel('y axis')

# 그리드
plt.grid(color = "black", alpha=0.5, linestyle='--')

# 그리고자 하는 식
plt.plot(x, my_f_func(x), label='$e^x cos x+sin x$')
plt.plot(tan_x, my_tan_line_f_func(tan_x), label='$2x+1$')

# 범례
plt.legend()
plt.show()