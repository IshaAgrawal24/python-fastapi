from sqlalchemy import create_engine, Column, Integer, String, Enum
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from fastapi import FastAPI, Depends
import enum

app = FastAPI()

DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    DATABASE_URL, 
    connect_args={"check_same_thread": False}
    )

sessionLocal = sessionmaker(bind = engine)
Base = declarative_base()

class TodoStatus(str, enum.Enum):
    COMPLETED = "Completed"
    IN_PROCESS = "In Process"
    PENDING = "Pending"
    
class Todo(Base):
    __tablename__="todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    status = Column(Enum(TodoStatus))

Base.metadata.create_all(bind = engine)

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home(db: Session = Depends(get_db)):
    return {
        "message": "DB connected successfully!"
    }