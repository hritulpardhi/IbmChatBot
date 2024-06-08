from django.http import HttpResponse
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.conf import settings

@csrf_exempt
def watsonApiCall(request):
    if request.method == 'POST':
        print("request", request)
        json_data = json.loads(request.body)
        print("json_data", json_data)
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

        {} [/INST]""".format({json_data.get("message")}),
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
            "Authorization": 'Bearer eyJraWQiOiIyMDI0MDYwNDA4NDAiLCJhbGciOiJSUzI1NiJ9.eyJpYW1faWQiOiJJQk1pZC02OTQwMDBDWlZZIiwiaWQiOiJJQk1pZC02OTQwMDBDWlZZIiwicmVhbG1pZCI6IklCTWlkIiwianRpIjoiYmRkY2ZlODMtMWE3YS00NDM0LWEwNzktZGExZmE3ZTEzMTczIiwiaWRlbnRpZmllciI6IjY5NDAwMENaVlkiLCJnaXZlbl9uYW1lIjoiSHJpdHVsIiwiZmFtaWx5X25hbWUiOiJQYXJkaGkiLCJuYW1lIjoiSHJpdHVsIFBhcmRoaSIsImVtYWlsIjoiaHJpdHVscGFyZGhpMjcwNkBnbWFpbC5jb20iLCJzdWIiOiJocml0dWxwYXJkaGkyNzA2QGdtYWlsLmNvbSIsImF1dGhuIjp7InN1YiI6ImhyaXR1bHBhcmRoaTI3MDZAZ21haWwuY29tIiwiaWFtX2lkIjoiSUJNaWQtNjk0MDAwQ1pWWSIsIm5hbWUiOiJIcml0dWwgUGFyZGhpIiwiZ2l2ZW5fbmFtZSI6IkhyaXR1bCIsImZhbWlseV9uYW1lIjoiUGFyZGhpIiwiZW1haWwiOiJocml0dWxwYXJkaGkyNzA2QGdtYWlsLmNvbSJ9LCJhY2NvdW50Ijp7InZhbGlkIjp0cnVlLCJic3MiOiJlMTQwOGIwZTcxMGQ0OTFjOTczYjFlMzgxMGZmODEzZCIsImZyb3plbiI6dHJ1ZX0sImlhdCI6MTcxNzgzOTYzMCwiZXhwIjoxNzE3ODQzMjMwLCJpc3MiOiJodHRwczovL2lhbS5jbG91ZC5pYm0uY29tL2lkZW50aXR5IiwiZ3JhbnRfdHlwZSI6InVybjppYm06cGFyYW1zOm9hdXRoOmdyYW50LXR5cGU6YXBpa2V5Iiwic2NvcGUiOiJpYm0gb3BlbmlkIiwiY2xpZW50X2lkIjoiZGVmYXVsdCIsImFjciI6MSwiYW1yIjpbInB3ZCJdfQ.OmXFeGxSEWdL_WsNxxlJG7oTOpCWn4C_-gFHgviFbRX0nc1ZBRH9ED5xRMv48efBe1yBezV-dGDR-T3nGTwQcDofaO5pmdcUjSH0qPUcHYLEG-QrrhjFHm2ilnxl_kXMCUso3zELUMg8rGpFpjR3SKndmmwbqSG5xKTGQcq4vN0KjZUbxE7LuxoUhaQK27qZihsZo1iWg4oWYHyb0gO3GuWrJOpGI0PFquFjK_PxDRPlg0WpW91p3Q1ZCG5ewaU7lzM39R47mSo33h0PZjTLqaBEGBJU3ncREPbiBhPNX1N4HaU8thcNrGqSM_dJEunp6efdxVfZiAiCRiHVxA7xYg'
        }

        response = requests.post(
            url,
            headers=headers,
            json=body
        )

        # response = {
        #             "model_id": "meta-llama/llama-2-70b-chat",
        #             "created_at": "2024-04-23T18:12:24.579Z",
        #             "results": [
        #                 {
        #                     "generated_text": "Watson is a supercomputer developed by IBM that uses artificial intelligence (AI) and machine learning to answer questions and solve problems. It was named after IBM's first CEO, Thomas J. Watson. Watson was first developed in the early 2000s and gained widespread attention in 2011 when it competed on the game show Jeopardy! against two human champions. Watson won the competition, demonstrating its ability to process and analyze large amounts of data quickly and accurately.\n\nWatson uses a combination of natural language processing (NLP) and machine learning algorithms to understand and respond to questions. It can process up to 500 gigabytes of data per second and perform calculations at a rate of 80 trillion operations per second. This allows Watson to quickly analyze large amounts of data and provide accurate answers to complex questions.\n\nWatson has a wide range of applications across various industries, including healthcare, finance, and education. In healthcare, Watson can help doctors and researchers analyze medical data to identify patterns and make predictions about patient outcomes. In finance, Watson can help financial analysts identify trends and make predictions about market performance. In education, Watson can help teachers personalize learning for students based on their individual needs and abilities.\n\nOverall, Watson represents a significant advancement in the field of artificial intelligence and has the potential to revolutionize many industries and fields. Its ability to quickly process and analyze large amounts of data makes it a powerful tool for solving complex problems and making informed decisions.",
        #                     "generated_token_count": 339,
        #                     "input_token_count": 6,
        #                     "stop_reason": "eos_token"
        #                 }
        #             ],
        #             "system": {
        #                 "warnings": [
        #                     {
        #                         "message": "This model is a Non-IBM Product governed by a third-party license that may impose use restrictions and other obligations. By using this model you agree to its terms as identified in the following URL.",
        #                         "id": "disclaimer_warning",
        #                         "more_info": "https://dataplatform.cloud.ibm.com/docs/content/wsj/analyze-data/fm-models.html?context=wx"
        #                     },
        #                     {
        #                         "message": "token usage, 46090 of 50000, is at 92 % of the limit",
        #                         "id": "token_quota"
        #                     }
        #                 ]
        #             }
        #         }   
            
        # data = response
        data = response.json()
        print("data", data)
        
        if data.get('errors'):
            new_bearer_token_response = getNewToken()
            if new_bearer_token_response.get('success'):
                headers = {
                    "Accept": "application/json",
                    "Content-Type": "application/json",
                    "Authorization": "Bearer {}".format(new_bearer_token_response.get('bearer_token'))
                }
                response = requests.post(
                    url,
                    headers=headers,
                    json=body
                )
        # failure response
        #  {'errors': [{'code': 'authentication_token_expired', 'message': 'Failed to authenticate the request due to an expired token'}], 'trace': '97f1288fbb278f98cabbacb5b61aac15', 'status_code': 401}
        return JsonResponse({'message': 'Request recieved successfully!', 'data':data}, status=response.status_code)
        # return JsonResponse({'message': 'Request recieved successfully!', 'data':data}, status=200)
    
    else:
        # If the request method is not POST, return a 405 Method Not Allowed response
        return JsonResponse({'error': 'Method Not Allowed'}, status=405)


def getNewToken():
    url = "https://iam.cloud.ibm.com/identity/token"
    payload = f'grant_type={settings.IBM_WATSON_GRANT_TYPE}'
    headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    response = response.json()
    print(response)
    if response.get('access_token'):
        return {"success": True, "message" : "Failed to generate new token.", "bearer_token" : response.get('access_token')}
    else:
        return {"success": False, "message" : "Failed to generate new token."}
#         {F
#     "access_token": "",
#     "refresh_token": "not_supported",
#     "token_type": "Bearer",
#     "expires_in": 3600,
#     "expiration": 1713895115,
#     "scope": "ibm openid"
# }