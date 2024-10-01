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

# แสดงหัวตาราง
def display_students(students):
    print("=" * 90)
    print(f"{'No.':<3} {'ID':<15} {'Name':<20} {'Midterm':<10} {'Final':<10} {'Assessment':<15} {'Behavioral':<10}")
    print("=" * 90)

    for student in students:
        student.display_info()

    print("-" * 90)

# อ่านข้อมูลจากไฟล์ 'students.txt'
students = read_students_from_file('students.txt')

# แสดงข้อมูลนักเรียน
display_students(students)
