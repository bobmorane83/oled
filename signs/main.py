# save this as app.py
from sign import Oled
from flask import Flask, request

app = Flask(__name__)

oled = Oled()

@app.route("/sign", methods=['GET'])
def sign():
    speed = request.args.get('speed')
    oled.display(int(speed))
    return f"Sign : {speed}"

@app.route("/clear", methods=['GET'])
def clear():
    oled.clear()
    return f"Clear"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
