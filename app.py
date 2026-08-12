
import streamlit as st
import joblib
from text_preprocessor import TextPreprocessor
# Load model
@st.cache_resource
def load_model():
    return joblib.load("spam_ham_classifier.pkl")

model = load_model()

st.title("📩 Spam/Ham Message Classifier")

message = st.text_area(
    "Enter your message:",
    height=150
)

if st.button("🔍 Classify Message"):

    if not message.strip():
        st.warning("Please enter a message.")

    else:
        prediction = model.predict([message])[0]

        if prediction == 1:
            st.error("🚨 SPAM MESSAGE")
        else:
            st.success("✅ HAM MESSAGE")
