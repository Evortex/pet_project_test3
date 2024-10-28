from sqlalchemy.orm import Session

from schemas import project_dto
from models.project import Project


# Функция для создания проекта, принимает в качестве аргументов DTO класса Project и экземпляр класса Session.
def create_project(project_dto: project_dto.Project, db: Session):
    # Создаем экземпляр класса Project, используя данные из project_dto.
    project = Project(name=project_dto.name, category=project_dto.category,
                      description=project_dto.description, author=project_dto.author)

    # Пытаемся выполнить код в блоке try.
    try:
        # Добавляем экземпляр класса Project в сессию.
        db.add(project)
        # Коммитим изменения в БД.
        db.commit()
        # Обновляем экземпляр класса Project.
        db.refresh(project)
    except Exception as e:
        # Если произошла ошибка, выводим ее в консоль.
        print(e)

    # Возвращаем сохраненный экземпляр класса Project.
    return project


# Функция для получения всех проектов, принимает в качестве аргумента экземпляр класса Session.
def get_all_projects(db: Session):
    # Получаем все проекты из БД, используя метод query().all(), затем возвращаем их.
    return db.query(Project).all()


# Начало (пиши код внутри комментария)
# Функция для получения проекта по id, принимает в качестве аргументов id проекта и экземпляр класса Session.
def get_by_id(id: int, db: Session):
    # Получаем проект из БД, используя метод query().get(), затем возвращаем его.
    return db.query(Project).get(id)
# Конец


# Функция для обновления проекта, принимает в качестве аргументов id проекта,
# DTO класса Project и экземпляр класса Session.
def update_project(id: int, project_dto: project_dto.Project, db: Session):
    # Получаем проект из БД, используя метод query().get().
    project = db.query(Project).get(id)

    # Обновляем поля проекта, используя данные из project_dto.
    project.name = project_dto.name
    project.category = project_dto.category
    project.description = project_dto.description
    project.author = project_dto.author

    # Пытаемся выполнить код в блоке try.
    try:
        # Добавляем экземпляр класса Project в сессию.
        db.add(project)
        # Коммитим изменения в БД.
        db.commit()
        # Обновляем экземпляр класса Project.
        db.refresh(project)
    except Exception as e:
        # Если произошла ошибка, выводим ее в консоль.
        print(e)

    # Возвращаем обновленный экземпляр класса Project.
    return project


# Функция для удаления проекта, принимает в качестве аргументов id проекта и экземпляр класса Session.
def delete_project(db: Session, id: int):
    # Получаем проект из БД, используя метод query().filter(), затем удаляем его функцией delete().
    project = db.query(Project).filter(Project.id == id).delete()

    # Коммитим изменения в БД.
    db.commit()

    # Возвращаем удаленный экземпляр класса Project.
    return project
