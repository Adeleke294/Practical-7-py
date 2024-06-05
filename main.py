class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.subjects = {}

    def add_subject(self, subject, score):
        self.subjects[subject] = score

    def calculate_grade(self):
        total_score = sum(self.subjects.values())
        average_score = total_score / len(self.subjects)
        if average_score >= 90:
            return 'A'
        elif average_score >= 80:
            return 'B'
        elif average_score >= 70:
            return 'C'
        elif average_score >= 60:
            return 'D'
        else:
            return 'F'

    def generate_report(self):
        report = f"Report for {self.name} (ID: {self.student_id})\n"
        report += "Subject Scores:\n"
        for subject, score in self.subjects.items():
            report += f"  {subject}: {score}\n"
        report += f"Overall Grade: {self.calculate_grade()}\n"
        return report


class School:
    def __init__(self):
        self.students = {}

    def add_student(self, student_id, name):
        if student_id not in self.students:
            self.students[student_id] = Student(student_id, name)
        else:
            print(f"Student with ID {student_id} already exists.")

    def add_score(self, student_id, subject, score):
        if student_id in self.students:
            self.students[student_id].add_subject(subject, score)
        else:
            print(f"No student found with ID {student_id}.")

    def generate_student_report(self, student_id):
        if student_id in self.students:
            return self.students[student_id].generate_report()
        else:
            return f"No student found with ID {student_id}."

    def generate_all_reports(self):
        reports = ""
        for student_id in self.students:
            reports += self.students[student_id].generate_report() + "\n"
        return reports


def main():
    school = School()
    
    while True:
        print("\n--- Secondary School Result Computation System ---")
        print("1. Add Student")
        print("2. Add Score")
        print("3. Generate Student Report")
        print("4. Generate All Reports")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            student_id = input("Enter Student ID: ")
            name = input("Enter Student Name: ")
            school.add_student(student_id, name)

        elif choice == '2':
            student_id = input("Enter Student ID: ")
            subject = input("Enter Subject: ")
            score = float(input("Enter Score: "))
            school.add_score(student_id, subject, score)

        elif choice == '3':
            student_id = input("Enter Student ID: ")
            print(school.generate_student_report(student_id))

        elif choice == '4':
            print(school.generate_all_reports())

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
