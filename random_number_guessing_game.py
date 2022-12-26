import random
import streamlit as st

#----TITLE----#
st.title("Random Number Guessing Game")

st.write("Tip: The number changes everytime you guess wrong, can you do it?")
st.write("####")

a = st.slider("Enter a number between 1 and ", min_value=1, max_value=100)

#----CODE----#
def game():
    b = st.number_input(f"Enter a number between 1 and: {a}", min_value=1, max_value=a, key=int)
    range = random.randint(1, a)
    while True:
        if b == range:
            st.write("You guessed the number\n")
            st.write("Change slider to play again, or keep guessing!")
            st.write("###")
            break
        elif b > range:
            st.write("Your guess was high\n")
            st.write("###")
            break
        elif b < range:
            st.write("Your guess was low\n")
            st.write("###")
            break
game()

st.write("###") 
st.write("Other projects: https://share.streamlit.io/") 
    
