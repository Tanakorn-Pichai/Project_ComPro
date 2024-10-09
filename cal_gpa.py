import pickle  # ใช้สำหรับการจัดการไฟล์ไบนารี
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

# ฟังก์ชันสำหรับอ่านข้อมูลจากไฟล์ไบนารี
def read_students_from_file(file_name):
    try:
        with open(file_name, 'rb') as file:  # ใช้โหมด 'rb' สำหรับอ่านไฟล์ไบนารี
            students = pickle.load(file)
    except FileNotFoundError:
        print(f"ไม่พบไฟล์ {file_name} จะเริ่มต้นข้อมูลใหม่")
        students = []
    except (EOFError, pickle.UnpicklingError) as e:
        print(f"เกิดข้อผิดพลาดในการอ่านไฟล์: {e}")
        students = []
    except Exception as e:
        print(f"เกิดข้อผิดพลาดอื่น ๆ: {e}")
        students = []
    return students

# ฟังก์ชันสำหรับบันทึกข้อมูลนักเรียนลงในไฟล์ไบนารี
def save_students_to_file(file_name, students):
    try:
        with open(file_name, 'wb') as file:  # ใช้โหมด 'wb' สำหรับเขียนไฟล์ไบนารี
            pickle.dump(students, file)
        print(f"บันทึกข้อมูลลงในไฟล์ {file_name} สำเร็จ")
    except Exception as e:
        print(f"เกิดข้อผิดพลาดในการบันทึกไฟล์: {e}")

# ฟังก์ชันสำหรับรับคะแนนโดยมีการตรวจสอบค่า
def input_float(prompt, min_val=0, max_val=100):
    while True:
        try:
            value = input(prompt)
            if value.lower() == 'exit':
                return 'exit'
            value = float(value)
            if min_val <= value <= max_val:
                return value
            else:
                print(f"กรุณากรอกค่าระหว่าง {min_val} ถึง {max_val}")
        except ValueError:
            print("กรุณากรอกตัวเลขที่ถูกต้อง")


# ฟังก์ชันสำหรับเพิ่มข้อมูล
def add_student(students):
    try:
        while True:
            if students:
                no = students[-1].no + 1  # ลำดับถัดไปจากนักเรียนคนสุดท้ายในลิสต์
            else:
                no = 1  # หากลิสต์ว่าง จะให้ลำดับที่เป็น 1
            print("=" * 160)
            print(f"ลำดับที่ :{no}")
            print("พิมพ์ 'exit' เพื่อยกเลิก")
            # รับรหัสนักเรียน ห้ามซ้ำ
            while True:
                student_id = input("กรอกรหัสนักเรียน : ")
                if student_id.lower() == 'exit':
                    print("ยกเลิกการเพิ่มข้อมูลนักเรียน")
                    return
                if any(s.student_id == student_id for s in students):
                    print(f"รหัสนักเรียน {student_id} มีอยู่แล้วในระบบ กรุณากรอกรหัสใหม่")
                else:
                    break
            
            # รับชื่อ ห้ามซ้ำ
            while True:
                name = input("กรอกชื่อ : ")
                if name.lower() == 'exit':
                    print("ยกเลิกการเพิ่มข้อมูลนักเรียน")
                    return
                if any(s.name == name for s in students):
                    print(f"ชื่อ {name} มีอยู่แล้วในระบบ กรุณากรอกชื่อใหม่")
                else:
                    break
            
            # รับคะแนนโดยมีการตรวจสอบ exit
            midterm = input_float("กรอกคะแนนกลางภาค (ไม่เกิน 30 คะแนน ): ", 0, 30)
            if midterm == 'exit':
                print("ยกเลิกการเพิ่มข้อมูลนักเรียน")
                return

            final = input_float("กรอกคะแนนปลายภาค (ไม่เกิน 30 คะแนน ): ", 0, 30)
            if final == 'exit':
                print("ยกเลิกการเพิ่มข้อมูลนักเรียน")
                return

            assessment = input_float("กรอกคะแนนประเมิน (ไม่เกิน 20 คะแนน ): ", 0, 20)
            if assessment == 'exit':
                print("ยกเลิกการเพิ่มข้อมูลนักเรียน")
                return

            behavioral = input_float("กรอกคะแนนพฤติกรรม (ไม่เกิน 20 คะแนน ): ", 0, 20)
            if behavioral == 'exit':
                print("ยกเลิกการเพิ่มข้อมูลนักเรียน")
                return

            # สร้าง record ของนักเรียนใหม่
            new_student = StudentRecord(no, student_id, name, midterm, final, assessment, behavioral)

            # เพิ่ม record ใหม่นี้ในลิสต์
            students.append(new_student)
            print(f"เพิ่มข้อมูลนักเรียน {name} (ลำดับที่ {no}) สำเร็จแล้ว!")
        
    except Exception as e:
        print(f"เกิดข้อผิดพลาด: {e}")

