# GET обработчик корневого пути / с тегом root, возвращает в ответе HTML страницу.
@app.get('/', tags=["root"], response_class=HTMLResponse)
# Функция обработчик корневого пути.
def get_index(request: Request):
    # Возвращаем рендер шаблона index.html из папки templates, передаем в него запрос.
    return templates.TemplateResponse("index.html", {"request": request})
