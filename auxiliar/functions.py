import json
import requests
import time
import os
from gtts import gTTS
import numpy as np
import gradio as gr


def askQuestion(question, history):
    # url='http://localhost:8008/answerQuestion/'

    # headers={
    #     'Authorization':'Basic YWRtaW46YWRtaW4='
    #     }
    # params= {
    #     'question':question
    #     }

    # response=requests.get(url, params=params, headers=headers)
    # answer = response.json().get('answer')
    response={"answer":"The tenth richest person in the world is **Steve Ballmer**.\n \n \n \n\nDISCLAIMER: This response has been generated based on an LLM's interpretation of the data and may not be accurate.","sql_query":"SELECT \"name\" FROM \"global_wealth\".\"p_richest500\" WHERE \"rank\" = '10.0'","query_explanation":"The user is asking for the name of the 10th richest person in the world. I can use the table \"global_wealth\".\"p_richest500\" to answer this question. I will select the name from this table where the rank is 10.","tokens":{"input_tokens":0,"output_tokens":0,"total_tokens":0},"related_questions":["What is the total net worth of the top 10 richest people?","Which industry has the most individuals in the top 500 richest people?","What is the average YTD change in net worth for the top 50 richest people?"],"execution_result":{"Row 1":[{"columnName":"name","value":"Steve Ballmer"}]},"tables_used":["global_wealth.join_general_economy","global_wealth.richest500","global_wealth.p_richest500","global_wealth.p_cost_of_living","global_wealth.p_countries_gpd_hist"],"raw_graph":"","sql_execution_time":0.3,"vector_store_search_time":0.02,"llm_time":3.91,"total_execution_time":4.23}
    global answer
    answer=response.get('answer')
    
    return answer

def flip_text(x):
    return x[::-1]

def flip_image(x):
    return np.fliplr(x)

def text_to_speech():
    tts = gTTS(answer, lang="es")  
    tts.save("output.mp3") 
    os.system("mpg321 output.mp3")
