from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from flask import redirect, url_for
from .extensions import admin, db
from .models import User

class SecurityModelView(ModelView):
    column_exclude_list = ["password"]

    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for("auth.login"))
def setup_admin(app, db):
    from flask_admin import Admin
    admin = Admin(app, name="Repostería", template_mode="bootstrap4")
    admin.add_view(SecurityModelView(User, db.session))
    