# Create a student management system (OOP + files)
import os
import json
from stringprep import b3_exceptions
import tkinter as tk
from tkinter import messagebox

# --- Student Class ---
class Student:
    def __init__(self, student_id, student_name, age, grade):
        self.__student_id = student_id
        self.__student_name = student_name
        self.__age = age
        self.__grade = grade

    # --- Display Student Info ---
    def display_student_info(self):
        print(f"ID: {self.__student_id}")
        print(f"Name: {self.__student_name}")
        print(f"Age: {self.__age}")
        print(f"Grade: {self.__grade}")
        print("-" * 25)

    # --- Convert to dictionary ---
    def to_dict(self):
        return {
            "student_id": self.__student_id,
            "student_name": self.__student_name,
            "age": self.__age,
            "grade": self.__grade
        }

    # --- String Representation ---
    def __str__(self):
        return f"{self.__student_id} - {self.__student_name} ({self.__grade})"


# --- StudentManager Class ---
class StudentManager:
    FILENAME = "students.json"

    def __init__(self):
        self.students = []
        self.load_students()

    def load_students(self):
        """Load students from file"""
        if not os.path.exists(self.FILENAME):
            self.students = []
            return

        with open(self.FILENAME, "r") as f:
            try:
                data = json.load(f)
                # 2 ways to get students data
                # Solution 1
                # self.students = [
                #     Student(
                #         s.get("student_id"),
                #         s.get("student_name") or s.get("student name: "),
                #         s.get("age"),
                #         s.get("grade")
                #     )
                #     for s in data
                # ]

                # Solution 2
                self.students = [Student(**s) for s in data]
            except json.JSONDecodeError:
                self.students = []

    def save_students(self):
        """Save all students into file"""
        with open(self.FILENAME, "w") as f:
            json.dump([s.to_dict() for s in self.students], f, indent=4)

    def add_student(self, student):
        for s in self.students:
            if s.to_dict()["student_id"] == student.to_dict()["student_id"]:
                raise ValueError("Student ID already exists!")
        
        self.students.append(student)
        self.save_students()

    def search_student(self):
        """Search student by ID"""
        sid = input("Enter Student ID to search: ")
        found = next((s for s in self.students if s.student_id == sid), None)
        if found:
            print("\n--- Student Found ---")
            found.display_student_info()
        else:
            print("Student not found!")

    def update_student(self, student):
        """Update existing student info"""
        for i, s in enumerate(self.students):
            if s.to_dict()["student_id"] == student.to_dict()["student_id"]:
                self.students[i] = student
                self.save_students()
                return True
        return False

    def delete_student(self, student_id):
        """Delete student by ID"""
        for s in self.students:
            if s.to_dict()["student_id"] == student_id:
                self.students.remove(s)
                self.save_students()
                return True
        return False

    def get_all(self):
        return self.students

