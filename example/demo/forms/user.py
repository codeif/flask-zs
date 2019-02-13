from flask_zs.forms import BaseItemForm
from flask_zs.forms.fields import StringField
from flask_zs.forms.validators import DataRequired, PhoneNumber
from ..core import db
from ..models.user import User


class UserForm(BaseItemForm):
    name = StringField('姓名', [DataRequired()])
    phone = StringField('手机号', [DataRequired(), PhoneNumber()])

    def save(self):
        if not self.item:
            item = User()
            db.session.add(item)
        else:
            item = self.item

        item.name = self.name.data
        item.phone = self.phone.data

        db.session.commit()
        return item
