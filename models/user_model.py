from .create_db import db
from datetime import datetime
from flask_login import UserMixin
from mongoengine import fields as f

class UserModel(db.Document, UserMixin):
    id          = f.StringField()
    name        = f.StringField()
    email       = f.EmailField()
    type        = f.StringField()
    NI          = f.IntField()
    password    = f.StringField()
    create_at   = f.DateTimeField()
    last_update = f.DateTimeField()

    def __repr__(self) -> str:
        match self.type:
            case "operator" | "guru":
                return f"<{self.name} NIP {self.NI}>"
            case "siswa":
                return f"<{self.name} NIS {self.NI}>"
        
    # requirement for flask_login.LoginManager 
    def is_authenticated(self):
        return True
    def is_active(self):
        return True
    def is_anonymous(self):
        return False
    def get_id(self):
        return str(self.id)

    # def load_user(self):
    #     return UserModel.query.get(int(id))