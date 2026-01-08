from asgiref.wsgi import WsgiToAsgi
from src.main import app  # import your FastAPI app from src.main

# Wrap FastAPI ASGI app for WSGI
wsgi_app = WsgiToAsgi(app)
