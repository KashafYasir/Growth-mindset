import streamlit as st

st.set_page_config(page_title="growth mindset project")
st.title("Growth Mindset Challenge: Web App with Stremlit")

st.header("🚀 Welcome to your Growth Journey")
st.write("Embrace challenge, learn from mistakes , and unlock your full potential. This AI-powered app helps you build a growth mindset with reflection , challenge, and achievement 💜")

#qoute section
st.header("🏵️ Today's Growth Mindset Qoute")
st.write("'Success is not how high you have climbed, but how you make a positive difference to the world. '– Roy T. Bennett ")

st.header("°•. 👑 .•°  What's Your Challenge Today?")
user_input = st.text_input("Describe a challenge you're facing?")

#conditions
if user_input:
    st.success(f"🕺 You're facing: {user_input}. Keep pushing forward toward your goal!✌️")
else:
    st.warning("Tell us about your challenge to get started!")

    #reflecting
    st.header("Reflect On Your Learning")
    reflection = st.text_area("🧠Write your reflection here:")

    if reflection:(f"Great insight! Your reflection: {reflection}")
    else:
        st.info("Reflecting on past experience help you grow! Share your difficulties")

#achivements
st.header("♛ Celebrate  Your Wins!") 
acheivment = st.text_input("Share something you recently accomplished:")
if acheivment:
    st.success(f"🎉 Amazing! you achieved: {acheivment}")
else:
    st.info("Big or small , every achievment counts! Share one now ⭐")

    # footer
    st.write("- - -")
    st.write("🌺keep believing in your self. Growth is a journey, not adestination  ")
    st.write("**⛔ Created by Kashaf Yasir**")


