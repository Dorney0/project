from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from uvicorn import main as uvicorn_main

from sql_app import SessionLocal, crud, schemas

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # значение порта Vue
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/users/{user_id}/items/", response_model=schemas.Item)
def create_item_for_user(
        user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
):
    return crud.create_user_item(db=db, item=item, user_id=user_id)


@app.get("/items/", response_model=list[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items


@app.post("/register")
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    try:
        db_user = crud.get_user_by_email(db, email=user.email)
        if db_user:
            raise HTTPException(status_code=400, detail="Email already registered")
        return crud.create_user(db=db, user=user)
    except Exception as e:
        # Печатаем дополнительные сведения об ошибке
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


# Новые конечные точки для работы с изображениями
@app.post("/flowers/", response_model=schemas.Flower)
def create_flower(flower: schemas.FlowerCreate, db: Session = Depends(get_db)):
    return crud.create_flower(db=db, flower=flower)

@app.get("/flowers/", response_model=list[schemas.Flower])
def read_flowers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    flowers = crud.get_flowers(db, skip=skip, limit=limit)
    return flowers

@app.get("/flowers/{flower_id}", response_model=schemas.Flower)
def read_flower(flower_id: int, db: Session = Depends(get_db)):
    db_flower = crud.get_flower(db, flower_id=flower_id)
    if db_flower is None:
        raise HTTPException(status_code=404, detail="Flower not found")
    return db_flower
