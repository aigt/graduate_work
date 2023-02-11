from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/cancel", response_class=HTMLResponse)
async def cancel_page(request: Request):
    """Метод для возвращения шаблона неуспешной страницы оплаты.

    Args: request: Request - запрос
    Returns: Jinja2Templates - шаблон страницы неуспешной оплаты html
    """
    return templates.TemplateResponse("cancel.html", {"request": request})
