import json
import requests
import time
import os
import numpy as np
import gradio as gr


def askQuestion(question, history):
    url='http://localhost:8008/answerQuestion/'

    headers={
        'Authorization':'Basic YWRtaW46YWRtaW4='
    }
    params= {
        'question':question,
        'custom_instructions': 'prioriza buscar en los join antes de las tablas'
    }

    response=requests.get(url, params=params, headers=headers)
    answer = response.json().get('answer')
   
    return answer

def flip_text(x):
    return x[::-1]

def flip_image(x):
    return np.fliplr(x)