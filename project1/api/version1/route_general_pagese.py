"""
Not needed from a api perspective
"""
from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")
core_routes = APIRouter()

@core_routes.get("/")
async def home(request: Request):
    return templates.TemplateResponse("homepage.html",{"request":request})
