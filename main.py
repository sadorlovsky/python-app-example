from sanic import Sanic
from sanic.response import json
from auth import authorized

app = Sanic()

@app.route("/")
async def index(request):
    return json({ "data": "Hello World" })

@app.route("/test")
async def test(request):
    return json({ "data": "It's a test" })

@app.route("/private")
@authorized()
async def private(request):
    return json({ "data": "Private endpoint" })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
