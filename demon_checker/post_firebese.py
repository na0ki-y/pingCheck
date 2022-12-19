import toml
import json
from google.oauth2 import service_account
from google.cloud import firestore
def main():
    with open("../server/.streamlit/secrets.toml") as toml_file:
        toml_text = toml_file.read()
        key_dict = json.loads(toml.loads(toml_text)["firebase_key"])
        creds = service_account.Credentials.from_service_account_info(key_dict)
        db = firestore.Client(credentials=creds, project="pingCheckDB")
        print(db.collection('ip_mac').document("2").path)

        #for doc in db.collection('ip_mac').stream():
        #        print('{} => {}'.format(doc.id, doc.to_dict()))

    

if __name__ == '__main__':
    main()