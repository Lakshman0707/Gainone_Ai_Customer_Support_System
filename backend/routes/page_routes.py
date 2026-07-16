from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter(tags=["Pages"])

templates = Jinja2Templates(directory="templates")


@router.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        "login.html",
        {
            "request": request
        }
    )


@router.get("/login")
def login(request: Request):
    return templates.TemplateResponse(
        "login.html",
        {
            "request": request
        }
    )


@router.get("/register")
def register(request: Request):
    return templates.TemplateResponse(
        "register.html",
        {
            "request": request
        }
    )


@router.get("/dashboard")
def dashboard(request: Request):
    return templates.TemplateResponse(
        "dashboard.html",
        {
            "request": request
        }
    )


@router.get("/chat")
def chat(request: Request):
    return templates.TemplateResponse(
        "chat.html",
        {
            "request": request
        }
    )