#12 
# 環境変数にアクセスするためのプログラムを作成(osライブラリを使用)
import os
import subprocess

print(os.environ.get('LANG'))

print(os.environ.get('NEW_KEY'))

print(os.environ.get('NEW_KEY', 'default'))

os.environ['NEW_KEY'] = 'test'
print(os.environ['NEW_KEY'])

os.environ['NEW_KEY'] = '100'
print(os.environ['NEW_KEY'])