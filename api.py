from sanic import Sanic
from sanic.response import json
import ssl

context = ssl.create_default_context(purpose=ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain("./localhost.crt", keyfile="./localhost.key")

app = Sanic(__name__)


@app.get('/')
def echo(request):
    print(request.json)
    return json(
        dict(headers=dict(request.headers),
             args=request.args,
             json=dict(request.json) if request.json else None))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8443, ssl=context)
