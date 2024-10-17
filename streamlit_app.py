import streamlit as st
import math

def solve_quadratic_equation(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return f"二つの実数解: x1 = {x1:.2f}, x2 = {x2:.2f}"
    elif discriminant == 0:
        x = -b / (2*a)
        return f"重解: x = {x:.2f}"
    else:
        real = -b / (2*a)
        imag = math.sqrt(-discriminant) / (2*a)
        return f"二つの複素数解: x1 = {real:.2f} + {imag:.2f}i, x2 = {real:.2f} - {imag:.2f}i"

st.title('二次方程式ソルバー')
st.write('ax² + bx + c = 0 の形の二次方程式を解きます。')

a = st.number_input('a の値を入力してください:', value=1.0)
b = st.number_input('b の値を入力してください:', value=0.0)
c = st.number_input('c の値を入力してください:', value=0.0)

if st.button('解を計算'):
    if a == 0:
        st.error('aは0以外の値を入力してください。')
    else:
        result = solve_quadratic_equation(a, b, c)
        st.success(result)