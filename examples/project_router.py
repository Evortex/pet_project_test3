# GET обработчик пути /project/{id} с тегом project, возвращает в ответе HTML страницу.
@router.get('/{id}', tags=["project"], response_class=HTMLResponse)
# Функция get_by_id, принимает в параметрах запроса id проекта, а также зависимость от класса Session.
def get_by_id(request: Request, id: int = None, db: Session = Depends(get_db)):

    # Вызываем функцию get_by_id из project_service, передаем ей id проекта и экземпляр сессии.
    project = project_service.get_by_id(id, db)

    # Возвращаем рендер шаблона project_page.html из папки templates, передаем в него запрос, id проекта и проект.
    return templates.TemplateResponse("project_page.html", {"request": request, "id": id, "project": project})
