import os
import time
from utiles_firebese import firebase_conect
from utiles_firebese import firebase_read
from utiles_firebese import firebase_post
private_addr_list=["192.168.11","192.168.1"]
def pingGetmacAll(flag_print=True):
    """ 
    ローカルネット内にいるすべてのデバイスのMAC Addressを返す
    --
    input:flag_print=True
    output:mac_list
    --
    ローカルネットのすべてのipアドレスが存在するかpingして、arpでMAC Addressの取得をする

    """
    st=os.popen("ipconfig getifaddr en0")
    addr=st.read()
    private_addr=".".join(addr.split(".")[:3])#"192.168.11."
    mac_list=[]
    for i in range(0,255):
        stream = os.popen('ping -c 1 -W 10 {}.{}'.format(private_addr,i))
        stream = os.popen('arp {}.{}'.format(private_addr,i))
        output = stream.read()
        if "at" in output and not("(incomplete)" in output.split("at")[1]):#"Found"
            mac_list.append(output.split("at")[1].split(" ")[1])
            if flag_print:
                print("ip:{}{}/mac:{}".format(private_addr,i,output.split("at")[1].split(" ")[1]))

    return mac_list
def check_user(user_list={"user":["Allice","Bob","Char"],"mac":['3X:XX:XX:XX:XX:XX','23:XX:XX:XX:XX:XX','35:XX:XX:XX:XX:XX']},exit_mac_list=['51:XX:XX:XX:XX:XX','11:XX:XX:XX:XX:XX','12:XX:XX:XX:XX:XX','23:XX:XX:XX:XX:XX']):
    """ 
    DBに登録されたユーザ(mac addr)が取得済みローカル内デバイスとマッチするかチェックする
    --
    input:user_list(登録されたユーザ),exit_max_list(ローカル内デバイス)
    output:onoff_result
    --
    総当りで２重ループで確認

    """
    onoff_result=[]
    for i,u_m in enumerate(user_list["mac"]):
        flag_onoff=False
        for ex_m in exit_mac_list:
            print(u_m,ex_m)
            if ex_m ==u_m:
                flag_onoff=True
                break
        onoff_result.append(flag_onoff)
    return onoff_result

def one_check_and_post(db):
    """ 
    １回のチェックの一連の動作
    --
    input:db
    output:なし(firebase_postでpost)
    --
    firebase_read()でDBのユーザを取得し、exit_mac_list()でローカル内デバイスを取得
    check_user()で確認そしてfirebase_post()でpost
    """
    user_list=firebase_read(db)#DBのユーザを取得
    exit_mac_list=pingGetmacAll()#ローカル内のデバイスのmacを取得
    onoff_result=check_user(user_list,exit_mac_list)#DBに登録されたユーザ(mac addr)が取得済みローカル内デバイスとマッチするかチェックする
    firebase_post(db,collection_name="log_db",post_field={"time":time.time(),'user_list':user_list["user"],'result': onoff_result,})#結果のpost
    print(time.time(),user_list["user"],onoff_result)

def main():
    db=firebase_conect()
    i=0
    while True:
        print(i)
        one_check_and_post(db)
        time.sleep(600)#n秒ごとに実行
        i+=1
    
if __name__ == '__main__':
    main()
    