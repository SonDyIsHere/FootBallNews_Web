from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship
from app import db, app
from flask_login import UserMixin
import enum


class UserRoleEnum(enum.Enum):
    USER = 1
    ADMIN = 2


class User(db.Model, UserMixin):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    user_role = Column(Enum(UserRoleEnum), default=UserRoleEnum.USER)

    def __str__(self):
        return self.name


class Category(db.Model):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False, unique=True)
    new = relationship('News', backref='category', lazy=True)

    def __str__(self):
        return self.name


class News(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(500), nullable=False, unique=True)
    content = Column(String(5000), default="qwertyuiopp[]asdfghjkl;'zxcvbnm,,./")
    img = Column(String(200),
                 default="https://media.bongda.com.vn/resize/240x145/files/news/2023/12/02/khong-can-ton-tien-liverpool-da-tim-thay-phuong-an-thay-the-van-dijk-195051.jpg")
    id_category = Column(Integer, ForeignKey(Category.id), nullable=False)

    def __str__(self):
        return self.title


if __name__ == '__main__':
    with app.app_context():
        # db.create_all()
        import hashlib

        # u = User(name='Admin', username='admin', password=str(hashlib.md5('123456'.encode('utf-8')).hexdigest()),
        #          user_role=UserRoleEnum.ADMIN)
        # db.session.add(u)
        # db.session.commit()
        #
        # db.session.add(u)
        # db.session.commit()
        c1 = Category(name="Anh")
        c2 = Category(name="TBN")
        c3 = Category(name="Pháp")
        c4 = Category(name="Ý")
        c5 = Category(name="Đức")
        c1 = News(title="Supper Sunday nước Anh", id_category=1)
        c2 = News(title="Supper Sunday nước Ý", id_category=4)
        c3 = News(title="Supper Sunday nước Pháp", id_category=3)
        c4 = News(title="Supper Sunday nước TBN", id_category=2)
        c5 = News(title="Supper Sunday nước Đức", id_category=5)
        c6 = News(title="Đại chiến thành MAN", id_category=1)
        db.session.add(c1)
        db.session.add(c2)
        db.session.add(c3)
        db.session.add(c4)
        db.session.add(c5)
        # db.session.add(c6)
        db.session.commit()
