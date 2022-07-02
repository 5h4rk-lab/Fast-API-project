from fastapi import FastAPI, Path, Query 
from typing import Optional
from pydantic import BaseModel

app = FastAPI()
# path parameters 
students = {
    1:{
        "name":"john",
        "class":"ks07",
        "age":17
    },
    2:{
        "name":"charan",
        "class":"ks07",
        "age":19
    },
    3:{
        "name":"sandeep",
        "class":"ks07",
        "age":20
    },
    4:{
        "name":"prafull",
        "class":"ks07",
        "age":23
    }
}

class Student(BaseModel):
    name: str
    age: int
    year: str

class UpdateStudent(BaseModel):
    name: Optional[str]=None
    age: Optional[int]=None
    year: Optional[str]=None


@app.get("/")
def index():
    return {"name" : "First API"}

@app.get("/get-student/{student_id}")
def get_students(student_id : int = Path(None, description="enter The Id you want to view.",)):
    if student_id not in students:
        return {"error": "Student does not exist"}
    return students[student_id]

@app.get("/get-by-name/{student_id}")
def get_student(*, student_id:int, name:Optional[str] = None ):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
        return {"Data" : "Not found"}

@app.post("/create-student/{student_id}")

def create_student(*, student_id: int = Path(None, description="create a student with id:"), student: Student):
    if student_id in students:
        return {"Error" : "student exists"}  

    students[student_id] = student
    return students[student_id]

@app.put("/update-student/{student_id}")
def update_student(student_id: int,student:UpdateStudent):
    if student_id not in students:
        return {"error": "Student does not exist"}
    
    if student.name != None:
        students[student_id].name = student.name

    if student.age != None:
        students[student_id].age = student.age
    
    if student.year != None:
        students[student_id].year = student.year 

    return students[student_id]

@app.delete("/delete-student/{student_id}")
def delete_Student(student_id: int):
    if student_id not in students:
        return {"error": "Student does not exist or alredy deleted"}
    del students[student_id]
    return {"Message" : " Student deleted successfully"}

