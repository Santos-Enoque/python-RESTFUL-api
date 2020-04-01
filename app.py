from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    msg = request.form.get('Body')

    # Create reply
    resp = MessagingResponse()
    resp.message("*Bem vindo ao chatbot demo moçambicano sobre COVID 19* \n\n Obtenha informações e orientações da XXXX sobre o atual surto de doença por coronavírus (COVID-19). \n\n *O que você gostaria de saber sobre coronavírus?* \n\n Responda com um número a qualquer momento para obter as informações mais recentes sobre o tópico:\n 1. Latest numbers \n 2. Protect yourself \n 3. Your questions answered \n 4. Mythbusters \n 5. Travel advice \n 6. News & Press \n 7. Share \n 8. Donate now \n 9. Change language")

    if msg =='1' or  msg ==1:
         resp.message("Funcionalidade em desenvolvimento")
         return str(resp)
   

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
