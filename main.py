from sanic import Sanic
from sanic.response import json

app = Sanic()

@app.route("/")
async def index(request):
    return json({ "data": "Hello World" })

@app.route("/test")
async def test(request):
    return json({ "data": "It's a test" })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
