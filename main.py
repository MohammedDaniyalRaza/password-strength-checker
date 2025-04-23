import streamlit as st
import re
import random
import string

st.set_page_config(page_title="Password Strength Checker", page_icon="🔐")

st.title("🔒 Password Strength Checker")
st.markdown("### 👋🏻 Welcome To The Ultimate Password Strength Checker \n Use This Simple Tool To Check The Strength Of Your Password and Get Suggestion on how to make it stronger \n We Will Give You helpful tips to create a **strong Password**")

password = st.text_input("Enter Your Password", type="password")

review = []

score = 0

if password:
    if len(password)>=8:
        score+=1
    else:
        review.append("✖️ Password Should be at least 8 characters long.")
    
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score +=1
    else:
        review.append("✖️ Password Should Contain both upper and lower case characters")

    # if re.search(r'[0-9]', password )
    if re.search(r'\d', password):
        score+=1

    else:
        review.append("✖️ Password Should contain at least one digit")

    if re.search(r"[!@#$%^&*()-_]", password):
        score+=1

    else:
        review.append("✖️ Password Should contain atleast special character 👉🏻 !@#$%^&*()-_")

    if score == 4 :
        review.append("☑️ Now Your Password Is Storng!🔒")
    elif score == 3:
        review.append("🟨 Your Password is Medium. It Could be stronger 💪🏻")

    else :
        review.append("⚠️Your Password is weak, 🙏🏻 Please Make it Stronger.")
    
    if review :
        st.markdown("### Improvement Suggestion.")
        for clu in review:
            st.write(clu)

else:
    st.info("🙏🏻 Please enter your password to get started!") 



def generate_password(length=12):
    chars = string.ascii_letters + string.digits + "!@#$%^&*()-_"
    return ''.join(random.choice(chars) for _ in range(length))

if st.button("Generate Strong Password"):
    password = generate_password()
    st.write("🔐 Generated Password:", password)
