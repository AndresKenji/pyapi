import os
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from datetime import datetime

router = APIRouter(
    tags=["hello","main_page"],
    responses={404:{"description":"Not Found"}}
)

template_dir = os.path.join(os.path.dirname(__file__), '../templates')
templates = Jinja2Templates(directory=template_dir)


@router.get("/",summary="Retorna un documento html con la bienvenida y la hora", response_class=HTMLResponse)
async def hello(request:Request):
    return templates.TemplateResponse("greatings.html", {"request":request, "date":datetime.now()})