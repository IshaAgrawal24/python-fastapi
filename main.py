from sqlalchemy import create_engine, Column, Integer, String, Enum
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from fastapi import FastAPI, Depends, status, HTTPException
import enum

app = FastAPI()

DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

sessionLocal = sessionmaker(bind=engine)
Base = declarative_base()


class TodoStatus(str, enum.Enum):
    COMPLETED = "Completed"
    IN_PROCESS = "In Process"
    PENDING = "Pending"


class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    status = Column(Enum(TodoStatus))


Base.metadata.create_all(bind=engine)


def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home(db: Session = Depends(get_db)):
    return {"message": "DB connected successfully!"}


# CREATE API
@app.post("/create-todo", status_code=status.HTTP_201_CREATED)
def create_todo(title: str, status: TodoStatus, db: Session = Depends(get_db)):
    todo = Todo(title=title, status=status)
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return {"status_code": 201, "message": "Todo created successfully!", "data": todo}


# READ ALL DATA
@app.get("/todos")
def todos_list(db: Session = Depends(get_db)):
    todo_list = db.query(Todo).all()
    return {
        "status_code": 200,
        "message": "Data ftched successfully",
        "data": todo_list,
    }


# Read a todo data from a particular ID
@app.get("/todo/{id}")
def get_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="ID not found!")
    return {"status_code": 200, "message": "Data fetched successfully", "data": todo}


# UPDATE THE DATA
@app.put("/edit-todo/{id}")
def edit_todo(
    id: int, title: str, status: TodoStatus, db: Session = Depends(get_db)
):
    todo = db.query(Todo).filter(Todo.id == id).first()

    if not todo:
        raise HTTPException(status_code=404, detail="ID not found!")

    todo.title = title
    todo.status = status

    db.commit()
    db.refresh(todo)
    return {"status_code": 200, "message": "Data fetched successfully", "data": todo}


# DELETE THE TODO..
@app.delete("/remove-todo/{id}")
def remove_todo(id: int, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="ID not found")
    
    db.delete(todo)
    db.commit()
    
    return {
        "status_code": 200,
        "message": "Task deleted successfully!",
        "data": todo
    }