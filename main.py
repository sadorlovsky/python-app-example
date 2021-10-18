"""
Python app example
"""
from sanic import Sanic
from sanic.response import json

app = Sanic(name='app-example')

@app.route("/")
async def index():
    """
    Returns sample JSON data
    """
    return json({ "data": "Hello World" })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
