import base64
import ast


def make_password(password):

    if password is None:
        raise ValueError("Cannot encode a None password")

    encoded = base64.b64encode(
        password.encode("utf-8")
    )

    # Keep the old format:
    # "b'...'"
    return str(encoded)


def r_password(password):

    if password is None:
        raise ValueError("Rhino password is missing")

    if not password:
        raise ValueError("Rhino password is empty")

    try:
        value = ast.literal_eval(password)

        if not isinstance(value, bytes):
            raise ValueError(
                "Stored Rhino password is not a bytes literal"
            )

        return base64.b64decode(value).decode("utf-8")

    except Exception as e:

        raise ValueError(
            f"Invalid stored Rhino password: {e}"
        ) from e