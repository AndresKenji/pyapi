from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from datetime import datetime

router = APIRouter(
    tags=["hello","main_page"],
    responses={404:{"description":"Not Found"}}
)

templates = Jinja2Templates(directory="src/templates")


@router.get("/", response_class=HTMLResponse)
async def hello(request:Request):
    return templates.TemplateResponse("greatings.html", {"request":request, "date":datetime.now()})