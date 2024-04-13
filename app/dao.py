from app.model import Category, News, User
import hashlib


def get_categories():
    return Category.query.all()


def get_news():
    products = News.query
    # if kw:
    #     products = products.filter(News.name.contains(kw))
    return products.all()


def get_user_by_id(user_id):
    return User.query.get(user_id)


def auth_user(username, password):
    password = str(hashlib.md5(password.encode('utf-8')).hexdigest())

    return User.query.filter(User.username.__eq__(username),
                             User.password.__eq__(password)).first()
