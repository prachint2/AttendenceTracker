from fastapi import FastAPI, Depends
from students.schemas import Record, AbsentTracker, Roster
from sqlalchemy.orm import Session
from students.database import engine, SessionLocal, Base, get_db
from students.models import Student
from typing import List
from . import models

models.Base.metadata.create_all(bind=engine)


app = FastAPI()




   
# POST route to create a record
@app.post("/record")
def create_record(request: Record, db: Session = Depends(get_db)):
    new_student = Student(id = request.id, name = request.name, age = request.age, is_present= request.is_present)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student

@app.get("/record")
def get_all(db: Session = Depends(get_db)):
   get_records = db.query(Student).all()
   return get_records

# GET route to fetch a record (example: /record?id=123)
@app.get("/record/{id}")
def get(id, db: Session = Depends(get_db)):
    return db.query(Student).filter(Student.id == id).first()


@app.delete("/record")
def deletion(id, db: Session = Depends(get_db)):
    db.query(Student).filter(Student.id == id).delete()
    db.commit()
    return 'deleted'


@app.put("/record")
def update(id, status: AbsentTracker, db: Session = Depends(get_db)):
    db.query(Student).filter(Student.id == id).update(status.dict(exclude_unset=True))
    db.commit()
    return 'updated'



@app.get("/record/roster", response_model=List[Roster])
def get_roster(db: Session = Depends(get_db)):
   roster_name = db.query(Student).all()
   print("roster_name", roster_name)
   return roster_name

