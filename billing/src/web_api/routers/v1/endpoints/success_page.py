from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates(directory="templates")


@router.get("/success", response_class=HTMLResponse)
async def success_page(request: Request):
    """Метод для возвращения шаблона успешной страницы оплаты.

    Args: request: Request - запрос
    Returns: Jinja2Templates - шаблон успешной страницы оплаты html
    """
    return templates.TemplateResponse("success.html", {"request": request})