# --- GUI Class ---
class StudentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("480x400")
        self.root.resizable(False, False)
    
        self.manager = StudentManager()

        # --- Title ---
        tk.Label(root, text="Student Management System", font=("Arial",16, "bold")).pack(pady=10)

        # --- Form Frame ---
        form_frame = tk.Frame(root)
        form_frame.pack(pady=5)

        tk.Label(form_frame, text="ID: ").grid(row=0, column=0, sticky="e", padx=5, pady=5)
        tk.Label(form_frame, text="Name: ").grid(row=1, column=0, sticky="e", padx=5, pady=5)
        tk.Label(form_frame, text="Age: ").grid(row=2, column=0, sticky="e", padx=5, pady=5)
        tk.Label(form_frame, text="Grade: ").grid(row=3, column=0, sticky="e", padx=5, pady=5)

        self.entry_id = tk.Entry(form_frame)
        self.entry_name = tk.Entry(form_frame)
        self.entry_age = tk.Entry(form_frame)
        self.entry_grade = tk.Entry(form_frame)

        self.entry_id.grid(row=0, column=1)
        self.entry_name.grid(row=1, column=1)
        self.entry_age.grid(row=2, column=1)
        self.entry_grade.grid(row=3, column=1)


        # Buttons
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Add Student", width=15, command=self.add_student).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Update Student", width=15, command=self.update_student).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="Delete Student", width=15, command=self.delete_student).grid(row=0, column=2, padx=5)        

        # --- ListBox ---
        # Use to show students information
        self.listbox = tk.Listbox(root,width=60, height=10)
        self.listbox.pack(pady=10)
        # load listbox with students information at initialization
        self.load_students()

    # --- functions ---
    def add_student(self):
        sid = self.entry_id.get().strip()
        name = self.entry_name.get().strip()
        age = self.entry_age.get().strip()
        grade = self.entry_grade.get().strip()

        if not sid or not name or not age or not grade:
            messagebox.showerror("Error", "All fields are required!")
            return
        try:
            age = int(age)
            new_student = Student(sid, name, age, grade)
            self.manager.add_student(new_student)
            messagebox.showinfo("Success", "Student added successfully!")
            self.clear_entries()
            self.load_students()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def delete_student(self):
        sid = self.entry_id.get().strip()

        if not sid:
            messagebox.showerror("Error", "Student ID required to proceed delete!")
            return
        try:
            self.manager.delete_student(sid)
            messagebox.showinfo("Success", "Student deleted successfully!")
            self.clear_entries()
            self.load_students()
        except ValueError as e:
            messagebox.showerror("Error", str(e))


    def update_student(self):
        sid = self.entry_id.get().strip()
        if not sid:
            messagebox.showerror("Error", "Student ID required to update!")
            return

        # find existing student
        existing = next((s for s in self.manager.get_all() if s.to_dict()["student_id"] == sid), None)
        if not existing:
            messagebox.showerror("Error", "Student not found!")
            return

        # use new values if provided, otherwise keep existing ones
        name = self.entry_name.get().strip() or existing.to_dict()["student_name"]
        age_text = self.entry_age.get().strip()
        grade = self.entry_grade.get().strip() or existing.to_dict()["grade"]

        try:
            age = int(age_text) if age_text else existing.to_dict()["age"]
        except ValueError:
            messagebox.showerror("Error", "Age must be a number.")
            return

        updated_student = Student(sid, name, age, grade)
        updated = self.manager.update_student(updated_student)
        if updated:
            messagebox.showinfo("Success", "Student updated successfully!")
            self.clear_entries()
            self.load_students()
        else:
            messagebox.showerror("Error", "Failed to update student.")

    def load_students(self):
        # clear listbox before loading information
        self.listbox.delete(0, tk.END)

        # Sort students by ID
        sorted_students = sorted(self.manager.get_all(), key=lambda s : s.to_dict()["student_id"])

        # load data into listbox
        for s in sorted_students:
            self.listbox.insert(tk.END, str(s))

    def clear_entries(self):
        self.entry_id.delete(0, tk.END)
        self.entry_name.delete(0, tk.END)
        self.entry_age.delete(0, tk.END)
        self.entry_grade.delete(0, tk.END)

# --- Main ---
if __name__ == "__main__":
    root = tk.Tk()
    app = StudentApp(root)
    root.mainloop()
    

# # --- Main Menu ---
# def main():
#     manager = StudentManager()

#     while True:
#         print("\n======== Student Management System =========")
#         print("1. Add Student")
#         print("2. View All Students")
#         print("3. Search Student")
#         print("4. Update Student")
#         print("5. Delete Student")
#         print("6. Exit")

#         choice = input("Enter your choice: ")

#         if choice == "1":
#             manager.add_student()
#         elif choice == "2":
#             manager.view_all_students()
#         elif choice == "3":
#             manager.search_student()
#         elif choice == "4":
#             manager.update_student()
#         elif choice == "5":
#             manager.delete_student()
#         elif choice == "6":
#             print("Goodbye!\n")
#             break
#         else:
#             print("Invalid choice. Try again.")


# if __name__ == "__main__":
#     main()
