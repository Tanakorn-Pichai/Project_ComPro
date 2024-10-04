import pickle  # ใช้สำหรับการจัดการไฟล์ไบนารี
from dataclasses import dataclass
import keyboard

@dataclass
class StudentRecord:
    no: int
    student_id: str
    name: str
    midterm: float
    final: float
    assessment: float
    behavioral: float

    # ฟังก์ชันสำหรับแสดงข้อมูลนักเรียนในรูปแบบตาราง
    def display_info(self):
        print(f"{self.no:<3} {self.student_id:<15} {self.name:<20} {self.midterm:<10} {self.final:<10} {self.assessment:<15} {self.behavioral:<10}")

# ฟังก์ชันสำหรับอ่านข้อมูลจากไฟล์ไบนารี
def read_students_from_file(file_name):
    try:
        with open(file_name, 'rb') as file:  # ใช้โหมด 'rb' สำหรับอ่านไฟล์ไบนารี
            students = pickle.load(file)
    except FileNotFoundError:
        students = []

    return students

# ฟังก์ชันสำหรับบันทึกข้อมูลนักเรียนลงในไฟล์ไบนารี
def save_students_to_file(file_name, students):
    with open(file_name, 'wb') as file:  # ใช้โหมด 'wb' สำหรับเขียนไฟล์ไบนารี
        pickle.dump(students, file)

# ฟังก์ชันสำหรับเพิ่มข้อมูลนักเรียนใหม่
def add_student(students):
    no = int(input("กรอกลำดับที่: "))
    student_id = input("กรอกรหัสนักเรียน: ")
    name = input("กรอกชื่อ: ")
    midterm = float(input("กรอกคะแนนกลางภาค: "))
    final = float(input("กรอกคะแนนปลายภาค: "))
    assessment = float(input("กรอกคะแนนประเมิน: "))
    behavioral = float(input("กรอกคะแนนพฤติกรรม: "))

    # สร้าง record ของนักเรียนใหม่
    new_student = StudentRecord(no, student_id, name, midterm, final, assessment, behavioral)

    # เพิ่ม record ใหม่นี้ในลิสต์
    students.append(new_student)
    print(f"เพิ่มข้อมูลนักเรียน {name} สำเร็จแล้ว!")

# ฟังก์ชันสำหรับลบข้อมูลนักเรียน
def delete_student(students):
    student_no = int(input("กรอกลำดับที่ของนักเรียนที่ต้องการลบ: "))
    
    # ค้นหาและลบนักเรียนที่มีลำดับที่ตรงกัน
    for student in students:
        if student.no == student_no:
            students.remove(student)
            print(f"ลบข้อมูลนักเรียนลำดับที่ {student_no} สำเร็จแล้ว!")
            return
    print(f"ไม่พบนักเรียนที่มีลำดับที่ {student_no}")

# ฟังก์ชันสำหรับคำนวณเกรดจากคะแนนรวม
def calculate_grade(total_score):
    if total_score >= 80:
        return "A"
    elif total_score >= 75:
        return "B+"
    elif total_score >= 70:
        return "B"
    elif total_score >= 65:
        return "C+"
    elif total_score >= 60:
        return "C"
    elif total_score >= 55:
        return "D+"
    elif total_score >= 50:
        return "D"
    else:
        return "F"

# ฟังก์ชันสำหรับแสดงข้อมูลนักเรียน รวมถึง Total Score และ Grade
def display_students(students):
    print("=" * 130)
    print(f"{'No.':<3} {'ID':<15} {'Name':<20} {'Midterm':<10} {'Final':<10} {'Assessment':<15} {'Behavioral':<10} {'Total Score':<12} {'Grade':<5}")
    print("=" * 130)

    total_people = len(students)
    total_scores = 0
    for student in students:
        total_score = student.midterm + student.final + student.assessment + student.behavioral  # คำนวณคะแนนรวม
        grade = calculate_grade(total_score)  # คำนวณเกรดจากคะแนนรวม

        # แสดงข้อมูลนักเรียนพร้อม Total Score และ Grade
        print(f"{student.no:<3} {student.student_id:<15} {student.name:<20} {student.midterm:<10} {student.final:<10} {student.assessment:<15} {student.behavioral:<10} {total_score:<12} {grade:<5}")
        total_scores += total_score

    average_score = total_scores / total_people if total_people > 0 else 0
    print("=" * 130)
    print(f"{'Total number of people:':<90} {total_people:<5}")
    print(f"{'Average Total Score:':<90} {average_score:<5.2f}")
    print("-" * 130)
    
    input("กดปุ่มใดก็ได้เพื่อกลับสู่เมนู...")  # หยุดรอให้ผู้ใช้กดปุ่ม


