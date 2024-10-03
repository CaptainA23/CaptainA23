import openai
import streamlit as st

# Set up OpenAI API (replace with your actual API key)
openai.api_key = "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"

def get_advice(prompt):
    # Call GPT-4 (or GPT-3.5-turbo) to get career/course suggestions using the new API
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # You can use "gpt-4" if you have access
        messages=[
            {"role": "system", "content": "You are a helpful assistant that provides advice on Health Information Sciences courses and careers."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150
    )
    return response['choices'][0]['message']['content'].strip()

# App title
st.title("Health Information Sciences Student Support")

# Sidebar navigation
st.sidebar.title("Navigation")
option = st.sidebar.selectbox("Choose a page:", ["Home", "Course Overview", "Skills Tracker", "Career Guidance"])

# Home page
if option == "Home":
    st.header("Welcome to the Health Information Sciences Support App")
    st.write("This AI-based app is designed to guide students through their studies, providing information on courses, "
             "skills to acquire, and career paths in Health Information Sciences.")

# Course Overview page
elif option == "Course Overview":
    st.header("Course Overview")
    st.write("Here you can find detailed descriptions of the Health Information Sciences course. "
             "Including topics, objectives, and learning outcomes.")

# Skills Tracker page
elif option == "Skills Tracker":
    st.header("Skills to Acquire")
    skills = st.text_input("Enter your current skills (separated by commas):")

    # Provide learning resource recommendations
    if st.button("Get Learning Resources"):
        if skills:
            prompt = f"Recommend online courses or resources for improving these skills: {skills} in Health Information Sciences."
            recommendations = get_advice(prompt)
            st.write("### Recommended Learning Resources:")
            st.write(recommendations)
        else:
            st.write("Please enter your skills to get recommendations.")

# Career Guidance page
elif option == "Career Guidance":
    st.header("Career Path Guidance")
    career_input = st.text_input("Enter your interests or career aspirations:")

    # Provide career recommendations
    if st.button("Get Career Advice"):
        if career_input:
            prompt = f"Based on the current job market trends in Tanzania, recommend career paths for someone interested in {career_input} in Health Information Sciences."
            career_advice = get_advice(prompt)
            st.write("### AI-Powered Career Path Suggestions:")
            st.write(career_advice)
        else:
            st.write("Please enter your career interests.")
