import streamlit as st
import json
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

default_u_name="Allice"
default_mac_addr="XX:XX:XX:XX:XX:XX"

def init_session(db):
    if "flags" not in st.session_state:
        st.session_state.input_u_name=default_u_name
        st.session_state.input_mac_addr=default_mac_addr
        u_name_list=load_user_db(db)
        st.session_state.icons={}
        st.flags=[]
        for u_name in u_name_list:#["Alice","Bob","Carol","Dave","Ellen","Pat","Zoe"]:
            st.session_state.icons[u_name]=make_icon(u_name)
            st.flags.append(1)

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
    ##############################read
def check_db(db):
    pass


def main():
    st.title("pingChecker")
    db=init_firebase()
    init_session(db)
    load_user_db(db)
    
    tab1, tab2 = st.tabs(["Check", "User Regster"])
    with tab1:
        
        l_flag = st.checkbox('left off')
        if l_flag:
            for i,(u_name,icons) in enumerate(st.session_state["icons"].items()):
                if i%3==0:
                    st.flags[i]=0
        st.write(l_flag)#,st.flags)

        col1, col2, col3 = st.columns(3)

        with col1:
            for i,(u_name,icons) in enumerate(st.session_state["icons"].items()):
                if i%3==0:
                    st.image(icons[st.flags[i]])
            
        with col2:
            for i,(u_name,icons) in enumerate(st.session_state["icons"].items()):
                if i%3==1:
                    st.image(icons[st.flags[i]])

        with col3:
            for i,(u_name,icons) in enumerate(st.session_state["icons"].items()):
                if i%3==2:
                    st.image(icons[st.flags[i]])
        #######

    with tab2:
        st.session_state.input_u_name = st.text_input('UserName', default_u_name)
        st.session_state.input_mac_addr = st.text_input('MacAddress ', default_mac_addr)
        st.button('Register',on_click=register(db))
    


if __name__ == '__main__':
    main()