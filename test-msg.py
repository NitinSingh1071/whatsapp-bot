
from flask import Flask, request, Response
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/sms", methods=['GET','POST'])
def sms_reply():
    # Get the incoming message from the user
    incoming_msg = request.values.get('Body', '').lower()

    # Start our TwiML response
    resp = MessagingResponse()

    # Check the user's message and provide a response
    if 'hello' in incoming_msg:
        resp.message("Hello! How can I assist you today?")
    elif 'products' in incoming_msg:
        # Implement logic to retrieve and display products
        products_response = "Here are some products: Product 1, Product 2, Product 3"
        resp.message(products_response)
    else:
        resp.message("I'm sorry, I didn't understand that. Please try again.")

    return Response(str(resp), content_type='application/xml')

if __name__ == "__main__":
    app.run(debug=True)
