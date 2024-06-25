from flask import Flask, render_template, request
import dotenv
import openai
import os

env_vars = dotenv.dotenv_values()
openai.api_key = env_vars["openai-key"]

app=Flask(__name__, template_folder='../templates', static_folder='../static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get-response', methods=['POST'])
def get_response():
    user_message = request.form['user_message']
    
    # Chame a API do GPT-3 para gerar uma resposta
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages = [
        {
            "role": "system",
            "content": "Voce dever estar pronto para responder qualquer pergunta sobre instituto nacional de pesquisas espaciais, todas as perguntas sao sobre o mesmo e vc deve se identificar como Heldinho."
        },    
        {
            "role": "user",
            "content": user_message,
        }
    ],
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    )  

    print(response)
    # Pegue a resposta gerada pelo modelo
    chat_response = response.choices[0].message.content
    
    return chat_response

if __name__ == '__main__':
    app.run(debug=True)