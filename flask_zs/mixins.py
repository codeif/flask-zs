from sqlalchemy import Boolean, Column, DateTime, String, func
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.ext.hybrid import hybrid_property
from werkzeug.security import check_password_hash, generate_password_hash


class TimestampMixin:
    @declared_attr
    def created_at(cls):
        return Column(DateTime, default=func.now())

    @declared_attr
    def updated_at(cls):
        return Column(DateTime, default=func.now(), onupdate=func.now())


class LoginMixin:
    @declared_attr
    def _password(cls):
        return Column('password', String(191), comment='login password')

    @declared_attr
    def login_allowed(cls):
        return Column(Boolean, server_default='0')

    @hybrid_property
    def password(self):
        return self._password
        # raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, value):
        self._password = generate_password_hash(value)

    def check_password(self, password):
        return check_password_hash(self._password, password)
