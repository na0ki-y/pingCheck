import streamlit as st
def main():
    st.title("pingChecker")

    st.write("secrets_sample-a:", st.secrets["secrets_sample"]["a"])
    st.write("secrets_sample-b:", st.secrets["secrets_sample"]["b"])

    st.markdown("firebaseの秘密鍵はJSONファイルなのでTOMLに変換して同様にlocal/deployにペーストすれば良い[Streamlit ❤️ Firestore (continued)](https://blog.streamlit.io/streamlit-firestore-continued/)")
    st.markdown("# sesstion state counter")

if __name__ == '__main__':
    main()