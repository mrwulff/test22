def make_password(p):
    import base64
    import ast

    p2 = base64.b64encode(p.encode("utf-8"))
    p2 = str(p2)

    return p2


def r_password(p):
    import ast
    import base64

    p3 = ast.literal_eval(p)
    return str(base64.b64decode(p3).decode("utf-8"))
