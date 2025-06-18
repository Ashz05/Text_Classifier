import torch 
import gradio as gr
import pandas as pd 
import matplotlib.pyplot as plt


# Use a pipeline as a high-level helper
from transformers import pipeline

model_path = ("models--distilbert--distilbert-base-uncased-finetuned-sst-2-english"
              "/snapshots/714eb0fa89d2f80546fda750413ed43d93601a13")

analyzer = pipeline("text-classification", model=model_path)

# print(analyzer(["This product is good","This product was quite expensive"]))
# pipe = pipeline("text-classification", model="distilbert/distilbert-base-uncased-finetuned-sst-2-english")

def sentiment_analysis(review):
    sentiment = analyzer(review)
    return sentiment[0]['label']

def sentiment_bar_chart(df):
    sentiment_counts= df['Sentiment'].value_counts()

    fig,ax=plt.subplots()
    sentiment_counts.plot(kind='pie',ax=ax, color=['green','red'],autopct='%1.1f%%')
    ax.set_title("Review Sentiment Counts")
    ax.set_xlabel("Sentiment")
    ax.set_ylabel("Count")
    # ax.set_xticklabels(['Postitive','Negative'], rotation=0)


    return fig

def read_reviews_and_analyze_sentiment(file_object):

    df = pd.read_excel(file_object)

    if 'Review' not in df.columns:
        raise ValueError("Excel file must contain a 'Review' column.")
    #Apply the get_sentiment
    
    df['Sentiment']=df['Review'].apply(sentiment_analysis)
    chart_object =sentiment_bar_chart(df)
    return df,chart_object

#result=read_reviews_and_analyze_sentiment("Files/Reviews.xlsx")
#print(result)

#demo=gr.Interface(fn=summary, inputs="text",outputs="text")
demo=gr.Interface(fn=read_reviews_and_analyze_sentiment,
                  inputs=[gr.File(file_types=[".xlsx"],label="Upload your review comment")],
                  outputs=[gr.Dataframe(label="Sentiments"),gr.Plot(label="Sentiment Analysis")],
                  title="SentimentAI : Sentiment Analyzer",
                  description="This project is used to Analyze the sentiment of the text by providing the file")


demo.launch()

