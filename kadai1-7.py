#(7) ユーザーに名前と年齢の入力を求めるプログラムを作成します．彼らが 100 歳になる年を告げるメッセージを表示してください．
print('名前を入力してください')
name = input()
print('年齢を入力してください')
age =int(input())

message=100-age
print('%d年後に100才になります。'%message)
