import random
from user import User  # Assuming User class is defined in user.py

class Teacher(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = [
            "str is a data type in Python",
            "programming is hard, but it's worth it",
            "JavaScript async web request",
            "Python function call definition",
            "object-oriented teacher instance",
            "programming computers hacking learning terminal",
            "pipenv install pipenv shell",
            "pytest -x flag to fail fast",
        ]
    

    def teach(self):
        print(random.choice(self.knowledge))
        pass

simon = Teacher("love","bi")
print(simon.teach())