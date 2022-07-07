import os
from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from flask_mongoengine import MongoEngine
from .configs.mongo import MONGO_CONNECTION

app = Flask(__name__)
CORS(app)


# initialize Mongo Engine connection
app.config['MONGODB_SETTINGS'] = MONGO_CONNECTION


db = MongoEngine(app)
api = Api(app)

# login register routes

# api.add_resource(Login, '/auth/login')


if __name__ == '__main__':
    app.run(debug=True)
