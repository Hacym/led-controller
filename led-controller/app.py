from bottle import Bottle

from leds import ledAPI
from strips import stripAPI

app = Bottle()

@app.route('/')
def index():
    return "Test"

if __name__ == '__main__':
    app.merge(ledAPI)
    app.merge(stripAPI)

    app.run(debug=True, port=5250)
