"""
TEC — The Everything Calculator
FastAPI application entry point.
"""

import os
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# diretório base do projeto (onde este arquivo vive)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = FastAPI(title="TEC", description="The Everything Calculator")

# arquivos estáticos (CSS, futuras imagens) servidos em /static/...
app.mount(
    "/static",
    StaticFiles(directory=os.path.join(BASE_DIR, "static")),
    name="static",
)

# motor de templates Jinja2, lendo da pasta templates/
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))


# ---------- rotas ----------

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    """Página inicial: introdução ao TEC e ao autor."""
    return templates.TemplateResponse(
        "home.html",
        {"request": request, "page": "home"},
    )


# novas rotas entram aqui conforme módulos forem adicionados:
#
# @app.get("/portfolio", response_class=HTMLResponse)
# def portfolio_page(request: Request):
#     return templates.TemplateResponse(
#         "portfolio.html",
#         {"request": request, "page": "portfolio"},
#     )
