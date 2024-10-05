import keyboard

menu = ["1. แสดงข้อมูลนักเรียน", 
        "2. เพิ่มข้อมูลนักเรียนใหม่", 
        "3. บันทึกและออกจากโปรแกรม"]

current_row = 0

def print_menu():
    for idx, row in enumerate(menu):
        if idx == current_row:
            print(f"> {row}")  # Highlight the current row
        else:
            print(f"  {row}")

while True:
    print_menu()
    key = keyboard.read_event()

    if key.event_type == keyboard.KEY_DOWN and key.name == "up":
        current_row = (current_row - 1) % len(menu)
    elif key.event_type == keyboard.KEY_DOWN and key.name == "down":
        current_row = (current_row + 1) % len(menu)
    elif key.event_type == keyboard.KEY_DOWN and key.name == "enter":
        if current_row == 2:  # Exit the program
            print("บันทึกและออกจากโปรแกรม")
            break
        # Process other menu options here
    print("\033c", end="")  # Clear the console for next display
# แสดงเมนูให้ผู้ใช้เลือก
# while True:
#     print("1. แสดงข้อมูลนักเรียน")
#     print("2. เพิ่มข้อมูลนักเรียนใหม่")
#     print("3. ลบข้อมูลนักเรียน")
#     print("4. บันทึกและออกจากโปรแกรม")
#     choice = input("เลือกตัวเลือก: ")

#     if choice == '1':
#         display_students(students)
#     elif choice == '2':
#         add_student(students)
#     elif choice == '3':
#         display_students(students)
#         delete_student(students)
#     elif choice == '4':
#         save_students_to_file('students.txt', students)
#         print("บันทึกข้อมูลสำเร็จและออกจากโปรแกรม")
#         break
#     else:
#         print("เลือกตัวเลือกไม่ถูกต้อง")


# menu = ["1. แสดงข้อมูลนักเรียน", 
#         "2. เพิ่มข้อมูลนักเรียนใหม่",
#         "3. แก้ไขข้อมูลนักเรียน",  
#         "4. ลบข้อมูลนักเรียน", 
#         "5. บันทึกและออกจากโปรแกรม"]

# while True:
#     print("ใช้ up/down เพื่อเลื่อนขึ้นเลื่อนลง ")
#     print_menu()
#     key = keyboard.read_event()

#     if key.event_type == keyboard.KEY_DOWN and key.name == "up":
#         current_row = (current_row - 1) % len(menu)
#     elif key.event_type == keyboard.KEY_DOWN and key.name == "down":
#         current_row = (current_row + 1) % len(menu)
#     elif key.event_type == keyboard.KEY_DOWN and key.name == "enter":
#         if current_row == 0:
#             display_students(students)
#         elif current_row == 1:
#             add_student(students)
#             display_students(students)
#         elif current_row == 2:
#             display_students(students)
#             edit_student(students)  
#             display_students(students)
#         elif current_row == 3:
#             display_students(students)
#             delete_student(students)
#             display_students(students)
#         elif current_row == 4: 
#             save_students_to_file('students.bin', students) 
#             print("บันทึกและออกจากโปรแกรม")
#             break
#     print("\033c", end="")  
    # Clear the console for next display