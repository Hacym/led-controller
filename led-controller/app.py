from bottle import (
    Bottle,
    static_file
)

from leds import ledAPI
from strips import stripAPI

app = Bottle()

@app.route('/')
def index():
    return static_file("index.html", "static")

@app.route('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='static')

if __name__ == '__main__':
    app.merge(ledAPI)
    app.merge(stripAPI)

    app.run(debug=True, port=5250)
