import socket
import time
import json
import datetime

def broadcastMessage(tablename=None, action=None, PK=None):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    PORT = 1060
    network = '<broadcast>'
    act = {
        'confirmation': '确认',
        'Submit': '提交',
        'edit': '修改',
        'new': '新增',
        'delete': '删除'
    }
    tn = {
        't_order': '订单表',
        'sysusers': '用户表',
        't_receivables': '收款表',
        't_customer': '客户表',
        't_quotation': '报价单表'
    }
    curtime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    curtab = tn[tablename]
    curact = act[action]
    curpk = PK
    curuser = "doighsdfg"
    txt = f'{curtime}:用户[{curuser}]操作,[{curtab}]有新的记录被用户[{curact}],编号为[{curpk}]'
    msg = json.dumps((tablename, txt))
    s.sendto(msg.encode('utf-8'), (network, PORT))
    s.close()

if __name__ == "__main__":
    for i in range(1000):
        print(i)
        broadcastMessage(tablename='t_receivables',action='edit',PK='9087350892234')
        time.sleep(5)