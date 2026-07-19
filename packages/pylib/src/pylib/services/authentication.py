"""Authentication service functions."""


def login(email: str, password: str) -> dict[str, str]:
    return {
        "status": "ok",
        "message": "Login successful",
        "email": email,
    }


def register(email: str, password: str, name: str) -> dict[str, str]:
    return {
        "status": "ok",
        "message": "Registration successful",
        "email": email,
        "name": name,
    }


def forgot_password(email: str) -> dict[str, str]:
    return {
        "status": "ok",
        "message": "Password reset instructions sent",
        "email": email,
    }


def reset_password(token: str, new_password: str) -> dict[str, str]:
    return {
        "status": "ok",
        "message": "Password reset successful",
        "token": token,
    }
