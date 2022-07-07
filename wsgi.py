from app.routes import app
from settings import HOST,PORT
if __name__ == '__main__':
    app.run(debug=True, host= HOST, port= int(PORT))
