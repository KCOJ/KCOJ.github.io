import os
import sys
from os.path import isdir, isfile
from base64 import b64encode


# 產生 instance 的 key
if not isdir(sys.path[0] + '/instance'):
    os.mkdir(sys.path[0] + '/instance')
if not isfile(sys.path[0] + '/instance/config.py'):
    with open(sys.path[0] + '/instance/config.py', 'w') as f:
        f.write('SECRET_KEY = \'{SECRET_KEY}\''.format(
            SECRET_KEY=b64encode(os.urandom(32)).decode('utf-8')))

# 初始化資料庫
from KCOJ.models.user import User
User.create_table()

# 開啟伺服器
from KCOJ import app
if __name__ == '__main__':
    SERVER_PORT = int(os.environ.get('SERVER_PORT') or 5000)
    app.run(port=SERVER_PORT, threaded=True)
