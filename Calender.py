# Todo List:
# 1. fix delete button problem (when deleting a middle item task may be 1, 3)
# 2. setup the clear list button
# 3. add the spacial check boxes (event,...)

from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import *
from ProgramGui import Ui_allprograms
from datetime import *
from PyQt5.QtCore import QTime, QTimer
import glob
import operator

class Calender(QMainWindow, Ui_allprograms,):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.cal_main_button_selectedday.clicked.connect(self.selected_list)
        self.cal_main_button_today.clicked.connect(self.current_list)

        self.cal_todo_back.clicked.connect(self.back_func)
        self.cal_todo_add.clicked.connect(self.add_func)
        self.cal_todo_delete.clicked.connect(self.delete_func)

        self.is_today_pressed = False
        self.is_selected_pressed = False

        exist = glob.glob("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\data_Calender.txt")
        if not exist:
            file_create = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\data_Calender.txt", "a")
            file_create.close()

        today = date.today()
        self.date_name = today.strftime("%A, %B, %Y")
        self.date_number = today.strftime("%d/%m/%Y")
        self.cal_main_date_names.setText(self.date_name)
        self.cal_main_date_numbers.setText(self.date_number)

        dateSelected = self.cal_main_calendar.selectedDate()
        year = ""
        month = ""
        day = ""
        sel_date_unorg = str(dateSelected.toPyDate())

        self.hide_todo()
        self.gui_fix()

    def gui_fix(self):
        self.cal_main_button_today.setStyleSheet("background-color : #002776;"
                                                 "color : white;"
                                                 "border-radius : 10px;")
        self.cal_main_button_selectedday.setStyleSheet("background-color : #002776;"
                                                       "color : white;"
                                                       "border-radius : 10px;")
        self.cal_todo_back.setStyleSheet("background-color : #002776;"
                                         "color : white;"
                                         "border-radius : 20px;")
        self.cal_todo_add.setStyleSheet("background-color : #005500;"
                                        "color : white;"
                                        "border-radius : 10px")
        self.cal_todo_delete.setStyleSheet("background : #660000;"
                                           "color : white;"
                                           "border-radius : 10px")
        self.cal_todo_clear.setStyleSheet("background-color : #c16701;"
                                          "color : white;"
                                          "border-radius : 10px")

    def selected_date_thing(self):
        dateSelected = self.cal_main_calendar.selectedDate()
        year = ""
        month = ""
        day = ""
        sel_date_unorg = str(dateSelected.toPyDate())
        for num1 in sel_date_unorg.split("-"):
            year = num1
            break
        for num2 in sel_date_unorg.split("-"):
            if num2 == year:
                pass
            else:
                month = num2
                break
        for num3 in sel_date_unorg.split("-"):
            if num3 == year:
                pass
            elif num3 == month:
                pass
            else:
                day = num3
                break
        self.selected_date = f"{day}/{month}/{year}"

    def task_number(self):
        self.selected_date_thing()

        file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\data_Calender.txt", "r")
        lines = file.read()
        file.close()

        # steps:
        # 1. match the selected date to the date on the file
        # 2. make a new list that is just the date and its tasks
        # 3. find the last tasks task number and up it by 1

        # case of list existing
        # 1
        already_done = False
        for title in lines.split("\n"):
            if already_done:
                break
            elif title == self.cal_main_title.text():
                already_done = True
        # 2
                list = ""
                correct_list = False
                for line in lines.split("\n"):
                    if line == title:
                        correct_list = True
                        continue
                    if correct_list:
                        if ".)" in line:
                            if list == "":
                                list = line
                            elif list != "":
                                list = f"{list}\n{line}"
                        elif line == "---":
                            list = f"{list}\n{line}"
                            break
        # 3
                last_task = "0"
                for line in list.split("\n"):
                    if ".)" in line:
                        last_task = line
                    if line == "---":
                        self.task = int(last_task[0])+1
            # case of list not existing
            else:
                self.task = 1

    def file_to_list(self):
        self.cal_todo_list.clear()
        file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\data_Calender.txt", "r")
        lines = file.read()
        file.close()

        # steps:
        # 1. find the wanted date
        # 2. make a seperate list
        # 3. get rid of title and "---"
        # 4. display it line by line

        # 1
        already_done = False
        for title in lines.split("\n"):
            if already_done:
                break
            elif title == self.cal_main_title.text():
                already_done = True
        # 2 and 3
                list = ""
                correct_list = False
                for line in lines.split("\n"):
                    if line == title:
                        correct_list = True
                        continue
                    if correct_list:
                        if ".)" in line:
                            if list == "":
                                list = line
                            elif list != "":
                                list = f"{list}\n{line}"
                        elif line == "---":
                            break
        # 4
                for line2 in list.split("\n"):
                    self.cal_todo_list.addItem(line2)

            elif lines == "":
                pass

    def rem_empty_dates(self):
        file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\data_Calender.txt", "r")
        lines = file.read()
        file.close()

        # steps
        # 1. find the date and after it the "---"
        # 2. if date or "---" in data: pass
        # 3. overwrite the file with the new list

        # 1
        linesfound = False
        isdate = False
        for line in lines.split("\n"):
            if "/" in line:
                isdate = True
                date = line
                continue
            elif ".)" in line:
                isdate = False
            elif line == "---" and isdate == True:
                linesfound = True
                break
        # 2
        new_data = ""
        datefound = False
        if linesfound == False:
            pass
        elif linesfound == True:
            for line1 in lines.split("\n"):
                if line1 != date and datefound == False:
                    datefound = False
                    if new_data == "":
                        new_data = line1
                    elif new_data != "":
                        new_data = f"{new_data}\n{line1}"
                elif line1 == date:
                    datefound = True
                    continue
                elif line1 == "---" and datefound == True:
                    continue
        # 3
            file_add = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\data_Calender.txt", "w")
            file_add.write(new_data)
            file_add.close()

    def fix_task(self):
        # steps:
        # 1. find wanted list
        # 2. create seperate list (with everything) list 1
        # 3. create seperate list (only tasks) list 2
        # 4. check each line of list 2 and if the next lines task is not the lines before task + 1 then make it + 1
        # 5. remove list 1 from data
        # 6. add list 2 to data with date and "---"
        file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\data_Calender.txt", "r")
        data = file.read()
        file.close()

        # 1
        found_list = False
        list1 = ""
        list2 = ""
        for line in data.split("\n"):
            if line == self.cal_main_title:
                found_list = True
        # 2
                list1 = line
            elif ".)" in line and found_list:
                list1 += line
        # 3
                if list2 == "":
                    list2 = line
                elif list2 != "":
                    list2 += line
        # 2
            elif line == "---" and found_list:
                list1 += line
                break
            else:
                found_list = False
        # 4


    def hide_todo(self):
        self.cal_todo_textbox.hide()
        self.cal_todo_add.hide()
        self.cal_todo_delete.hide()
        self.cal_todo_clear.hide()
        self.cal_todo_list.hide()
        self.cal_todo_back.hide()
        self.cal_main_calendar.show()
        self.cal_main_currentdate.show()
        self.cal_main_date_names.show()
        self.cal_main_date_numbers.show()
        self.cal_main_button_today.show()
        self.cal_main_button_selectedday.show()
        self.cal_line1.show()

    def show_todo(self):
        self.cal_todo_textbox.show()
        self.cal_todo_add.show()
        self.cal_todo_delete.show()
        self.cal_todo_clear.show()
        self.cal_todo_list.show()
        self.cal_todo_back.show()
        self.cal_main_calendar.hide()
        self.cal_main_currentdate.hide()
        self.cal_main_date_names.hide()
        self.cal_main_date_numbers.hide()
        self.cal_main_button_today.hide()
        self.cal_main_button_selectedday.hide()
        self.cal_line1.hide()

    def current_list(self):
        self.show_todo()

        self.cal_main_title.setText(self.date_number)
        self.is_today_pressed = True

        self.task_number()
        self.file_to_list()

    def selected_list(self):
        self.show_todo()
        self.selected_date_thing()

        self.is_selected_pressed = True
        self.cal_main_title.setText(self.selected_date)

        self.task_number()
        self.file_to_list()

    def back_func(self):
        self.hide_todo()

        self.cal_todo_list.clear()
        self.cal_todo_textbox.clear()
        self.cal_main_title.setText("Calender And To Do Lists")

        self.is_today_pressed = False
        self.is_selected_pressed = False

    def add_func(self):
        file_read = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\data_Calender.txt", "r")
        data = file_read.read()
        file_read.close()

        # possibilities:
        # 1. empty file
        # 2. only wanted date
        # 3. multiple dates
        # 4. no wanted date

        # steps1:
        # 1. find if its an empty file. if yes then add new date
        # 2. find if wanted date is in file
        # 3. if yes then go to steps2
        # 4. if no then add new date

        # steps2:
        # 1. make a seperate list
        # 2. add the item to the list
        # 3. get rid of the list in the original file
        # 4. add the new list to the file.

        # 1 1
        self.task_number()
        item_added = False
        new_data = ""
        if data == "":
            if self.is_today_pressed:
                new_data = f"{self.date_number}\n{self.task}.) {self.cal_todo_textbox.text()}\n---"
                item_added = True
            elif self.is_selected_pressed:
                new_data = f"{self.selected_date}\n{self.task}.) {self.cal_todo_textbox.text()}\n---"
                item_added = True
        # 1 2
        if item_added: # if data == ""
            pass
        else: # if data != ""
            already_done = False
            already_done1 = False
            for line in data.split("\n"):
                if line == self.cal_main_title.text() and already_done == False:
                    already_done = True
        # 2 1
                    list = ""
                    correct_list = False
                    for line in data.split("\n"):
                        if line == self.cal_main_title.text():
                            correct_list = True
                        elif ".)" in line and correct_list == True:
                            if list == "":
                                list = f"{self.cal_main_title.text()}\n{line}"
                            elif list != "":
                                list = f"{list}\n{line}"
                        elif line == "---" and correct_list == True:
                            break

        # 2 2
                    new_list = ""
                    if already_done1:
                        pass
                    else:
                        new_list = f"{list}\n{self.task}.) {self.cal_todo_textbox.text()}\n---"
        # 2 3
                    if already_done1:
                        pass
                    else:
                        list_for_next = f"{list}\n---"
                        listless = ""
                        for line in data.split("\n"):
                            if line in list_for_next:
                                continue
                            else:
                                if listless == "":
                                    listless = f"{line}"
                                elif listless != "":
                                    listless = f"{listless}\n{line}"
                        if listless == "":
                            listless = ""
                        else:
                            listless = f"{listless}\n---"

        # 2 4
                        if listless == "":
                            new_data = f"{new_list}"
                        else:
                            new_data = f"{listless}\n{new_list}"
        # 1 4
                elif self.cal_main_title.text() not in data and data != "":
                    already_done1 = True
                    if new_data == "":
                        if self.is_today_pressed:
                            new_data = f"{data}\n{self.date_number}\n{self.task}.) {self.cal_todo_textbox.text()}\n---"
                        elif self.is_selected_pressed:
                            new_data = f"{data}\n{self.selected_date}\n{self.task}.) {self.cal_todo_textbox.text()}\n---"

        file_add = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\data_Calender.txt", "w")
        file_add.write(new_data)
        file_add.close()
        self.cal_todo_textbox.clear()
        self.file_to_list()

    def delete_func(self):
        file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\data_Calender.txt", "r")
        data = file.read()
        file.close()

        # steps:
        # 1. find wanted list
        # 2. create seperate list
        # 3. find wanted item in the created list
        # 4. write every line exept the wanted item (another list)
        # 5. remove wanted list from original file
        # 6. and new list to file from step 5

        # 1
        list = ""
        correct_list = False
        for line in data.split("\n"):
            if line == self.cal_main_title.text():
                correct_list = True
                continue
        # 2
            if correct_list:
                if ".)" in line:
                    if list == "":
                        list = f"{self.cal_main_title.text()}\n{line}"
                    elif list != "":
                        list = f"{list}\n{line}"
                elif line == "---":
                    list = f"{list}\n{line}"
                    break
        # 3
        selected_line = self.cal_todo_list.currentItem().text()
        # 4
        new_list = ""
        for list_line in list.split("\n"):
            if selected_line != list_line:
                if new_list == "":
                    new_list = list_line
                elif new_list != "":
                    new_list = f"{new_list}\n{list_line}"
            if selected_line == list_line:
                pass
        # 5
        listless = ""
        for data_line in data.split("\n"):
            if data_line in list:
                continue
            if data_line not in list:
                if listless == "":
                    listless = data_line
                elif listless != "":
                    listless = f"{listless}\n{data_line}"
        # 6
        new_data = ""
        if listless == "":
            new_data = new_list
        elif listless != "":
            new_data = f"{listless}\n{new_list}"

        file_add = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\data_Calender.txt", "w")
        file_add.write(new_data)
        file_add.close()
        self.rem_empty_dates()
        self.fix_task()
        self.cal_todo_textbox.clear()
        self.file_to_list()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    gui = Calender()
    gui.show()
    app.exec_()