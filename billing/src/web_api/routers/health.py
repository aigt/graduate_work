from typing import Dict

from fastapi import APIRouter, status

router = APIRouter()


@router.get("/", status_code=status.HTTP_200_OK)
async def health() -> Dict[str, str]:
    """Эндпоинт для хэлсчека.
    \f
    Returns:
        Отклик со статусом 200, говорящий о том, что сервис жив.
    """
    return {"message": "Alive!"}
