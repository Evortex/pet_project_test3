# Функция для получения проекта по id, принимает в качестве аргументов id проекта и экземпляр класса Session.
def get_by_id(id: int, db: Session):
    # Получаем проект из БД, используя метод query().get(), затем возвращаем его.
    return db.query(Project).get(id)
