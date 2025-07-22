import streamlit as st
import random

# Initialize session state
if 'balance' not in st.session_state:
    st.session_state.balance = 100
if 'result' not in st.session_state:
    st.session_state.result = ''
if 'number' not in st.session_state:
    st.session_state.number = 0

st.title("🎰 High-Low Gambling Game")

st.markdown("""
Welcome to a simple gambling game.  
You start with *$100*.  
You can bet if a random number (1–100) is *High (>50)* or *Low (<50)*.  
If it's exactly 50, *the house wins*.
""")

st.write(f"### 💰 Current Balance: ${st.session_state.balance}")

# Get user input
bet = st.number_input("Enter your bet amount:", min_value=1, max_value=st.session_state.balance, step=1)
guess = st.radio("Your guess:", ["High", "Low"])

# Play function
def play():
    number = random.randint(1, 100)
    st.session_state.number = number

    if number == 50:
        st.session_state.balance -= bet
        st.session_state.result = f"🎲 Number is *50*! House wins. You lose ${bet}."
    elif (number > 50 and guess == "High") or (number < 50 and guess == "Low"):
        st.session_state.balance += bet
        st.session_state.result = f"🎲 Number is *{number}*. You guessed right! You win ${bet}!"
    else:
        st.session_state.balance -= bet
        st.session_state.result = f"🎲 Number is *{number}*. You guessed wrong. You lose ${bet}."

# Button to play
if st.button("Play Round"):
    play()

# Show result
if st.session_state.result:
    st.success(st.session_state.result)

# Game over
if st.session_state.balance <= 0:
    st.error("💀 You're broke. Refresh the page to restart.")

# Reset button
if st.button("🔁 Reset Game"):
    st.session_state.balance = 100
    st.session_state.result = ''
    st.session_state.number = 0