import toml
import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
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
            print('error')
        ##############################read
        print(db.collection('ip_mac').document("2").path)

        docs = db.collection(u'ip_mac').stream()

        for doc in docs:
            print(f'{doc.id} => {doc.to_dict()}')
        #for doc in db.collection('ip_mac').stream():
        #        print('{} => {}'.format(doc.id, doc.to_dict()))

    

if __name__ == '__main__':
    main()