
from sqlalchemy.orm import Session
import models
from sqlalchemy.exc import DBAPIError
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi import HTTPException

# 概要
# dbに対して操作するコード

# user_idをキーにuserの情報を取得する
def get_user(session:Session, user_id:int) -> any:
    response =  session.query(models.User).filter(models.User.user_id == user_id).first()
    if response is None:
        raise HTTPException(status_code=404, detail="user_id is not found")

    return response

# userを新規作成すeる
def create_user(session, user_name:str, user_mail:str ,user_password: str) -> any:
    user_obj = models.User(
        user_mail =  user_mail,
        user_name =  user_name,
        user_password = user_password
    )
    try:
        session.add(user_obj)
    except:
        raise HTTPException(status_code=500, detail='error')
    session.commit()
    session.refresh(user_obj)
    return user_obj



# userのpasswordを更新する。
def update_password(session:Session, user_id:int, user_mail:str,user_password:str) -> any:
    response = get_user(session,user_id)
    # user_idがある場合のみの処理でよい。
    # user_idがない場合は、get_user関数でHTTPexceptionが返るので、この関数内では不要。
    if response:
        if response.user_mail == user_mail:
            response.user_password = user_password
            session.commit()
            # コミットしたresponseを取得するには、再度sessionを取得する必要がある。
            session.refresh(response)
            return response
        elif response.user_mail != user_mail:
            raise HTTPException(status_code=404, detail='user_mail is wrong')


# userを削除する
def delete_user(session:Session, user_id:int,user_mail:str, user_password:str):
    # user_idがデータベースに存在しているかを確認する
    response = get_user(session, user_id)
    # user_idがデータベースに存在している場合
    if response:
        # idのuserのデータが空ではなく、かつ、malとpasswordともに合致しているか
        if response.user_mail == user_mail and response.user_password == user_password:
            session.delete(response)
            session.commit()

            return response
        else:
            raise HTTPException(status_code=404, detail="not match")


