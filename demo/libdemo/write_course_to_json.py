from course import Course
import json

courses = [Course('Java', 36, 8000),
           Course('C', 30, 5000),
           Course("DS", 30, 10000)
           ]

with open("courses.json", "wt") as f:
    # Convert list of Courses to list of dict
    #course_dicts = [c.__dict__ for c in courses]
    course_dicts = [c.to_dict() for c in courses]
    json.dump(course_dicts, f)
