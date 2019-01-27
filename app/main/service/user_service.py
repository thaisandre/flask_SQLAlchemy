import uuid
import datetime
from app.main import db
from app.main.model.user import User


def get_all():
    return User.query.all()


def get_user(public_id):
    return User.query.filter_by(public_id=public_id).first()


def save(data):
    user = User.query.filter_by(email=data['email']).first()

    if not user:
        new_user = User(
            public_id=str(uuid.uuid4()),
            email=data['email'],
            username=data['username'],
            password=data['password'],
            creation_date=datetime.datetime.utcnow()
        )

        db.session.add(new_user)
        db.session.commit()

        response = {
            'status': 'success',
            'message': 'registrado com sucesso'
        }

        return response, 201
    else:
        response = {
            'status': 'fail',
            'message': 'usuário já existe'
        }
        return response, 409

