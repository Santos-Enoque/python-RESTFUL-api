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
    resp.message("Disse: {} (em breve estaremos dando atualizações sobre corona em Mozambique!! Ability Team)".format(msg))

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
