#14
# Pythonで指定されたパスからファイル名を抽出
import os

filepath = './dir/subdir/filename.ext'

print(os.path.basename(filepath))