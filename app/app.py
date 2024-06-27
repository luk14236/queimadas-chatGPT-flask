from flask import Flask, render_template, request
import json 
import openai
import os

openai.api_key = os.environ["openai-key"]

app=Flask(__name__, template_folder='../templates', static_folder='../static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get-response', methods=['POST'])
def get_response():
    user_message = request.form['user_message']

    mensagens_geral = [
        {
            "role": "system",
            "content": "Voce dever estar pronto para responder qualquer pergunta sobre instituto nacional de pesquisas espaciais, todas as perguntas sao sobre o mesmo e vc deve se identificar como Heldinho."
        }
    ]

    messages = json.loads(user_message)

    mensagens_geral.extend(messages)
    
    # Chame a API do GPT-3 para gerar uma resposta
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages = json.loads(json.dumps(mensagens_geral)),
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.2,
    )  

    chat_response = response.choices[0].message.content
    
    return chat_response

if __name__ == '__main__':
    app.run(debug=True)