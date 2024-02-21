import streamlit as st
st.title("--------------FLAMES------------------")
a=st.text_input("FIRST NAME")
b=st.text_input("SECOND NAME")
s1=list(a)
s2=list(b)
c=0
for i in range(len(s1)):
    for j in range(len(s2)):
        if s1[i]==s2[j]:
            s1[i]=0
            s2[i]=0
            break
for i in s1+s2:
    if i!=0:
        c+=1



l=['FRIENDS','LOVE','AFFECTION','MARRIAGE','ENEMIES','SIBLINGS']
while len(l)>1:
    si=(c%len(l)-1)
    if si>=0:
        right=l[si+1:]
        left=l[:si]
        l=right+left
    else:
        l=l[:len(l)-1]

if(st.button("submit")):
    st.success(l[0])
    