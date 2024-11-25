import sympy as sym

# 로피탈 정리 함수
def LHospital_rule(func_f, func_g, val_a):
    import sympy as sym
    x = sym.Symbol('x')
    
    lim_f = sym.limit(func_f, x, val_a)
    lim_g = sym.limit(func_g, x, val_a)
    
    cond_f = (lim_f == 0) | (lim_f == sym.oo)
    cond_g = (lim_g == 0) | (lim_g == sym.oo)
    # 로피탈 정리의 조건을 만족할 경우 계산
    if cond_f & cond_g == True:
        diff_f = sym.diff(func_f,x)
        diff_g = sym.diff(func_g,x)
        LHospital_value = sym.limit(diff_f/diff_g, x, val_a)
        return LHospital_value
    # 로피탈 정리의 조건을 만족하지 않을 경우 사용할 수 없다는 문구를 결과로 출력
    else:
        output_txt = "It doesn't work"
        return output_txt

# 문제 (a)
# 함수 f(x), g(x) 정의
x = sym.Symbol('x')
f = x-3
g = x**2-9
x_val = 3
print("문제 (a)")
print("극한값 = ", LHospital_rule(f,g,x_val))
print("\n")

# 문제 (b)
# 함수 f(x), g(x) 정의
x = sym.Symbol('x')
f = sym.exp(x)+sym.exp(-x)-2
g = sym.exp(x)-x-1
x_val = 0
print("문제 (b)")
print("극한값 = ", LHospital_rule(f,g,x_val))
print("\n")

# 문제 (c)
# 함수 f(x), g(x) 정의
x = sym.Symbol('x')
f = 1-sym.cos(x)
g = sym.sin(x)
x_val = sym.pi
print("문제 (c)")
print("극한값 = ", LHospital_rule(f,g,x_val))
print("\n")

# 문제 (d)
# 함수 f(x), g(x) 정의
x = sym.Symbol('x')
f = 3*x
g = sym.sqrt(x**2+10)
x_val = sym.oo
print("문제 (d)")
print("극한값 = ", LHospital_rule(f,g,x_val))