# อ่านข้อมูลจากไฟล์ 'students.bin'
students = read_students_from_file('students.bin')


current_row = 0


def print_menu():
    for idx, row in enumerate(menu):
        if idx == current_row:
            print(f"> {row}") 
             # Highlight the current row
        else:
            print(f"  {row}")
# ฟังก์ชันสำหรับแก้ไขข้อมูลนักเรียน
def edit_student(students):
    student_no = int(input("กรอกลำดับที่ของนักเรียนที่ต้องการแก้ไข: "))
    # ค้นหานักเรียนที่มีลำดับที่ตรงกัน
    for student in students:
        if student.no == student_no:
            print(f"กำลังแก้ไขข้อมูลนักเรียนลำดับที่ {student_no}")
            print("ถ้าต้องการแก้ไขข้อมูล กรุณากรอกข้อมูลใหม่ ถ้าไม่ต้องการแก้ไข กด Enter เพื่อข้าม")

            # ป้อนข้อมูลใหม่หรือกด Enter เพื่อข้าม
            new_student_id = input(f"รหัสนักเรียน [{student.student_id}]: ") or student.student_id
            new_name = input(f"ชื่อ [{student.name}]: ") or student.name
            new_midterm = input(f"คะแนนกลางภาค [{student.midterm}]: ")
            new_final = input(f"คะแนนปลายภาค [{student.final}]: ")
            new_assessment = input(f"คะแนนประเมิน [{student.assessment}]: ")
            new_behavioral = input(f"คะแนนพฤติกรรม [{student.behavioral}]: ")

            # อัปเดตข้อมูลที่ถูกแก้ไข (ถ้ามี)
            student.student_id = new_student_id
            student.name = new_name
            student.midterm = float(new_midterm) if new_midterm else student.midterm
            student.final = float(new_final) if new_final else student.final
            student.assessment = float(new_assessment) if new_assessment else student.assessment
            student.behavioral = float(new_behavioral) if new_behavioral else student.behavioral

            print(f"แก้ไขข้อมูลนักเรียนลำดับที่ {student_no} สำเร็จแล้ว!")
            return
    print(f"ไม่พบนักเรียนที่มีลำดับที่ {student_no}")

# แก้ไขเมนูเพื่อเพิ่มตัวเลือกสำหรับแก้ไขข้อมูลนักเรียน

menu = ["1. แสดงข้อมูลนักเรียน", 
        "2. เพิ่มข้อมูลนักเรียนใหม่",
        "3. แก้ไขข้อมูลนักเรียน",  # เพิ่มเมนูแก้ไขข้อมูลนักเรียน
        "4. ลบข้อมูลนักเรียน", 
        "5. บันทึกและออกจากโปรแกรม"]

while True:
    print_menu()
    key = keyboard.read_event()

    if key.event_type == keyboard.KEY_DOWN and key.name == "up":
        current_row = (current_row - 1) % len(menu)
    elif key.event_type == keyboard.KEY_DOWN and key.name == "down":
        current_row = (current_row + 1) % len(menu)
    elif key.event_type == keyboard.KEY_DOWN and key.name == "enter":
        if current_row == 0:
            display_students(students)
        elif current_row == 1:
            add_student(students)
            display_students(students)
        elif current_row == 2:
            display_students(students)
            edit_student(students)  # เพิ่มฟังก์ชันแก้ไขข้อมูล
            display_students(students)
        elif current_row == 3:
            display_students(students)
            delete_student(students)
            display_students(students)
        elif current_row == 4:  # Exit the program
            save_students_to_file('students.bin', students)  # บันทึกข้อมูลก่อนออกจากโปรแกรม
            print("บันทึกและออกจากโปรแกรม")
            break
    print("\033c", end="")  # Clear the console for next display

