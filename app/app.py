from flask import Flask, render_template, request
import openai

# Configure a sua chave de API da OpenAI
openai.api_key = 'sua_chave_de_api_aqui'

app=Flask(__name__, template_folder='../templates', static_folder='../static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get-response', methods=['POST'])
def get_response():
    user_message = request.form['user_message']
    
    # Chame a API do GPT-3 para gerar uma resposta
    response = openai.Completion.create(
        engine="text-davinci-003",  # Escolha o mecanismo de linguagem adequado
        prompt=user_message,
        max_tokens=50  # Número máximo de tokens na resposta
    )
    
    # Pegue a resposta gerada pelo modelo
    chat_response = response.choices[0].text.strip()
    
    return chat_response

if __name__ == '__main__':
    app.run(debug=True)