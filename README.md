<h2 align="center"># Lyric_LLM_Project</h2>

# Aim: 

Developing an RAG using the Langchain LLMs and HuggingFaceHub model to perform sentiment analysis on BTS songs lyrics translations and suggest a playlist and set of quotes from the songs according to the user's emotions.

# Libraries Required:
- Langchain 
- NLTK
- HuggingFaceHub
- Streamlit
- Beautifulsoup
- Pandas
- JSON

# Procedure:
1. Scrape data from![Doolset Bangtan Lyric Translations](https://doolsetbangtan.wordpress.com/) to obtain all BTS songs and their lyrics with translations
2. Clean the scraped data and extract only the translations into a JSON
3. Create two Langchain LLMs using the HuggingFaceHub model to perform sentimental analysis and obtain
    - emotion for every line translation for every song in the JSON
    - the overall emotion of each song
5. Save the results in a consolidated dataset
6. Using Streamlit obtain user input for any emotions and derive the appropriate playlist and quotes for the user based on the emotions

# How to run:

Clone the repository and run the emotion_chatbot.py file using Streamlit 
```
streamlit run emotion_chatbot.py
```

# Output
![Streamlit Output](https://github.com/HarshiniR4/Lyric_LLM_Project/blob/main/output/Streamlit%20Recommendation%20output%201.png)
(![image](https://github.com/HarshiniR4/Lyric_LLM_Project/assets/59364581/017fa257-0235-4a2c-bf59-16826e31b031)
![image](https://github.com/HarshiniR4/Lyric_LLM_Project/assets/59364581/d1b1623a-36c8-4cc7-8de7-9c0a4c48d4de)

)
