import numpy as np
#変数の数の入力
variable_n = int(input())
#loop数と刻み幅
loops = 1000
dt = 0.1
#変数の生成
x = np.zeros((variable_n, loops))
#式の入力
expressions = [input() for _ in range(variable_n)]
#式の解釈と定義
def_func = 'def func:\n return np.array(['
for (i, expr) in enumerate(expressions):
    if i==variable_n-1:
        expressions += expr + '])'
    else:
        expressions += expr + ','
exec(def_func)

#式の実行
for i in range(variable_n):
    exec('x'+str(i)+'=func'+str(i)+'()')
    #exec('print(\'x\'+str(i))')
    print(eval('x'+str(i)))