# ฟังก์ชันสำหรับลบข้อมูลนักเรียน
def delete_student(students):
    print("=" * 160)
    print("พิมพ์ 'exit' เพื่อยกเลิก")
    while True:
        user_input = input("กรอกลำดับที่ของนักเรียนที่ต้องการลบ : ")
        
        if user_input.lower() == 'exit':
            print("ยกเลิกการลบข้อมูลนักเรียน")
            break
        
        try:
            student_no = int(user_input)
            
            # ค้นหาและลบนักเรียนที่มีลำดับที่ตรงกัน
            for student in students:
                if student.no == student_no:
                    students.remove(student)
                    print(f"ลบข้อมูลนักเรียนลำดับที่ {student_no} สำเร็จแล้ว!")
                    
                    # อัปเดตลำดับ (no) ของนักเรียนที่เหลือหลังจากการลบ
                    for i, student in enumerate(students):
                        student.no = i + 1  # อัปเดตหมายเลขลำดับใหม่ เริ่มต้นที่ 1
                    return
            
            print(f"ไม่พบนักเรียนที่มีลำดับที่ {student_no}")
        
        except ValueError:
            print("กรุณากรอกตัวเลขที่ถูกต้อง")


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
def report_students(students):
    with open('students.txt', 'w', encoding='utf-8') as file:  # เปิดไฟล์ 'students.txt' เพื่อเขียนข้อมูล
        header = "=" * 170 + "\n"
        title = (f"{'No.':<5} {'ID':<15} {'Name':<30} {'Midterm':>10} {'Final':>10} "
                 f"{'Assessment':>15} {'Behavioral':>15} {'Total Score':>15} {'Grade':>20}\n")
        file.write(header)
        file.write(title)
        file.write(header)

        print(header, end='')  # แสดงส่วนหัวทางหน้าจอ
        print(title, end='')   # แสดงส่วนหัวของข้อมูลทางหน้าจอ
        print(header, end='')  # แสดงเส้นคั่นทางหน้าจอ

        total_people = len(students)
        total_scores = 0
        for student in students:
            total_score = (student.midterm + student.final + 
                           student.assessment + student.behavioral)  # คำนวณคะแนนรวม
            grade = calculate_grade(total_score)  # คำนวณเกรดจากคะแนนรวม

            # แสดงข้อมูลนักเรียนพร้อม Total Score และ Grade และบันทึกลงไฟล์
            line = (f"{student.no:<5} {student.student_id:<15} {student.name:<30} "
                    f"{student.midterm:>10.1f} {student.final:>10.1f} "
                    f"{student.assessment:>15.1f} {student.behavioral:>15.1f} "
                    f"{total_score:>15.1f} {grade:>20.1f}\n")
            file.write(line)
            print(line, end='')  # แสดงข้อมูลนักเรียนทางหน้าจอ
            total_scores += total_score

        average_score = total_scores / total_people if total_people > 0 else 0
        summary = (header + 
                   f"{'Total number of people:':<90} {total_people:<5}\n"
                   f"{'Average Total Score:':<90} {average_score:>5.2f}\n")
        file.write(summary)

        print(summary, end='')  # แสดงข้อมูลสรุปทางหน้าจอ

    print("บันทึกข้อมูลลงในไฟล์ students.txt สำเร็จ")







def display_students(students):
    print("=" * 160)
    print(f"{'No.':<3} {'ID':<15} {'Name':<25} {'Midterm':<20} {'Final':<20} {'Assessment':<20} {'Behavioral':<20} ")
    print("=" * 160)

    for student in students:
        # แสดงข้อมูลนักเรียนพร้อม Total Score และ Grade
        print(f"{student.no:<3} {student.student_id:<15} {student.name:<25} {student.midterm:<20} {student.final:<20} {student.assessment:<20} {student.behavioral:<20} ")

    
