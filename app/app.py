from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from app import include_routers
from app.openapi import DESCRIPTION, TAGS_METADATA


def get_application() -> FastAPI:
    app = FastAPI(
        title="Workout Tracker API",
        description=DESCRIPTION,
        version="0.1.0",
        default_response_class=ORJSONResponse,
        contact={
            "name": "Paulechka Uladzislau",
        },
        openapi_tags=TAGS_METADATA
    )

    include_routers(app)
    return app
