import toml
import json
from google.oauth2 import service_account
from google.cloud import firestore 
def main():
    pass

def firebase_conect(secrets_path='../server/.streamlit/secrets.toml'):
    """ 
    DB(firebase)と接続
    --
    input:なし
    output:db
    """
    toml_file = open(secrets_path)
    toml_text = toml_file.read()
    key_dict = json.loads(toml.loads(toml_text)["firebase_key"])
    creds = service_account.Credentials.from_service_account_info(key_dict)
    db = firestore.Client(credentials=creds)#project="pingcheckdatabese"
    toml_file.close()
    return db
        
def firebase_post(db,collection_name="user",post_field={'mac': "aa.aa.aa.rr",'name': "Sample",}):
    """ 
    DB(firebase)にpost
    --
    input:db,collection_name,post_field
    output:なし(post)
    collection_nameへpost_fieldをpost
    """
    doc_ref = db.collection(collection_name)
    ##############################post
    try:
        doc_ref.add(post_field)
    except:
        print('error_post')

def collection_check_and_make(db,collection_name,sample_dic):
    """ 
    DB-collection(firebase)を読み込む
    --
    input:db,collection_name
    output:read_result
    collection_nameの内容をread_result
    """
    ref = db.collection(collection_name)
    ref_item =[i for i in ref.stream()]
    if len(ref_item)>0:
        print("->OK(aleady exits collection:{})".format(collection_name))
    else:
        ref.add(sample_dic)
        print("->OK(createcollection:{})".format(collection_name))

    return
    for doc in posts_ref.stream():
        read_result["user"].append(doc.to_dict()["name"])
        read_result["mac"].append(doc.to_dict()["mac"])
        if flag_print:
            print(f'{doc.id} => {doc.to_dict()}')
    return read_result

def firebase_read(db,collection_name="user",flag_print=False):
    """ 
    DB(firebase)を読み込む
    --
    input:db,collection_name
    output:read_result
    collection_nameの内容をread_result
    """
    posts_ref = db.collection(collection_name)
    read_result={"user":[],"mac":[]}
    for doc in posts_ref.stream():
        read_result["user"].append(doc.to_dict()["name"])
        read_result["mac"].append(doc.to_dict()["mac"])
        if flag_print:
            print(f'{doc.id} => {doc.to_dict()}')
    return read_result
    
    

if __name__ == '__main__':
    db=firebase_conect()
    #firebase_post(db)
    read_result=firebase_read(db)
    print(read_result)