# ฟังก์ชันสำหรับค้นหานักเรียนตามเงื่อนไขต่างๆ
def search_student(students):
    while True:
        print("-" * 160)
        print("ค้นหาข้อมูลนักเรียน:")
        print("1. ค้นหาจากชื่อ")
        print("2. ค้นหาจากรหัสนักศึกษา")
        print("3. ค้นหานักเรียนที่มีเกรดสูงที่สุด")
        print("4. ค้นหานักเรียนที่มีเกรดต่ำที่สุด")
        print("5. กลับสู่หน้าหลัก")
        print("-" * 160)
    
        choice = input("เลือกตัวเลือก: ")

        if choice == "1":
            while  True:
                print("'exit' กลับสู่เมนูก่อน ")
                name = input("กรอกชื่อนักเรียนที่ต้องการค้นหา: ").strip().lower()
                if name == "exit":
                    break
                result = [s for s in students if any(char in s.name.lower() for char in name)]
                if result:
                    print("ผลการค้นหา:")
                    display_students(result)
                elif name == "exit":
                    break
                else:
                    print("ไม่พบนักเรียนที่มีชื่อนี้")
                
        elif choice == "2":
            while  True:
                print("'exit' กลับสู่เมนูก่อน ")
                student_id = input("กรอกรหัสนักศึกษาที่ต้องการค้นหา: ")
                result = [s for s in students if s.student_id == student_id]
                if result:
                    print("ผลการค้นหา:")
                    display_students(result)
                elif student_id == "exit":
                    break
                else:
                    print("ไม่พบนักเรียนที่มีรหัสนักศึกษานี้")
        
        elif choice == "3":
            if students:
                # คำนวณคะแนนรวมสูงสุด
                max_score = max(s.midterm + s.final + s.assessment + s.behavioral for s in students)
                
                # กรองนักเรียนที่มีคะแนนรวมเท่ากับคะแนนสูงสุด
                top_students = [s for s in students if s.midterm + s.final + s.assessment + s.behavioral == max_score]
                
                # แสดงรายชื่อนักเรียนที่มีคะแนนสูงสุด
                print("นักเรียนที่มีเกรดสูงที่สุดคือ:")
                display_students(top_students)
            else:
                print("ไม่มีข้อมูลนักเรียน")

        elif choice == "4":
            if students:
                # คำนวณคะแนนรวมสูงสุด
                min_score = min(s.midterm + s.final + s.assessment + s.behavioral for s in students)
                
                # กรองนักเรียนที่มีคะแนนรวมเท่ากับคะแนนสูงสุด
                min_students = [s for s in students if s.midterm + s.final + s.assessment + s.behavioral == min_score]
                
                # แสดงรายชื่อนักเรียนที่มีคะแนนสูงสุด
                print("นักเรียนที่มีเกรดสูงที่สุดคือ:")
                display_students(min_students)
            else:
                print("ไม่มีข้อมูลนักเรียน")

        elif choice == "5":
            break
        else:
            print("กรุณาเลือกตัวเลือกที่ถูกต้อง")

# อ่านข้อมูลจากไฟล์ 'students.bin'
students = read_students_from_file('students.bin')

