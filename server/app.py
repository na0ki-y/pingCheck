import streamlit as st
import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from make_icon import make_icon
def main():
    st.title("pingChecker")

    st.write("secrets_sample-a:", st.secrets["secrets_sample"]["a"])
    st.write("secrets_sample-b:", st.secrets["secrets_sample"]["b"])
    if "docs" not in st.session_state:
        key_dict = json.loads(st.secrets["firebase_key"]) 
        #creds = service_account.Credentials.from_service_account_info(key_dict)
        creds = credentials.Certificate(key_dict)
        firebase_admin.initialize_app(creds)    
        db = firestore.client()        
        st.session_state.docs = db.collection(u'ip_mac').stream()
    ##############################post
    try:
        pass
        #doc_ref = db.collection('ip_mac')
        #doc_ref.add({'ip': "192.449.596",'mac': "aa.aa.aa.rr",'user': "user3",})
    except:
        print('error')
    ##############################read
    #icons=make_icon("Alice")
    #st.image(icons[1])

    #st.image(cv2.imread("./icon/Alice_icon_in.png"))



        
    for doc in st.session_state.docs:
        st.markdown(f'{doc.id} => {doc.to_dict()}')

    st.markdown("firebaseの秘密鍵はJSONファイルなのでTOMLに変換して同様にlocal/deployにペーストすれば良い[Streamlit ❤️ Firestore (continued)](https://blog.streamlit.io/streamlit-firestore-continued/)")
    st.markdown("# sesstion state counter")

if __name__ == '__main__':
    main()