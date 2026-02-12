import streamlit as st

st.title("Simple Streamlit App")


name = st.text_input("Enter your name:")
rangeNumber = st.slider("Pick a number")

st.write(f"Hello, {name}!")
st.color_picker("Pick a color", "#f04")

st.feedback("stars")


speech = st.audio_input("Record a voice message")

st.image("https://via.placeholder.com/300", caption="Sample Image", use_column_width=True)


if st.button("Click Me!"):
    st.write("You clicked the button! 🎉")
    print("Button Clicked")
