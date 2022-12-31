import streamlit as st
import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import cv2
import numpy as np
from make_icon import make_icon
def main():
    st.title("pingChecker")

    if "flags" not in st.session_state:
        print("reload")
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


if __name__ == '__main__':
    main()