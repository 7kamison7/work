#15 
# 現在のディレクトリのファイル

import os

print('getcwd:      ', os.getcwd())
print('__file__:    ', __file__)

print('basename:    ', os.path.basename(__file__))