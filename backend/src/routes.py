from fastapi import APIRouter   
from src.database.models import StudentEligibilityRequest
from src.services.eligibility import EligibilityChecker


router = APIRouter()


@router.post("/EligibilityChecker")
def elig(student: StudentEligibilityRequest):
    E1 = EligibilityChecker()
    E1.check_eligibility(student)