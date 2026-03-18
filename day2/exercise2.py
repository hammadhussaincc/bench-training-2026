"""Store 5 students as a list of dicts: [{name, scores: [list of scores], subject}].
Write functions: calculate_average(scores), get_grade(avg), class_topper(students).
Print a formatted report: student name | avg score | grade. Bold the top scorer's row (add '***
TOP ***' to their line).
Bonus: sort the report by average score (descending) without modifying the original list."""

class ReportCard:
    def __init__(self, students):
        self.students = students
        
    def calculate_average(self, scores):
        return sum(scores) / len(scores)

    def get_grade(self, avg):
        if avg >= 80:
            return "A"
        elif avg >= 70:
            return "B"
        else:
            return "C"
        
    def class_topper(self):
        return max(self.students, key=lambda s: self.calculate_average(s["scores"]))
    
    def print_report(self):
        top_student = self.class_topper()
        sorted_students = sorted(self.students, key=lambda s: self.calculate_average(s["scores"]), reverse=True)
        print(f"{'Student Name':<10} | {'Avg Score':<9} | Grade")
        print("-"*32)
        for s in sorted_students:
            avg = self.calculate_average(s["scores"])
            grade = self.get_grade(avg)
            line = f"{s['name']:<10} | {avg:<9.2f} | {grade}"
            if s == top_student:
                line += " ***TOP***"
            print(line)
            
students = [
    {"name": "Ali", "scores": [85, 90, 78], "subject": "Math"},
    {"name": "Sara", "scores": [92, 88, 95], "subject": "Science"},
    {"name": "Zara", "scores": [70, 65, 80], "subject": "English"},
    {"name": "Hassan", "scores": [60, 58, 72], "subject": "History"},
    {"name": "Amina", "scores": [88, 82, 91], "subject": "Math"}
    ]
    
if __name__=="__main__":
    report = ReportCard(students=students)
    report.print_report()
        