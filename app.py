from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

# IMPORTANT NOTE: 
# This code was used just for test, hence the use of flask instead of the more rubust flask-restful package
# the scripts on the folders RESOURCES and MODELS are not related to this particular bot, but we decided to keep them in the project becaue we believe they would be usefull in the future, when we build more features

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

    if msg =='1' or  msg ==1:
         resp = MessagingResponse()
         resp.message("Número de casos \n\n Painel de situação de novo coronavírus (COVID-19) em Moçambique O site do INS fornece os últimos números nacionais de casos COVID-19 diariamente. \n https://covid19.ins.gov.mz/ \n\n Digite 0 para visualizar o Menu")
         return str(resp)
    elif msg =='2' or  msg ==2:
         resp = MessagingResponse()
         resp.message("*Como prevenir a infecção por COVID-19? * \n\n Pode prevenir a infecção por COVID-19 seguindo medidas de higiene básicas, tais como: \n\n Lavar as mão com água corrente e sabão ou cinza. \n\n Evitar tocar os olhos, nariz e a boca; \n\n Manter uma distância mínima de 1 metro das outras pessoas; \n Ficar em casa se estiver com febre, tosse ou sintomas de constipaçao; \n\n Evite o aperto de mão, beijos e abraços; \n\n Evitar viajar para locais (províncias) que ja tenham casos registados; \n\n Abrir as janelas ou portas para maior circulação do ar; \n\n Cobrir a boca com o braço em formato de V, sempre que tossir ou espirrar; \n\n Lavar com água e sabão utensílios domésticos (pratos, copos, chávenas, panelas, colheres, etc.); \n\n  Evitar locais com aglomerados de pessoas. \n\n A *DIKA* mantém-vos informados a partir de casa… \n Entra na Play Store baixe o aplicativo DIKA através do link http://bit.ly/dika-app mantenha-te informado sobre o COVID-19. \n Partilhe a informação com os teus familiares e amigos e salvarás mais vidas… \n Siga a #dika #ficaemcasa")
         return str(resp)
    elif msg =='3' or  msg ==3 or msg =='4' or  msg ==4 or msg =='5' or  msg ==5 or msg =='6' or  msg ==6 or msg =='7' or  msg ==7:
         resp = MessagingResponse()
         resp.message("Funcionalidade em desenvolvimento")
         return str(resp)         
    else:
        resp = MessagingResponse()
        resp.message("*Bem vindo ao chatbot demo moçambicano sobre COVID 19* \n\n Obtenha informações e orientações da XXXX sobre o atual surto de doença por coronavírus (COVID-19). \n\n O que você gostaria de saber sobre coronavírus? \n\n *Nota este serviço não é oficial e ainda esta a ser desenvolvido pela empresa Ability Team* \n\n Responda com um número a qualquer momento para obter as informações mais recentes sobre o tópico:\n 1. Números de casos  \n 2. Cuidados de protecção \n 3. Faça uma pergunta especifica \n 4. Mitos sobre COVID-19 \n 5. Como ficar em quarentena  \n 6. Comunicados oficiais \n 7. Mudar lingua ")
        return str(resp)

   


if __name__ == "__main__":
    app.run(debug=True)
