from requests import request

from src.services.validator import validate_student
import json





class EligibilityChecker:
    def check_eligibility(self, student):

        data = student.model_dump()
        course = data.get("desired_course")
        marks = data.get("marks")
        jee = data.get("qualification_exam")
        

        if jee :=True:
            print("Student is eligible for admission.")
            if data.get("desired_course") == "Computer Science":
                

        # print(data.get("desired_course"))