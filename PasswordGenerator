import streamlit as st
import random
import string

st.title("Password Generator")

strength = ["Strong", "Solid", "Medium", "Weak", "Bad"]
password_strength = st.select_slider("Choose a strength level", options=strength)
st.write(password_strength, "Password")
st.write("#")

number_of_characters = st.number_input("How many characters? ", min_value=0, max_value=100)



#strong password variables
strong_characters = string.ascii_letters + string.punctuation + string.digits
spassword = ''.join(random.choice(strong_characters) for i in range (number_of_characters))

#solid password variables
solid_characters = string.ascii_letters + string.punctuation + string.digits
sopassword = ''.join(random.choice(solid_characters) for i in range (number_of_characters))

#medium password variables
medium_characters = string.ascii_letters + string.digits
mpassword = ''.join(random.choice(medium_characters) for i in range (number_of_characters))

#weak password variables
weak_characters = string.ascii_letters + string.digits
wpassword = ''.join(random.choice(weak_characters) for i in range(number_of_characters))

#bad password variables
bad_characters = string.ascii_letters + string.digits
bpassword = ''.join(random.choice(bad_characters) for i in range(number_of_characters))


if password_strength == "Strong":
    if number_of_characters < 10:
        st.write("You might want more characters for a password")
    st.write(spassword)
elif password_strength == "Solid":
    if number_of_characters < 9:
        st.write("You might want more characters for a password")
    st.write(sopassword)
elif password_strength == "Medium":
    if number_of_characters < 8:
        st.write("You might want more characters for a password")
    st.write(mpassword)
elif password_strength == "Weak":
    if number_of_characters < 5:
        st.write("You might want more characters for a password")
    st.write(wpassword)
elif password_strength == "Bad":
    if number_of_characters < 4:
        st.write("Are you sure you want a password that short?")
    st.write(bpassword)
