from functools import wraps
from flask import request, jsonify
from wsgi import app
import jwt


def is_authenticated(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None
        if 'authorization' in request.headers:
            token = request.headers['authorization']

        if not token:
            return jsonify({'message': 'access token not found in request headers[authorization].'})

        try:
            jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
        except:
            return jsonify({'message': 'access token is invalid.'})

        return f(*args, **kwargs)

    return decorator


def is_authenticated_with_user(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None
        if 'authorization' in request.headers:
            token = request.headers['authorization']

        if not token:
            return jsonify({'message': 'access token not found in request headers[authorization].'})

        try:
            user = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
        except:
            return jsonify({'message': 'access token is invalid.'})

        return f(user, *args, **kwargs)

    return decorator