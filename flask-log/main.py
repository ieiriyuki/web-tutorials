from flask import Flask, request

app = Flask(__name__)

@app.get('/index/<int:id>')
def index(id):
    app.logger.debug('A value for debugging')
    app.logger.info('An info message')
    app.logger.warning('A warning message')
    app.logger.error('An error occurred')
    return {"msg": 'Hello, World!', "id": id}


@app.post("/user")
def user():
    data = request.json
    app.logger.info(f"User data: {data}")
    return {"msg": "User data received"}
