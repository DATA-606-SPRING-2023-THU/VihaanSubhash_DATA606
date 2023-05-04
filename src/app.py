import streamlit as st
import joblib
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize

# load model and CountVectorizer object
logregg = joblib.load('logregg.joblib')
bow_ct = joblib.load('bow_ct.joblib')


def predict_sentiment(input_str):
    preprocessed_input = preprocess_input(input_str)
    input_bow = bow_ct.transform([preprocessed_input])
    sentiment_rating = logregg.predict(input_bow)
    if sentiment_rating[0] == 1:
        return "Positive review"
    else:
        return "Negative review"


# function to preprocess user input
def preprocess_input(input_str):
    lowercase_str = input_str.lower() # convert to lowercase
    tokenized_str = word_tokenize(lowercase_str) # tokenize words
    return ' '.join(tokenized_str) # join tokenized words with spaces

# set app title
st.title('Online Review Sentiment Analysis')

# get user input
user_input = st.text_input('Enter your review:')

import csv
import time

current_time = time.strftime('%Y-%m-%d %H:%M:%S')


if st.button('predict'):
    sentiment = predict_sentiment(user_input)
    st.write("Sentiment: ", sentiment)

    # Check if the review is negative or positive
    if sentiment in ["Negative review", "Positive review"]:
        # Write the review to a sheet with a unique id and the current time
        with open('output_reviews.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([sentiment, user_input, time.strftime('%Y-%m-%d'), time.strftime('%H:%M:%S')])
