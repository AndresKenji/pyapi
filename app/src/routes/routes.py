from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from datetime import datetime

router = APIRouter(
    tags=["hello","main_page"],
    responses={404:{"description":"Not Found"}}
)

templates = Jinja2Templates(directory="/app/src/templates")


@router.get("/",summary="Retorna un documento html con la bienvenida y la hora", response_class=HTMLResponse)
async def hello(request:Request):
    return templates.TemplateResponse("/app/src/templates/greatings.html", {"request":request, "date":datetime.now()})