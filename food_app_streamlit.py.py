import streamlit as st
import time
import datetime

st.set_page_config(page_title="Food application",layout="centered")
st.divider()
st.title("Food App")

st.header("Welcome to our food app")

st.caption("This is a demo food app created using Streamlit")


first_name = st.text_input("Enter your First name:",placeholder="Type your first name here...")
last_name = st.text_input("Enter your Last name:",placeholder="Type your last name here...")


city = st.selectbox("City",["Vadodara","surat","ahmedabad","gandhinagar","anand", "rajkot"])

food_prefs = st.multiselect("Food Preferences",["Pizza", "Burger", "Pasta", "Dosa", "Idli", "Noodles",
                                   "Biryani", "Sandwich"])

num_items = st.slider("How many food items you have ordered",min_value=0,max_value=100,value=1)

gender = st.radio("What is your gender?",["Male","Female","Other"])

dob = st.date_input("Date of Birth", min_value=datetime.date(1900, 1, 1))

c1,c2=st.columns(2)
food_category = c1.selectbox("Food Category", ["Indian", "Chinese", "Italian", "Mexican", "Continental"])

beverage = c2.selectbox("Beverage", ["Soft Drinks", "Juices", "Tea", "Coffee", "Water"])


audio_message=st.audio_input("Record your audio")
if audio_message:
    st.write("Audio recorded successfully!")
    st.audio(audio_message)
    
feedback = st.text_area("Any Feedback?")
    
terms = st.checkbox("I agree to the terms and conditions")

_, col, _ = st.columns(3)

with col:
    if st.button("Place Order"):
        if first_name and last_name and terms:
            with st.spinner("Placing your order..."):
                time.sleep(3)
                st.write("Your order has been placed!")
            
            st.success("Your order has been placed successfully!")
            
            st.divider()
            st.subheader("📋 Order Details")
            
            col1, col2 = st.columns(2)
            with col1:
                st.write(f"First Name: {first_name}")
                st.write(f"Last Name: {last_name}")
                st.write(f"City:{city}")
                st.write(f"Gender: {gender}")
                st.write(f"Date of Birth: {dob}")
            
            with col2:
                st.write(f"Food Category: {food_category}")
                st.write(f"Beverage: {beverage}")
                st.write(f"Number of Items: {num_items}")
                st.write(f"Food Preferences: {', '.join(food_prefs) if food_prefs else 'None'}")
            
            if feedback:
                st.write(f"Feedback: {feedback}")
        else:
            if not first_name or not last_name:
                st.error("Please enter your first and last name!")
            if not terms:
                st.error("Please agree to the terms and conditions!")