from flask_zs.forms import JSONForm
from flask_zs.forms.fields import StringField
from flask_zs.forms.validators import DataRequired, Email, PhoneNumber


class TestForm(JSONForm):
    email = StringField('邮箱', [DataRequired(), Email()])
    phone = StringField('手机号', [PhoneNumber()])
