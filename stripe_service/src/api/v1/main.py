import logging

import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from core import config
from core.logger import LOGGING

from api.v1 import payment

app = FastAPI(
    title=config.PROJECT_NAME,
    docs_url='/api/openapi',
    openapi_url='/api/openapi.json',
    default_response_class=ORJSONResponse,
)

app.include_router(payment.router, prefix='/api/v1', tags=['payment'])

if __name__ == '__main__':

    uvicorn.run(
        'main:app',
        host='0.0.0.0',
        port=8000,
        log_config=LOGGING,
        log_level=logging.DEBUG,
    )
