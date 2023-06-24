from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import *
from ProgramGui import Ui_allprograms
from PyQt5.QtCore import QTime, QTimer
from datetime import *
import glob
import operator

class MoneyMP(QMainWindow, Ui_allprograms):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.main_totalmoney.setText("Total Money - 0")
        self.main_edit_button.clicked.connect(self.edit_mode)
        self.main_delete_button.clicked.connect(self.delete_function)
        self.main_add_button.clicked.connect(self.add_mode)

        self.edit_cancel_button.clicked.connect(self.cancel_edit_mode)
        self.edit_enter_button.clicked.connect(self.edit_function)

        self.add_cancel_button.clicked.connect(self.cancel_add_mode)
        self.add_add_button.clicked.connect(self.add_function)

        self.hide_edit()
        self.hide_add()
        self.add_data()
        self.gui_fix()

        exist_data = glob.glob("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\data_MMP.txt")
        if not exist_data:
            file_create = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\data_MMP.txt", "a")
            file_create.close()

        exist_actions = glob.glob("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\\actions_MMP.txt")
        if not exist_actions:
            file_create = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\\actions_MMP.txt", "a")
            file_create.close()

        self.list_lists = [self.main_list_1, self.main_list_2, self.main_list_3]
        for widget in self.list_lists:
            widget.currentItemChanged.connect(self.deselect)

    def gui_fix(self):
        self.main_edit_button.setStyleSheet("background-color : #002776;"
                                            "color : white;"
                                            "border-radius : 10px")
        self.main_delete_button.setStyleSheet("background-color : #002776;"
                                            "color : white;"
                                            "border-radius : 10px")
        self.main_add_button.setStyleSheet("background-color : #002776;"
                                            "color : white;"
                                            "border-radius : 10px")
        self.edit_cancel_button.setStyleSheet("background-color : #002776;"
                                            "color : white;"
                                            "border-radius : 10px")
        self.edit_enter_button.setStyleSheet("background-color : #002776;"
                                            "color : white;"
                                            "border-radius : 10px")
        self.add_cancel_button.setStyleSheet("background-color : #002776;"
                                            "color : white;"
                                            "border-radius : 10px")
        self.add_add_button.setStyleSheet("background-color : #002776;"
                                            "color : white;"
                                            "border-radius : 10px")

        self.edit_action_1.setStyleSheet("background-color : #343434;")
        self.edit_action_2.setStyleSheet("background-color : #343434;")
        self.edit_action_3.setStyleSheet("background-color : #343434;")
        self.edit_action_4.setStyleSheet("background-color : #343434;")
        self.edit_action_5.setStyleSheet("background-color : #343434;")
        self.edit_action_6.setStyleSheet("background-color : #343434;")
        self.edit_action_7.setStyleSheet("background-color : #343434;")
        self.edit_action_8.setStyleSheet("background-color : #343434;")
        self.edit_action_9.setStyleSheet("background-color : #343434;")
        self.edit_action_10.setStyleSheet("background-color : #343434;")
        self.edit_action_11.setStyleSheet("background-color : #343434;")
        self.edit_action_12.setStyleSheet("background-color : #343434;")
        self.edit_action_13.setStyleSheet("background-color : #343434;")
        self.edit_action_14.setStyleSheet("background-color : #343434;")
        self.edit_action_15.setStyleSheet("background-color : #343434;")
        self.edit_action_16.setStyleSheet("background-color : #343434;")
        self.edit_action_17.setStyleSheet("background-color : #343434;")
        self.edit_action_18.setStyleSheet("background-color : #343434;")
        self.edit_action_19.setStyleSheet("background-color : #343434;")
        self.edit_action_20.setStyleSheet("background-color : #343434;")
        self.edit_action_21.setStyleSheet("background-color : #343434;")
        self.edit_action_22.setStyleSheet("background-color : #343434;")
        self.edit_action_23.setStyleSheet("background-color : #343434;")
        self.edit_action_24.setStyleSheet("background-color : #343434;")
        self.edit_action_25.setStyleSheet("background-color : #343434;")
        self.edit_action_26.setStyleSheet("background-color : #343434;")
        self.edit_action_27.setStyleSheet("background-color : #343434;")
        self.edit_action_28.setStyleSheet("background-color : #343434;")
        self.edit_action_29.setStyleSheet("background-color : #343434;")
        self.edit_action_30.setStyleSheet("background-color : #343434;")
        self.edit_action_31.setStyleSheet("background-color : #343434;")
        self.edit_action_32.setStyleSheet("background-color : #343434;")
        self.edit_action_33.setStyleSheet("background-color : #343434;")
        self.edit_action_34.setStyleSheet("background-color : #343434;")
        self.edit_action_35.setStyleSheet("background-color : #343434;")
        self.edit_action_36.setStyleSheet("background-color : #343434;")
        self.edit_action_37.setStyleSheet("background-color : #343434;")
        self.edit_action_38.setStyleSheet("background-color : #343434;")
        self.edit_action_39.setStyleSheet("background-color : #343434;")
        self.edit_action_40.setStyleSheet("background-color : #343434;")
        self.edit_action_41.setStyleSheet("background-color : #343434;")
        self.edit_action_42.setStyleSheet("background-color : #343434;")
        self.edit_action_43.setStyleSheet("background-color : #343434;")
        self.edit_action_44.setStyleSheet("background-color : #343434;")
        self.edit_action_45.setStyleSheet("background-color : #343434;")
        self.edit_action_46.setStyleSheet("background-color : #343434;")
        self.edit_action_47.setStyleSheet("background-color : #343434;")
        self.edit_action_48.setStyleSheet("background-color : #343434;")
        self.edit_action_49.setStyleSheet("background-color : #343434;")
        self.edit_action_50.setStyleSheet("background-color : #343434;")
        self.edit_action_51.setStyleSheet("background-color : #343434;")
        self.edit_action_52.setStyleSheet("background-color : #343434;")
        self.edit_action_53.setStyleSheet("background-color : #343434;")
        self.edit_action_54.setStyleSheet("background-color : #343434;")
        self.edit_action_55.setStyleSheet("background-color : #343434;")
        self.edit_action_56.setStyleSheet("background-color : #343434;")
        self.edit_action_57.setStyleSheet("background-color : #343434;")

    def deselect(self, new):
        if not new: return
        instance = new.listWidget()
        for widget in self.list_lists:
            if widget != instance:
                widget.setCurrentRow(-1)

    def add_data(self):
        self.main_list_1.clear()
        self.main_list_2.clear()
        self.main_list_3.clear()

        file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\data_MMP.txt", "r")
        file_data = file.read()

        printed_line_number = 0
        for data_line in file_data.split("\n"):
            self.main_list_1.addItem(data_line)
            printed_line_number += 1
            if printed_line_number == 19:
                break
        printed_line_number = 0
        for data_line in file_data.split("\n"):
            printed_line_number += 1
            if printed_line_number <= 19:
                pass
            else:
                self.main_list_2.addItem(data_line)
            if printed_line_number == 38:
                break
        printed_line_number = 0
        for data_line in file_data.split("\n"):
            printed_line_number += 1
            if printed_line_number <= 38:
                pass
            else:
                self.main_list_3.addItem(data_line)
            if printed_line_number == 57:
                break

        file.close()
        self.total_money()

    def add_function(self):
        check_if_digit = self.add_name_textbox.toPlainText().isdigit()
        check_if_letter = self.add_amount_textbox.toPlainText().isalpha()

        file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\data_MMP.txt", "r")
        lines = file.read()
        file.close()
        for line in lines.split("\n"):
            name = line.split(" ")[0]
            if name == self.add_name_textbox.toPlainText():
                self.add_amount_textbox.hide()
                self.add_name_textbox.hide()
                self.main_title.show()
                font = QtGui.QFont()
                font.setPointSize(18)
                font.setBold(True)
                self.main_title.setStyleSheet("color : red")
                self.main_title.setFont(font)
                self.main_title.setText("You cant enter the same name twice")
                self.after = QTimer()
                self.after.timeout.connect(self.timer_add)
                self.after.start(1000)
                self.add_name_textbox.clear()
                self.add_amount_textbox.clear()
            elif check_if_digit:
                self.add_amount_textbox.hide()
                self.add_name_textbox.hide()
                self.main_title.show()
                font = QtGui.QFont()
                font.setPointSize(18)
                font.setBold(True)
                self.main_title.setStyleSheet("color : red")
                self.main_title.setFont(font)
                self.main_title.setText("You must only type letters in the name text box")
                self.after = QTimer()
                self.after.timeout.connect(self.timer_add)
                self.after.start(1000)
                self.add_name_textbox.clear()
                self.add_amount_textbox.clear()
            elif check_if_letter:
                self.add_amount_textbox.hide()
                self.add_name_textbox.hide()
                self.main_title.show()
                font = QtGui.QFont()
                font.setPointSize(18)
                font.setBold(True)
                self.main_title.setStyleSheet("color : red")
                self.main_title.setFont(font)
                self.main_title.setText("You must only type numbers in the amount text box")
                self.after = QTimer()
                self.after.timeout.connect(self.timer_add)
                self.after.start(1000)
                self.add_name_textbox.clear()
                self.add_amount_textbox.clear()
            elif self.add_name_textbox.toPlainText() == "" or self.add_amount_textbox.toPlainText() == "":
                self.add_amount_textbox.hide()
                self.add_name_textbox.hide()
                self.main_title.show()
                font = QtGui.QFont()
                font.setPointSize(18)
                font.setBold(True)
                self.main_title.setStyleSheet("color : red")
                self.main_title.setFont(font)
                self.main_title.setText("You cannot leave a text box empty")
                self.after = QTimer()
                self.after.timeout.connect(self.timer_add)
                self.after.start(1000)
                self.add_name_textbox.clear()
                self.add_amount_textbox.clear()
            else:
                file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\data_MMP.txt", "r")
                file_text = file.read()
                file.close()
                if file_text == "":
                    file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\data_MMP.txt", "a")
                    file.write(f"{self.add_name_textbox.toPlainText()} - {self.add_amount_textbox.toPlainText()}")
                    file.close()
                else:
                    file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\data_MMP.txt", "a")
                    file.write(f"\n{self.add_name_textbox.toPlainText()} - {self.add_amount_textbox.toPlainText()}")
                    file.close()

                self.hide_add()
                self.add_data()

                today = date.today()
                ac_date = today.strftime("%d/%m/%Y")
                actions = f"added {self.add_name_textbox.toPlainText()} with {self.add_amount_textbox.toPlainText()} money at {ac_date}\n"
                actions_file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\\actions_MMP.txt", "a")
                actions_file.write(actions)
                actions_file.close()

                self.add_name_textbox.clear()
                self.add_amount_textbox.clear()

    def hide_add(self):
        self.add_add_button.hide()
        self.add_cancel_button.hide()
        self.add_name_textbox.hide()
        self.add_amount_textbox.hide()
        self.main_delete_button.show()
        self.main_title.show()

    def hide_edit(self):
        self.edit_action_1.hide()
        self.edit_action_2.hide()
        self.edit_action_3.hide()
        self.edit_action_4.hide()
        self.edit_action_5.hide()
        self.edit_action_6.hide()
        self.edit_action_7.hide()
        self.edit_action_8.hide()
        self.edit_action_9.hide()
        self.edit_action_10.hide()
        self.edit_action_11.hide()
        self.edit_action_12.hide()
        self.edit_action_13.hide()
        self.edit_action_14.hide()
        self.edit_action_15.hide()
        self.edit_action_16.hide()
        self.edit_action_17.hide()
        self.edit_action_18.hide()
        self.edit_action_19.hide()
        self.edit_action_20.hide()
        self.edit_action_21.hide()
        self.edit_action_22.hide()
        self.edit_action_23.hide()
        self.edit_action_24.hide()
        self.edit_action_25.hide()
        self.edit_action_26.hide()
        self.edit_action_27.hide()
        self.edit_action_28.hide()
        self.edit_action_29.hide()
        self.edit_action_30.hide()
        self.edit_action_31.hide()
        self.edit_action_32.hide()
        self.edit_action_33.hide()
        self.edit_action_34.hide()
        self.edit_action_35.hide()
        self.edit_action_36.hide()
        self.edit_action_37.hide()
        self.edit_action_38.hide()
        self.edit_action_39.hide()
        self.edit_action_40.hide()
        self.edit_action_41.hide()
        self.edit_action_42.hide()
        self.edit_action_43.hide()
        self.edit_action_44.hide()
        self.edit_action_45.hide()
        self.edit_action_46.hide()
        self.edit_action_47.hide()
        self.edit_action_48.hide()
        self.edit_action_49.hide()
        self.edit_action_50.hide()
        self.edit_action_51.hide()
        self.edit_action_52.hide()
        self.edit_action_53.hide()
        self.edit_action_54.hide()
        self.edit_action_55.hide()
        self.edit_action_56.hide()
        self.edit_action_57.hide()
        self.edit_amount_1.hide()
        self.edit_amount_2.hide()
        self.edit_amount_3.hide()
        self.edit_amount_4.hide()
        self.edit_amount_5.hide()
        self.edit_amount_6.hide()
        self.edit_amount_7.hide()
        self.edit_amount_8.hide()
        self.edit_amount_9.hide()
        self.edit_amount_10.hide()
        self.edit_amount_11.hide()
        self.edit_amount_12.hide()
        self.edit_amount_13.hide()
        self.edit_amount_14.hide()
        self.edit_amount_15.hide()
        self.edit_amount_16.hide()
        self.edit_amount_17.hide()
        self.edit_amount_18.hide()
        self.edit_amount_19.hide()
        self.edit_amount_20.hide()
        self.edit_amount_21.hide()
        self.edit_amount_22.hide()
        self.edit_amount_23.hide()
        self.edit_amount_24.hide()
        self.edit_amount_25.hide()
        self.edit_amount_26.hide()
        self.edit_amount_27.hide()
        self.edit_amount_28.hide()
        self.edit_amount_29.hide()
        self.edit_amount_30.hide()
        self.edit_amount_31.hide()
        self.edit_amount_32.hide()
        self.edit_amount_33.hide()
        self.edit_amount_34.hide()
        self.edit_amount_35.hide()
        self.edit_amount_36.hide()
        self.edit_amount_37.hide()
        self.edit_amount_38.hide()
        self.edit_amount_39.hide()
        self.edit_amount_40.hide()
        self.edit_amount_41.hide()
        self.edit_amount_42.hide()
        self.edit_amount_43.hide()
        self.edit_amount_44.hide()
        self.edit_amount_45.hide()
        self.edit_amount_46.hide()
        self.edit_amount_47.hide()
        self.edit_amount_48.hide()
        self.edit_amount_49.hide()
        self.edit_amount_50.hide()
        self.edit_amount_51.hide()
        self.edit_amount_52.hide()
        self.edit_amount_53.hide()
        self.edit_amount_54.hide()
        self.edit_amount_55.hide()
        self.edit_amount_56.hide()
        self.edit_amount_57.hide()
        self.edit_cancel_button.hide()
        self.edit_enter_button.hide()
        self.main_delete_button.show()

    def show_add(self):
        self.add_add_button.show()
        self.add_cancel_button.show()
        self.add_name_textbox.show()
        self.add_amount_textbox.show()

    def show_edit(self):
        self.edit_action_1.show()
        self.edit_action_2.show()
        self.edit_action_3.show()
        self.edit_action_4.show()
        self.edit_action_5.show()
        self.edit_action_6.show()
        self.edit_action_7.show()
        self.edit_action_8.show()
        self.edit_action_9.show()
        self.edit_action_10.show()
        self.edit_action_11.show()
        self.edit_action_12.show()
        self.edit_action_13.show()
        self.edit_action_14.show()
        self.edit_action_15.show()
        self.edit_action_16.show()
        self.edit_action_17.show()
        self.edit_action_18.show()
        self.edit_action_19.show()
        self.edit_action_20.show()
        self.edit_action_21.show()
        self.edit_action_22.show()
        self.edit_action_23.show()
        self.edit_action_24.show()
        self.edit_action_25.show()
        self.edit_action_26.show()
        self.edit_action_27.show()
        self.edit_action_28.show()
        self.edit_action_29.show()
        self.edit_action_30.show()
        self.edit_action_31.show()
        self.edit_action_32.show()
        self.edit_action_33.show()
        self.edit_action_34.show()
        self.edit_action_35.show()
        self.edit_action_36.show()
        self.edit_action_37.show()
        self.edit_action_38.show()
        self.edit_action_39.show()
        self.edit_action_40.show()
        self.edit_action_41.show()
        self.edit_action_42.show()
        self.edit_action_43.show()
        self.edit_action_44.show()
        self.edit_action_45.show()
        self.edit_action_46.show()
        self.edit_action_47.show()
        self.edit_action_48.show()
        self.edit_action_49.show()
        self.edit_action_50.show()
        self.edit_action_51.show()
        self.edit_action_52.show()
        self.edit_action_53.show()
        self.edit_action_54.show()
        self.edit_action_55.show()
        self.edit_action_56.show()
        self.edit_action_57.show()
        self.edit_amount_1.show()
        self.edit_amount_2.show()
        self.edit_amount_3.show()
        self.edit_amount_4.show()
        self.edit_amount_5.show()
        self.edit_amount_6.show()
        self.edit_amount_7.show()
        self.edit_amount_8.show()
        self.edit_amount_9.show()
        self.edit_amount_10.show()
        self.edit_amount_11.show()
        self.edit_amount_12.show()
        self.edit_amount_13.show()
        self.edit_amount_14.show()
        self.edit_amount_15.show()
        self.edit_amount_16.show()
        self.edit_amount_17.show()
        self.edit_amount_18.show()
        self.edit_amount_19.show()
        self.edit_amount_20.show()
        self.edit_amount_21.show()
        self.edit_amount_22.show()
        self.edit_amount_23.show()
        self.edit_amount_24.show()
        self.edit_amount_25.show()
        self.edit_amount_26.show()
        self.edit_amount_27.show()
        self.edit_amount_28.show()
        self.edit_amount_29.show()
        self.edit_amount_30.show()
        self.edit_amount_31.show()
        self.edit_amount_32.show()
        self.edit_amount_33.show()
        self.edit_amount_34.show()
        self.edit_amount_35.show()
        self.edit_amount_36.show()
        self.edit_amount_37.show()
        self.edit_amount_38.show()
        self.edit_amount_39.show()
        self.edit_amount_40.show()
        self.edit_amount_41.show()
        self.edit_amount_42.show()
        self.edit_amount_43.show()
        self.edit_amount_44.show()
        self.edit_amount_45.show()
        self.edit_amount_46.show()
        self.edit_amount_47.show()
        self.edit_amount_48.show()
        self.edit_amount_49.show()
        self.edit_amount_50.show()
        self.edit_amount_51.show()
        self.edit_amount_52.show()
        self.edit_amount_53.show()
        self.edit_amount_54.show()
        self.edit_amount_55.show()
        self.edit_amount_56.show()
        self.edit_amount_57.show()
        self.edit_cancel_button.show()
        self.edit_enter_button.show()

    def timer_add(self):
        self.main_title.setText("Money Manegment Program")
        self.main_title.setStyleSheet("color : white")
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        self.main_title.setFont(font)
        self.add_name_textbox.show()
        self.add_amount_textbox.show()
        self.main_title.hide()

    def timer(self):
        self.main_title.setText("Money Manegment Program")
        self.main_title.setStyleSheet("color : white")
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        self.main_title.setFont(font)

    def edit_mode(self):
        selected_row_1 = self.main_list_1.currentRow()
        selected_row_2 = self.main_list_2.currentRow()
        selected_row_3 = self.main_list_3.currentRow()
        if selected_row_1 >= 0:
            action_amount_number = selected_row_1 + 1
        elif selected_row_2 >= 0:
            action_amount_number = selected_row_2 + 20
        elif selected_row_3 >= 0:
            action_amount_number = selected_row_3 + 39
        else:
            action_amount_number = 0
            font = QtGui.QFont()
            font.setPointSize(18)
            font.setBold(True)
            self.main_title.setStyleSheet("color : red")
            self.main_title.setFont(font)
            self.main_title.setText("You Must Select A Row Before Editing It")
            self.after = QTimer()
            self.after.timeout.connect(self.timer)
            self.after.start(1000)

        if action_amount_number == 1:
            self.edit_action_1.show()
            self.edit_amount_1.show()
            self.main_delete_button.hide()
            self.edit_cancel_button.show()
            self.edit_enter_button.show()
        elif action_amount_number == 2:
            self.edit_action_2.show()
            self.edit_amount_2.show()
            self.main_delete_button.hide()
            self.edit_cancel_button.show()
            self.edit_enter_button.show()
        elif action_amount_number == 3:
            self.edit_action_3.show()
            self.edit_amount_3.show()
            self.main_delete_button.hide()
            self.edit_cancel_button.show()
            self.edit_enter_button.show()
        elif action_amount_number == 4:
            self.edit_action_4.show()
            self.edit_amount_4.show()
            self.main_delete_button.hide()
            self.edit_cancel_button.show()
            self.edit_enter_button.show()
        elif action_amount_number == 5:
            self.edit_action_5.show()
            self.edit_amount_5.show()
            self.main_delete_button.hide()
            self.edit_cancel_button.show()
            self.edit_enter_button.show()
        elif action_amount_number == 6:
            self.edit_action_6.show()
            self.edit_amount_6.show()
            self.main_delete_button.hide()
            self.edit_cancel_button.show()
            self.edit_enter_button.show()
        elif action_amount_number == 7:
            self.edit_action_7.show()
            self.edit_amount_7.show()
            self.main_delete_button.hide()
            self.edit_cancel_button.show()
            self.edit_enter_button.show()
        elif action_amount_number == 8:
            self.edit_action_8.show()
            self.edit_amount_8.show()
            self.main_delete_button.hide()
            self.edit_cancel_button.show()
            self.edit_enter_button.show()
        elif action_amount_number == 9:
            self.edit_action_9.show()
            self.edit_amount_9.show()
            self.main_delete_button.hide()
            self.edit_cancel_button.show()
            self.edit_enter_button.show()
        elif action_amount_number == 10:
            self.edit_action_10.show()
            self.edit_amount_10.show()
            self.main_delete_button.hide()
            self.edit_cancel_button.show()
            self.edit_enter_button.show()
        elif action_amount_number == 11:
            self.edit_action_11.show()
            self.edit_amount_11.show()
            self.main_delete_button.hide()
            self.edit_cancel_button.show()
            self.edit_enter_button.show()
        elif action_amount_number == 12:
            self.edit_action_12.show()
            self.edit_amount_12.show()
            self.main_delete_button.hide()
            self.edit_cancel_button.show()
            self.edit_enter_button.show()
        elif action_amount_number == 13:
            self.edit_action_13.show()
            self.edit_amount_13.show()
            self.main_delete_button.hide()
            self.edit_cancel_button.show()
            self.edit_enter_button.show()
        elif action_amount_number == 14:
            self.edit_action_14.show()
            self.edit_amount_14.show()
            self.main_delete_button.hide()
            self.edit_cancel_button.show()
            self.edit_enter_button.show()
        elif action_amount_number == 15:
            self.edit_action_15.show()
            self.edit_amount_15.show()
            self.main_delete_button.hide()
            self.edit_cancel_button.show()
            self.edit_enter_button.show()
        elif action_amount_number == 16:
            self.edit_action_16.show()
            self.edit_amount_16.show()
            self.main_delete_button.hide()
            self.edit_cancel_button.show()
            self.edit_enter_button.show()
        elif action_amount_number == 17:
            self.edit_action_17.show()
            self.edit_amount_17.show()
            self.main_delete_button.hide()
            self.edit_cancel_button.show()
            self.edit_enter_button.show()
        elif action_amount_number == 18:
            self.edit_action_18.show()
            self.edit_amount_18.show()
            self.main_delete_button.hide()
            self.edit_cancel_button.show()
            self.edit_enter_button.show()
        elif action_amount_number == 19:
            self.edit_action_19.show()
            self.edit_amount_19.show()
            self.main_delete_button.hide()
            self.edit_cancel_button.show()
            self.edit_enter_button.show()
        elif action_amount_number == 20:
            self.edit_action_20.show()
            self.edit_amount_20.show()
            self.main_delete_button.hide()
            self.edit_cancel_button.show()
            self.edit_enter_button.show()
        elif action_amount_number == 21:
            self.edit_action_21.show()
            self.edit_amount_21.show()
            self.main_delete_button.hide()
            self.edit_cancel_button.show()
            self.edit_enter_button.show()
        elif action_amount_number == 22:
            self.edit_action_22.show()
            self.edit_amount_22.show()
            self.main_delete_button.hide()
            self.edit_cancel_button.show()
            self.edit_enter_button.show()
        elif action_amount_number == 23:
            self.edit_action_23.show()
            self.edit_amount_23.show()
            self.main_delete_button.hide()
            self.edit_cancel_button.show()
            self.edit_enter_button.show()
        elif action_amount_number == 24:
            self.edit_action_24.show()
            self.edit_amount_24.show()
            self.main_delete_button.hide()
            self.edit_cancel_button.show()
            self.edit_enter_button.show()
        elif action_amount_number == 25:
            self.edit_action_25.show()
            self.edit_amount_25.show()
            self.main_delete_button.hide()
            self.edit_cancel_button.show()
            self.edit_enter_button.show()
        elif action_amount_number == 26:
            self.edit_action_26.show()
            self.edit_amount_26.show()
            self.main_delete_button.hide()
            self.edit_cancel_button.show()
            self.edit_enter_button.show()
        elif action_amount_number == 27:
            self.edit_action_27.show()
            self.edit_amount_27.show()
            self.main_delete_button.hide()
            self.edit_cancel_button.show()
            self.edit_enter_button.show()
        elif action_amount_number == 28:
            self.edit_action_28.show()
            self.edit_amount_28.show()
            self.main_delete_button.hide()
            self.edit_cancel_button.show()
            self.edit_enter_button.show()
        elif action_amount_number == 29:
            self.edit_action_29.show()
            self.edit_amount_29.show()
            self.main_delete_button.hide()
            self.edit_cancel_button.show()
            self.edit_enter_button.show()
        elif action_amount_number == 30:
            self.edit_action_30.show()
            self.edit_amount_30.show()
            self.main_delete_button.hide()
            self.edit_cancel_button.show()
            self.edit_enter_button.show()
        elif action_amount_number == 31:
            self.edit_action_31.show()
            self.edit_amount_31.show()
            self.main_delete_button.hide()
            self.edit_cancel_button.show()
            self.edit_enter_button.show()
        elif action_amount_number == 32:
            self.edit_action_32.show()
            self.edit_amount_32.show()
            self.main_delete_button.hide()
            self.edit_cancel_button.show()
            self.edit_enter_button.show()
        elif action_amount_number == 33:
            self.edit_action_33.show()
            self.edit_amount_33.show()
            self.main_delete_button.hide()
            self.edit_cancel_button.show()
            self.edit_enter_button.show()
        elif action_amount_number == 34:
            self.edit_action_34.show()
            self.edit_amount_34.show()
            self.main_delete_button.hide()
            self.edit_cancel_button.show()
            self.edit_enter_button.show()
        elif action_amount_number == 35:
            self.edit_action_35.show()
            self.edit_amount_35.show()
            self.main_delete_button.hide()
            self.edit_cancel_button.show()
            self.edit_enter_button.show()
        elif action_amount_number == 36:
            self.edit_action_36.show()
            self.edit_amount_36.show()
            self.main_delete_button.hide()
            self.edit_cancel_button.show()
            self.edit_enter_button.show()
        elif action_amount_number == 37:
            self.edit_action_37.show()
            self.edit_amount_37.show()
            self.main_delete_button.hide()
            self.edit_cancel_button.show()
            self.edit_enter_button.show()
        elif action_amount_number == 38:
            self.edit_action_38.show()
            self.edit_amount_38.show()
            self.main_delete_button.hide()
            self.edit_cancel_button.show()
            self.edit_enter_button.show()
        elif action_amount_number == 39:
            self.edit_action_39.show()
            self.edit_amount_39.show()
            self.main_delete_button.hide()
            self.edit_cancel_button.show()
            self.edit_enter_button.show()
        elif action_amount_number == 40:
            self.edit_action_40.show()
            self.edit_amount_40.show()
            self.main_delete_button.hide()
            self.edit_cancel_button.show()
            self.edit_enter_button.show()
        elif action_amount_number == 41:
            self.edit_action_41.show()
            self.edit_amount_41.show()
            self.main_delete_button.hide()
            self.edit_cancel_button.show()
            self.edit_enter_button.show()
        elif action_amount_number == 42:
            self.edit_action_42.show()
            self.edit_amount_42.show()
            self.main_delete_button.hide()
            self.edit_cancel_button.show()
            self.edit_enter_button.show()
        elif action_amount_number == 43:
            self.edit_action_43.show()
            self.edit_amount_43.show()
            self.main_delete_button.hide()
            self.edit_cancel_button.show()
            self.edit_enter_button.show()
        elif action_amount_number == 44:
            self.edit_action_44.show()
            self.edit_amount_44.show()
            self.main_delete_button.hide()
            self.edit_cancel_button.show()
            self.edit_enter_button.show()
        elif action_amount_number == 45:
            self.edit_action_45.show()
            self.edit_amount_45.show()
            self.main_delete_button.hide()
            self.edit_cancel_button.show()
            self.edit_enter_button.show()
        elif action_amount_number == 46:
            self.edit_action_46.show()
            self.edit_amount_46.show()
            self.main_delete_button.hide()
            self.edit_cancel_button.show()
            self.edit_enter_button.show()
        elif action_amount_number == 47:
            self.edit_action_47.show()
            self.edit_amount_47.show()
            self.main_delete_button.hide()
            self.edit_cancel_button.show()
            self.edit_enter_button.show()
        elif action_amount_number == 48:
            self.edit_action_48.show()
            self.edit_amount_48.show()
            self.main_delete_button.hide()
            self.edit_cancel_button.show()
            self.edit_enter_button.show()
        elif action_amount_number == 49:
            self.edit_action_49.show()
            self.edit_amount_49.show()
            self.main_delete_button.hide()
            self.edit_cancel_button.show()
            self.edit_enter_button.show()
        elif action_amount_number == 50:
            self.edit_action_50.show()
            self.edit_amount_50.show()
            self.main_delete_button.hide()
            self.edit_cancel_button.show()
            self.edit_enter_button.show()
        elif action_amount_number == 51:
            self.edit_action_51.show()
            self.edit_amount_51.show()
            self.main_delete_button.hide()
            self.edit_cancel_button.show()
            self.edit_enter_button.show()
        elif action_amount_number == 52:
            self.edit_action_52.show()
            self.edit_amount_52.show()
            self.main_delete_button.hide()
            self.edit_cancel_button.show()
            self.edit_enter_button.show()
        elif action_amount_number == 53:
            self.edit_action_53.show()
            self.edit_amount_53.show()
            self.main_delete_button.hide()
            self.edit_cancel_button.show()
            self.edit_enter_button.show()
        elif action_amount_number == 54:
            self.edit_action_54.show()
            self.edit_amount_54.show()
            self.main_delete_button.hide()
            self.edit_cancel_button.show()
            self.edit_enter_button.show()
        elif action_amount_number == 55:
            self.edit_action_55.show()
            self.edit_amount_55.show()
            self.main_delete_button.hide()
            self.edit_cancel_button.show()
            self.edit_enter_button.show()
        elif action_amount_number == 56:
            self.edit_action_56.show()
            self.edit_amount_56.show()
            self.main_delete_button.hide()
            self.edit_cancel_button.show()
            self.edit_enter_button.show()
        elif action_amount_number == 57:
            self.edit_action_57.show()
            self.edit_amount_57.show()
            self.main_delete_button.hide()
            self.edit_cancel_button.show()
            self.edit_enter_button.show()
        elif action_amount_number == 58:
            self.edit_action_58.show()
            self.edit_amount_58.show()
            self.main_delete_button.hide()
            self.edit_cancel_button.show()
            self.edit_enter_button.show()
        elif action_amount_number == 59:
            self.edit_action_59.show()
            self.edit_amount_59.show()
            self.main_delete_button.hide()
            self.edit_cancel_button.show()
            self.edit_enter_button.show()
        elif action_amount_number == 60:
            self.edit_action_60.show()
            self.edit_amount_60.show()
            self.main_delete_button.hide()
            self.edit_cancel_button.show()
            self.edit_enter_button.show()

    def edit_function(self):
        #this is about to be horrible
        selected_row_1 = int(self.main_list_1.currentRow()) + 1
        selected_row_2 = int(self.main_list_2.currentRow()) + 21
        selected_row_3 = int(self.main_list_3.currentRow()) + 41

        ops = {"+": operator.add, "-": operator.sub}

        file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\data_MMP.txt", "r")
        lines = file.read()
        file.close()

        if selected_row_1 == 1:
            check_if_digit = self.edit_amount_1.text().isdigit()
            if check_if_digit:
                old_line = self.main_list_1.currentItem().text()
                final_num = str(ops[str(self.edit_action_1.currentText())](int(old_line.split()[-1]), int(self.edit_amount_1.text())))
                new_line = f"{old_line.split()[0]} - {final_num}"
                new_data = ""
                for file_line in lines.split("\n"):
                    if file_line == old_line:
                        if new_data == "":
                            new_data = f"{new_line}"
                        else:
                          new_data = f"{new_data}\n{new_line}"
                    else:
                        if new_data == "":
                            new_data = f"{file_line}"
                        else:
                            new_data = f"{new_data}\n{file_line}"
                file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\data_MMP.txt", "w")
                file.write(new_data)
                file.close()

                today = date.today()
                ac_date = today.strftime("%d/%m/%Y")
                if str(self.edit_action_1.currentText()) == "+":
                    add_sub = "added"
                    for_from = "for"
                else:
                    add_sub = "subtracted"
                    for_from = "from"
                name = new_line.split(" ")[0]
                actions = f"{add_sub} {for_from} {name} {self.edit_amount_1.text()} money at {ac_date}\n"
                actions_file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\\actions_MMP.txt", "a")
                actions_file.write(actions)
                actions_file.close()

                self.add_data()
                self.hide_edit()
                self.edit_amount_1.clear()
            elif check_if_digit == False or self.edit_amount_1.text() == "":
                font = QtGui.QFont()
                font.setPointSize(18)
                font.setBold(True)
                self.main_title.setStyleSheet("color : red")
                self.main_title.setFont(font)
                self.main_title.setText("You must type only digits into the text box")
                self.after = QTimer()
                self.after.timeout.connect(self.timer)
                self.after.start(1000)
                self.edit_amount_1.clear()

            #this is gonna take forever

        if selected_row_1 == 2:
            check_if_digit = self.edit_amount_2.text().isdigit()
            if check_if_digit:
                old_line = self.main_list_1.currentItem().text()
                temp = str(ops[str(self.edit_action_2.currentText())](int(old_line.split()[-1]), int(self.edit_amount_2.text())))
                new_line = f"{old_line.split()[0]} - {temp}"
                new_data = ""
                for file_line in lines.split("\n"):
                    if file_line == old_line:
                        if new_data == "":
                            new_data = f"{new_line}"
                        else:
                          new_data = f"{new_data}\n{new_line}"
                    else:
                        if new_data == "":
                            new_data = f"{file_line}"
                        else:
                            new_data = f"{new_data}\n{file_line}"
                file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\data_MMP.txt", "w")
                file.write(new_data)
                file.close()

                today = date.today()
                ac_date = today.strftime("%d/%m/%Y")
                if str(self.edit_action_2.currentText()) == "+":
                    add_sub = "added"
                    for_from = "for"
                else:
                    add_sub = "subtracted"
                    for_from = "from"
                name = new_line.split(" ")[0]
                actions = f"{add_sub} {for_from} {name} {self.edit_amount_2.text()} money at {ac_date}\n"
                actions_file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\\actions_MMP.txt", "a")
                actions_file.write(actions)
                actions_file.close()

                self.add_data()
                self.hide_edit()
                self.edit_amount_2.clear()
            elif check_if_digit == False or self.edit_amount_2.text() == "":
                font = QtGui.QFont()
                font.setPointSize(18)
                font.setBold(True)
                self.main_title.setStyleSheet("color : red")
                self.main_title.setFont(font)
                self.main_title.setText("You must type only digits into the text box")
                self.after = QTimer()
                self.after.timeout.connect(self.timer)
                self.after.start(1000)
                self.edit_amount_2.clear()

            # just realized i m gonna have to put errors into 60 different if statments that is gonna be a huge grind

        if selected_row_1 == 3:
            check_if_digit = self.edit_amount_3.text().isdigit()
            if check_if_digit:
                old_line = self.main_list_3.currentItem().text()
                temp = str(ops[str(self.edit_action_3.currentText())](int(old_line.split()[-1]), int(self.edit_amount_3.text())))
                new_line = f"{old_line.split()[0]} - {temp}"
                new_data = ""

                for file_line in lines.split("\n"):
                    if file_line == old_line:
                        if new_data == "":
                            new_data = f"{new_line}"
                        else:
                            new_data = f"{new_data}\n{new_line}"
                    else:
                        if new_data == "":
                            new_data = f"{file_line}"
                        else:
                            new_data = f"{new_data}\n{file_line}"
                file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\data_MMP.txt", "w")
                file.write(new_data)
                file.close()
                today = date.today()
                ac_date = today.strftime("%d/%m/%Y")
                if str(self.edit_action_3.currentText()) == "+":
                    add_sub = "added"
                    for_from = "for"
                else:
                    add_sub = "subtracted"
                    for_from = "from"
                name = new_line.split(" ")[0]
                actions = f"{add_sub} {for_from} {name} {self.edit_amount_3.text()} money at {ac_date}\n"
                actions_file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\\actions_MMP.txt", "a")
                actions_file.write(actions)
                actions_file.close()

                self.add_data()
                self.hide_edit()
                self.edit_amount_3.clear()
            elif check_if_digit == False or self.edit_amount_3.text() == "":
                font = QtGui.QFont()
                font.setPointSize(18)
                font.setBold(True)
                self.main_title.setStyleSheet("color : red")
                self.main_title.setFont(font)
                self.main_title.setText("You must type only digits into the text box")
                self.after = QTimer()
                self.after.timeout.connect(self.timer)
                self.after.start(1000)
                self.edit_amount_3.clear()

        if selected_row_1 == 4:
            check_if_digit = self.edit_amount_4.text().isdigit()
            if check_if_digit:
                old_line = self.main_list_1.currentItem().text()
                temp = str(ops[str(self.edit_action_4.currentText())](int(old_line.split()[-1]), int(self.edit_amount_4.text())))
                new_line = f"{old_line.split()[0]} - {temp}"
                new_data = ""

                for file_line in lines.split("\n"):
                    if file_line == old_line:
                        if new_data == "":
                            new_data = f"{new_line}"
                        else:
                            new_data = f"{new_data}\n{new_line}"
                    else:
                        if new_data == "":
                            new_data = f"{file_line}"
                        else:
                            new_data = f"{new_data}\n{file_line}"
                file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\data_MMP.txt", "w")
                file.write(new_data)
                file.close()

                today = date.today()
                ac_date = today.strftime("%d/%m/%Y")
                if str(self.edit_action_4.currentText()) == "+":
                    add_sub = "added"
                    for_from = "for"
                else:
                    add_sub = "subtracted"
                    for_from = "from"
                name = new_line.split(" ")[0]
                actions = f"{add_sub} {for_from} {name} {self.edit_amount_4.text()} money at {ac_date}\n"
                actions_file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\\actions_MMP.txt", "a")
                actions_file.write(actions)
                actions_file.close()

                self.add_data()
                self.hide_edit()
                self.edit_amount_4.clear()
            elif check_if_digit == False or self.edit_amount_4.text() == "":
                font = QtGui.QFont()
                font.setPointSize(18)
                font.setBold(True)
                self.main_title.setStyleSheet("color : red")
                self.main_title.setFont(font)
                self.main_title.setText("You must type only digits into the text box")
                self.after = QTimer()
                self.after.timeout.connect(self.timer)
                self.after.start(1000)
                self.edit_amount_4.clear()

        if selected_row_1 == 5:
            check_if_digit = self.edit_amount_5.text().isdigit()
            if check_if_digit:
                old_line = self.main_list_1.currentItem().text()
                temp = str(ops[str(self.edit_action_5.currentText())](int(old_line.split()[-1]), int(self.edit_amount_5.text())))
                new_line = f"{old_line.split()[0]} - {temp}"
                new_data = ""

                for file_line in lines.split("\n"):
                    if file_line == old_line:
                        if new_data == "":
                            new_data = f"{new_line}"
                        else:
                            new_data = f"{new_data}\n{new_line}"
                    else:
                        if new_data == "":
                            new_data = f"{file_line}"
                        else:
                            new_data = f"{new_data}\n{file_line}"
                file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\data_MMP.txt", "w")
                file.write(new_data)
                file.close()

                today = date.today()
                ac_date = today.strftime("%d/%m/%Y")
                if str(self.edit_action_5.currentText()) == "+":
                    add_sub = "added"
                    for_from = "for"
                else:
                    add_sub = "subtracted"
                    for_from = "from"
                name = new_line.split(" ")[0]
                actions = f"{add_sub} {for_from} {name} {self.edit_amount_5.text()} money at {ac_date}\n"
                actions_file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\\actions_MMP.txt", "a")
                actions_file.write(actions)
                actions_file.close()

                self.add_data()
                self.hide_edit()
                self.edit_amount_5.clear()
            elif check_if_digit == False or self.edit_amount_5.text() == "":
                font = QtGui.QFont()
                font.setPointSize(18)
                font.setBold(True)
                self.main_title.setStyleSheet("color : red")
                self.main_title.setFont(font)
                self.main_title.setText("You must type only digits into the text box")
                self.after = QTimer()
                self.after.timeout.connect(self.timer)
                self.after.start(1000)
                self.edit_amount_5.clear()

        if selected_row_1 == 6:
            check_if_digit = self.edit_amount_6.text().isdigit()
            if check_if_digit:
                old_line = self.main_list_1.currentItem().text()
                temp = str(ops[str(self.edit_action_6.currentText())](int(old_line.split()[-1]), int(self.edit_amount_6.text())))
                new_line = f"{old_line.split()[0]} - {temp}"
                new_data = ""

                for file_line in lines.split("\n"):
                    if file_line == old_line:
                        if new_data == "":
                            new_data = f"{new_line}"
                        else:
                            new_data = f"{new_data}\n{new_line}"
                    else:
                        if new_data == "":
                            new_data = f"{file_line}"
                        else:
                            new_data = f"{new_data}\n{file_line}"
                file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\data_MMP.txt", "w")
                file.write(new_data)
                file.close()

                today = date.today()
                ac_date = today.strftime("%d/%m/%Y")
                if str(self.edit_action_6.currentText()) == "+":
                    add_sub = "added"
                    for_from = "for"
                else:
                    add_sub = "subtracted"
                    for_from = "from"
                name = new_line.split(" ")[0]
                actions = f"{add_sub} {for_from} {name} {self.edit_amount_6.text()} money at {ac_date}\n"
                actions_file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\\actions_MMP.txt", "a")
                actions_file.write(actions)
                actions_file.close()

                self.add_data()
                self.hide_edit()
                self.edit_amount_6.clear()
            elif check_if_digit == False or self.edit_amount_6.text() == "":
                font = QtGui.QFont()
                font.setPointSize(18)
                font.setBold(True)
                self.main_title.setStyleSheet("color : red")
                self.main_title.setFont(font)
                self.main_title.setText("You must type only digits into the text box")
                self.after = QTimer()
                self.after.timeout.connect(self.timer)
                self.after.start(1000)
                self.edit_amount_6.clear()

        if selected_row_1 == 7:
            check_if_digit = self.edit_amount_7.text().isdigit()
            if check_if_digit:
                old_line = self.main_list_1.currentItem().text()
                temp = str(ops[str(self.edit_action_7.currentText())](int(old_line.split()[-1]), int(self.edit_amount_7.text())))
                new_line = f"{old_line.split()[0]} - {temp}"
                new_data = ""

                for file_line in lines.split("\n"):
                    if file_line == old_line:
                        if new_data == "":
                            new_data = f"{new_line}"
                        else:
                            new_data = f"{new_data}\n{new_line}"
                    else:
                        if new_data == "":
                            new_data = f"{file_line}"
                        else:
                            new_data = f"{new_data}\n{file_line}"
                file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\data_MMP.txt", "w")
                file.write(new_data)
                file.close()

                today = date.today()
                ac_date = today.strftime("%d/%m/%Y")
                if str(self.edit_action_7.currentText()) == "+":
                    add_sub = "added"
                    for_from = "for"
                else:
                    add_sub = "subtracted"
                    for_from = "from"
                name = new_line.split(" ")[0]
                actions = f"{add_sub} {for_from} {name} {self.edit_amount_7.text()} money at {ac_date}\n"
                actions_file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\\actions_MMP.txt", "a")
                actions_file.write(actions)
                actions_file.close()

                self.add_data()
                self.hide_edit()
                self.edit_amount_7.clear()
            elif check_if_digit == False or self.edit_amount_7.text() == "":
                font = QtGui.QFont()
                font.setPointSize(18)
                font.setBold(True)
                self.main_title.setStyleSheet("color : red")
                self.main_title.setFont(font)
                self.main_title.setText("You must type only digits into the text box")
                self.after = QTimer()
                self.after.timeout.connect(self.timer)
                self.after.start(1000)
                self.edit_amount_7.clear()

        if selected_row_1 == 8:
            check_if_digit = self.edit_amount_8.text().isdigit()
            if check_if_digit:
                old_line = self.main_list_1.currentItem().text()
                temp = str(ops[str(self.edit_action_8.currentText())](int(old_line.split()[-1]), int(self.edit_amount_8.text())))
                new_line = f"{old_line.split()[0]} - {temp}"
                new_data = ""

                for file_line in lines.split("\n"):
                    if file_line == old_line:
                        if new_data == "":
                            new_data = f"{new_line}"
                        else:
                            new_data = f"{new_data}\n{new_line}"
                    else:
                        if new_data == "":
                            new_data = f"{file_line}"
                        else:
                            new_data = f"{new_data}\n{file_line}"
                file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\data_MMP.txt", "w")
                file.write(new_data)
                file.close()

                today = date.today()
                ac_date = today.strftime("%d/%m/%Y")
                if str(self.edit_action_8.currentText()) == "+":
                    add_sub = "added"
                    for_from = "for"
                else:
                    add_sub = "subtracted"
                    for_from = "from"
                name = new_line.split(" ")[0]
                actions = f"{add_sub} {for_from} {name} {self.edit_amount_8.text()} money at {ac_date}\n"
                actions_file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\\actions_MMP.txt", "a")
                actions_file.write(actions)
                actions_file.close()

                self.add_data()
                self.hide_edit()
                self.edit_amount_8.clear()
            elif check_if_digit == False or self.edit_amount_8.text() == "":
                font = QtGui.QFont()
                font.setPointSize(18)
                font.setBold(True)
                self.main_title.setStyleSheet("color : red")
                self.main_title.setFont(font)
                self.main_title.setText("You must type only digits into the text box")
                self.after = QTimer()
                self.after.timeout.connect(self.timer)
                self.after.start(1000)
                self.edit_amount_8.clear()

        if selected_row_1 == 9:
            check_if_digit = self.edit_amount_9.text().isdigit()
            if check_if_digit:
                old_line = self.main_list_1.currentItem().text()
                temp = str(ops[str(self.edit_action_9.currentText())](int(old_line.split()[-1]), int(self.edit_amount_9.text())))
                new_line = f"{old_line.split()[0]} - {temp}"
                new_data = ""

                for file_line in lines.split("\n"):
                    if file_line == old_line:
                        if new_data == "":
                            new_data = f"{new_line}"
                        else:
                            new_data = f"{new_data}\n{new_line}"
                    else:
                        if new_data == "":
                            new_data = f"{file_line}"
                        else:
                            new_data = f"{new_data}\n{file_line}"
                file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\data_MMP.txt", "w")
                file.write(new_data)
                file.close()

                today = date.today()
                ac_date = today.strftime("%d/%m/%Y")
                if str(self.edit_action_9.currentText()) == "+":
                    add_sub = "added"
                    for_from = "for"
                else:
                    add_sub = "subtracted"
                    for_from = "from"
                name = new_line.split(" ")[0]
                actions = f"{add_sub} {for_from} {name} {self.edit_amount_9.text()} money at {ac_date}\n"
                actions_file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\\actions_MMP.txt", "a")
                actions_file.write(actions)
                actions_file.close()

                self.add_data()
                self.hide_edit()
                self.edit_amount_9.clear()
            elif check_if_digit == False or self.edit_amount_9.text() == "":
                font = QtGui.QFont()
                font.setPointSize(18)
                font.setBold(True)
                self.main_title.setStyleSheet("color : red")
                self.main_title.setFont(font)
                self.main_title.setText("You must type only digits into the text box")
                self.after = QTimer()
                self.after.timeout.connect(self.timer)
                self.after.start(1000)
                self.edit_amount_9.clear()

        if selected_row_1 == 10:
            check_if_digit = self.edit_amount_10.text().isdigit()
            if check_if_digit:
                old_line = self.main_list_1.currentItem().text()
                temp = str(ops[str(self.edit_action_10.currentText())](int(old_line.split()[-1]), int(self.edit_amount_10.text())))
                new_line = f"{old_line.split()[0]} - {temp}"
                new_data = ""

                for file_line in lines.split("\n"):
                    if file_line == old_line:
                        if new_data == "":
                            new_data = f"{new_line}"
                        else:
                            new_data = f"{new_data}\n{new_line}"
                    else:
                        if new_data == "":
                            new_data = f"{file_line}"
                        else:
                            new_data = f"{new_data}\n{file_line}"
                file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\data_MMP.txt", "w")
                file.write(new_data)
                file.close()

                today = date.today()
                ac_date = today.strftime("%d/%m/%Y")
                if str(self.edit_action_10.currentText()) == "+":
                    add_sub = "added"
                    for_from = "for"
                else:
                    add_sub = "subtracted"
                    for_from = "from"
                name = new_line.split(" ")[0]
                actions = f"{add_sub} {for_from} {name} {self.edit_amount_10.text()} money at {ac_date}\n"
                actions_file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\\actions_MMP.txt", "a")
                actions_file.write(actions)
                actions_file.close()

                self.add_data()
                self.hide_edit()
                self.edit_amount_10.clear()
            elif check_if_digit == False or self.edit_amount_10.text() == "":
                font = QtGui.QFont()
                font.setPointSize(18)
                font.setBold(True)
                self.main_title.setStyleSheet("color : red")
                self.main_title.setFont(font)
                self.main_title.setText("You must type only digits into the text box")
                self.after = QTimer()
                self.after.timeout.connect(self.timer)
                self.after.start(1000)
                self.edit_amount_10.clear()

        if selected_row_1 == 11:
            check_if_digit = self.edit_amount_11.text().isdigit()
            if check_if_digit:
                old_line = self.main_list_1.currentItem().text()
                temp = str(ops[str(self.edit_action_11.currentText())](int(old_line.split()[-1]), int(self.edit_amount_11.text())))
                new_line = f"{old_line.split()[0]} - {temp}"
                new_data = ""

                for file_line in lines.split("\n"):
                    if file_line == old_line:
                        if new_data == "":
                            new_data = f"{new_line}"
                        else:
                            new_data = f"{new_data}\n{new_line}"
                    else:
                        if new_data == "":
                            new_data = f"{file_line}"
                        else:
                            new_data = f"{new_data}\n{file_line}"
                file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\data_MMP.txt", "w")
                file.write(new_data)
                file.close()

                today = date.today()
                ac_date = today.strftime("%d/%m/%Y")
                if str(self.edit_action_11.currentText()) == "+":
                    add_sub = "added"
                    for_from = "for"
                else:
                    add_sub = "subtracted"
                    for_from = "from"
                name = new_line.split(" ")[0]
                actions = f"{add_sub} {for_from} {name} {self.edit_amount_11.text()} money at {ac_date}\n"
                actions_file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\\actions_MMP.txt", "a")
                actions_file.write(actions)
                actions_file.close()

                self.add_data()
                self.hide_edit()
                self.edit_amount_11.clear()
            elif check_if_digit == False or self.edit_amount_11.text() == "":
                font = QtGui.QFont()
                font.setPointSize(18)
                font.setBold(True)
                self.main_title.setStyleSheet("color : red")
                self.main_title.setFont(font)
                self.main_title.setText("You must type only digits into the text box")
                self.after = QTimer()
                self.after.timeout.connect(self.timer)
                self.after.start(1000)
                self.edit_amount_11.clear()

        if selected_row_1 == 12:
            check_if_digit = self.edit_amount_12.text().isdigit()
            if check_if_digit:
                old_line = self.main_list_1.currentItem().text()
                temp = str(ops[str(self.edit_action_12.currentText())](int(old_line.split()[-1]), int(self.edit_amount_12.text())))
                new_line = f"{old_line.split()[0]} - {temp}"
                new_data = ""

                for file_line in lines.split("\n"):
                    if file_line == old_line:
                        if new_data == "":
                            new_data = f"{new_line}"
                        else:
                            new_data = f"{new_data}\n{new_line}"
                    else:
                        if new_data == "":
                            new_data = f"{file_line}"
                        else:
                            new_data = f"{new_data}\n{file_line}"
                file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\data_MMP.txt", "w")
                file.write(new_data)
                file.close()

                today = date.today()
                ac_date = today.strftime("%d/%m/%Y")
                if str(self.edit_action_12.currentText()) == "+":
                    add_sub = "added"
                    for_from = "for"
                else:
                    add_sub = "subtracted"
                    for_from = "from"
                name = new_line.split(" ")[0]
                actions = f"{add_sub} {for_from} {name} {self.edit_amount_12.text()} money at {ac_date}\n"
                actions_file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\\actions_MMP.txt", "a")
                actions_file.write(actions)
                actions_file.close()

                self.add_data()
                self.hide_edit()
                self.edit_amount_12.clear()
            elif check_if_digit == False or self.edit_amount_12.text() == "":
                font = QtGui.QFont()
                font.setPointSize(18)
                font.setBold(True)
                self.main_title.setStyleSheet("color : red")
                self.main_title.setFont(font)
                self.main_title.setText("You must type only digits into the text box")
                self.after = QTimer()
                self.after.timeout.connect(self.timer)
                self.after.start(1000)
                self.edit_amount_12.clear()

        if selected_row_1 == 13:
            check_if_digit = self.edit_amount_3.text().isdigit()
            if check_if_digit:
                old_line = self.main_list_1.currentItem().text()
                temp = str(ops[str(self.edit_action_13.currentText())](int(old_line.split()[-1]), int(self.edit_amount_13.text())))
                new_line = f"{old_line.split()[0]} - {temp}"
                new_data = ""

                for file_line in lines.split("\n"):
                    if file_line == old_line:
                        if new_data == "":
                            new_data = f"{new_line}"
                        else:
                            new_data = f"{new_data}\n{new_line}"
                    else:
                        if new_data == "":
                            new_data = f"{file_line}"
                        else:
                            new_data = f"{new_data}\n{file_line}"
                file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\data_MMP.txt", "w")
                file.write(new_data)
                file.close()

                today = date.today()
                ac_date = today.strftime("%d/%m/%Y")
                if str(self.edit_action_13.currentText()) == "+":
                    add_sub = "added"
                    for_from = "for"
                else:
                    add_sub = "subtracted"
                    for_from = "from"
                name = new_line.split(" ")[0]
                actions = f"{add_sub} {for_from} {name} {self.edit_amount_13.text()} money at {ac_date}\n"
                actions_file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\\actions_MMP.txt", "a")
                actions_file.write(actions)
                actions_file.close()

                self.add_data()
                self.hide_edit()
                self.edit_amount_13.clear()
            elif check_if_digit == False or self.edit_amount_13.text() == "":
                font = QtGui.QFont()
                font.setPointSize(18)
                font.setBold(True)
                self.main_title.setStyleSheet("color : red")
                self.main_title.setFont(font)
                self.main_title.setText("You must type only digits into the text box")
                self.after = QTimer()
                self.after.timeout.connect(self.timer)
                self.after.start(1000)
                self.edit_amount_13.clear()

        if selected_row_1 == 14:
            check_if_digit = self.edit_amount_14.text().isdigit()
            if check_if_digit:
                old_line = self.main_list_1.currentItem().text()
                temp = str(ops[str(self.edit_action_14.currentText())](int(old_line.split()[-1]), int(self.edit_amount_14.text())))
                new_line = f"{old_line.split()[0]} - {temp}"
                new_data = ""

                for file_line in lines.split("\n"):
                    if file_line == old_line:
                        if new_data == "":
                            new_data = f"{new_line}"
                        else:
                            new_data = f"{new_data}\n{new_line}"
                    else:
                        if new_data == "":
                            new_data = f"{file_line}"
                        else:
                            new_data = f"{new_data}\n{file_line}"
                file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\data_MMP.txt", "w")
                file.write(new_data)
                file.close()

                today = date.today()
                ac_date = today.strftime("%d/%m/%Y")
                if str(self.edit_action_14.currentText()) == "+":
                    add_sub = "added"
                    for_from = "for"
                else:
                    add_sub = "subtracted"
                    for_from = "from"
                name = new_line.split(" ")[0]
                actions = f"{add_sub} {for_from} {name} {self.edit_amount_14.text()} money at {ac_date}\n"
                actions_file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\\actions_MMP.txt", "a")
                actions_file.write(actions)
                actions_file.close()

                self.add_data()
                self.hide_edit()
                self.edit_amount_14.clear()
            elif check_if_digit == False or self.edit_amount_14.text() == "":
                font = QtGui.QFont()
                font.setPointSize(18)
                font.setBold(True)
                self.main_title.setStyleSheet("color : red")
                self.main_title.setFont(font)
                self.main_title.setText("You must type only digits into the text box")
                self.after = QTimer()
                self.after.timeout.connect(self.timer)
                self.after.start(1000)
                self.edit_amount_14.clear()

        if selected_row_1 == 15:
            check_if_digit = self.edit_amount_15.text().isdigit()
            if check_if_digit:
                old_line = self.main_list_1.currentItem().text()
                temp = str(ops[str(self.edit_action_15.currentText())](int(old_line.split()[-1]), int(self.edit_amount_15.text())))
                new_line = f"{old_line.split()[0]} - {temp}"
                new_data = ""

                for file_line in lines.split("\n"):
                    if file_line == old_line:
                        if new_data == "":
                            new_data = f"{new_line}"
                        else:
                            new_data = f"{new_data}\n{new_line}"
                    else:
                        if new_data == "":
                            new_data = f"{file_line}"
                        else:
                            new_data = f"{new_data}\n{file_line}"
                file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\data_MMP.txt", "w")
                file.write(new_data)
                file.close()

                today = date.today()
                ac_date = today.strftime("%d/%m/%Y")
                if str(self.edit_action_15.currentText()) == "+":
                    add_sub = "added"
                    for_from = "for"
                else:
                    add_sub = "subtracted"
                    for_from = "from"
                name = new_line.split(" ")[0]
                actions = f"{add_sub} {for_from} {name} {self.edit_amount_15.text()} money at {ac_date}\n"
                actions_file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\\actions_MMP.txt", "a")
                actions_file.write(actions)
                actions_file.close()

                self.add_data()
                self.hide_edit()
                self.edit_amount_15.clear()
            elif check_if_digit == False or self.edit_amount_15.text() == "":
                font = QtGui.QFont()
                font.setPointSize(18)
                font.setBold(True)
                self.main_title.setStyleSheet("color : red")
                self.main_title.setFont(font)
                self.main_title.setText("You must type only digits into the text box")
                self.after = QTimer()
                self.after.timeout.connect(self.timer)
                self.after.start(1000)
                self.edit_amount_15.clear()

        if selected_row_1 == 16:
            check_if_digit = self.edit_amount_16.text().isdigit()
            if check_if_digit:
                old_line = self.main_list_1.currentItem().text()
                temp = str(ops[str(self.edit_action_16.currentText())](int(old_line.split()[-1]), int(self.edit_amount_16.text())))
                new_line = f"{old_line.split()[0]} - {temp}"
                new_data = ""

                for file_line in lines.split("\n"):
                    if file_line == old_line:
                        if new_data == "":
                            new_data = f"{new_line}"
                        else:
                            new_data = f"{new_data}\n{new_line}"
                    else:
                        if new_data == "":
                            new_data = f"{file_line}"
                        else:
                            new_data = f"{new_data}\n{file_line}"
                file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\data_MMP.txt", "w")
                file.write(new_data)
                file.close()

                today = date.today()
                ac_date = today.strftime("%d/%m/%Y")
                if str(self.edit_action_16.currentText()) == "+":
                    add_sub = "added"
                    for_from = "for"
                else:
                    add_sub = "subtracted"
                    for_from = "from"
                name = new_line.split(" ")[0]
                actions = f"{add_sub} {for_from} {name} {self.edit_amount_16.text()} money at {ac_date}\n"
                actions_file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\\actions_MMP.txt", "a")
                actions_file.write(actions)
                actions_file.close()

                self.add_data()
                self.hide_edit()
                self.edit_amount_16.clear()
            elif check_if_digit == False or self.edit_amount_16.text() == "":
                font = QtGui.QFont()
                font.setPointSize(18)
                font.setBold(True)
                self.main_title.setStyleSheet("color : red")
                self.main_title.setFont(font)
                self.main_title.setText("You must type only digits into the text box")
                self.after = QTimer()
                self.after.timeout.connect(self.timer)
                self.after.start(1000)
                self.edit_amount_16.clear()

        if selected_row_1 == 17:
            check_if_digit = self.edit_amount_17.text().isdigit()
            if check_if_digit:
                old_line = self.main_list_1.currentItem().text()
                temp = str(ops[str(self.edit_action_17.currentText())](int(old_line.split()[-1]), int(self.edit_amount_17.text())))
                new_line = f"{old_line.split()[0]} - {temp}"
                new_data = ""

                for file_line in lines.split("\n"):
                    if file_line == old_line:
                        if new_data == "":
                            new_data = f"{new_line}"
                        else:
                            new_data = f"{new_data}\n{new_line}"
                    else:
                        if new_data == "":
                            new_data = f"{file_line}"
                        else:
                            new_data = f"{new_data}\n{file_line}"
                file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\data_MMP.txt", "w")
                file.write(new_data)
                file.close()

                today = date.today()
                ac_date = today.strftime("%d/%m/%Y")
                if str(self.edit_action_17.currentText()) == "+":
                    add_sub = "added"
                    for_from = "for"
                else:
                    add_sub = "subtracted"
                    for_from = "from"
                name = new_line.split(" ")[0]
                actions = f"{add_sub} {for_from} {name} {self.edit_amount_17.text()} money at {ac_date}\n"
                actions_file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\\actions_MMP.txt", "a")
                actions_file.write(actions)
                actions_file.close()

                self.add_data()
                self.hide_edit()
                self.edit_amount_17.clear()
            elif check_if_digit == False or self.edit_amount_17.text() == "":
                font = QtGui.QFont()
                font.setPointSize(18)
                font.setBold(True)
                self.main_title.setStyleSheet("color : red")
                self.main_title.setFont(font)
                self.main_title.setText("You must type only digits into the text box")
                self.after = QTimer()
                self.after.timeout.connect(self.timer)
                self.after.start(1000)
                self.edit_amount_17.clear()

        if selected_row_1 == 18:
            check_if_digit = self.edit_amount_18.text().isdigit()
            if check_if_digit:
                old_line = self.main_list_1.currentItem().text()
                temp = str(ops[str(self.edit_action_18.currentText())](int(old_line.split()[-1]), int(self.edit_amount_18.text())))
                new_line = f"{old_line.split()[0]} - {temp}"
                new_data = ""

                for file_line in lines.split("\n"):
                    if file_line == old_line:
                        if new_data == "":
                            new_data = f"{new_line}"
                        else:
                            new_data = f"{new_data}\n{new_line}"
                    else:
                        if new_data == "":
                            new_data = f"{file_line}"
                        else:
                            new_data = f"{new_data}\n{file_line}"
                file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\data_MMP.txt", "w")
                file.write(new_data)
                file.close()

                today = date.today()
                ac_date = today.strftime("%d/%m/%Y")
                if str(self.edit_action_18.currentText()) == "+":
                    add_sub = "added"
                    for_from = "for"
                else:
                    add_sub = "subtracted"
                    for_from = "from"
                name = new_line.split(" ")[0]
                actions = f"{add_sub} {for_from} {name} {self.edit_amount_18.text()} money at {ac_date}\n"
                actions_file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\\actions_MMP.txt", "a")
                actions_file.write(actions)
                actions_file.close()

                self.add_data()
                self.hide_edit()
                self.edit_amount_18.clear()
            elif check_if_digit == False or self.edit_amount_18.text() == "":
                font = QtGui.QFont()
                font.setPointSize(18)
                font.setBold(True)
                self.main_title.setStyleSheet("color : red")
                self.main_title.setFont(font)
                self.main_title.setText("You must type only digits into the text box")
                self.after = QTimer()
                self.after.timeout.connect(self.timer)
                self.after.start(1000)
                self.edit_amount_18.clear()

        if selected_row_1 == 19:
            check_if_digit = self.edit_amount_19.text().isdigit()
            if check_if_digit:
                old_line = self.main_list_1.currentItem().text()
                temp = str(ops[str(self.edit_action_19.currentText())](int(old_line.split()[-1]), int(self.edit_amount_19.text())))
                new_line = f"{old_line.split()[0]} - {temp}"
                new_data = ""

                for file_line in lines.split("\n"):
                    if file_line == old_line:
                        if new_data == "":
                            new_data = f"{new_line}"
                        else:
                            new_data = f"{new_data}\n{new_line}"
                    else:
                        if new_data == "":
                            new_data = f"{file_line}"
                        else:
                            new_data = f"{new_data}\n{file_line}"
                file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\data_MMP.txt", "w")
                file.write(new_data)
                file.close()

                today = date.today()
                ac_date = today.strftime("%d/%m/%Y")
                if str(self.edit_action_19.currentText()) == "+":
                    add_sub = "added"
                    for_from = "for"
                else:
                    add_sub = "subtracted"
                    for_from = "from"
                name = new_line.split(" ")[0]
                actions = f"{add_sub} {for_from} {name} {self.edit_amount_19.text()} money at {ac_date}\n"
                actions_file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\\actions_MMP.txt", "a")
                actions_file.write(actions)
                actions_file.close()

                self.add_data()
                self.hide_edit()
                self.edit_amount_19.clear()
            elif check_if_digit == False or self.edit_amount_19.text() == "":
                font = QtGui.QFont()
                font.setPointSize(18)
                font.setBold(True)
                self.main_title.setStyleSheet("color : red")
                self.main_title.setFont(font)
                self.main_title.setText("You must type only digits into the text box")
                self.after = QTimer()
                self.after.timeout.connect(self.timer)
                self.after.start(1000)
                self.edit_amount_19.clear()

        if selected_row_1 == 20:
            check_if_digit = self.edit_amount_20.text().isdigit()
            if check_if_digit:
                old_line = self.main_list_1.currentItem().text()
                temp = str(ops[str(self.edit_action_20.currentText())](int(old_line.split()[-1]), int(self.edit_amount_20.text())))
                new_line = f"{old_line.split()[0]} - {temp}"
                new_data = ""

                for file_line in lines.split("\n"):
                    if file_line == old_line:
                        if new_data == "":
                            new_data = f"{new_line}"
                        else:
                            new_data = f"{new_data}\n{new_line}"
                    else:
                        if new_data == "":
                            new_data = f"{file_line}"
                        else:
                            new_data = f"{new_data}\n{file_line}"
                file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\data_MMP.txt", "w")
                file.write(new_data)
                file.close()

                today = date.today()
                ac_date = today.strftime("%d/%m/%Y")
                if str(self.edit_action_20.currentText()) == "+":
                    add_sub = "added"
                    for_from = "for"
                else:
                    add_sub = "subtracted"
                    for_from = "from"
                name = new_line.split(" ")[0]
                actions = f"{add_sub} {for_from} {name} {self.edit_amount_20.text()} money at {ac_date}\n"
                actions_file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\\actions_MMP.txt", "a")
                actions_file.write(actions)
                actions_file.close()

                self.add_data()
                self.hide_edit()
                self.edit_amount_20.clear()
            elif check_if_digit == False or self.edit_amount_20.text() == "":
                font = QtGui.QFont()
                font.setPointSize(18)
                font.setBold(True)
                self.main_title.setStyleSheet("color : red")
                self.main_title.setFont(font)
                self.main_title.setText("You must type only digits into the text box")
                self.after = QTimer()
                self.after.timeout.connect(self.timer)
                self.after.start(1000)
                self.edit_amount_20.clear()

        if selected_row_2 == 21:
            check_if_digit = self.edit_amount_21.text().isdigit()
            if check_if_digit:
                old_line = self.main_list_2.currentItem().text()
                temp = str(ops[str(self.edit_action_21.currentText())](int(old_line.split()[-1]), int(self.edit_amount_21.text())))
                new_line = f"{old_line.split()[0]} - {temp}"
                new_data = ""

                for file_line in lines.split("\n"):
                    if file_line == old_line:
                        if new_data == "":
                            new_data = f"{new_line}"
                        else:
                            new_data = f"{new_data}\n{new_line}"
                    else:
                        if new_data == "":
                            new_data = f"{file_line}"
                        else:
                            new_data = f"{new_data}\n{file_line}"
                file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\data_MMP.txt", "w")
                file.write(new_data)
                file.close()

                today = date.today()
                ac_date = today.strftime("%d/%m/%Y")
                if str(self.edit_action_21.currentText()) == "+":
                    add_sub = "added"
                    for_from = "for"
                else:
                    add_sub = "subtracted"
                    for_from = "from"
                name = new_line.split(" ")[0]
                actions = f"{add_sub} {for_from} {name} {self.edit_amount_21.text()} money at {ac_date}\n"
                actions_file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\\actions_MMP.txt", "a")
                actions_file.write(actions)
                actions_file.close()

                self.add_data()
                self.hide_edit()
                self.edit_amount_21.clear()
            elif check_if_digit == False or self.edit_amount_21.text() == "":
                font = QtGui.QFont()
                font.setPointSize(18)
                font.setBold(True)
                self.main_title.setStyleSheet("color : red")
                self.main_title.setFont(font)
                self.main_title.setText("You must type only digits into the text box")
                self.after = QTimer()
                self.after.timeout.connect(self.timer)
                self.after.start(1000)
                self.edit_amount_21.clear()

        if selected_row_2 == 22:
            check_if_digit = self.edit_amount_22.text().isdigit()
            if check_if_digit:
                old_line = self.main_list_2.currentItem().text()
                temp = str(ops[str(self.edit_action_22.currentText())](int(old_line.split()[-1]), int(self.edit_amount_22.text())))
                new_line = f"{old_line.split()[0]} - {temp}"
                new_data = ""

                for file_line in lines.split("\n"):
                    if file_line == old_line:
                        if new_data == "":
                            new_data = f"{new_line}"
                        else:
                            new_data = f"{new_data}\n{new_line}"
                    else:
                        if new_data == "":
                            new_data = f"{file_line}"
                        else:
                            new_data = f"{new_data}\n{file_line}"
                file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\data_MMP.txt", "w")
                file.write(new_data)
                file.close()

                today = date.today()
                ac_date = today.strftime("%d/%m/%Y")
                if str(self.edit_action_22.currentText()) == "+":
                    add_sub = "added"
                    for_from = "for"
                else:
                    add_sub = "subtracted"
                    for_from = "from"
                name = new_line.split(" ")[0]
                actions = f"{add_sub} {for_from} {name} {self.edit_amount_22.text()} money at {ac_date}\n"
                actions_file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\\actions_MMP.txt", "a")
                actions_file.write(actions)
                actions_file.close()

                self.add_data()
                self.hide_edit()
                self.edit_amount_22.clear()
            elif check_if_digit == False or self.edit_amount_22.text() == "":
                font = QtGui.QFont()
                font.setPointSize(18)
                font.setBold(True)
                self.main_title.setStyleSheet("color : red")
                self.main_title.setFont(font)
                self.main_title.setText("You must type only digits into the text box")
                self.after = QTimer()
                self.after.timeout.connect(self.timer)
                self.after.start(1000)
                self.edit_amount_22.clear()

        if selected_row_2 == 23:
            check_if_digit = self.edit_amount_23.text().isdigit()
            if check_if_digit:
                old_line = self.main_list_2.currentItem().text()
                temp = str(ops[str(self.edit_action_23.currentText())](int(old_line.split()[-1]), int(self.edit_amount_23.text())))
                new_line = f"{old_line.split()[0]} - {temp}"
                new_data = ""

                for file_line in lines.split("\n"):
                    if file_line == old_line:
                        if new_data == "":
                            new_data = f"{new_line}"
                        else:
                            new_data = f"{new_data}\n{new_line}"
                    else:
                        if new_data == "":
                            new_data = f"{file_line}"
                        else:
                            new_data = f"{new_data}\n{file_line}"
                file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\data_MMP.txt", "w")
                file.write(new_data)
                file.close()

                today = date.today()
                ac_date = today.strftime("%d/%m/%Y")
                if str(self.edit_action_23.currentText()) == "+":
                    add_sub = "added"
                    for_from = "for"
                else:
                    add_sub = "subtracted"
                    for_from = "from"
                name = new_line.split(" ")[0]
                actions = f"{add_sub} {for_from} {name} {self.edit_amount_23.text()} money at {ac_date}\n"
                actions_file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\\actions_MMP.txt", "a")
                actions_file.write(actions)
                actions_file.close()

                self.add_data()
                self.hide_edit()
                self.edit_amount_23.clear()
            elif check_if_digit == False or self.edit_amount_23.text() == "":
                font = QtGui.QFont()
                font.setPointSize(18)
                font.setBold(True)
                self.main_title.setStyleSheet("color : red")
                self.main_title.setFont(font)
                self.main_title.setText("You must type only digits into the text box")
                self.after = QTimer()
                self.after.timeout.connect(self.timer)
                self.after.start(1000)
                self.edit_amount_23.clear()

        if selected_row_2 == 24:
            check_if_digit = self.edit_amount_24.text().isdigit()
            if check_if_digit:
                old_line = self.main_list_2.currentItem().text()
                temp = str(ops[str(self.edit_action_24.currentText())](int(old_line.split()[-1]), int(self.edit_amount_24.text())))
                new_line = f"{old_line.split()[0]} - {temp}"
                new_data = ""

                for file_line in lines.split("\n"):
                    if file_line == old_line:
                        if new_data == "":
                            new_data = f"{new_line}"
                        else:
                            new_data = f"{new_data}\n{new_line}"
                    else:
                        if new_data == "":
                            new_data = f"{file_line}"
                        else:
                            new_data = f"{new_data}\n{file_line}"
                file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\data_MMP.txt", "w")
                file.write(new_data)
                file.close()

                today = date.today()
                ac_date = today.strftime("%d/%m/%Y")
                if str(self.edit_action_24.currentText()) == "+":
                    add_sub = "added"
                    for_from = "for"
                else:
                    add_sub = "subtracted"
                    for_from = "from"
                name = new_line.split(" ")[0]
                actions = f"{add_sub} {for_from} {name} {self.edit_amount_24.text()} money at {ac_date}\n"
                actions_file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\\actions_MMP.txt", "a")
                actions_file.write(actions)
                actions_file.close()

                self.add_data()
                self.hide_edit()
                self.edit_amount_24.clear()
            elif check_if_digit == False or self.edit_amount_24.text() == "":
                font = QtGui.QFont()
                font.setPointSize(18)
                font.setBold(True)
                self.main_title.setStyleSheet("color : red")
                self.main_title.setFont(font)
                self.main_title.setText("You must type only digits into the text box")
                self.after = QTimer()
                self.after.timeout.connect(self.timer)
                self.after.start(1000)
                self.edit_amount_24.clear()

        if selected_row_2 == 25:
            check_if_digit = self.edit_amount_25.text().isdigit()
            if check_if_digit:
                old_line = self.main_list_2.currentItem().text()
                temp = str(ops[str(self.edit_action_25.currentText())](int(old_line.split()[-1]), int(self.edit_amount_25.text())))
                new_line = f"{old_line.split()[0]} - {temp}"
                new_data = ""

                for file_line in lines.split("\n"):
                    if file_line == old_line:
                        if new_data == "":
                            new_data = f"{new_line}"
                        else:
                            new_data = f"{new_data}\n{new_line}"
                    else:
                        if new_data == "":
                            new_data = f"{file_line}"
                        else:
                            new_data = f"{new_data}\n{file_line}"
                file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\data_MMP.txt", "w")
                file.write(new_data)
                file.close()

                today = date.today()
                ac_date = today.strftime("%d/%m/%Y")
                if str(self.edit_action_25.currentText()) == "+":
                    add_sub = "added"
                    for_from = "for"
                else:
                    add_sub = "subtracted"
                    for_from = "from"
                name = new_line.split(" ")[0]
                actions = f"{add_sub} {for_from} {name} {self.edit_amount_25.text()} money at {ac_date}\n"
                actions_file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\\actions_MMP.txt", "a")
                actions_file.write(actions)
                actions_file.close()

                self.add_data()
                self.hide_edit()
                self.edit_amount_25.clear()
            elif check_if_digit == False or self.edit_amount_25.text() == "":
                font = QtGui.QFont()
                font.setPointSize(18)
                font.setBold(True)
                self.main_title.setStyleSheet("color : red")
                self.main_title.setFont(font)
                self.main_title.setText("You must type only digits into the text box")
                self.after = QTimer()
                self.after.timeout.connect(self.timer)
                self.after.start(1000)
                self.edit_amount_25.clear()

        if selected_row_2 == 26:
            check_if_digit = self.edit_amount_26.text().isdigit()
            if check_if_digit:
                old_line = self.main_list_2.currentItem().text()
                temp = str(ops[str(self.edit_action_26.currentText())](int(old_line.split()[-1]), int(self.edit_amount_26.text())))
                new_line = f"{old_line.split()[0]} - {temp}"
                new_data = ""

                for file_line in lines.split("\n"):
                    if file_line == old_line:
                        if new_data == "":
                            new_data = f"{new_line}"
                        else:
                            new_data = f"{new_data}\n{new_line}"
                    else:
                        if new_data == "":
                            new_data = f"{file_line}"
                        else:
                            new_data = f"{new_data}\n{file_line}"
                file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\data_MMP.txt", "w")
                file.write(new_data)
                file.close()

                today = date.today()
                ac_date = today.strftime("%d/%m/%Y")
                if str(self.edit_action_26.currentText()) == "+":
                    add_sub = "added"
                    for_from = "for"
                else:
                    add_sub = "subtracted"
                    for_from = "from"
                name = new_line.split(" ")[0]
                actions = f"{add_sub} {for_from} {name} {self.edit_amount_26.text()} money at {ac_date}\n"
                actions_file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\\actions_MMP.txt", "a")
                actions_file.write(actions)
                actions_file.close()

                self.add_data()
                self.hide_edit()
                self.edit_amount_26.clear()
            elif check_if_digit == False or self.edit_amount_26.text() == "":
                font = QtGui.QFont()
                font.setPointSize(18)
                font.setBold(True)
                self.main_title.setStyleSheet("color : red")
                self.main_title.setFont(font)
                self.main_title.setText("You must type only digits into the text box")
                self.after = QTimer()
                self.after.timeout.connect(self.timer)
                self.after.start(1000)
                self.edit_amount_26.clear()

        if selected_row_2 == 27:
            check_if_digit = self.edit_amount_27.text().isdigit()
            if check_if_digit:
                old_line = self.main_list_2.currentItem().text()
                temp = str(ops[str(self.edit_action_27.currentText())](int(old_line.split()[-1]), int(self.edit_amount_27.text())))
                new_line = f"{old_line.split()[0]} - {temp}"
                new_data = ""

                for file_line in lines.split("\n"):
                    if file_line == old_line:
                        if new_data == "":
                            new_data = f"{new_line}"
                        else:
                            new_data = f"{new_data}\n{new_line}"
                    else:
                        if new_data == "":
                            new_data = f"{file_line}"
                        else:
                            new_data = f"{new_data}\n{file_line}"
                file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\data_MMP.txt", "w")
                file.write(new_data)
                file.close()

                today = date.today()
                ac_date = today.strftime("%d/%m/%Y")
                if str(self.edit_action_27.currentText()) == "+":
                    add_sub = "added"
                    for_from = "for"
                else:
                    add_sub = "subtracted"
                    for_from = "from"
                name = new_line.split(" ")[0]
                actions = f"{add_sub} {for_from} {name} {self.edit_amount_27.text()} money at {ac_date}\n"
                actions_file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\\actions_MMP.txt", "a")
                actions_file.write(actions)
                actions_file.close()

                self.add_data()
                self.hide_edit()
                self.edit_amount_27.clear()
            elif check_if_digit == False or self.edit_amount_27.text() == "":
                font = QtGui.QFont()
                font.setPointSize(18)
                font.setBold(True)
                self.main_title.setStyleSheet("color : red")
                self.main_title.setFont(font)
                self.main_title.setText("You must type only digits into the text box")
                self.after = QTimer()
                self.after.timeout.connect(self.timer)
                self.after.start(1000)
                self.edit_amount_27.clear()

        if selected_row_2 == 28:
            check_if_digit = self.edit_amount_28.text().isdigit()
            if check_if_digit:
                old_line = self.main_list_2.currentItem().text()
                temp = str(ops[str(self.edit_action_28.currentText())](int(old_line.split()[-1]), int(self.edit_amount_28.text())))
                new_line = f"{old_line.split()[0]} - {temp}"
                new_data = ""

                for file_line in lines.split("\n"):
                    if file_line == old_line:
                        if new_data == "":
                            new_data = f"{new_line}"
                        else:
                            new_data = f"{new_data}\n{new_line}"
                    else:
                        if new_data == "":
                            new_data = f"{file_line}"
                        else:
                            new_data = f"{new_data}\n{file_line}"
                file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\data_MMP.txt", "w")
                file.write(new_data)
                file.close()

                today = date.today()
                ac_date = today.strftime("%d/%m/%Y")
                if str(self.edit_action_28.currentText()) == "+":
                    add_sub = "added"
                    for_from = "for"
                else:
                    add_sub = "subtracted"
                    for_from = "from"
                name = new_line.split(" ")[0]
                actions = f"{add_sub} {for_from} {name} {self.edit_amount_28.text()} money at {ac_date}\n"
                actions_file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\\actions_MMP.txt", "a")
                actions_file.write(actions)
                actions_file.close()

                self.add_data()
                self.hide_edit()
                self.edit_amount_28.clear()
            elif check_if_digit == False or self.edit_amount_28.text() == "":
                font = QtGui.QFont()
                font.setPointSize(18)
                font.setBold(True)
                self.main_title.setStyleSheet("color : red")
                self.main_title.setFont(font)
                self.main_title.setText("You must type only digits into the text box")
                self.after = QTimer()
                self.after.timeout.connect(self.timer)
                self.after.start(1000)
                self.edit_amount_28.clear()

        if selected_row_2 == 29:
            check_if_digit = self.edit_amount_29.text().isdigit()
            if check_if_digit:
                old_line = self.main_list_2.currentItem().text()
                temp = str(ops[str(self.edit_action_29.currentText())](int(old_line.split()[-1]), int(self.edit_amount_29.text())))
                new_line = f"{old_line.split()[0]} - {temp}"
                new_data = ""

                for file_line in lines.split("\n"):
                    if file_line == old_line:
                        if new_data == "":
                            new_data = f"{new_line}"
                        else:
                            new_data = f"{new_data}\n{new_line}"
                    else:
                        if new_data == "":
                            new_data = f"{file_line}"
                        else:
                            new_data = f"{new_data}\n{file_line}"
                file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\data_MMP.txt", "w")
                file.write(new_data)
                file.close()

                today = date.today()
                ac_date = today.strftime("%d/%m/%Y")
                if str(self.edit_action_29.currentText()) == "+":
                    add_sub = "added"
                    for_from = "for"
                else:
                    add_sub = "subtracted"
                    for_from = "from"
                name = new_line.split(" ")[0]
                actions = f"{add_sub} {for_from} {name} {self.edit_amount_29.text()} money at {ac_date}\n"
                actions_file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\\actions_MMP.txt", "a")
                actions_file.write(actions)
                actions_file.close()

                self.add_data()
                self.hide_edit()
                self.edit_amount_29.clear()
            elif check_if_digit == False or self.edit_amount_29.text() == "":
                font = QtGui.QFont()
                font.setPointSize(18)
                font.setBold(True)
                self.main_title.setStyleSheet("color : red")
                self.main_title.setFont(font)
                self.main_title.setText("You must type only digits into the text box")
                self.after = QTimer()
                self.after.timeout.connect(self.timer)
                self.after.start(1000)
                self.edit_amount_29.clear()

        if selected_row_2 == 30:
            check_if_digit = self.edit_amount_30.text().isdigit()
            if check_if_digit:
                old_line = self.main_list_2.currentItem().text()
                temp = str(ops[str(self.edit_action_30.currentText())](int(old_line.split()[-1]), int(self.edit_amount_30.text())))
                new_line = f"{old_line.split()[0]} - {temp}"
                new_data = ""

                for file_line in lines.split("\n"):
                    if file_line == old_line:
                        if new_data == "":
                            new_data = f"{new_line}"
                        else:
                            new_data = f"{new_data}\n{new_line}"
                    else:
                        if new_data == "":
                            new_data = f"{file_line}"
                        else:
                            new_data = f"{new_data}\n{file_line}"
                file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\data_MMP.txt", "w")
                file.write(new_data)
                file.close()

                today = date.today()
                ac_date = today.strftime("%d/%m/%Y")
                if str(self.edit_action_30.currentText()) == "+":
                    add_sub = "added"
                    for_from = "for"
                else:
                    add_sub = "subtracted"
                    for_from = "from"
                name = new_line.split(" ")[0]
                actions = f"{add_sub} {for_from} {name} {self.edit_amount_30.text()} money at {ac_date}\n"
                actions_file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\\actions_MMP.txt", "a")
                actions_file.write(actions)
                actions_file.close()

                self.add_data()
                self.hide_edit()
                self.edit_amount_30.clear()
            elif check_if_digit == False or self.edit_amount_30.text() == "":
                font = QtGui.QFont()
                font.setPointSize(18)
                font.setBold(True)
                self.main_title.setStyleSheet("color : red")
                self.main_title.setFont(font)
                self.main_title.setText("You must type only digits into the text box")
                self.after = QTimer()
                self.after.timeout.connect(self.timer)
                self.after.start(1000)
                self.edit_amount_30.clear()

        if selected_row_2 == 31:
            check_if_digit = self.edit_amount_31.text().isdigit()
            if check_if_digit:
                old_line = self.main_list_2.currentItem().text()
                temp = str(ops[str(self.edit_action_31.currentText())](int(old_line.split()[-1]), int(self.edit_amount_31.text())))
                new_line = f"{old_line.split()[0]} - {temp}"
                new_data = ""

                for file_line in lines.split("\n"):
                    if file_line == old_line:
                        if new_data == "":
                            new_data = f"{new_line}"
                        else:
                            new_data = f"{new_data}\n{new_line}"
                    else:
                        if new_data == "":
                            new_data = f"{file_line}"
                        else:
                            new_data = f"{new_data}\n{file_line}"
                file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\data_MMP.txt", "w")
                file.write(new_data)
                file.close()

                today = date.today()
                ac_date = today.strftime("%d/%m/%Y")
                if str(self.edit_action_31.currentText()) == "+":
                    add_sub = "added"
                    for_from = "for"
                else:
                    add_sub = "subtracted"
                    for_from = "from"
                name = new_line.split(" ")[0]
                actions = f"{add_sub} {for_from} {name} {self.edit_amount_31.text()} money at {ac_date}\n"
                actions_file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\\actions_MMP.txt", "a")
                actions_file.write(actions)
                actions_file.close()

                self.add_data()
                self.hide_edit()
                self.edit_amount_31.clear()
            elif check_if_digit == False or self.edit_amount_31.text() == "":
                font = QtGui.QFont()
                font.setPointSize(18)
                font.setBold(True)
                self.main_title.setStyleSheet("color : red")
                self.main_title.setFont(font)
                self.main_title.setText("You must type only digits into the text box")
                self.after = QTimer()
                self.after.timeout.connect(self.timer)
                self.after.start(1000)
                self.edit_amount_31.clear()

        if selected_row_2 == 32:
            check_if_digit = self.edit_amount_32.text().isdigit()
            if check_if_digit:
                old_line = self.main_list_2.currentItem().text()
                temp = str(ops[str(self.edit_action_32.currentText())](int(old_line.split()[-1]), int(self.edit_amount_32.text())))
                new_line = f"{old_line.split()[0]} - {temp}"
                new_data = ""

                for file_line in lines.split("\n"):
                    if file_line == old_line:
                        if new_data == "":
                            new_data = f"{new_line}"
                        else:
                            new_data = f"{new_data}\n{new_line}"
                    else:
                        if new_data == "":
                            new_data = f"{file_line}"
                        else:
                            new_data = f"{new_data}\n{file_line}"
                file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\data_MMP.txt", "w")
                file.write(new_data)
                file.close()

                today = date.today()
                ac_date = today.strftime("%d/%m/%Y")
                if str(self.edit_action_32.currentText()) == "+":
                    add_sub = "added"
                    for_from = "for"
                else:
                    add_sub = "subtracted"
                    for_from = "from"
                name = new_line.split(" ")[0]
                actions = f"{add_sub} {for_from} {name} {self.edit_amount_32.text()} money at {ac_date}\n"
                actions_file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\\actions_MMP.txt", "a")
                actions_file.write(actions)
                actions_file.close()

                self.add_data()
                self.hide_edit()
                self.edit_amount_32.clear()
            elif check_if_digit == False or self.edit_amount_32.text() == "":
                font = QtGui.QFont()
                font.setPointSize(18)
                font.setBold(True)
                self.main_title.setStyleSheet("color : red")
                self.main_title.setFont(font)
                self.main_title.setText("You must type only digits into the text box")
                self.after = QTimer()
                self.after.timeout.connect(self.timer)
                self.after.start(1000)
                self.edit_amount_32.clear()

        if selected_row_2 == 33:
            check_if_digit = self.edit_amount_33.text().isdigit()
            if check_if_digit:
                old_line = self.main_list_2.currentItem().text()
                temp = str(ops[str(self.edit_action_33.currentText())](int(old_line.split()[-1]), int(self.edit_amount_33.text())))
                new_line = f"{old_line.split()[0]} - {temp}"
                new_data = ""

                for file_line in lines.split("\n"):
                    if file_line == old_line:
                        if new_data == "":
                            new_data = f"{new_line}"
                        else:
                            new_data = f"{new_data}\n{new_line}"
                    else:
                        if new_data == "":
                            new_data = f"{file_line}"
                        else:
                            new_data = f"{new_data}\n{file_line}"
                file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\data_MMP.txt", "w")
                file.write(new_data)
                file.close()

                today = date.today()
                ac_date = today.strftime("%d/%m/%Y")
                if str(self.edit_action_33.currentText()) == "+":
                    add_sub = "added"
                    for_from = "for"
                else:
                    add_sub = "subtracted"
                    for_from = "from"
                name = new_line.split(" ")[0]
                actions = f"{add_sub} {for_from} {name} {self.edit_amount_33.text()} money at {ac_date}\n"
                actions_file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\\actions_MMP.txt", "a")
                actions_file.write(actions)
                actions_file.close()

                self.add_data()
                self.hide_edit()
                self.edit_amount_33.clear()
            elif check_if_digit == False or self.edit_amount_33.text() == "":
                font = QtGui.QFont()
                font.setPointSize(18)
                font.setBold(True)
                self.main_title.setStyleSheet("color : red")
                self.main_title.setFont(font)
                self.main_title.setText("You must type only digits into the text box")
                self.after = QTimer()
                self.after.timeout.connect(self.timer)
                self.after.start(1000)
                self.edit_amount_33.clear()

        if selected_row_2 == 34:
            check_if_digit = self.edit_amount_34.text().isdigit()
            if check_if_digit:
                old_line = self.main_list_2.currentItem().text()
                temp = str(ops[str(self.edit_action_34.currentText())](int(old_line.split()[-1]), int(self.edit_amount_34.text())))
                new_line = f"{old_line.split()[0]} - {temp}"
                new_data = ""

                for file_line in lines.split("\n"):
                    if file_line == old_line:
                        if new_data == "":
                            new_data = f"{new_line}"
                        else:
                            new_data = f"{new_data}\n{new_line}"
                    else:
                        if new_data == "":
                            new_data = f"{file_line}"
                        else:
                            new_data = f"{new_data}\n{file_line}"
                file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\data_MMP.txt", "w")
                file.write(new_data)
                file.close()

                today = date.today()
                ac_date = today.strftime("%d/%m/%Y")
                if str(self.edit_action_34.currentText()) == "+":
                    add_sub = "added"
                    for_from = "for"
                else:
                    add_sub = "subtracted"
                    for_from = "from"
                name = new_line.split(" ")[0]
                actions = f"{add_sub} {for_from} {name} {self.edit_amount_34.text()} money at {ac_date}\n"
                actions_file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\\actions_MMP.txt", "a")
                actions_file.write(actions)
                actions_file.close()

                self.add_data()
                self.hide_edit()
                self.edit_amount_34.clear()
            elif check_if_digit == False or self.edit_amount_34.text() == "":
                font = QtGui.QFont()
                font.setPointSize(18)
                font.setBold(True)
                self.main_title.setStyleSheet("color : red")
                self.main_title.setFont(font)
                self.main_title.setText("You must type only digits into the text box")
                self.after = QTimer()
                self.after.timeout.connect(self.timer)
                self.after.start(1000)
                self.edit_amount_34.clear()

        if selected_row_2 == 35:
            check_if_digit = self.edit_amount_35.text().isdigit()
            if check_if_digit:
                old_line = self.main_list_2.currentItem().text()
                temp = str(ops[str(self.edit_action_35.currentText())](int(old_line.split()[-1]), int(self.edit_amount_35.text())))
                new_line = f"{old_line.split()[0]} - {temp}"
                new_data = ""

                for file_line in lines.split("\n"):
                    if file_line == old_line:
                        if new_data == "":
                            new_data = f"{new_line}"
                        else:
                            new_data = f"{new_data}\n{new_line}"
                    else:
                        if new_data == "":
                            new_data = f"{file_line}"
                        else:
                            new_data = f"{new_data}\n{file_line}"
                file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\data_MMP.txt", "w")
                file.write(new_data)
                file.close()

                today = date.today()
                ac_date = today.strftime("%d/%m/%Y")
                if str(self.edit_action_35.currentText()) == "+":
                    add_sub = "added"
                    for_from = "for"
                else:
                    add_sub = "subtracted"
                    for_from = "from"
                name = new_line.split(" ")[0]
                actions = f"{add_sub} {for_from} {name} {self.edit_amount_35.text()} money at {ac_date}\n"
                actions_file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\\actions_MMP.txt", "a")
                actions_file.write(actions)
                actions_file.close()

                self.add_data()
                self.hide_edit()
                self.edit_amount_35.clear()
            elif check_if_digit == False or self.edit_amount_35.text() == "":
                font = QtGui.QFont()
                font.setPointSize(18)
                font.setBold(True)
                self.main_title.setStyleSheet("color : red")
                self.main_title.setFont(font)
                self.main_title.setText("You must type only digits into the text box")
                self.after = QTimer()
                self.after.timeout.connect(self.timer)
                self.after.start(1000)
                self.edit_amount_35.clear()

        if selected_row_2 == 36:
            check_if_digit = self.edit_amount_36.text().isdigit()
            if check_if_digit:
                old_line = self.main_list_2.currentItem().text()
                temp = str(ops[str(self.edit_action_36.currentText())](int(old_line.split()[-1]), int(self.edit_amount_36.text())))
                new_line = f"{old_line.split()[0]} - {temp}"
                new_data = ""

                for file_line in lines.split("\n"):
                    if file_line == old_line:
                        if new_data == "":
                            new_data = f"{new_line}"
                        else:
                            new_data = f"{new_data}\n{new_line}"
                    else:
                        if new_data == "":
                            new_data = f"{file_line}"
                        else:
                            new_data = f"{new_data}\n{file_line}"
                file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\data_MMP.txt", "w")
                file.write(new_data)
                file.close()

                today = date.today()
                ac_date = today.strftime("%d/%m/%Y")
                if str(self.edit_action_36.currentText()) == "+":
                    add_sub = "added"
                    for_from = "for"
                else:
                    add_sub = "subtracted"
                    for_from = "from"
                name = new_line.split(" ")[0]
                actions = f"{add_sub} {for_from} {name} {self.edit_amount_36.text()} money at {ac_date}\n"
                actions_file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\\actions_MMP.txt", "a")
                actions_file.write(actions)
                actions_file.close()

                self.add_data()
                self.hide_edit()
                self.edit_amount_36.clear()
            elif check_if_digit == False or self.edit_amount_36.text() == "":
                font = QtGui.QFont()
                font.setPointSize(18)
                font.setBold(True)
                self.main_title.setStyleSheet("color : red")
                self.main_title.setFont(font)
                self.main_title.setText("You must type only digits into the text box")
                self.after = QTimer()
                self.after.timeout.connect(self.timer)
                self.after.start(1000)
                self.edit_amount_36.clear()

        if selected_row_2 == 37:
            check_if_digit = self.edit_amount_37.text().isdigit()
            if check_if_digit:
                old_line = self.main_list_2.currentItem().text()
                temp = str(ops[str(self.edit_action_37.currentText())](int(old_line.split()[-1]), int(self.edit_amount_37.text())))
                new_line = f"{old_line.split()[0]} - {temp}"
                new_data = ""

                for file_line in lines.split("\n"):
                    if file_line == old_line:
                        if new_data == "":
                            new_data = f"{new_line}"
                        else:
                            new_data = f"{new_data}\n{new_line}"
                    else:
                        if new_data == "":
                            new_data = f"{file_line}"
                        else:
                            new_data = f"{new_data}\n{file_line}"
                file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\data_MMP.txt", "w")
                file.write(new_data)
                file.close()

                today = date.today()
                ac_date = today.strftime("%d/%m/%Y")
                if str(self.edit_action_37.currentText()) == "+":
                    add_sub = "added"
                    for_from = "for"
                else:
                    add_sub = "subtracted"
                    for_from = "from"
                name = new_line.split(" ")[0]
                actions = f"{add_sub} {for_from} {name} {self.edit_amount_37.text()} money at {ac_date}\n"
                actions_file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\\actions_MMP.txt", "a")
                actions_file.write(actions)
                actions_file.close()

                self.add_data()
                self.hide_edit()
                self.edit_amount_37.clear()
            elif check_if_digit == False or self.edit_amount_37.text() == "":
                font = QtGui.QFont()
                font.setPointSize(18)
                font.setBold(True)
                self.main_title.setStyleSheet("color : red")
                self.main_title.setFont(font)
                self.main_title.setText("You must type only digits into the text box")
                self.after = QTimer()
                self.after.timeout.connect(self.timer)
                self.after.start(1000)
                self.edit_amount_37.clear()

        if selected_row_2 == 38:
            check_if_digit = self.edit_amount_38.text().isdigit()
            if check_if_digit:
                old_line = self.main_list_2.currentItem().text()
                temp = str(ops[str(self.edit_action_38.currentText())](int(old_line.split()[-1]), int(self.edit_amount_38.text())))
                new_line = f"{old_line.split()[0]} - {temp}"
                new_data = ""

                for file_line in lines.split("\n"):
                    if file_line == old_line:
                        if new_data == "":
                            new_data = f"{new_line}"
                        else:
                            new_data = f"{new_data}\n{new_line}"
                    else:
                        if new_data == "":
                            new_data = f"{file_line}"
                        else:
                            new_data = f"{new_data}\n{file_line}"
                file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\data_MMP.txt", "w")
                file.write(new_data)
                file.close()

                today = date.today()
                ac_date = today.strftime("%d/%m/%Y")
                if str(self.edit_action_38.currentText()) == "+":
                    add_sub = "added"
                    for_from = "for"
                else:
                    add_sub = "subtracted"
                    for_from = "from"
                name = new_line.split(" ")[0]
                actions = f"{add_sub} {for_from} {name} {self.edit_amount_38.text()} money at {ac_date}\n"
                actions_file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\\actions_MMP.txt", "a")
                actions_file.write(actions)
                actions_file.close()

                self.add_data()
                self.hide_edit()
                self.edit_amount_38.clear()
            elif check_if_digit == False or self.edit_amount_38.text() == "":
                font = QtGui.QFont()
                font.setPointSize(18)
                font.setBold(True)
                self.main_title.setStyleSheet("color : red")
                self.main_title.setFont(font)
                self.main_title.setText("You must type only digits into the text box")
                self.after = QTimer()
                self.after.timeout.connect(self.timer)
                self.after.start(1000)
                self.edit_amount_38.clear()

        if selected_row_2 == 39:
            check_if_digit = self.edit_amount_39.text().isdigit()
            if check_if_digit:
                old_line = self.main_list_2.currentItem().text()
                temp = str(ops[str(self.edit_action_39.currentText())](int(old_line.split()[-1]), int(self.edit_amount_39.text())))
                new_line = f"{old_line.split()[0]} - {temp}"
                new_data = ""

                for file_line in lines.split("\n"):
                    if file_line == old_line:
                        if new_data == "":
                            new_data = f"{new_line}"
                        else:
                            new_data = f"{new_data}\n{new_line}"
                    else:
                        if new_data == "":
                            new_data = f"{file_line}"
                        else:
                            new_data = f"{new_data}\n{file_line}"
                file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\data_MMP.txt", "w")
                file.write(new_data)
                file.close()

                today = date.today()
                ac_date = today.strftime("%d/%m/%Y")
                if str(self.edit_action_39.currentText()) == "+":
                    add_sub = "added"
                    for_from = "for"
                else:
                    add_sub = "subtracted"
                    for_from = "from"
                name = new_line.split(" ")[0]
                actions = f"{add_sub} {for_from} {name} {self.edit_amount_39.text()} money at {ac_date}\n"
                actions_file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\\actions_MMP.txt", "a")
                actions_file.write(actions)
                actions_file.close()

                self.add_data()
                self.hide_edit()
                self.edit_amount_39.clear()
            elif check_if_digit == False or self.edit_amount_39.text() == "":
                font = QtGui.QFont()
                font.setPointSize(18)
                font.setBold(True)
                self.main_title.setStyleSheet("color : red")
                self.main_title.setFont(font)
                self.main_title.setText("You must type only digits into the text box")
                self.after = QTimer()
                self.after.timeout.connect(self.timer)
                self.after.start(1000)
                self.edit_amount_39.clear()

        if selected_row_2 == 40:
            check_if_digit = self.edit_amount_40.text().isdigit()
            if check_if_digit:
                old_line = self.main_list_2.currentItem().text()
                temp = str(ops[str(self.edit_action_40.currentText())](int(old_line.split()[-1]), int(self.edit_amount_40.text())))
                new_line = f"{old_line.split()[0]} - {temp}"
                new_data = ""

                for file_line in lines.split("\n"):
                    if file_line == old_line:
                        if new_data == "":
                            new_data = f"{new_line}"
                        else:
                            new_data = f"{new_data}\n{new_line}"
                    else:
                        if new_data == "":
                            new_data = f"{file_line}"
                        else:
                            new_data = f"{new_data}\n{file_line}"
                file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\data_MMP.txt", "w")
                file.write(new_data)
                file.close()

                today = date.today()
                ac_date = today.strftime("%d/%m/%Y")
                if str(self.edit_action_40.currentText()) == "+":
                    add_sub = "added"
                    for_from = "for"
                else:
                    add_sub = "subtracted"
                    for_from = "from"
                name = new_line.split(" ")[0]
                actions = f"{add_sub} {for_from} {name} {self.edit_amount_40.text()} money at {ac_date}\n"
                actions_file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\\actions_MMP.txt", "a")
                actions_file.write(actions)
                actions_file.close()

                self.add_data()
                self.hide_edit()
                self.edit_amount_40.clear()
            elif check_if_digit == False or self.edit_amount_40.text() == "":
                font = QtGui.QFont()
                font.setPointSize(18)
                font.setBold(True)
                self.main_title.setStyleSheet("color : red")
                self.main_title.setFont(font)
                self.main_title.setText("You must type only digits into the text box")
                self.after = QTimer()
                self.after.timeout.connect(self.timer)
                self.after.start(1000)
                self.edit_amount_40.clear()

        if selected_row_3 == 41:
            check_if_digit = self.edit_amount_41.text().isdigit()
            if check_if_digit:
                old_line = self.main_list_3.currentItem().text()
                temp = str(ops[str(self.edit_action_41.currentText())](int(old_line.split()[-1]), int(self.edit_amount_41.text())))
                new_line = f"{old_line.split()[0]} - {temp}"
                new_data = ""

                for file_line in lines.split("\n"):
                    if file_line == old_line:
                        if new_data == "":
                            new_data = f"{new_line}"
                        else:
                            new_data = f"{new_data}\n{new_line}"
                    else:
                        if new_data == "":
                            new_data = f"{file_line}"
                        else:
                            new_data = f"{new_data}\n{file_line}"
                file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\data_MMP.txt", "w")
                file.write(new_data)
                file.close()

                today = date.today()
                ac_date = today.strftime("%d/%m/%Y")
                if str(self.edit_action_41.currentText()) == "+":
                    add_sub = "added"
                    for_from = "for"
                else:
                    add_sub = "subtracted"
                    for_from = "from"
                name = new_line.split(" ")[0]
                actions = f"{add_sub} {for_from} {name} {self.edit_amount_41.text()} money at {ac_date}\n"
                actions_file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\\actions_MMP.txt", "a")
                actions_file.write(actions)
                actions_file.close()

                self.add_data()
                self.hide_edit()
                self.edit_amount_41.clear()
            elif check_if_digit == False or self.edit_amount_41.text() == "":
                font = QtGui.QFont()
                font.setPointSize(18)
                font.setBold(True)
                self.main_title.setStyleSheet("color : red")
                self.main_title.setFont(font)
                self.main_title.setText("You must type only digits into the text box")
                self.after = QTimer()
                self.after.timeout.connect(self.timer)
                self.after.start(1000)
                self.edit_amount_41.clear()

        if selected_row_3 == 42:
            check_if_digit = self.edit_amount_42.text().isdigit()
            if check_if_digit:
                old_line = self.main_list_3.currentItem().text()
                temp = str(ops[str(self.edit_action_42.currentText())](int(old_line.split()[-1]), int(self.edit_amount_42.text())))
                new_line = f"{old_line.split()[0]} - {temp}"
                new_data = ""

                for file_line in lines.split("\n"):
                    if file_line == old_line:
                        if new_data == "":
                            new_data = f"{new_line}"
                        else:
                            new_data = f"{new_data}\n{new_line}"
                    else:
                        if new_data == "":
                            new_data = f"{file_line}"
                        else:
                            new_data = f"{new_data}\n{file_line}"
                file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\data_MMP.txt", "w")
                file.write(new_data)
                file.close()

                today = date.today()
                ac_date = today.strftime("%d/%m/%Y")
                if str(self.edit_action_42.currentText()) == "+":
                    add_sub = "added"
                    for_from = "for"
                else:
                    add_sub = "subtracted"
                    for_from = "from"
                name = new_line.split(" ")[0]
                actions = f"{add_sub} {for_from} {name} {self.edit_amount_42.text()} money at {ac_date}\n"
                actions_file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\\actions_MMP.txt", "a")
                actions_file.write(actions)
                actions_file.close()

                self.add_data()
                self.hide_edit()
                self.edit_amount_42.clear()
            elif check_if_digit == False or self.edit_amount_42.text() == "":
                font = QtGui.QFont()
                font.setPointSize(18)
                font.setBold(True)
                self.main_title.setStyleSheet("color : red")
                self.main_title.setFont(font)
                self.main_title.setText("You must type only digits into the text box")
                self.after = QTimer()
                self.after.timeout.connect(self.timer)
                self.after.start(1000)
                self.edit_amount_42.clear()

        if selected_row_3 == 43:
            check_if_digit = self.edit_amount_43.text().isdigit()
            if check_if_digit:
                old_line = self.main_list_3.currentItem().text()
                temp = str(ops[str(self.edit_action_43.currentText())](int(old_line.split()[-1]), int(self.edit_amount_43.text())))
                new_line = f"{old_line.split()[0]} - {temp}"
                new_data = ""

                for file_line in lines.split("\n"):
                    if file_line == old_line:
                        if new_data == "":
                            new_data = f"{new_line}"
                        else:
                            new_data = f"{new_data}\n{new_line}"
                    else:
                        if new_data == "":
                            new_data = f"{file_line}"
                        else:
                            new_data = f"{new_data}\n{file_line}"
                file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\data_MMP.txt", "w")
                file.write(new_data)
                file.close()

                today = date.today()
                ac_date = today.strftime("%d/%m/%Y")
                if str(self.edit_action_43.currentText()) == "+":
                    add_sub = "added"
                    for_from = "for"
                else:
                    add_sub = "subtracted"
                    for_from = "from"
                name = new_line.split(" ")[0]
                actions = f"{add_sub} {for_from} {name} {self.edit_amount_43.text()} money at {ac_date}\n"
                actions_file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\\actions_MMP.txt", "a")
                actions_file.write(actions)
                actions_file.close()

                self.add_data()
                self.hide_edit()
                self.edit_amount_43.clear()
            elif check_if_digit == False or self.edit_amount_43.text() == "":
                font = QtGui.QFont()
                font.setPointSize(18)
                font.setBold(True)
                self.main_title.setStyleSheet("color : red")
                self.main_title.setFont(font)
                self.main_title.setText("You must type only digits into the text box")
                self.after = QTimer()
                self.after.timeout.connect(self.timer)
                self.after.start(1000)
                self.edit_amount_43.clear()

        if selected_row_3 == 44:
            check_if_digit = self.edit_amount_44.text().isdigit()
            if check_if_digit:
                old_line = self.main_list_3.currentItem().text()
                temp = str(ops[str(self.edit_action_44.currentText())](int(old_line.split()[-1]), int(self.edit_amount_44.text())))
                new_line = f"{old_line.split()[0]} - {temp}"
                new_data = ""

                for file_line in lines.split("\n"):
                    if file_line == old_line:
                        if new_data == "":
                            new_data = f"{new_line}"
                        else:
                            new_data = f"{new_data}\n{new_line}"
                    else:
                        if new_data == "":
                            new_data = f"{file_line}"
                        else:
                            new_data = f"{new_data}\n{file_line}"
                file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\data_MMP.txt", "w")
                file.write(new_data)
                file.close()

                today = date.today()
                ac_date = today.strftime("%d/%m/%Y")
                if str(self.edit_action_44.currentText()) == "+":
                    add_sub = "added"
                    for_from = "for"
                else:
                    add_sub = "subtracted"
                    for_from = "from"
                name = new_line.split(" ")[0]
                actions = f"{add_sub} {for_from} {name} {self.edit_amount_44.text()} money at {ac_date}\n"
                actions_file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\\actions_MMP.txt", "a")
                actions_file.write(actions)
                actions_file.close()

                self.add_data()
                self.hide_edit()
                self.edit_amount_44.clear()
            elif check_if_digit == False or self.edit_amount_44.text() == "":
                font = QtGui.QFont()
                font.setPointSize(18)
                font.setBold(True)
                self.main_title.setStyleSheet("color : red")
                self.main_title.setFont(font)
                self.main_title.setText("You must type only digits into the text box")
                self.after = QTimer()
                self.after.timeout.connect(self.timer)
                self.after.start(1000)
                self.edit_amount_44.clear()

        if selected_row_3 == 45:
            check_if_digit = self.edit_amount_45.text().isdigit()
            if check_if_digit:
                old_line = self.main_list_3.currentItem().text()
                temp = str(ops[str(self.edit_action_45.currentText())](int(old_line.split()[-1]), int(self.edit_amount_45.text())))
                new_line = f"{old_line.split()[0]} - {temp}"
                new_data = ""

                for file_line in lines.split("\n"):
                    if file_line == old_line:
                        if new_data == "":
                            new_data = f"{new_line}"
                        else:
                            new_data = f"{new_data}\n{new_line}"
                    else:
                        if new_data == "":
                            new_data = f"{file_line}"
                        else:
                            new_data = f"{new_data}\n{file_line}"
                file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\data_MMP.txt", "w")
                file.write(new_data)
                file.close()

                today = date.today()
                ac_date = today.strftime("%d/%m/%Y")
                if str(self.edit_action_45.currentText()) == "+":
                    add_sub = "added"
                    for_from = "for"
                else:
                    add_sub = "subtracted"
                    for_from = "from"
                name = new_line.split(" ")[0]
                actions = f"{add_sub} {for_from} {name} {self.edit_amount_45.text()} money at {ac_date}\n"
                actions_file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\\actions_MMP.txt", "a")
                actions_file.write(actions)
                actions_file.close()

                self.add_data()
                self.hide_edit()
                self.edit_amount_45.clear()
            elif check_if_digit == False or self.edit_amount_45.text() == "":
                font = QtGui.QFont()
                font.setPointSize(18)
                font.setBold(True)
                self.main_title.setStyleSheet("color : red")
                self.main_title.setFont(font)
                self.main_title.setText("You must type only digits into the text box")
                self.after = QTimer()
                self.after.timeout.connect(self.timer)
                self.after.start(1000)
                self.edit_amount_45.clear()

        if selected_row_3 == 46:
            check_if_digit = self.edit_amount_46.text().isdigit()
            if check_if_digit:
                old_line = self.main_list_3.currentItem().text()
                temp = str(ops[str(self.edit_action_46.currentText())](int(old_line.split()[-1]), int(self.edit_amount_46.text())))
                new_line = f"{old_line.split()[0]} - {temp}"
                new_data = ""

                for file_line in lines.split("\n"):
                    if file_line == old_line:
                        if new_data == "":
                            new_data = f"{new_line}"
                        else:
                            new_data = f"{new_data}\n{new_line}"
                    else:
                        if new_data == "":
                            new_data = f"{file_line}"
                        else:
                            new_data = f"{new_data}\n{file_line}"
                file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\data_MMP.txt", "w")
                file.write(new_data)
                file.close()

                today = date.today()
                ac_date = today.strftime("%d/%m/%Y")
                if str(self.edit_action_46.currentText()) == "+":
                    add_sub = "added"
                    for_from = "for"
                else:
                    add_sub = "subtracted"
                    for_from = "from"
                name = new_line.split(" ")[0]
                actions = f"{add_sub} {for_from} {name} {self.edit_amount_46.text()} money at {ac_date}\n"
                actions_file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\\actions_MMP.txt", "a")
                actions_file.write(actions)
                actions_file.close()

                self.add_data()
                self.hide_edit()
                self.edit_amount_46.clear()
            elif check_if_digit == False or self.edit_amount_46.text() == "":
                font = QtGui.QFont()
                font.setPointSize(18)
                font.setBold(True)
                self.main_title.setStyleSheet("color : red")
                self.main_title.setFont(font)
                self.main_title.setText("You must type only digits into the text box")
                self.after = QTimer()
                self.after.timeout.connect(self.timer)
                self.after.start(1000)
                self.edit_amount_46.clear()

        if selected_row_3 == 47:
            check_if_digit = self.edit_amount_47.text().isdigit()
            if check_if_digit:
                old_line = self.main_list_3.currentItem().text()
                temp = str(ops[str(self.edit_action_47.currentText())](int(old_line.split()[-1]), int(self.edit_amount_47.text())))
                new_line = f"{old_line.split()[0]} - {temp}"
                new_data = ""

                for file_line in lines.split("\n"):
                    if file_line == old_line:
                        if new_data == "":
                            new_data = f"{new_line}"
                        else:
                            new_data = f"{new_data}\n{new_line}"
                    else:
                        if new_data == "":
                            new_data = f"{file_line}"
                        else:
                            new_data = f"{new_data}\n{file_line}"
                file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\data_MMP.txt", "w")
                file.write(new_data)
                file.close()

                today = date.today()
                ac_date = today.strftime("%d/%m/%Y")
                if str(self.edit_action_47.currentText()) == "+":
                    add_sub = "added"
                    for_from = "for"
                else:
                    add_sub = "subtracted"
                    for_from = "from"
                name = new_line.split(" ")[0]
                actions = f"{add_sub} {for_from} {name} {self.edit_amount_47.text()} money at {ac_date}\n"
                actions_file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\\actions_MMP.txt", "a")
                actions_file.write(actions)
                actions_file.close()

                self.add_data()
                self.hide_edit()
                self.edit_amount_47.clear()
            elif check_if_digit == False or self.edit_amount_47.text() == "":
                font = QtGui.QFont()
                font.setPointSize(18)
                font.setBold(True)
                self.main_title.setStyleSheet("color : red")
                self.main_title.setFont(font)
                self.main_title.setText("You must type only digits into the text box")
                self.after = QTimer()
                self.after.timeout.connect(self.timer)
                self.after.start(1000)
                self.edit_amount_47.clear()

        if selected_row_3 == 48:
            check_if_digit = self.edit_amount_48.text().isdigit()
            if check_if_digit:
                old_line = self.main_list_3.currentItem().text()
                temp = str(ops[str(self.edit_action_48.currentText())](int(old_line.split()[-1]), int(self.edit_amount_48.text())))
                new_line = f"{old_line.split()[0]} - {temp}"
                new_data = ""

                for file_line in lines.split("\n"):
                    if file_line == old_line:
                        if new_data == "":
                            new_data = f"{new_line}"
                        else:
                            new_data = f"{new_data}\n{new_line}"
                    else:
                        if new_data == "":
                            new_data = f"{file_line}"
                        else:
                            new_data = f"{new_data}\n{file_line}"
                file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\data_MMP.txt", "w")
                file.write(new_data)
                file.close()

                today = date.today()
                ac_date = today.strftime("%d/%m/%Y")
                if str(self.edit_action_48.currentText()) == "+":
                    add_sub = "added"
                    for_from = "for"
                else:
                    add_sub = "subtracted"
                    for_from = "from"
                name = new_line.split(" ")[0]
                actions = f"{add_sub} {for_from} {name} {self.edit_amount_48.text()} money at {ac_date}\n"
                actions_file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\\actions_MMP.txt", "a")
                actions_file.write(actions)
                actions_file.close()

                self.add_data()
                self.hide_edit()
                self.edit_amount_48.clear()
            elif check_if_digit == False or self.edit_amount_48.text() == "":
                font = QtGui.QFont()
                font.setPointSize(18)
                font.setBold(True)
                self.main_title.setStyleSheet("color : red")
                self.main_title.setFont(font)
                self.main_title.setText("You must type only digits into the text box")
                self.after = QTimer()
                self.after.timeout.connect(self.timer)
                self.after.start(1000)
                self.edit_amount_48.clear()

        if selected_row_3 == 49:
            check_if_digit = self.edit_amount_49.text().isdigit()
            if check_if_digit:
                old_line = self.main_list_3.currentItem().text()
                temp = str(ops[str(self.edit_action_49.currentText())](int(old_line.split()[-1]), int(self.edit_amount_49.text())))
                new_line = f"{old_line.split()[0]} - {temp}"
                new_data = ""

                for file_line in lines.split("\n"):
                    if file_line == old_line:
                        if new_data == "":
                            new_data = f"{new_line}"
                        else:
                            new_data = f"{new_data}\n{new_line}"
                    else:
                        if new_data == "":
                            new_data = f"{file_line}"
                        else:
                            new_data = f"{new_data}\n{file_line}"
                file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\data_MMP.txt", "w")
                file.write(new_data)
                file.close()

                today = date.today()
                ac_date = today.strftime("%d/%m/%Y")
                if str(self.edit_action_49.currentText()) == "+":
                    add_sub = "added"
                    for_from = "for"
                else:
                    add_sub = "subtracted"
                    for_from = "from"
                name = new_line.split(" ")[0]
                actions = f"{add_sub} {for_from} {name} {self.edit_amount_49.text()} money at {ac_date}\n"
                actions_file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\\actions_MMP.txt", "a")
                actions_file.write(actions)
                actions_file.close()

                self.add_data()
                self.hide_edit()
                self.edit_amount_49.clear()
            elif check_if_digit == False or self.edit_amount_49.text() == "":
                font = QtGui.QFont()
                font.setPointSize(18)
                font.setBold(True)
                self.main_title.setStyleSheet("color : red")
                self.main_title.setFont(font)
                self.main_title.setText("You must type only digits into the text box")
                self.after = QTimer()
                self.after.timeout.connect(self.timer)
                self.after.start(1000)
                self.edit_amount_49.clear()

        if selected_row_3 == 50:
            check_if_digit = self.edit_amount_50.text().isdigit()
            if check_if_digit:
                old_line = self.main_list_3.currentItem().text()
                temp = str(ops[str(self.edit_action_50.currentText())](int(old_line.split()[-1]), int(self.edit_amount_50.text())))
                new_line = f"{old_line.split()[0]} - {temp}"
                new_data = ""

                for file_line in lines.split("\n"):
                    if file_line == old_line:
                        if new_data == "":
                            new_data = f"{new_line}"
                        else:
                            new_data = f"{new_data}\n{new_line}"
                    else:
                        if new_data == "":
                            new_data = f"{file_line}"
                        else:
                            new_data = f"{new_data}\n{file_line}"
                file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\data_MMP.txt", "w")
                file.write(new_data)
                file.close()

                today = date.today()
                ac_date = today.strftime("%d/%m/%Y")
                if str(self.edit_action_50.currentText()) == "+":
                    add_sub = "added"
                    for_from = "for"
                else:
                    add_sub = "subtracted"
                    for_from = "from"
                name = new_line.split(" ")[0]
                actions = f"{add_sub} {for_from} {name} {self.edit_amount_50.text()} money at {ac_date}\n"
                actions_file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\\actions_MMP.txt", "a")
                actions_file.write(actions)
                actions_file.close()

                self.add_data()
                self.hide_edit()
                self.edit_amount_50.clear()
            elif check_if_digit == False or self.edit_amount_50.text() == "":
                font = QtGui.QFont()
                font.setPointSize(18)
                font.setBold(True)
                self.main_title.setStyleSheet("color : red")
                self.main_title.setFont(font)
                self.main_title.setText("You must type only digits into the text box")
                self.after = QTimer()
                self.after.timeout.connect(self.timer)
                self.after.start(1000)
                self.edit_amount_50.clear()

        if selected_row_3 == 51:
            check_if_digit = self.edit_amount_51.text().isdigit()
            if check_if_digit:
                old_line = self.main_list_3.currentItem().text()
                temp = str(ops[str(self.edit_action_51.currentText())](int(old_line.split()[-1]), int(self.edit_amount_51.text())))
                new_line = f"{old_line.split()[0]} - {temp}"
                new_data = ""

                for file_line in lines.split("\n"):
                    if file_line == old_line:
                        if new_data == "":
                            new_data = f"{new_line}"
                        else:
                            new_data = f"{new_data}\n{new_line}"
                    else:
                        if new_data == "":
                            new_data = f"{file_line}"
                        else:
                            new_data = f"{new_data}\n{file_line}"
                file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\data_MMP.txt", "w")
                file.write(new_data)
                file.close()

                today = date.today()
                ac_date = today.strftime("%d/%m/%Y")
                if str(self.edit_action_51.currentText()) == "+":
                    add_sub = "added"
                    for_from = "for"
                else:
                    add_sub = "subtracted"
                    for_from = "from"
                name = new_line.split(" ")[0]
                actions = f"{add_sub} {for_from} {name} {self.edit_amount_51.text()} money at {ac_date}\n"
                actions_file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\\actions_MMP.txt", "a")
                actions_file.write(actions)
                actions_file.close()

                self.add_data()
                self.hide_edit()
                self.edit_amount_51.clear()
            elif check_if_digit == False or self.edit_amount_51.text() == "":
                font = QtGui.QFont()
                font.setPointSize(18)
                font.setBold(True)
                self.main_title.setStyleSheet("color : red")
                self.main_title.setFont(font)
                self.main_title.setText("You must type only digits into the text box")
                self.after = QTimer()
                self.after.timeout.connect(self.timer)
                self.after.start(1000)
                self.edit_amount_51.clear()

        if selected_row_3 == 52:
            check_if_digit = self.edit_amount_52.text().isdigit()
            if check_if_digit:
                old_line = self.main_list_3.currentItem().text()
                temp = str(ops[str(self.edit_action_52.currentText())](int(old_line.split()[-1]), int(self.edit_amount_52.text())))
                new_line = f"{old_line.split()[0]} - {temp}"
                new_data = ""

                for file_line in lines.split("\n"):
                    if file_line == old_line:
                        if new_data == "":
                            new_data = f"{new_line}"
                        else:
                            new_data = f"{new_data}\n{new_line}"
                    else:
                        if new_data == "":
                            new_data = f"{file_line}"
                        else:
                            new_data = f"{new_data}\n{file_line}"
                file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\data_MMP.txt", "w")
                file.write(new_data)
                file.close()

                today = date.today()
                ac_date = today.strftime("%d/%m/%Y")
                if str(self.edit_action_52.currentText()) == "+":
                    add_sub = "added"
                    for_from = "for"
                else:
                    add_sub = "subtracted"
                    for_from = "from"
                name = new_line.split(" ")[0]
                actions = f"{add_sub} {for_from} {name} {self.edit_amount_52.text()} money at {ac_date}\n"
                actions_file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\\actions_MMP.txt", "a")
                actions_file.write(actions)
                actions_file.close()

                self.add_data()
                self.hide_edit()
                self.edit_amount_52.clear()
            elif check_if_digit == False or self.edit_amount_52.text() == "":
                font = QtGui.QFont()
                font.setPointSize(18)
                font.setBold(True)
                self.main_title.setStyleSheet("color : red")
                self.main_title.setFont(font)
                self.main_title.setText("You must type only digits into the text box")
                self.after = QTimer()
                self.after.timeout.connect(self.timer)
                self.after.start(1000)
                self.edit_amount_52.clear()

        if selected_row_3 == 53:
            check_if_digit = self.edit_amount_53.text().isdigit()
            if check_if_digit:
                old_line = self.main_list_3.currentItem().text()
                temp = str(ops[str(self.edit_action_53.currentText())](int(old_line.split()[-1]), int(self.edit_amount_53.text())))
                new_line = f"{old_line.split()[0]} - {temp}"
                new_data = ""

                for file_line in lines.split("\n"):
                    if file_line == old_line:
                        if new_data == "":
                            new_data = f"{new_line}"
                        else:
                            new_data = f"{new_data}\n{new_line}"
                    else:
                        if new_data == "":
                            new_data = f"{file_line}"
                        else:
                            new_data = f"{new_data}\n{file_line}"
                file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\data_MMP.txt", "w")
                file.write(new_data)
                file.close()

                today = date.today()
                ac_date = today.strftime("%d/%m/%Y")
                if str(self.edit_action_53.currentText()) == "+":
                    add_sub = "added"
                    for_from = "for"
                else:
                    add_sub = "subtracted"
                    for_from = "from"
                name = new_line.split(" ")[0]
                actions = f"{add_sub} {for_from} {name} {self.edit_amount_53.text()} money at {ac_date}\n"
                actions_file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\\actions_MMP.txt", "a")
                actions_file.write(actions)
                actions_file.close()

                self.add_data()
                self.hide_edit()
                self.edit_amount_53.clear()
            elif check_if_digit == False or self.edit_amount_53.text() == "":
                font = QtGui.QFont()
                font.setPointSize(18)
                font.setBold(True)
                self.main_title.setStyleSheet("color : red")
                self.main_title.setFont(font)
                self.main_title.setText("You must type only digits into the text box")
                self.after = QTimer()
                self.after.timeout.connect(self.timer)
                self.after.start(1000)
                self.edit_amount_53.clear()

        if selected_row_3 == 54:
            check_if_digit = self.edit_amount_54.text().isdigit()
            if check_if_digit:
                old_line = self.main_list_3.currentItem().text()
                temp = str(ops[str(self.edit_action_54.currentText())](int(old_line.split()[-1]), int(self.edit_amount_54.text())))
                new_line = f"{old_line.split()[0]} - {temp}"
                new_data = ""

                for file_line in lines.split("\n"):
                    if file_line == old_line:
                        if new_data == "":
                            new_data = f"{new_line}"
                        else:
                            new_data = f"{new_data}\n{new_line}"
                    else:
                        if new_data == "":
                            new_data = f"{file_line}"
                        else:
                            new_data = f"{new_data}\n{file_line}"
                file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\data_MMP.txt", "w")
                file.write(new_data)
                file.close()

                today = date.today()
                ac_date = today.strftime("%d/%m/%Y")
                if str(self.edit_action_54.currentText()) == "+":
                    add_sub = "added"
                    for_from = "for"
                else:
                    add_sub = "subtracted"
                    for_from = "from"
                name = new_line.split(" ")[0]
                actions = f"{add_sub} {for_from} {name} {self.edit_amount_54.text()} money at {ac_date}\n"
                actions_file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\\actions_MMP.txt", "a")
                actions_file.write(actions)
                actions_file.close()

                self.add_data()
                self.hide_edit()
                self.edit_amount_54.clear()
            elif check_if_digit == False or self.edit_amount_54.text() == "":
                font = QtGui.QFont()
                font.setPointSize(18)
                font.setBold(True)
                self.main_title.setStyleSheet("color : red")
                self.main_title.setFont(font)
                self.main_title.setText("You must type only digits into the text box")
                self.after = QTimer()
                self.after.timeout.connect(self.timer)
                self.after.start(1000)
                self.edit_amount_54.clear()

        if selected_row_3 == 55:
            check_if_digit = self.edit_amount_55.text().isdigit()
            if check_if_digit:
                old_line = self.main_list_3.currentItem().text()
                temp = str(ops[str(self.edit_action_55.currentText())](int(old_line.split()[-1]), int(self.edit_amount_55.text())))
                new_line = f"{old_line.split()[0]} - {temp}"
                new_data = ""

                for file_line in lines.split("\n"):
                    if file_line == old_line:
                        if new_data == "":
                            new_data = f"{new_line}"
                        else:
                            new_data = f"{new_data}\n{new_line}"
                    else:
                        if new_data == "":
                            new_data = f"{file_line}"
                        else:
                            new_data = f"{new_data}\n{file_line}"
                file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\data_MMP.txt", "w")
                file.write(new_data)
                file.close()

                today = date.today()
                ac_date = today.strftime("%d/%m/%Y")
                if str(self.edit_action_55.currentText()) == "+":
                    add_sub = "added"
                    for_from = "for"
                else:
                    add_sub = "subtracted"
                    for_from = "from"
                name = new_line.split(" ")[0]
                actions = f"{add_sub} {for_from} {name} {self.edit_amount_55.text()} money at {ac_date}\n"
                actions_file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\\actions_MMP.txt", "a")
                actions_file.write(actions)
                actions_file.close()

                self.add_data()
                self.hide_edit()
                self.edit_amount_55.clear()
            elif check_if_digit == False or self.edit_amount_55.text() == "":
                font = QtGui.QFont()
                font.setPointSize(18)
                font.setBold(True)
                self.main_title.setStyleSheet("color : red")
                self.main_title.setFont(font)
                self.main_title.setText("You must type only digits into the text box")
                self.after = QTimer()
                self.after.timeout.connect(self.timer)
                self.after.start(1000)
                self.edit_amount_55.clear()

        if selected_row_3 == 56:
            check_if_digit = self.edit_amount_56.text().isdigit()
            if check_if_digit:
                old_line = self.main_list_3.currentItem().text()
                temp = str(ops[str(self.edit_action_56.currentText())](int(old_line.split()[-1]), int(self.edit_amount_56.text())))
                new_line = f"{old_line.split()[0]} - {temp}"
                new_data = ""

                for file_line in lines.split("\n"):
                    if file_line == old_line:
                        if new_data == "":
                            new_data = f"{new_line}"
                        else:
                            new_data = f"{new_data}\n{new_line}"
                    else:
                        if new_data == "":
                            new_data = f"{file_line}"
                        else:
                            new_data = f"{new_data}\n{file_line}"
                file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\data_MMP.txt", "w")
                file.write(new_data)
                file.close()

                today = date.today()
                ac_date = today.strftime("%d/%m/%Y")
                if str(self.edit_action_56.currentText()) == "+":
                    add_sub = "added"
                    for_from = "for"
                else:
                    add_sub = "subtracted"
                    for_from = "from"
                name = new_line.split(" ")[0]
                actions = f"{add_sub} {for_from} {name} {self.edit_amount_56.text()} money at {ac_date}\n"
                actions_file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\\actions_MMP.txt", "a")
                actions_file.write(actions)
                actions_file.close()

                self.add_data()
                self.hide_edit()
                self.edit_amount_56.clear()
            elif check_if_digit == False or self.edit_amount_56.text() == "":
                font = QtGui.QFont()
                font.setPointSize(18)
                font.setBold(True)
                self.main_title.setStyleSheet("color : red")
                self.main_title.setFont(font)
                self.main_title.setText("You must type only digits into the text box")
                self.after = QTimer()
                self.after.timeout.connect(self.timer)
                self.after.start(1000)
                self.edit_amount_56.clear()

        if selected_row_3 == 57:
            check_if_digit = self.edit_amount_57.text().isdigit()
            if check_if_digit:
                old_line = self.main_list_3.currentItem().text()
                temp = str(ops[str(self.edit_action_57.currentText())](int(old_line.split()[-1]), int(self.edit_amount_57.text())))
                new_line = f"{old_line.split()[0]} - {temp}"
                new_data = ""

                for file_line in lines.split("\n"):
                    if file_line == old_line:
                        if new_data == "":
                            new_data = f"{new_line}"
                        else:
                            new_data = f"{new_data}\n{new_line}"
                    else:
                        if new_data == "":
                            new_data = f"{file_line}"
                        else:
                            new_data = f"{new_data}\n{file_line}"
                file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\data_MMP.txt", "w")
                file.write(new_data)
                file.close()

                today = date.today()
                ac_date = today.strftime("%d/%m/%Y")
                if str(self.edit_action_57.currentText()) == "+":
                    add_sub = "added"
                    for_from = "for"
                else:
                    add_sub = "subtracted"
                    for_from = "from"
                name = new_line.split(" ")[0]
                actions = f"{add_sub} {for_from} {name} {self.edit_amount_57.text()} money at {ac_date}\n"
                actions_file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\\actions_MMP.txt", "a")
                actions_file.write(actions)
                actions_file.close()

                self.add_data()
                self.hide_edit()
                self.edit_amount_57.clear()
            elif check_if_digit == False or self.edit_amount_57.text() == "":
                font = QtGui.QFont()
                font.setPointSize(18)
                font.setBold(True)
                self.main_title.setStyleSheet("color : red")
                self.main_title.setFont(font)
                self.main_title.setText("You must type only digits into the text box")
                self.after = QTimer()
                self.after.timeout.connect(self.timer)
                self.after.start(1000)
                self.edit_amount_57.clear()

        if selected_row_3 == 58:
            check_if_digit = self.edit_amount_58.text().isdigit()
            if check_if_digit:
                old_line = self.main_list_3.currentItem().text()
                temp = str(ops[str(self.edit_action_58.currentText())](int(old_line.split()[-1]), int(self.edit_amount_58.text())))
                new_line = f"{old_line.split()[0]} - {temp}"
                new_data = ""

                for file_line in lines.split("\n"):
                    if file_line == old_line:
                        if new_data == "":
                            new_data = f"{new_line}"
                        else:
                            new_data = f"{new_data}\n{new_line}"
                    else:
                        if new_data == "":
                            new_data = f"{file_line}"
                        else:
                            new_data = f"{new_data}\n{file_line}"
                file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\data_MMP.txt", "w")
                file.write(new_data)
                file.close()

                today = date.today()
                ac_date = today.strftime("%d/%m/%Y")
                if str(self.edit_action_58.currentText()) == "+":
                    add_sub = "added"
                    for_from = "for"
                else:
                    add_sub = "subtracted"
                    for_from = "from"
                name = new_line.split(" ")[0]
                actions = f"{add_sub} {for_from} {name} {self.edit_amount_58.text()} money at {ac_date}\n"
                actions_file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\\actions_MMP.txt", "a")
                actions_file.write(actions)
                actions_file.close()

                self.add_data()
                self.hide_edit()
                self.edit_amount_58.clear()
            elif check_if_digit == False or self.edit_amount_58.text() == "":
                font = QtGui.QFont()
                font.setPointSize(18)
                font.setBold(True)
                self.main_title.setStyleSheet("color : red")
                self.main_title.setFont(font)
                self.main_title.setText("You must type only digits into the text box")
                self.after = QTimer()
                self.after.timeout.connect(self.timer)
                self.after.start(1000)
                self.edit_amount_58.clear()

        if selected_row_3 == 59:
            check_if_digit = self.edit_amount_59.text().isdigit()
            if check_if_digit:
                old_line = self.main_list_3.currentItem().text()
                temp = str(ops[str(self.edit_action_59.currentText())](int(old_line.split()[-1]), int(self.edit_amount_59.text())))
                new_line = f"{old_line.split()[0]} - {temp}"
                new_data = ""

                for file_line in lines.split("\n"):
                    if file_line == old_line:
                        if new_data == "":
                            new_data = f"{new_line}"
                        else:
                            new_data = f"{new_data}\n{new_line}"
                    else:
                        if new_data == "":
                            new_data = f"{file_line}"
                        else:
                            new_data = f"{new_data}\n{file_line}"
                file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\data_MMP.txt", "w")
                file.write(new_data)
                file.close()

                today = date.today()
                ac_date = today.strftime("%d/%m/%Y")
                if str(self.edit_action_59.currentText()) == "+":
                    add_sub = "added"
                    for_from = "for"
                else:
                    add_sub = "subtracted"
                    for_from = "from"
                name = new_line.split(" ")[0]
                actions = f"{add_sub} {for_from} {name} {self.edit_amount_59.text()} money at {ac_date}\n"
                actions_file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\\actions_MMP.txt", "a")
                actions_file.write(actions)
                actions_file.close()

                self.add_data()
                self.hide_edit()
                self.edit_amount_59.clear()
            elif check_if_digit == False or self.edit_amount_59.text() == "":
                font = QtGui.QFont()
                font.setPointSize(18)
                font.setBold(True)
                self.main_title.setStyleSheet("color : red")
                self.main_title.setFont(font)
                self.main_title.setText("You must type only digits into the text box")
                self.after = QTimer()
                self.after.timeout.connect(self.timer)
                self.after.start(1000)
                self.edit_amount_59.clear()

        if selected_row_3 == 60:
            check_if_digit = self.edit_amount_60.text().isdigit()
            if check_if_digit:
                old_line = self.main_list_3.currentItem().text()
                temp = str(ops[str(self.edit_action_60.currentText())](int(old_line.split()[-1]), int(self.edit_amount_60.text())))
                new_line = f"{old_line.split()[0]} - {temp}"
                new_data = ""

                for file_line in lines.split("\n"):
                    if file_line == old_line:
                        if new_data == "":
                            new_data = f"{new_line}"
                        else:
                            new_data = f"{new_data}\n{new_line}"
                    else:
                        if new_data == "":
                            new_data = f"{file_line}"
                        else:
                            new_data = f"{new_data}\n{file_line}"
                file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\data_MMP.txt", "w")
                file.write(new_data)
                file.close()

                today = date.today()
                ac_date = today.strftime("%d/%m/%Y")
                if str(self.edit_action_60.currentText()) == "+":
                    add_sub = "added"
                    for_from = "for"
                else:
                    add_sub = "subtracted"
                    for_from = "from"
                name = new_line.split(" ")[0]
                actions = f"{add_sub} {for_from} {name} {self.edit_amount_60.text()} money at {ac_date}\n"
                actions_file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\\actions_MMP.txt", "a")
                actions_file.write(actions)
                actions_file.close()

                self.add_data()
                self.hide_edit()
                self.edit_amount_60.clear()
            elif check_if_digit == False or self.edit_amount_60.text() == "":
                font = QtGui.QFont()
                font.setPointSize(18)
                font.setBold(True)
                self.main_title.setStyleSheet("color : red")
                self.main_title.setFont(font)
                self.main_title.setText("You must type only digits into the text box")
                self.after = QTimer()
                self.after.timeout.connect(self.timer)
                self.after.start(1000)
                self.edit_amount_60.clear()

    def cancel_edit_mode(self):
        self.hide_edit()
        self.main_delete_button.show()

    def delete_function(self):
        row1 = self.main_list_1.currentRow()
        row2 = self.main_list_2.currentRow()
        row3 = self.main_list_3.currentRow()
        if row1 == -1 and row2 == -1 and row3 == -1:
            font = QtGui.QFont()
            font.setPointSize(18)
            font.setBold(True)
            self.main_title.setStyleSheet("color : red")
            self.main_title.setFont(font)
            self.main_title.setText("You must select a row in order to delete it")
            self.after = QTimer()
            self.after.timeout.connect(self.timer)
            self.after.start(1000)
        else:
            if self.main_list_1.currentRow() != -1:
                selected_line_text1 = self.main_list_1.currentItem().text()
            else:
                selected_line_text1 = ""
            if self.main_list_2.currentRow() != -1:
                selected_line_text2 = self.main_list_2.currentItem().text()
            else:
                selected_line_text2 = ""
            if self.main_list_3.currentRow() != -1:
                selected_line_text3 = self.main_list_3.currentItem().text()
            else:
                selected_line_text3 = ""

            file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\data_MMP.txt", "r")
            lines = file.read()
            file.close()

            new_data = ""
            for line in lines.split("\n"):
                if line == selected_line_text1:
                    pass
                elif line == selected_line_text2:
                    pass
                elif line == selected_line_text3:
                    pass
                elif line != selected_line_text1 or selected_line_text2 or selected_line_text3:
                    if new_data == "":
                        new_data = line
                    else:
                        new_data = f"{new_data}\n{line}"

            today = date.today()
            ac_date = today.strftime("%d/%m/%Y")
            name = selected_line_text1.split(" ")[0] + selected_line_text2.split(" ")[0] + selected_line_text3.split(" ")[0]
            actions = f"removed {name} at {ac_date}"
            actions_file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\\actions_MMP.txt", "a")
            actions_file.write(actions)
            actions_file.close()

            file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\data_MMP.txt", "w")
            file.write(new_data)
            file.close()

            self.add_data()

    def add_mode(self):
        self.show_add()
        self.main_title.hide()
        self.main_delete_button.hide()

    def cancel_add_mode(self):
        self.hide_add()
        self.main_title.show()
        self.main_delete_button.show()

    def total_money(self):
        file = open("C:\Users\iliaz\PycharmProjects\Mega Management Program\program files\data_MMP.txt", "r")
        lines = file.read()
        file.close()

        ops = {"+": operator.add, "-": operator.sub}
        total_number = 0
        for line in lines.split("\n"):
            for number in line.split():
                check_if_digit = number.isdigit()
                if check_if_digit:
                    total_number = str(ops["+"](int(number), int(total_number)))
        self.main_totalmoney.setText(f"Total Money - {total_number}")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    gui = MoneyMP()
    gui.show()
    app.exec_()