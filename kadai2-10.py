#10​
# 数値が1000または2000の100以内であるかどうかをテストするPythonプログラム作成
n = int(input('数字：'))


if (900 <= n <= 1100) or (1900 <= n <= 2100 ):
    print('OK')
else:
    print('NO')