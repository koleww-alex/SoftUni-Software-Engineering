class Programmer:
    def __init__(self, name: str, language: str, skills: int):
        self.name = name
        self.language = language
        self.skills = skills

    def watch_course(self, course_name: str, course_language: str, skills_earned: int):
        if self.language == course_language:
            self.skills += skills_earned
            return f'{self.name} watched {course_name}'
        return f'{self.name} does not know {course_language}'

    def change_language(self, new_language: str, skills_needed: int):
        if skills_needed > self.skills:
            return f'{self.name} needs {skills_needed - self.skills} more skills'
        elif new_language == self.language:
            return f'{self.name} already knows {new_language}'
        else:
            old_language = self.language
            self.language = new_language
            return f'{self.name} switched from {old_language} to {new_language}'
