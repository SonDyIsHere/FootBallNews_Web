from app.model import Category, News, UserRoleEnum
from app import app, db
from flask_admin import Admin, BaseView, expose
from flask_admin.contrib.sqla import ModelView
from flask_login import logout_user, current_user
from flask import redirect


class AuthenticatedAdmin(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_role == UserRoleEnum.ADMIN


class AuthenticatedUser(BaseView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_role == UserRoleEnum.ADMIN


class AuthenticatedUser2(BaseView):
    def is_accessible(self):
        return current_user.is_authenticated


class MyNewsView(AuthenticatedAdmin):
    column_list = ['id', 'title', 'content', 'img', 'id_category']
    column_searchable_list = ['title']
    can_export = True
    edit_modal = True


class MyCategoryView(AuthenticatedAdmin):
    column_list = ['name', 'new']


class LogoutView(AuthenticatedUser2):
    @expose("/")
    def __index__(self):
        logout_user()
        return redirect('/admin')


admin = Admin(app=app, name='QUẢN TRỊ', template_mode='bootstrap4')
admin.add_view(MyCategoryView(Category, db.session))
admin.add_view(MyNewsView(News, db.session))
admin.add_view(LogoutView(name="Đăng xuất"))
