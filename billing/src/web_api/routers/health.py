from fastapi import APIRouter, status

from web_api.routers.v1.schemas.responses import SimpleResponse

router = APIRouter()


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=SimpleResponse,
)
async def health() -> SimpleResponse:
    """Эндпоинт для хэлсчека.
    \f
    Returns:
        Отклик со статусом 200, говорящий о том, что сервис жив.
    """
    return SimpleResponse(message="Alive!")
