from flask_restplus import Api
from flask import Blueprint
from .main.controller.user_controler import api as user_ns
#from .main.controller.auth_controller import api as auth_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='FLASK RESTPLUS API',
          version='1.0',
          description='a flask restplus webservice'
          )

api.add_namespace(user_ns, path='/user')
#api.add_namespace(auth_ns)