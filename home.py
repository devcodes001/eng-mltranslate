import streamlit as st
import requests
from bs4 import BeautifulSoup
from newspaper import Article
from deep_translator import GoogleTranslator

st.title("Translator")

url = st.text_input("Enter the URL of the webpage you want to scrape:")

if url:
    article = Article(url)
    article.download()
    article.parse()
    st.text_area("News : ",article.text)
    translated_text = GoogleTranslator(source='en', target='ml').translate(article.text)
    st.text_area("Malayalam",translated_text,height = 500)


 
