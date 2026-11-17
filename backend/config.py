import os


def configuracao():
    return {
        "SECRET_KEY": os.getenv("FLASK_SECRET_KEY"),
        "SESSION_COOKIE_HTTPONLY": True,
        "SESSION_COOKIE_SAMESITE": "Lax",
        "MAX_CONTENT_LENGTH": 64 * 1024,
    }
