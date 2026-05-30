from pydantic import BaseModel, Field
from typing import Literal


# Qualification Exam Model
class QualificationExam(BaseModel):
    JEE: bool = Field(..., description="JEE qualification status")


# Marks Model
class Marks(BaseModel):
    Physics: int = Field(..., ge=0, le=100)
    Chemistry: int = Field(..., ge=0, le=100)
    Mathematics: int = Field(..., ge=0, le=100)
    English: int = Field(..., ge=0, le=100)

    Computer_Science: int = Field(
        ...,
        alias="Computer Science",
        ge=0,
        le=100
    )

    Physical_Education: int = Field(
        ...,
        alias="Physical Education",
        ge=0,
        le=100
    )


# Main Student Model
class StudentEligibilityRequest(BaseModel):

    name: str = Field(..., min_length=3, max_length=50)

    age: int = Field(..., ge=17, le=25)

    gender: Literal["Male", "Female", "Other"]

    desired_course: str

    qualification_exam: QualificationExam

    marks: Marks