# ฟังก์ชันสำหรับแก้ไขข้อมูลนักเรียน
def edit_student(students):
    print("=" * 160)
    print("พิมพ์ 'exit' เพื่อยกเลิก")
    while True:
        user_input = input("กรอกลำดับที่ของนักเรียนที่ต้องการแก้ไข : ")
        if user_input.lower() == 'exit':
            print("ยกเลิกการแก้ไขข้อมูลนักเรียน")
            return

        try:
            student_no = int(user_input)

            # ค้นหานักเรียนที่มีลำดับที่ตรงกัน
            for student in students:
                if student.no == student_no:
                    print(f"กำลังแก้ไขข้อมูลนักเรียนลำดับที่ {student_no}")
                    print("ถ้าต้องการแก้ไขข้อมูล กรุณากรอกข้อมูลใหม่ ถ้าไม่ต้องการแก้ไข กด Enter เพื่อข้าม")

                    # ตรวจสอบว่ารหัสนักเรียนใหม่ไม่ซ้ำกับนักเรียนคนอื่น
                    while True:
                        new_student_id = input(f"รหัสนักเรียน [{student.student_id}]: ") or student.student_id
                        if new_student_id.lower() == 'exit':
                            print("ยกเลิกการแก้ไขข้อมูลนักเรียน")
                            return
                        if any(s.student_id == new_student_id and s.no != student_no for s in students):
                            print(f"รหัสนักเรียน {new_student_id} ซ้ำกับนักเรียนคนอื่น กรุณากรอกรหัสใหม่")
                        else:
                            break

                    # ตรวจสอบว่าชื่อใหม่ไม่ซ้ำกับนักเรียนคนอื่น
                    while True:
                        new_name = input(f"ชื่อ [{student.name}]: ") or student.name
                        if new_name.lower() == 'exit':
                            print("ยกเลิกการแก้ไขข้อมูลนักเรียน")
                            return
                        if any(s.name == new_name and s.no != student_no for s in students):
                            print(f"ชื่อ {new_name} ซ้ำกับนักเรียนคนอื่น กรุณากรอกรชื่อใหม่")
                        else:
                            break

                    # ป้อนคะแนนกลางภาค ไม่เกิน 30 คะแนน
                    while True:
                        new_midterm = input(f"คะแนนกลางภาค [{student.midterm}]: ")
                        if new_midterm.lower() == 'exit':
                            print("ยกเลิกการแก้ไขข้อมูลนักเรียน")
                            return
                        if new_midterm == "" or (0 <= float(new_midterm) <= 30):
                            new_midterm = float(new_midterm) if new_midterm else student.midterm
                            break
                        else:
                            print("กรุณากรอกคะแนนระหว่าง 0 ถึง 30")

                    # ป้อนคะแนนปลายภาค ไม่เกิน 30 คะแนน
                    while True:
                        new_final = input(f"คะแนนปลายภาค [{student.final}]: ")
                        if new_final.lower() == 'exit':
                            print("ยกเลิกการแก้ไขข้อมูลนักเรียน")
                            return
                        if new_final == "" or (0 <= float(new_final) <= 30):
                            new_final = float(new_final) if new_final else student.final
                            break
                        else:
                            print("กรุณากรอกคะแนนระหว่าง 0 ถึง 30")

                    # ป้อนคะแนนประเมิน ไม่เกิน 20 คะแนน
                    while True:
                        new_assessment = input(f"คะแนนประเมิน [{student.assessment}]: ")
                        if new_assessment.lower() == 'exit':
                            print("ยกเลิกการแก้ไขข้อมูลนักเรียน")
                            return
                        if new_assessment == "" or (0 <= float(new_assessment) <= 20):
                            new_assessment = float(new_assessment) if new_assessment else student.assessment
                            break
                        else:
                            print("กรุณากรอกคะแนนระหว่าง 0 ถึง 20")

                    # ป้อนคะแนนพฤติกรรม ไม่เกิน 20 คะแนน
                    while True:
                        new_behavioral = input(f"คะแนนพฤติกรรม [{student.behavioral}]: ")
                        if new_behavioral.lower() == 'exit':
                            print("ยกเลิกการแก้ไขข้อมูลนักเรียน")
                            return
                        if new_behavioral == "" or (0 <= float(new_behavioral) <= 20):
                            new_behavioral = float(new_behavioral) if new_behavioral else student.behavioral
                            break
                        else:
                            print("กรุณากรอกคะแนนระหว่าง 0 ถึง 20")

                    # อัปเดตข้อมูลนักเรียน
                    student.student_id = new_student_id
                    student.name = new_name
                    student.midterm = new_midterm
                    student.final = new_final
                    student.assessment = new_assessment
                    student.behavioral = new_behavioral

                    print(f"แก้ไขข้อมูลนักเรียนลำดับที่ {student_no} สำเร็จแล้ว!")
                    return

            print(f"ไม่พบนักเรียนที่มีลำดับที่ {student_no}")

        except ValueError:
            print("กรุณากรอกตัวเลขที่ถูกต้อง")


while True:
    print("=" * 160)
    print("กรุณาเลือกเมนูที่ต้องการ:")
    print("1. เพิ่มข้อมูลนักเรียนใหม่")
    print("2. แสดงข้อมูลนักเรียน")
    print("3. ค้นหาข้อมูลนักเรียน")
    print("4. แก้ไขข้อมูลนักเรียน")
    print("5. ลบข้อมูลนักเรียน")
    print("6. แสดงรายงาน")
    print("7. ออกจากโปรแกรม")
    print("=" * 160)
    choice = input("เลือกเมนู: ")  # รับค่าปกติจากการพิมพ์

    if choice == "1":
        display_students(students)
        add_student(students)
        display_students(students)
        save_students_to_file('students.bin', students) 
    elif choice == "2":
        display_students(students)
    elif choice == "3":
        search_student(students)  # เรียกใช้ฟังก์ชันค้นหาข้อมูลนักเรียน
    elif choice == "4":
        display_students(students)
        edit_student(students)  # เพิ่มฟังก์ชันแก้ไขข้อมูล
        display_students(students)
        save_students_to_file('students.bin', students) 
    elif choice == "5":
        display_students(students)
        delete_student(students)
        display_students(students)
        save_students_to_file('students.bin', students) 
    elif choice == "6":
        report_students(students)
    elif choice == "7":  # Exit the program
         # บันทึกข้อมูลก่อนออกจากโปรแกรม
        print("ออกจากโปรแกรม")
        break
    else:
        print("กรุณาเลือกหมายเลขเมนูที่ถูกต้อง")
