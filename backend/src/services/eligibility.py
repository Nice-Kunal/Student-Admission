from requests import request

from src.services.validator import validate_student
import json





class EligibilityChecker:
    def check_eligibility(self, student):

        data = student.model_dump()
        course = data.get("desired_course")
        marks = data.get("marks")
        jee = data.get("qualification_exam")
        

        

        # ----------------------
        # ENGINEERING COURSES
        # ----------------------

        engineering_courses = {
            "Computer Science Engineering": 75,
            "Mechanical Engineering": 70,
            "Electrical Engineering": 70,
            "Civil Engineering": 65,
            "Electronics and Communication Engineering": 70
        }

        if course in engineering_courses:

            if not exams.get("JEE"):
                return {
                    "eligible": False,
                    "message": "JEE qualification required"
                }

            pcm_average = (
                marks.get("Physics", 0)
                + marks.get("Chemistry", 0)
                + marks.get("Mathematics", 0)
            ) / 3

            cutoff = engineering_courses[course]

            if pcm_average >= cutoff:
                return {
                    "eligible": True,
                    "message": f"Eligible for {course}"
                }

            return {
                "eligible": False,
                "message": f"PCM average should be at least {cutoff}%"
            }

        # ----------------------
        # MEDICAL COURSES
        # ----------------------

        medical_courses = {
            "MBBS": 85,
            "BDS": 80,
            "BAMS": 75,
            "BHMS": 75,
            "BPT": 70
        }

        if course in medical_courses:

            if not exams.get("NEET"):
                return {
                    "eligible": False,
                    "message": "NEET qualification required"
                }

            pcb_average = (
                marks.get("Physics", 0)
                + marks.get("Chemistry", 0)
                + marks.get("Biology", 0)
            ) / 3

            cutoff = medical_courses[course]

            if pcb_average >= cutoff:
                return {
                    "eligible": True,
                    "message": f"Eligible for {course}"
                }

            return {
                "eligible": False,
                "message": f"PCB average should be at least {cutoff}%"
            }

        # ----------------------
        # COMMERCE COURSES
        # ----------------------

        commerce_courses = [
            "B.Com",
            "BBA",
            "BBM",
            "CA"
        ]

        if course in commerce_courses:

            required_subjects = [
                "Accountancy",
                "Business Studies",
                "Economics"
            ]

            for subject in required_subjects:
                if subject not in marks:
                    return {
                        "eligible": False,
                        "message": f"{subject} subject required"
                    }

            return {
                "eligible": True,
                "message": f"Eligible for {course}"
            }

        # ----------------------
        # HUMANITIES COURSES
        # ----------------------

        humanities_courses = {
            "BA in History":
                ["History", "Political Science", "Geography"],

            "BA in Psychology":
                ["Psychology", "Sociology", "English"],

            "BA in Sociology":
                ["Sociology", "Political Science", "History"],

            "BA in Political Science":
                ["Political Science", "History", "Geography"],

            "BA in English":
                ["English", "History", "Political Science"]
        }

        if course in humanities_courses:

            required_subjects = humanities_courses[course]

            for subject in required_subjects:
                if subject not in marks:
                    return {
                        "eligible": False,
                        "message": f"{subject} subject required"
                    }

            return {
                "eligible": True,
                "message": f"Eligible for {course}"
            }

        # ----------------------
        # INVALID COURSE
        # ----------------------

        return {
            "eligible": False,
            "message": "Invalid Course"
        }