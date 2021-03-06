# -*- coding: utf-8 -*-

from flask_restplus import Api

from .users import api as users
from .posts import api as posts
from .auth import api as auth

api = Api(title='API REST', version='1.0', description='Lista de APIS')

api.add_namespace(users)
api.add_namespace(posts)
api.add_namespace(auth)