from dataclasses import dataclass

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

# ฟังก์ชันสำหรับอ่านข้อมูลจากไฟล์ text
def read_students_from_file(file_name):
    students = []
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            data = line.split()  # แยกข้อมูลโดยใช้ช่องว่าง
            # ตรวจสอบว่าบรรทัดมีข้อมูลครบ
            if len(data) >= 7:
                no = int(data[0])
                student_id = data[1]
                name = " ".join(data[2:-4])  # รวมชื่อเต็มที่อาจมีหลายคำ
                midterm = float(data[-4])
                final = float(data[-3])
                assessment = float(data[-2])
                behavioral = float(data[-1])

                # สร้าง StudentRecord และเพิ่มเข้าไปในลิสต์
                student = StudentRecord(no, student_id, name, midterm, final, assessment, behavioral)
                students.append(student)
    return students

# ฟังก์ชันสำหรับบันทึกข้อมูลนักเรียนลงในไฟล์
def save_students_to_file(file_name, students):
    with open(file_name, 'w', encoding='utf-8') as file:
        for student in students:
            file.write(f"{student.no} {student.student_id} {student.name} {student.midterm} {student.final} {student.assessment} {student.behavioral}\n")

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

# ฟังก์ชันสำหรับแสดงหัวตาราง
def display_students(students):
    print("=" * 90)
    print(f"{'No.':<3} {'ID':<15} {'Name':<20} {'Midterm':<10} {'Final':<10} {'Assessment':<15} {'Behavioral':<10}")
    print("=" * 90)

    for student in students:
        student.display_info()

    print("-" * 90)

# อ่านข้อมูลจากไฟล์ 'students.txt'
students = read_students_from_file('students.txt')

# แสดงเมนูให้ผู้ใช้เลือก
while True:
    print("1. แสดงข้อมูลนักเรียน")
    print("2. เพิ่มข้อมูลนักเรียนใหม่")
    print("3. บันทึกและออกจากโปรแกรม")
    choice = input("เลือกตัวเลือก: ")

    if choice == '1':
        display_students(students)
    elif choice == '2':
        add_student(students)
    elif choice == '3':
        save_students_to_file('students.txt', students)
        print("บันทึกข้อมูลสำเร็จและออกจากโปรแกรม")
        break
    else:
        print("เลือกตัวเลือกไม่ถูกต้อง")
