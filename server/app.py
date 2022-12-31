import streamlit as st
import json
from google.cloud import firestore 
from google.oauth2 import service_account
from make_icon import make_icon

def main():
    st.title("pingChecker")

    st.write("secrets_sample-a:", st.secrets["secrets_sample"]["a"])
    st.write("secrets_sample-b:", st.secrets["secrets_sample"]["b"])

    key_dict = json.loads(st.secrets["firebase_key"]) 
    creds = service_account.Credentials.from_service_account_info(key_dict)
    db = firestore.Client(credentials=creds)#project="pingcheckdatabese"
    doc_ref = db.collection("ip_mac")
    ##############################post
    try:
        pass
        doc_ref = db.collection('ip_mac')
        doc_ref.add({'ip': "192.449.596",'mac': "aa.aa.aa.rr",'user': "user30",})
    except:
        print('error')
    ##############################read
    docs = db.collection(u'ip_mac').stream()

    for doc in docs:    
        st.markdown(f'{doc.id} => {doc.to_dict()}')


    ##############################image
    if "flags" not in st.session_state:
        st.session_state.icons={}
        st.flags=[]
        for u_name in ["Alice","Bob","Carol","Dave","Ellen","Pat","Zoe"]:
            st.session_state.icons[u_name]=make_icon(u_name)
            st.flags.append(1)
    #########
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

    st.markdown("firebaseの秘密鍵はJSONファイルなのでTOMLに変換して同様にlocal/deployにペーストすれば良い[Streamlit ❤️ Firestore (continued)](https://blog.streamlit.io/streamlit-firestore-continued/)")
    st.markdown("# sesstion state counter")

if __name__ == '__main__':
    main()