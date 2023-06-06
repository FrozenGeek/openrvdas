"""
    cgi-bin/secret.py

    Contains the secret we use for JWT encryption
"""

import sys
import os
import jwt
from datetime import datetime, timedelta
# from os.path import dirname, realpath

# sys.path.append(dirname(dirname(dirname(realpath(__file__)))))
# from sqlite_gui.sqlite_server_api import SQLiteServerAPI as serverapi # noqa E402
# api = serverapi()
##############################################################################
##############################################################################
#
#     You should (probably) change the SECRET to something,
#     you know, .... secret.  And keep it that way.  Otherwise
#     anyone could generate their OWN jwt and you'd think it
#     was peachy.
#
##############################################################################
##############################################################################
# https://xkcd.com/936/
SECRET = "correct horse battery staple"
#    LEN:"12345678901234567890123456789012"
# Ideally, SHA256 passwords/phrases *should* be at least 32 bytes


##############################################################################
def validate_token():
    """ We should have received a JWT in the Authorization header.
        Validate it.
    """

    auth_header = os.environ.get('HTTP_AUTHORIZATION', None)
    # Should be something like "Bearer [3 dot separated groups of Hex]
    if not auth_header:
        print("No 'Authorization' header found", file=sys.stderr)
        return None

    auth_split = auth_header.split(' ')
    if len(auth_split) > 1:
        token = auth_split[1]
    else:
        print("No Auth Token found", file=sys.stderr)
        return None
    payload = {}
    try:
        payload = jwt.decode(token, SECRET, algorithms="HS256")
    except jwt.PyJWTError as err:
        print("PyJWTError: ", err, file=sys.stderr)
        return None

    return payload.get('name', None)


##############################################################################
def validate_csrf(token):
    """ Validate a JWT used for CSRF protection

        In this instance, we are not concerned with
        payload contents, only that the encryption
        is valid and it has not expired
    """

    try:
        jwt.decode(token, SECRET, algorithms="HS256")
    except jwt.PyJWTError as err:
        print("CSRF Error: ", err, file=sys.stderr)
        return False
    else:
        return True


##############################################################################
def short_ttl_jwt(ttl=2):
    """ Build a short lived JWT for JWT for CSRF purposes

        ttl expressed in minutes
    """

    payload_data = {
        "name": 'CSRF Token',
        "exp": datetime.utcnow() + timedelta(minutes=ttl),
        "nbf": datetime.utcnow(),
        "iat": datetime.utcnow()
    }
    our_jwt = jwt.encode(payload_data,
                         SECRET,
                         algorithm="HS256")
    return our_jwt
