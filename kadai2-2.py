#2
# 2つの日付間の日数を計算(注：この関数を使うと便利 ​datetime.date（年、月、日）​
import datetime
int(input())
#yymmdd方式で分けて書くabcdefの変数を用いる
a = datetime.date(2015, 4, 1)
b = datetime.date(2016, 1, 25)
print(str((b-a).days)+'日')