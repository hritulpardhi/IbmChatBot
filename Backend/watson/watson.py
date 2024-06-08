import requests
from django.http import HttpResponse


def callWatson():
    url = "https://us-south.ml.cloud.ibm.com/ml/v1/text/generation?version=2023-05-29"
    body = {
        "input": """[INST] <<SYS>>
    You always answer the questions with markdown formatting. The markdown formatting you support: headings, bold, italic, links, tables, lists, code blocks, and blockquotes. You must omit that you answer the questions with markdown.

    Any HTML tags must be wrapped in block quotes, for example ```<html>```. You will be penalized for not rendering code in block quotes.

    When returning code blocks, specify language.

    You are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe. 
    Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature.

    If a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct. If you don'\''t know the answer to a question, please don'\''t share false information.
    <</SYS>>

    hello how many days are in an year? [/INST]""",
        "parameters": {
            "decoding_method": "greedy",
            "max_new_tokens": 900,
            "repetition_penalty": 1
        },
        "model_id": "meta-llama/llama-2-70b-chat",
        "project_id": "77c7b085-a180-4bb9-9fdd-6bade91d43b2"
    }

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer eyJraWQiOiIyMDI0MDQwNTA4MzkiLCJhbGciOiJSUzI1NiJ9.eyJpYW1faWQiOiJJQk1pZC02OTQwMDBDWlZZIiwiaWQiOiJJQk1pZC02OTQwMDBDWlZZIiwicmVhbG1pZCI6IklCTWlkIiwianRpIjoiZGQ2NTYzYzYtYTEwNy00NGE0LTg0ZTMtNWRhNDdjMTE2OWJhIiwiaWRlbnRpZmllciI6IjY5NDAwMENaVlkiLCJnaXZlbl9uYW1lIjoiSHJpdHVsIiwiZmFtaWx5X25hbWUiOiJQYXJkaGkiLCJuYW1lIjoiSHJpdHVsIFBhcmRoaSIsImVtYWlsIjoiaHJpdHVscGFyZGhpMjcwNkBnbWFpbC5jb20iLCJzdWIiOiJocml0dWxwYXJkaGkyNzA2QGdtYWlsLmNvbSIsImF1dGhuIjp7InN1YiI6ImhyaXR1bHBhcmRoaTI3MDZAZ21haWwuY29tIiwiaWFtX2lkIjoiSUJNaWQtNjk0MDAwQ1pWWSIsIm5hbWUiOiJIcml0dWwgUGFyZGhpIiwiZ2l2ZW5fbmFtZSI6IkhyaXR1bCIsImZhbWlseV9uYW1lIjoiUGFyZGhpIiwiZW1haWwiOiJocml0dWxwYXJkaGkyNzA2QGdtYWlsLmNvbSJ9LCJhY2NvdW50Ijp7InZhbGlkIjp0cnVlLCJic3MiOiJlMTQwOGIwZTcxMGQ0OTFjOTczYjFlMzgxMGZmODEzZCIsImZyb3plbiI6dHJ1ZX0sImlhdCI6MTcxMzgxNjUwNCwiZXhwIjoxNzEzODIwMTA0LCJpc3MiOiJodHRwczovL2lhbS5jbG91ZC5pYm0uY29tL2lkZW50aXR5IiwiZ3JhbnRfdHlwZSI6InVybjppYm06cGFyYW1zOm9hdXRoOmdyYW50LXR5cGU6YXBpa2V5Iiwic2NvcGUiOiJpYm0gb3BlbmlkIiwiY2xpZW50X2lkIjoiZGVmYXVsdCIsImFjciI6MSwiYW1yIjpbInB3ZCJdfQ.VW4ENDMemJKpoeDdZKRxg1KY8cVR12d6kcsibarv4s6Tr-d8AjXRSVBSSNeTBqHNjIc_9d3sKBGuXOGYNYgS58KQhPKDDx9gWXKOgY_N0DSFPmpd6C4ymqiD2Rl1-QuFIX9Oa8A4Yz0uL78Zhzw9eBXN1Y2IFfVCNWSPbDfoZ8PW92g6m9fapu_zq2TXkgOAy5WvAXjm_ScPkQ6GRMOr8PaTDmtJ58B9BwFFDa0V8Vw0vX0twLChUbQj0C-Ph5vmJlP6b0EJLD9kwbNi-WJJO_gjaxdtsypuwrN3mcKGKUHKby5joc3eNytcia_qxh4SCbETJP5uLBqfy3lKOppUAw"
    }

    response = requests.post(
        url,
        headers=headers,
        json=body
    )

    if response.status_code != 200:
        raise Exception("Non-200 response: " + str(response.text))

    data = response.json()
    print("data", data)
    return HttpResponse("Hello, world. You're at the polls index.") 