from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from applications.main_app.routes import api_router
from applications.error_processing import exception_handlers


def create_app(debug=True):
    app = FastAPI(exception_handlers=exception_handlers)
    app.mount('/static', StaticFiles(directory='static'), name='static')
    app.mount('/media', StaticFiles(directory='media'), name='media')
    app.include_router(api_router)
    return app
