
from typing import Optional

from fastapi import FastAPI
import models
import database
from sqlalchemy.orm import sessionmaker
from router import user


# DBコンテナとappコンテナが更新するために必要なもの

engine = database.engine
models.Base.metadata.create_all(engine)
DBsession = sessionmaker(bind=engine)
session = DBsession()

# パスオペレーションの設定
app = FastAPI()
app.include_router(user.router)


