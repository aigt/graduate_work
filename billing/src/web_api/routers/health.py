from fastapi import APIRouter, status

from web_api.routers.v1.schemas.responses import SimpleResponse

router = APIRouter()


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    summary="Хэлсчек.",
)
async def health() -> SimpleResponse:
    """Эндпоинт проверяет жив ли сервиса и возвращает статус 200 если всё хорошо.
    \f
    Returns:
        SimpleResponse: Отклик со статусом 200, говорящий о том, что сервис жив.
    """
    return SimpleResponse(message="Alive!")
