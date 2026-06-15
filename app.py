import streamlit as st
import joblib
import re

model = joblib.load("saved_model/logistic_regression_model.pkl")
vectorizer = joblib.load("saved_model/tfidf_vectorizer.pkl")

DARI_STOPWORDS = {
    "از", "به", "در", "که", "و", "را", "با", "برای", "این", "آن",
    "یک", "شود", "شد", "است", "بود", "های", "ها", "می", "بر",
    "تا", "هم", "اما", "یا", "اگر", "نیز", "کرد", "کند", "کرده"
}

def preprocess_dari_text(text):
    text = str(text)

    text = text.replace("ي", "ی").replace("ك", "ک")
    text = re.sub(r"[\u200c\u200f\u200e]", " ", text)
    text = re.sub(r"http\S+|www\S+", " ", text)
    text = re.sub(r"[A-Za-z]", " ", text)
    text = re.sub(r"\d+", " ", text)
    text = re.sub(r"[^\u0600-\u06FF\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()

    words = text.split()
    words = [word for word in words if word not in DARI_STOPWORDS and len(word) > 1]

    return " ".join(words)

st.set_page_config(
    page_title="Dari Fake News Detection",
    page_icon="📰",
    layout="centered"
)

st.title("Dari Fake News Detection System")
st.write("This application classifies Dari news text as Real or Fake using Logistic Regression.")

user_text = st.text_area("Enter Dari news text:", height=220)

if st.button("Predict"):
    if user_text.strip() == "":
        st.warning("Please enter a news text first.")
    else:
        clean_text = preprocess_dari_text(user_text)
        vectorized_text = vectorizer.transform([clean_text])
        prediction = model.predict(vectorized_text)[0]

        if prediction == "درست":
            st.success("Prediction: Real News")
        else:
            st.error("Prediction: Fake News")

        st.write("Original model label:", prediction)

        with st.expander("Show cleaned text"):
            st.write(clean_text)