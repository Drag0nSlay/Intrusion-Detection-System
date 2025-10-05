import os
from flask import request, jsonify

def require_api_key(func):
    def wrapper(*args, **kwargs):
        key = request.headers.get("X-API-Key")
        if key != os.getenv("API_KEY"):
            return jsonify({"error": "Unauthorized"}), 401
        return func(*args, **kwargs)
    wrapper.__name__ = func.__name__
    return wrapper