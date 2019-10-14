#11 
# Pythonのstdlibライブラリを使用してローカルIPアドレスを見つける

import socket
# ホスト名を取得、表示
host = socket.gethostname()
print(host)

# ipアドレスを取得、表示
ip = socket.gethostbyname(host)
print(ip)