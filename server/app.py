import streamlit as st
import json
from google.oauth2 import service_account
from google.cloud import firestore
def main():
    st.title("pingChecker")

    st.write("secrets_sample-a:", st.secrets["secrets_sample"]["a"])
    st.write("secrets_sample-b:", st.secrets["secrets_sample"]["b"])

    key_dict = json.loads(st.secrets["firebase_key"]) 
    creds = service_account.Credentials.from_service_account_info(key_dict)
    db = firestore.Client(credentials=creds, project="pingCheckDB")
    st.write(db.collection('ip_mac').document("2").path)

    #for doc in db.collection('ip_mac').stream():
        #        print('{} => {}'.format(doc.id, doc.to_dict()))

    st.markdown("firebaseの秘密鍵はJSONファイルなのでTOMLに変換して同様にlocal/deployにペーストすれば良い[Streamlit ❤️ Firestore (continued)](https://blog.streamlit.io/streamlit-firestore-continued/)")
    st.markdown("# sesstion state counter")

if __name__ == '__main__':
    main()