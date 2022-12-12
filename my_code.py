import json
import requests

student = {}
def creat_student():
    id = int(input("Please Enter Student Id (integer) : \n"))
    full_name = str(input("Please Enter Student full_name (string) : \n "))
    age =int(input("Please Enter Student age : (integer)\n"))
    level = str(input("level [A , B , C] : (string) \n"))
    mobile_number = str(input("Please Enter Student mobile_number :(integer) \n"))
    global studen
    student = {
        "id": id,
        "full_name": full_name,
        "age": age,
        "level": level,
        "mobile_number": mobile_number
    }
    print("is added : ",student)
    r_post = requests.post("http://staging.bldt.ca/api/method/build_it.test.register_student" ,params=student)
    return print(r_post.text ,"\n")

def edit_student():
    s_id = input("Please Enter the id_student you want to modify (integer) : \n")
    res = requests.get("http://staging.bldt.ca/api/method/build_it.test.get_student_details",params={'id':s_id})
    if res.status_code == 200:
        name = input("Please Enter Student full_name (string) : \n ")
        age = str(input("Please Enter Student age (string) : \n "))
        level = str(input("Please Enter Student level (string) : \n "))
        mobile = str(input("Please Enter Student mobile_number (string) : \n "))
        r_edit = requests.post("http://staging.bldt.ca/api/method/build_it.test.edit_student", params={'id':s_id , 'full_name':name , 'age':age,'level':level,'mobile_number':mobile})
        print(r_edit.text)
    if r_edit.status_code == 200:
        print("student has edited succseefuly")
    else:
        print("faild edited ")

def delete_student():
    s_id = input("Please Enter the id_student you want to delete (integer) : \n")
    res = requests.get("http://staging.bldt.ca/api/method/build_it.test.get_student_details", params={'id': s_id})
    if res.status_code == 200:
        r_delete = requests.delete("http://staging.bldt.ca/api/method/build_it.test.delete_student", params={'id':s_id })
        print(r_delete.text)
    if r_delete.status_code == 200:
        print("student has deleted succseefuly")
    else:
        print("faild deleted ")


def export_student_to_file():
    r_get = requests.get("http://staging.bldt.ca/api/method/build_it.test.get_students")
    if r_get.status_code == 200:
        file = open("all_students.json", "a")
        file.write(str(r_get.text))
        file.close()

    return print(r_get.text)

def export_student_detail_to_file():
    r_get_det = requests.get("http://staging.bldt.ca/api/method/build_it.test.get_student_details")
    return print(r_get_det.text)




while(True):
    x = int(input(
        "1.Register new sutudent\n"
        "2.Edit  sutudent details\n"
        "3.Delete  sutudent\n"
        "4.Export  sutudent to txt file\n"
        "5.Export details to txt sutudent\n"
        "6.Exit\n"
    ))
    if   x == 1:
       creat_student()
    elif x == 2:
        edit_student()
    elif x == 3:
        delete_student()
    elif x == 4:
        export_student_to_file()
    elif x == 5:
        export_student_detail_to_file()
    else:
        exit()
        pass