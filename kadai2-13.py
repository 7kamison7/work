#13 
# 絶対ファイルパスを取得する
import os

print('getcwd:      ', os.getcwd())

print('abspath:     ', os.path.abspath(__file__))
print('abs dirname: ', os.path.dirname(os.path.abspath(__file__)))