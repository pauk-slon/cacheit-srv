from aiohttp import web

from .routes import setup_routes


def init(**kwargs):
    app = web.Application()
    setup_routes(app)
    web.run_app(app, **kwargs)
    return app
