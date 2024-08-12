from sqlmodel import Session, create_engine, select, SQLModel

from app import crud
from app.core.config import settings
from app.models import User, UserCreate

# engine = create_engine(str(settings.SQLALCHEMY_DATABASE_URI))
# engine = create_engine(str(settings.SQLALCHEMY_DATABASE_URI), connect_args={"check_same_thread": False})
engine = create_engine(settings.SQLALCHEMY_DATABASE_URI, connect_args={"check_same_thread": False})


# make sure all SQLModel models are imported (app.models) before initializing DB
# otherwise, SQLModel might fail to initialize relationships properly
# for more details: https://github.com/fastapi/full-stack-fastapi-template/issues/28


def init_db(session: Session) -> None:
    # Tables should be created with Alembic migrations
    # But if you don't want to use migrations, create
    # the tables un-commenting the next lines
    # from sqlmodel import SQLModel

    # from app.core.engine import engine
    # This works because the models are already imported and registered from app.models
    # SQLModel.metadata.create_all(engine)

    # 如果不使用 Alembic 进行迁移，可以使用以下代码创建数据库表
    SQLModel.metadata.create_all(engine)
    user = session.exec(
        select(User).where(User.email == settings.FIRST_SUPERUSER)
    ).first()
    if not user:
        user_in = UserCreate(
            email=settings.FIRST_SUPERUSER,
            password=settings.FIRST_SUPERUSER_PASSWORD,
            is_superuser=True,
        )
        user = crud.create_user(session=session, user_create=user_in)
