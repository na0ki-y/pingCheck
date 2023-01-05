import os
import pathlib
import toml
import sys
import glob
from demon_checker.utiles_firebese import firebase_conect
from demon_checker.utiles_firebese import collection_check_and_make
import subprocess

patj_streamlit="./server/.streamlit"
key_name="firebase_key"
def mkdir_check():
    if not os.path.isdir(patj_streamlit):
        os.makedirs(patj_streamlit)
        if not os.path.isdir(patj_streamlit):
            print("->OK(Create success)")
        else:
            print("->ERROR")
    else:
        print("->OK(already exits)")
def touch_read_secrets():
    p = pathlib.Path(patj_streamlit+'/secrets.toml')
    p.touch()
    toml_file = open(patj_streamlit+'/secrets.toml')
    toml_dic = toml.load(toml_file)
    print("->OK(Create read secrets.toml)")
    return toml_dic
def ex_json_to_toml_key(toml_dic):
    json_s=glob.glob(patj_streamlit+"/firebase_secrets.json")
    if len(json_s)==1:
        print("->OK(exits {}:{}/**.json )".format(key_name,patj_streamlit))
        with open(json_s[0]) as json_file:
            json_text = json_file.read()
            toml_dic[key_name]=json_text
        toml.dump(toml_dic, open(patj_streamlit+'/secrets.toml', mode='w'))#上書きtoml_dicの中に古いものはある
    elif len(json_s)==0:
        print("->ERROR(please download and put {}/**.json({}) )".format(patj_streamlit,key_name))
        sys.exit()
    else :#len(json_s)>1:
        print("->ERROR(please  ONLY ONE FILE download and put {}/**.json({}) )".format(patj_streamlit,key_name))
        sys.exit()

    

def convert_firebasekey(toml_dic):
    if key_name in toml_dic.keys():
        print("->OK(already set '{}')".format(key_name))
    else:
        ex_json_to_toml_key(toml_dic)
        print("->OK(convert {}: json to secrets.toml )".format(key_name))
        

def exe_streamlit():
    os.chdir('./server')
    subprocess.run(["streamlit", "run", "app.py"])

def exe_demon():
    os.chdir('./demon_checker')
    subprocess.run(["python", "py_checker.py"])

def exec_multi():
    exe_demon()
    exe_streamlit()

def check_env_pipenv():
    try:
        a=subprocess.run(["pipenv","install"])

        a=subprocess.run(["pipenv","shell"])
        print("->OK pipenv env")

    except:
        print("ERRORplease make pipenv env")
        exit()



    
def main():
    print("###.pipenv の起動")
    check_env_pipenv()
    print("###1.フォルダ作成")
    mkdir_check()
    print("###2.firebasekey読み込み")
    toml_dic=touch_read_secrets()
    convert_firebasekey(toml_dic)
    print("###3.firebaseコレクション作成")
    db=firebase_conect(secrets_path=patj_streamlit+'/secrets.toml')
    print("->OK(conect firebase) {}".format(db))
    collection_check_and_make(db,"user",sample_dic={'mac': "aa.aa.aa.rr",'name': "Sample",})
    collection_check_and_make(db,"log_db",sample_dic={'result': [False,False],'time': 1672635475.220414,"user_list":["A","B"]})
    print("###4.起動/stremlit＆demon")
    args = sys.argv
    if args[1]=="only_demon":
        exe_demon()
    else:#both_demon_and_web
        exec_multi()
    

if __name__ == '__main__':
    main()