import toml
import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from google.oauth2 import service_account

def main():
    with open("../server/.streamlit/secrets.toml") as toml_file:
        toml_text = toml_file.read()
        key_dict = json.loads(toml.loads(toml_text)["firebase_key"])
        creds = credentials.Certificate(key_dict)
        firebase_admin.initialize_app(creds)
        db = firestore.client()        
        ##############################post
        try:
            # Firestoreのコレクションにアクセス
            doc_ref = db.collection('ip_mac')
            # Firestoreにドキュメントidを指定しないで１つづつニュースを保存
            doc_ref.add({
                'ip': "192.449.596",
                'mac': "aa.aa.aa.rr",
                'user': "user5",
            })
        except:
            print('error1')
        ##############################read
        print(db.collection('ip_mac').document("2").path)

        docs = db.collection(u'ip_mac').stream()


        for doc in docs:
            print(f'{doc.id} => {doc.to_dict()}')

    with open("../server/.streamlit/secrets.toml") as toml_file:
        from google.cloud import firestore as firestore2
        toml_text = toml_file.read()
        key_dict = json.loads(toml.loads(toml_text)["firebase_key"])
        creds = service_account.Credentials.from_service_account_info(key_dict)
        db2 = firestore2.Client(credentials=creds)#project="pingcheckdatabese"
        #db2 = firestore2.Client(credentials=creds2, project="pingCheckDB")
        doc_ref = db2.collection("ip_mac")
        
        

        ##############################post
        try:
        
            
            # Firestoreにドキュメントidを指定しないで１つづつニュースを保存
            doc_ref.add({
                'ip': "192.449.596",
                'mac': "aa.aa.aa.rr",
                'user': "user50",
            })
            print("seikou")
        except:
            print('error2')
        ##############################read
        print(db2.collection('ip_mac').document("10").path)
        posts_ref = db2.collection("ip_mac")
        print(posts_ref.stream())

        if True:
            for doc in posts_ref.stream():
                print(f'{doc.id} => {doc.to_dict()}')
        
    

if __name__ == '__main__':
    main()