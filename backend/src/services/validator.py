import re
from fastapi import HTTPException
from src.database.models import StudentEligibilityRequest
from src.utils.constants import VALID_COURSES

def validate_student(student: StudentEligibilityRequest):

    # ==========================================
    # NAME VALIDATION
    # ==========================================

    if not re.match(r'^[A-Za-z ]+$', student.name):

        raise HTTPException(
            status_code=400,
            detail="Name should contain only letters and spaces."
        )

    # ==========================================
    # AGE VALIDATION
    # ==========================================

    if not (17 <= student.age <= 25):

        raise HTTPException(
            status_code=400,
            detail="Age should be between 17 and 25."
        )

    # ==========================================
    # GENDER VALIDATION
    # ==========================================

    valid_genders = ["Male", "Female", "Other"]

    if student.gender not in valid_genders:

        raise HTTPException(
            status_code=400,
            detail="Gender must be Male, Female, or Other."
        )

    # ==========================================
    # COURSE VALIDATION
    # ==========================================

    if student.desired_course not in VALID_COURSES:

        raise HTTPException(
            status_code=400,
            detail="Invalid desired course."
        )

    # ==========================================
    # MARKS VALIDATION
    # ==========================================

    # Convert Marks model into dictionary
    marks_dict = student.marks.dict(by_alias=True)

    for subject, marks in marks_dict.items():

        if not (0 <= marks <= 100):

            raise HTTPException(
                status_code=400,
                detail=f"{subject} marks must be between 0 and 100."
            )

    # ==========================================
    # SUCCESS RESPONSE
    # ==========================================

    return {
        "message": "Validation Successful"
    }