from flask_frozen import Freezer
from app import app

app_freezer = Freezer(app)

if __name__ == '__main__':
    app_freezer.freeze()