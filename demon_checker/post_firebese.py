import toml
#from google.cloud import firestore
def main():
    with open("../server/.streamlit/secrets.toml") as toml_file:
        toml_text = toml_file.read()
        key_dict = toml.loads(toml_text)["firebase_key"]
        print(key_dict)
        #creds = firestore.Client.Credentials.from_service_account_info(key_dict)
        #db = firestore.Client(credentials=creds, project="streamlit-reddit")

    

if __name__ == '__main__':
    main()