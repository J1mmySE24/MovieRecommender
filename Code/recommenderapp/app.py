# from movierecommender import db

# from movierecommender.models import User, Post

# db.create_all()

from movierecommender import app

if __name__ == "__main__":
    app.run(port=5001, debug=True)
