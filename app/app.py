from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from app import include_routers


def get_application() -> FastAPI:
    app = FastAPI(
        title="Training Tracker API",
        description="description",
        version="0.1.0",
        default_response_class=ORJSONResponse,
        contact={
            "name": "Paulechka Uladzislau",
        }
    )

    include_routers(app)
    return app
