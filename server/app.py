import streamlit as st
import json
import datetime
import pandas as pd
from google.cloud import firestore 
from google.oauth2 import service_account
from make_icon import make_icon

def load_user_db(db):
    docs = db.collection(u'user').stream()
    u_name_list=[]
    for doc in docs:    
        #st.markdown(f'{doc.id} => {doc.to_dict()}')
        u_name_list.append(doc.to_dict()["name"])
    return u_name_list
def check_db(db,collection_name="log_db",flag_print=False):
    posts_ref = db.collection(collection_name)
    #########search latest
    for doc in posts_ref.stream():   
        if  st.session_state.latest["time"]<doc.to_dict()["time"]:#人数が等しい中で最新
            st.session_state.latest=doc.to_dict()
        if flag_print:
            st.write(f'{doc.id} => {doc.to_dict()}')
default_u_name="Allice"
default_mac_addr="XX:XX:XX:XX:XX:XX"

def init_session(db):
    if "flags" not in st.session_state:
        st.session_state.input_u_name=default_u_name
        st.session_state.input_mac_addr=default_mac_addr
        st.session_state.icons={}
        st.session_state.latest={"time":0,'user_list':[None],'result': [False]}
        check_db(db)
        for u_name in st.session_state.latest["user_list"]:#["Alice","Bob","Carol","Dave","Ellen","Pat","Zoe"]:
            st.session_state.icons[u_name]=make_icon(u_name)

def init_firebase():
    key_dict = json.loads(st.secrets["firebase_key"]) 
    creds = service_account.Credentials.from_service_account_info(key_dict)
    db = firestore.Client(credentials=creds)#project="pingcheckdatabese"
    return db
def  check_input():
    flga_u_name,flga_mac_addr=None,None
    if st.session_state.input_u_name!=default_u_name:#defaultのままならNone
        flga_u_name=True
    if st.session_state.input_mac_addr!=default_mac_addr:#defaultのままならNone
        flga_mac_addr=True
    return flga_u_name,flga_mac_addr
def register(db):
    flga_u_name,flga_mac_addr=check_input()
    if flga_u_name and flga_mac_addr==None:
        st.write("アドレスを入力してください")
    elif flga_u_name==None and flga_mac_addr:
        st.write("名前を入力してください")
    ##############################post
    elif flga_u_name and flga_mac_addr:
        try:
            pass
            doc_ref = db.collection('user')
            doc_ref.add({'mac': st.session_state.input_mac_addr,'name': st.session_state.input_u_name,})
            st.session_state.input_u_name=default_u_name
            st.session_state.input_mac_addr=default_mac_addr
        except:
            print('post error')


def get_flag(i):
    if len(st.session_state.latest["result"])<=i:
        return False #範囲外ならFalseとする
    return st.session_state.latest["result"][i]
@st.experimental_memo
def convert_df(df):
   return df.to_csv(index=False).encode('utf-8')
def main():
    st.title("pingChecker")
    db=init_firebase()
    init_session(db)
    load_user_db(db)
    
    tab1, tab2 ,tab3= st.tabs(["CheckNow","CheckLog" ,"User Regster"])
    with tab1:
        check_db(db)
        col1, col2, col3 = st.columns(3)

        with col1:
            for i,(u_name,icons) in enumerate(st.session_state["icons"].items()):
                if i%3==0:
                    st.image(icons[get_flag(i)])
            
        with col2:
            for i,(u_name,icons) in enumerate(st.session_state["icons"].items()):
                if i%3==1:
                    st.image(icons[get_flag(i)])

        with col3:
            for i,(u_name,icons) in enumerate(st.session_state["icons"].items()):
                if i%3==2:
                    st.image(icons[get_flag(i)])
        st.button('Update',on_click=register(db))
        st.write("最終更新　{}".format(datetime.datetime.fromtimestamp(st.session_state.latest["time"])))
        #######

    with tab2:
        st.write("Sample")
        db=pd.DataFrame({"Allice":[True,True,False],"Bob":[False,False,False],"Zoe":[False,True,False]},index=["11:00","11:10","11:20"])
        #st.dataframe(db.style.highlight_max())
        st.dataframe(db)
        st.download_button("Press to Download",convert_df(db),"pingCheck.csv","text/csv",key='download-csv')
    with tab3:
        st.session_state.input_u_name = st.text_input('UserName', default_u_name)
        st.session_state.input_mac_addr = st.text_input('MacAddress ', default_mac_addr)
        st.button('Register',on_click=register(db))
    


if __name__ == '__main__':
    main()