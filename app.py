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
    resp.message("Disse: {} (digite 'A' para ter atualizações sobre o covid19 em moçambique \n digite 'B' para saber sobre os métodos de prevenção)".format(msg))

    if msg =='A' or  msg =='a':
         resp.message("existem x casos de covid19 em moçambique")
         return str(resp)
    elif msg =='B' or  msg =='b':
         resp.message("Fique em casa!!!")
         return str(resp)

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
