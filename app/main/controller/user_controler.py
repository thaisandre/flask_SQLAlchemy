from flask import request
from flask_restplus import Resource
from ..util.dto import UserDto
from ..service.user_service import save, get_all, get_user

api = UserDto.api
_user = UserDto.user


@api.route('/')
class UserList(Resource):

    @api.doc('lista de usuários')
    @api.marshal_list_with(_user, envelope='data')
    def get(self):
        """"Lista todos usuários"""
        return get_all()

    @api.response(201, 'usuário criado com sucesso.')
    @api.doc('cria novo usuário')
    @api.expect(_user, validate=True)
    def post(self):
        """Cria novo usuário"""
        data = request.json
        return save(data=data)


@api.route('/<public_id>')
@api.param('public-id', 'identificação do usuário')
@api.response(404, 'usuário não encontrado')
class User(Resource):

    @api.doc('detalhes de um usuário')
    @api.marshal_with(_user)
    def get(self, public_id):
        """"Lista detalhes de um usuário"""
        user = get_user(public_id)
        if not user:
            api.abort(404)
        else:
            return user

