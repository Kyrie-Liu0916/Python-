from student import *


class StudentManager(object):
    def __init__(self):
        self.student_list = []

    # 程序入口函数
    def run(self):
        # 1.加载文件中学员信息
        self.load_student()
        while True:

            # 2. 显示功能菜单
            self.show_menu()
            # 3. 用户输入功能序号
            menu_num = int(input('请输入序号:'))
            # 4. 执行功能
            if menu_num == 1:
                # 添加学员
                self.add_student()
            elif menu_num == 2:
                # 删除学员
                self.del_student()
            elif menu_num == 3:
                # 修改学员信息
                self.modify_student()
            elif menu_num == 4:
                # 查询学员信息
                self.search_student()
            elif menu_num == 5:
                # 显示所有学员信息
                self.show_student()
            elif menu_num == 6:
                # 保存学员信息
                self.save_student()
            elif menu_num == 7:
                # 退出系统
                break
    # 系统功能函数
    # 2.1 显示功能菜单
    @staticmethod
    def show_menu():
        print('请选择功能')
        print('1.添加学员')
        print('2.删除学员')
        print('3.修改学员信息')
        print('4.查询学员信息')
        print('5.显示所有学员信息')
        print('6.保存学员信息')
        print('7.退出系统')

    # 2.2 添加学员
    def add_student(self):
        name = input('请输入姓名')
        gender = input('性别')
        tel = input('手机号')

        student = Student(name, gender, tel)

        self.student_list.append(student)

        print(self.student_list)
        print(student)

    # 2.3 删除学员
    def del_student(self):
        del_name = input('请输入要删除的学员姓名')

        for i in self.student_list:
            if del_name == i.name:
                self.student_list.remove(i)
                break
        else:
            print('目标学员不存在！')
        print(self.student_list)

    # 2.4 修改学员信息
    def modify_student(self):
        modify_name = input('请输入要修改的学员姓名：')
        for i in self.student_list:
            if i.name == modify_name:
                i.name = input('请输入姓名')
                i.gender = input('请输入性别')
                i.tel = input('请输入手机')
                print(f'修改信息成功, 姓名{i.name}, 性别{i.gender}, 手机号{i.tel}')
                break
        else:
            print('查无此人!')

    # 2.5 查询学员信息
    def search_student(self):
        search_name = input('请输入要查询的学员姓名：')

        for i in self.student_list:
            if i.name == search_name:
                print(f'姓名{i.name}, 性别{i.gender}, 手机号{i.tel}')
                break
        else:
            print('查无此人!')

    # 2.6 显示所有学员
    def show_student(self):
        print('姓名\t性别\t手机号')
        for i in self.student_list:
            print(f'{i.name}\t{i.gender}\t{i.tel}')

    # 2.7 保存学员信息
    def save_student(self):
        f = open('student.data', 'w')

        # 文件写入学员数据

        new_list = [i.__dict__ for i in self.student_list]
        print(new_list)
        # 文件内数据要求为字符串

        f.write(str(new_list))

        f.close()

    # 2.8 加载学员信息
    def load_student(self):
        try:
            f = open('student.data', 'r')
        except:
            f = open('student.data', 'w')
        else:
            data = f.read()

            # 文件中读取的数据都是字符串而且字符串内部为字典数据， 故需转换数据类型再转换字典为对象后存储到学员列表
            new_list = eval(data)
            self.student_list = [Student(i['name'], i['gender'], i['tel']) for i in new_list]
        finally:
            f.close()