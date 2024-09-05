
from fastapi import APIRouter,Depends, HTTPException
from database import SessionLocal, engine
import models,crud
import schemas
from sqlalchemy.orm import Session
import typing

# 概要
# APIの受け口

# 依存関係を作成する
# リクエスト毎に独室したデータベースセッション(データベースへの接続)を持つ必要がある。
models.Base.metadata.create_all(bind = engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db # returnではなくyieldがを記載することで繰り返し利用することが可能。
    finally:
        db.close

# ユーザーを取得する
@router.get("/user/get")
def read_user(user_id:int, db:Session=Depends(get_db)) -> any:
    return crud.get_user(db, user_id)

    # idをキーに取得したデータを返す

# ユーザーを新規作成
@router.post("/user/create")
def create_user(user_name:str,user_mail:str, user_password:str, db:Session = Depends(get_db)):
    return  crud.create_user(db, user_name,user_mail, user_password)


# passwordを更新する。
@router.put("/user/update")
def update_password(user_id:int, user_mail:str, user_password:str, db:Session = Depends(get_db) ):
    return crud.update_password(db,user_id, user_mail,user_password)

# ユーザーを削除する
@router.delete("/user/delete")
def delete_user(user_id:int, user_mail:str, user_password:str, db:Session = Depends(get_db)):
    return crud.delete_user(db, user_id,user_mail, user_password)


