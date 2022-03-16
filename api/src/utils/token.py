
session_manage = {
    "token12345": "mch001"
}


def auth_by_token(token):
    return session_manage.get(token)