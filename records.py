from design import (Ui_CreateCompanyWindow, Ui_PeopleSearchWindow, Ui_Alert,
    Ui_AddPerson, Ui_AddGroupWindow, Ui_ChoosePersonWindow,
    Ui_DeletePersonWindow, Ui_DeleteCompanyWindow,
    Ui_DeleteGroupWindow, Ui_ChoosePersonToChangeWindow,
    Ui_ChangePersonWindow, Ui_StartFaceRecognitionWindow)
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QAction
from PyQt5.QtGui import QIcon
from PIL.ImageQt import ImageQt
from PIL import Image
from matplotlib.image import imread
import numpy as np
from threading import Thread
import matplotlib.pyplot as plt
import face_recognition
import sqlite3
import secrets
import sys
import cv2
import os


# Defining variables
alert_text = ""
first_name, last_name, company_, group_, person_id = "", "", "", "", ""
conn = sqlite3.connect("data.db", timeout=10)
cur = conn.cursor()


def show_alert(parent, text, success):
    global alert_text
    if success:
        alert_text = "✔️ " + text
    else:
        alert_text = "❌ " + text
    alertWindow = AlertWindow(parent)
    alertWindow.show()


def transliterate(string):

    capital_letters = {u'А': u'A',
                       u'Б': u'B',
                       u'В': u'V',
                       u'Г': u'G',
                       u'Д': u'D',
                       u'Е': u'E',
                       u'Ё': u'E',
                       u'Ж': u'Zh',
                       u'З': u'Z',
                       u'И': u'I',
                       u'Й': u'Y',
                       u'К': u'K',
                       u'Л': u'L',
                       u'М': u'M',
                       u'Н': u'N',
                       u'О': u'O',
                       u'П': u'P',
                       u'Р': u'R',
                       u'С': u'S',
                       u'Т': u'T',
                       u'У': u'U',
                       u'Ф': u'F',
                       u'Х': u'H',
                       u'Ц': u'Ts',
                       u'Ч': u'Ch',
                       u'Ш': u'Sh',
                       u'Щ': u'Sch',
                       u'Ъ': u'',
                       u'Ы': u'Y',
                       u'Ь': u'',
                       u'Э': u'E',
                       u'Ю': u'Yu',
                       u'Я': u'Ya', }

    lower_case_letters = {u'а': u'a',
                          u'б': u'b',
                          u'в': u'v',
                          u'г': u'g',
                          u'д': u'd',
                          u'е': u'e',
                          u'ё': u'e',
                          u'ж': u'zh',
                          u'з': u'z',
                          u'и': u'i',
                          u'й': u'y',
                          u'к': u'k',
                          u'л': u'l',
                          u'м': u'm',
                          u'н': u'n',
                          u'о': u'o',
                          u'п': u'p',
                          u'р': u'r',
                          u'с': u's',
                          u'т': u't',
                          u'у': u'u',
                          u'ф': u'f',
                          u'х': u'h',
                          u'ц': u'ts',
                          u'ч': u'ch',
                          u'ш': u'sh',
                          u'щ': u'sch',
                          u'ъ': u'',
                          u'ы': u'y',
                          u'ь': u'',
                          u'э': u'e',
                          u'ю': u'yu',
                          u'я': u'ya', }

    translit_string = ""

    for index, char in enumerate(string):
        if char in lower_case_letters.keys():
            char = lower_case_letters[char]
        elif char in capital_letters.keys():
            char = capital_letters[char]
            if len(string) > index + 1:
                if string[index + 1] not in lower_case_letters.keys():
                    char = char.upper()
            else:
                char = char.upper()
        translit_string += char

    return translit_string


def take_snapshot():
    cap = cv2.VideoCapture(0)
    ret, frame = "", ""
    for i in range(5):
        ret, frame = cap.read()
    return frame


def get_face_from_image(image):
    face_locations = face_recognition.face_locations(image)

    if len(face_locations) == 1:
        for face_location in face_locations:
            top, right, bottom, left = face_location

            face_image = image[top:bottom, left:right]
            pil_image = Image.fromarray(face_image)
            return pil_image
    else:
        raise Exception


def quickly_recognize_faces(data):
    video_capture = cv2.VideoCapture(0)

    known_face_encodings = []
    known_face_names = []

    for i in data:
        img = face_recognition.load_image_file(i[2])
        face_encoding = face_recognition.face_encodings(img)[0]
        known_face_encodings.append(face_encoding)
        known_face_names.append(transliterate(i[0] + " " + i[1]))

    # Initialize some variables
    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True

    while True:
        # Grab a single frame of video
        ret, frame = video_capture.read()

        # Resize frame of video to 1/4 size for faster
        # face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Convert the image from BGR color (which OpenCV uses)
        # to RGB color (which face_recognition uses)
        rgb_small_frame = small_frame[:, :, ::-1]

        # Only process every other frame of video to save time
        if process_this_frame:
            # Find all the faces and face encodings in the
            # current frame of video
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(
                rgb_small_frame, face_locations)

            face_names = []
            for face_encoding in face_encodings:
                # See if the face is a match for the known face(s)
                matches = face_recognition.compare_faces(
                    known_face_encodings, face_encoding)
                name = "Unknown"

                # # If a match was found in known_face_encodings,
                # just use the first one.
                # if True in matches:
                #     first_match_index = matches.index(True)
                #     name = known_face_names[first_match_index]

                # Or instead, use the known face with the smallest
                # distance to the new face
                face_distances = face_recognition.face_distance(
                    known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]

                face_names.append(name)

        process_this_frame = not process_this_frame

        # Display the results
        for (top, right, bottom, left), name in zip(face_locations,
                                                    face_names):
            # Scale back up face locations since the frame we detected
            # in was scaled to 1/4 size
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 35),
                          (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6),
                        font, 1.0, (255, 255, 255), 1)

        # Display the resulting image
        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    # Release handle to the webcam
    video_capture.release()
    cv2.destroyWindow('Video')


def slowly_recognize_faces(data):
    video_capture = cv2.VideoCapture(0)

    known_face_encodings = []
    known_face_names = []

    for i in data:
        img = face_recognition.load_image_file(i[2])
        face_encoding = face_recognition.face_encodings(img)[0]
        known_face_encodings.append(face_encoding)
        known_face_names.append(transliterate(i[0] + " " + i[1]))

    while True:
        # Grab a single frame of video
        ret, frame = video_capture.read()

        # Convert the image from BGR color (which OpenCV uses) to RGB
        # color (which face_recognition uses)
        rgb_frame = frame[:, :, ::-1]

        # Find all the faces and face enqcodings in the frame of video
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(
            rgb_frame, face_locations)

        # Loop through each face in this frame of video
        for (top, right, bottom, left), face_encoding in zip(face_locations,
                                                             face_encodings):
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(
                known_face_encodings, face_encoding)

            name = "Unknown"

            # If a match was found in known_face_encodings,
            # just use the first one.
            # if True in matches:
            #     first_match_index = matches.index(True)
            #     name = known_face_names[first_match_index]

            # Or instead, use the known face with the smallest
            # distance to the new face
            face_distances = face_recognition.face_distance(
                known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 35),
                          (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6),
                        font, 1.0, (255, 255, 255), 1)

        # Display the resulting image
        cv2.imshow('Video', frame)

        # Hit 'q' on the keyboard to quit!
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # Release handle to the webcam
    video_capture.release()
    cv2.destroyWindow("Video")


class SearchWindow(QtWidgets.QMainWindow, Ui_PeopleSearchWindow):
    def __init__(self, parent=None):
        super(SearchWindow, self).__init__(parent)
        self.setupUi(self)

        # Triggers
        self.search_button.clicked.connect(self.search)

        # Creating actions
        addPersonAction = QAction(QIcon(), "Добавить пользователя", self)
        addGroupAction = QAction(QIcon(), "Добавить группу", self)
        createCompanyAction = QAction(QIcon(), "Добавить компанию", self)
        deletePersonAction = QAction(QIcon(), "Удалить пользователя", self)
        deleteCompanyAction = QAction(QIcon(), "Удалить компанию", self)
        deleteGroupAction = QAction(QIcon(), "Удалить группу", self)
        personChangeAction = QAction(QIcon(), "Изменить пользователя", self)
        startFaceRecognitionAction = QAction(
            QIcon(), "Начать распознавание", self)

        # Creating triggers
        addPersonAction.triggered.connect(self.open_person_addition_window)
        createCompanyAction.triggered.connect(
            self.open_company_creation_window)
        addGroupAction.triggered.connect(self.open_group_addition_window)
        deletePersonAction.triggered.connect(self.open_person_deletion_window)
        deleteCompanyAction.triggered.connect(
            self.open_company_deletion_window)
        deleteGroupAction.triggered.connect(self.open_group_deletion_window)
        personChangeAction.triggered.connect(self.open_person_change_window)
        startFaceRecognitionAction.triggered.connect(
            self.open_face_recognition_window)

        # Adding actions to the menubar
        additionMenu = self.menubar.addMenu("Добавить")
        additionMenu.addAction(addPersonAction)
        additionMenu.addAction(createCompanyAction)
        additionMenu.addAction(addGroupAction)
        changeMenu = self.menubar.addMenu("Изменить")
        changeMenu.addAction(personChangeAction)
        deletionMenu = self.menubar.addMenu("Удалить")
        deletionMenu.addAction(deletePersonAction)
        deletionMenu.addAction(deleteCompanyAction)
        deletionMenu.addAction(deleteGroupAction)
        recognitionMenu = self.menubar.addMenu("Распознавание")
        recognitionMenu.addAction(startFaceRecognitionAction)

    def search(self):
        result = cur.execute("""SELECT p.first_name, p.last_name,
                                            p.picture, c.name, g.name
                                     FROM people as p
                                     LEFT JOIN companies as c
                                     ON p.company = c.id
                                     LEFT JOIN groups as g
                                     ON p.group_id = g.id
                                     WHERE p.first_name = ?
                                     AND p.last_name = ?""",
                             (self.first_name_line.text(),
                              self.last_name_line.text(),))
        result = [i for i in result]
        if len(result) > 1:
            global first_name, last_name
            first_name = self.first_name_line.text()
            last_name = self.last_name_line.text()
            choosePerson = ChoosePersonWindow(self)
            choosePerson.show()
        elif result != []:
            self.update_data(*result[0])
        else:
            show_alert(self, "Такого пользователя не существует", False)

    def update_data(self, f_name, l_name, p_name, c_name, g_name):
        if c_name == None:
            c_name = "-"
        if g_name == None:
            g_name = "-"
        self.name_label.setText("Имя: " + f_name + " " + l_name)
        self.company_label.setText("Компания: " + c_name)
        self.group_label.setText("Группа: " + g_name)
        pixmap = QtGui.QPixmap(p_name)
        self.picture_label.setPixmap(pixmap.scaled(self.picture_label.size(),
                                                   Qt.KeepAspectRatio,
                                                   Qt.SmoothTransformation))
        self.repaint()

    def open_person_addition_window(self):
        addPerson = AddPersonWindow(self)
        addPerson.show()

    def open_company_creation_window(self):
        createCompany = CreateCompanyWindow(self)
        createCompany.show()

    def open_group_addition_window(self):
        addGroup = AddGroupWindow(self)
        addGroup.show()

    def open_person_deletion_window(self):
        deletePerson = DeletePersonWindow(self)
        deletePerson.show()

    def open_company_deletion_window(self):
        deleteCompany = DeleteCompanyWindow(self)
        deleteCompany.show()

    def open_group_deletion_window(self):
        deleteGroup = DeleteGroupWindow(self)
        deleteGroup.show()

    def open_person_change_window(self):
        changePerson = ChoosePersonToChangeWindow(self)
        changePerson.show()

    def open_face_recognition_window(self):
        faceRecognition = StartFaceRecognitionWindow(self)
        faceRecognition.show()


class AddPersonWindow(QtWidgets.QMainWindow, Ui_AddPerson):
    def __init__(self, parent=None):
        super(AddPersonWindow, self).__init__(parent)
        self.setupUi(self)

        # Creating triggers
        self.add_person_button.clicked.connect(self.add_person)
        self.open_image.clicked.connect(self.choose_picture)
        self.take_snapshot_button.clicked.connect(self.take_webcam_snapshot)

        # Setting up UI
        self.companies = [i for i in cur.execute(
            """SELECT * FROM companies ORDER BY id""")]
        self.companies_box.currentTextChanged.connect(self.on_combobox_changed)
        self.companies_box.clear()
        for company in self.companies:
            self.companies_box.addItem(company[1])

    def add_person(self):
        if self.picture_line.text() != "" and\
           self.first_name_line.text() != "" and\
           self.last_name_line.text() != "" and\
           self.companies_box.currentIndex() != -1 and\
           self.groups_box.currentIndex() != -1:
            # Creating picture
            if self.picture_line.text() != "images/temp.jpg":
                img = get_face_from_image(imread(self.picture_line.text()))
            else:
                img = Image.open("images/temp.jpg")
            pic_name = "images/" + secrets.token_hex(16) + ".png"
            img.save(pic_name)

            company_id = self.companies[self.companies_box.currentIndex()][0]
            result = cur.execute("""SELECT id
                                    FROM groups
                                    WHERE name = ?
                                    AND company_id = ?""",
                                 (self.groups_box.currentText(), company_id,))
            group_id = [i[0] for i in result][0]

            # Adding person to the database
            cur.execute("""INSERT INTO people (first_name, last_name,
                                               company, picture, group_id)
                            VALUES (?, ?, ?, ?, ?)""",
                        (self.first_name_line.text(),
                         self.last_name_line.text(),
                         company_id, pic_name, group_id,))
            conn.commit()
            show_alert(self, "Пользователь был успешно добавлен", True)
            self.close()
        else:
            show_alert(self, "Пожалуйста заполните все поля", False)

    def on_combobox_changed(self, value):
        cur_index = self.companies_box.currentIndex()
        res = cur.execute("""SELECT name
                             FROM groups
                             WHERE company_id = ?
                             ORDER BY id""",
                          (self.companies[cur_index][0],))
        self.groups_box.clear()
        self.groups_box.addItems([i[0] for i in res])

    def take_webcam_snapshot(self):
        try:
            cv2_im = cv2.cvtColor(take_snapshot(), cv2.COLOR_BGR2RGB)
            try:
                img = get_face_from_image(cv2_im)
                img.save("images/temp.jpg")
                qt_image = ImageQt(img)
                pixmap = QtGui.QPixmap.fromImage(qt_image)
                self.picture_label.setPixmap(pixmap.scaled(
                                             self.picture_label.size(),
                                             Qt.KeepAspectRatio,
                                             Qt.SmoothTransformation))
                self.picture_line.setText("images/temp.jpg")
                self.picture_label.repaint()
                self.picture_line.repaint()
            except Exception:
                self.picture_line.setText(" ")
                show_alert(
                    self, "Лицо не найдено. Сделайте новую фотографию", False)
        except Exception:
            show_alert(self, "Не найдено подключенных камер", False)

    def choose_picture(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        params = ("Выбрать фотографию", "", "Images (*.png, *.jpg)")
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, *params,
                                                            options=options)
        if fileName:
            self.picture_line.setText(fileName)
            get_face_from_image(imread(fileName)).save("images/temp.jpg")
            pixmap = QtGui.QPixmap("images/temp.jpg")
            self.picture_label.setPixmap(pixmap.scaled(
                self.picture_label.size(), Qt.KeepAspectRatio,
                Qt.SmoothTransformation))
            self.picture_label.repaint()


class CreateCompanyWindow(QtWidgets.QMainWindow, Ui_CreateCompanyWindow):
    def __init__(self, parent=None):
        super(CreateCompanyWindow, self).__init__(parent)
        self.setupUi(self)

        # Creating triggers
        self.create_company_button.clicked.connect(self.create_company)

    def create_company(self):
        # Check if there is a company with the given name
        res = cur.execute("""SELECT * FROM companies WHERE name = ?""",
                          (self.company_name_line.text(),))

        if [i for i in res] == []:
            # Add the company to the database
            res = cur.execute("""INSERT INTO companies (name)
                                 VALUES (?)""",
                              (self.company_name_line.text(),))
            conn.commit()
            show_alert(self, "Компания была успешно добавлена", True)
            self.close()
        else:
            show_alert(
                self, 'Компания с данным названием уже существует', False)


class AddGroupWindow(QtWidgets.QMainWindow, Ui_AddGroupWindow):
    def __init__(self, parent=None):
        super(AddGroupWindow, self).__init__(parent)
        self.setupUi(self)

        # Creating triggers
        self.add_group_button.clicked.connect(self.add_group)

        # Showing companies in comboBox
        self.companies = [i for i in cur.execute(
            """SELECT * FROM companies ORDER BY id""")]
        for company in self.companies:
            self.companies_box.addItem(company[1])

    def add_group(self):
        # Check if there is a group with the given name
        cur_index = self.companies_box.currentIndex()
        res = cur.execute("""SELECT *
                             FROM groups
                             WHERE name = ?
                             AND company_id = ?""",
                          (self.group_name_line.text(),
                           self.companies[cur_index][0],))
        if [i for i in res] == []:
            # Adding group to the company
            cur.execute("""INSERT INTO groups (company_id, name)
                           VALUES (?, ?)""",
                        (self.companies[self.companies_box.currentIndex()][0],
                         self.group_name_line.text(),))
            conn.commit()
            show_alert(self, "Группа была успешно добавлена", True)
            self.close()
        else:
            show_alert(self, "Группа с таким названием уже существует", False)


class ChoosePersonWindow(QtWidgets.QMainWindow, Ui_ChoosePersonWindow):
    def __init__(self, parent=None):
        super(ChoosePersonWindow, self).__init__(parent)
        self.setupUi(self)

        self.choose_person_button.clicked.connect(self.show_person)
        self.parent = parent

        result = cur.execute("""SELECT p.first_name, p.last_name,
                                            p.picture, c.name, g.name
                                     FROM people as p
                                     LEFT JOIN companies as c
                                     ON p.company = c.id
                                     LEFT JOIN groups as g
                                     ON p.group_id = g.id
                                     WHERE p.first_name = ?
                                     AND p.last_name = ?""",
                             (first_name, last_name,))
        self.people = [i for i in result]

        for person in self.people:
            item = QtWidgets.QListWidgetItem()
            icon = QIcon()
            icon.addPixmap(QtGui.QPixmap(person[2]))
            item.setIcon(icon)
            item.setText(f"{person[0]} {person[1]} {person[3]} {person[4]}")
            self.listWidget.setIconSize(QtCore.QSize(30, 30))
            self.listWidget.addItem(item)

        self.listWidget.setCurrentRow(0)

    def show_person(self):
        self.parent.update_data(*self.people[self.listWidget.currentRow()])
        self.close()


class DeletePersonWindow(QtWidgets.QMainWindow, Ui_DeletePersonWindow):
    def __init__(self, parent=None):
        super(DeletePersonWindow, self).__init__(parent)
        self.setupUi(self)

        self.delete_person_button.clicked.connect(self.delete_person)

    def delete_person(self):
        if self.first_name_line.text() != "" and\
                self.last_name_line.text() != "":
            # Check if there is more than 1 person with the given name
            result = cur.execute("""SELECT id, picture
                                    FROM people
                                    WHERE first_name = ?
                                    AND last_name = ?""",
                                 (self.first_name_line.text(),
                                  self.last_name_line.text(),))
            people = [i for i in result]
            if len(people) > 1:
                global first_name, last_name
                first_name = self.first_name_line.text()
                last_name = self.last_name_line.text()
                person_deletion = ChoosePersonForDeletionWindow(self)
                person_deletion.show()
            elif len(people) == 0:
                show_alert(self, "Такого пользователя не существует", False)
            else:
                cur.execute("DELETE FROM people WHERE id = ?", (people[0][0],))
                conn.commit()
                os.remove(people[0][1])
                self.close()
                show_alert(self, "Пользователь был успешно удален", True)


class ChoosePersonForDeletionWindow(QtWidgets.QMainWindow,
                                    Ui_ChoosePersonWindow):
    def __init__(self, parent=None):
        super(ChoosePersonForDeletionWindow, self).__init__(parent)
        self.setupUi(self)

        self.choose_person_button.setText("Удалить")
        self.choose_person_button.clicked.connect(self.delete_person)
        self.parent = parent

        # Getting all people with the given name
        result = cur.execute("""SELECT p.first_name, p.last_name,
                                       p.picture, c.name, g.name, p.id
                                FROM people as p
                                LEFT JOIN companies as c
                                ON p.company = c.id
                                LEFT JOIN groups as g
                                ON p.group_id = g.id
                                WHERE p.first_name = ?
                                AND p.last_name = ?""",
                             (first_name, last_name,))
        self.people = [i for i in result]

        for person in self.people:
            item = QtWidgets.QListWidgetItem()
            icon = QIcon()
            icon.addPixmap(QtGui.QPixmap(person[2]))
            item.setIcon(icon)
            item.setText(f"{person[0]} {person[1]} {person[3]} {person[4]}")
            self.listWidget.setIconSize(QtCore.QSize(30, 30))
            self.listWidget.addItem(item)

        self.listWidget.setCurrentRow(0)

    def delete_person(self):
        cur.execute("""DELETE FROM people WHERE id = ?""",
                    (self.people[self.listWidget.currentRow()][5],))
        conn.commit()
        os.remove(self.people[self.listWidget.currentRow()][2])
        self.close()
        self.parent.close()
        show_alert(self, "Пользователь был успешно удален", True)


class DeleteCompanyWindow(QtWidgets.QMainWindow, Ui_DeleteCompanyWindow):
    def __init__(self, parent=None):
        super(DeleteCompanyWindow, self).__init__(parent)
        self.setupUi(self)

        self.delete_company_button.clicked.connect(self.delete_company)

        # Getting all companies
        result = cur.execute("SELECT * FROM companies ORDER BY id")
        self.companies = [i for i in result]

        for company in self.companies:
            self.comboBox.addItem(company[1])

    def delete_company(self):
        company_id, _ = self.companies[self.comboBox.currentIndex()]
        cur.execute("""UPDATE people
                       SET company = 0
                       WHERE company = ?""", (company_id,))
        cur.execute("DELETE FROM companies WHERE id = ?", (company_id,))
        cur.execute("DELETE FROM groups WHERE company_id = ?", (company_id,))
        conn.commit()
        self.close()
        show_alert(self, "Компания была успешно удалена", True)


class DeleteGroupWindow(QtWidgets.QMainWindow, Ui_DeleteGroupWindow):
    def __init__(self, parent=None):
        super(DeleteGroupWindow, self).__init__(parent)
        self.setupUi(self)

        self.delete_group_button.clicked.connect(self.delete_group)

        self.companies = [i for i in cur.execute(
            """SELECT * FROM companies ORDER BY id""")]
        self.companies_box.currentTextChanged.connect(self.on_combobox_changed)
        self.companies_box.clear()
        for company in self.companies:
            self.companies_box.addItem(company[1])

    def on_combobox_changed(self, value):
        cur_index = self.companies_box.currentIndex()
        res = cur.execute("""SELECT name
                             FROM groups
                             WHERE company_id = ?
                             ORDER BY id""",
                          (self.companies[cur_index][0],))
        self.groups_box.clear()
        self.groups_box.addItems([i[0] for i in res])

    def delete_group(self):
        cur.execute("""UPDATE people
                       SET group_id = 0
                       WHERE group_id=(SELECT id
                                       FROM groups
                                       WHERE name = ? AND company_id = ?)""",
                    (self.groups_box.currentText(),
                     self.companies[self.groups_box.currentIndex()][0]))
        cur.execute("DELETE FROM groups WHERE name = ? AND company_id = ?",
                    (self.groups_box.currentText(),
                     self.companies[self.groups_box.currentIndex()][0]))
        conn.commit()
        self.close()
        show_alert(self, "Группа была успешно удалена", True)


class ChangePersonWindow(QtWidgets.QMainWindow, Ui_ChangePersonWindow):
    def __init__(self, parent=None):
        super(ChangePersonWindow, self).__init__(parent)
        self.setupUi(self)

        self.first_name_line.setText(first_name)
        self.last_name_line.setText(last_name)

        self.companies = [i for i in cur.execute(
            """SELECT * FROM companies ORDER BY id""")]
        self.companies_box.currentTextChanged.connect(self.on_combobox_changed)
        self.companies_box.clear()
        for company in self.companies:
            self.companies_box.addItem(company[1])
        self.companies_box.setCurrentText(company_)
        self.groups_box.setCurrentText(group_)

        self.save_button.clicked.connect(self.save_person_info)

    def on_combobox_changed(self, value):
        cur_index = self.companies_box.currentIndex()
        res = cur.execute("""SELECT name
                             FROM groups
                             WHERE company_id = ?
                             ORDER BY id""",
                          (self.companies[cur_index][0],))
        self.groups_box.clear()
        self.groups_box.addItems([i[0] for i in res])

    def save_person_info(self):
        groups_cur = self.groups_box.currentText()
        companies_cur = self.companies_box.currentText()
        company_id = [i for i in cur.execute("""SELECT id
                                                FROM companies
                                                WHERE name = ?""",
                                             (companies_cur,))][0][0]
        group_id = [i for i in cur.execute("""SELECT id
                                              FROM groups
                                              WHERE company_id = ?
                                              AND name = ?""",
                                           (company_id,
                                            groups_cur,))][0][0]
        cur.execute("""UPDATE people
                       SET group_id = ?, company = ?
                       WHERE id = ?""", (group_id, company_id, person_id))
        conn.commit()
        self.close()
        show_alert(self, "Данные были успешно сохранены", True)


class ChoosePersonToChangeWindow(QtWidgets.QMainWindow,
                                 Ui_ChoosePersonToChangeWindow):
    def __init__(self, parent=None):
        super(ChoosePersonToChangeWindow, self).__init__(parent)
        self.setupUi(self)

        self.change_button.clicked.connect(self.change_person)

    def change_person(self):
        if self.first_name_line.text() != "" and\
                self.last_name_line.text() != "":
            global company_, group_, person_id, first_name, last_name
            result = cur.execute("""SELECT *
                                    FROM people
                                    WHERE first_name = ?
                                    AND last_name = ?""",
                                 (self.first_name_line.text(),
                                  self.last_name_line.text(),))
            people = [i for i in result]
            if len(people) == 0:
                show_alert(self, "Такого пользователя не существует", False)
            elif len(people) == 1:
                company_ = [i for i in cur.execute("""SELECT name
                                                      FROM companies AS c
                                                      LEFT JOIN people AS p
                                                      ON c.id = p.company
                                                      WHERE p.id = ?""",
                                                   (people[0][0],))][0][0]
                group_ = [i for i in cur.execute("""SELECT name
                                                    FROM groups AS g
                                                    LEFT JOIN people AS p
                                                    ON g.id = p.group_id
                                                    WHERE p.id = ?""",
                                                 (people[0][0],))][0][0]
                person_id = people[0][0]
                first_name = self.first_name_line.text()
                last_name = self.last_name_line.text()
                changePerson = ChangePersonWindow(self)
                changePerson.show()
                self.close()
            elif len(people) > 1:
                # global first_name, last_name
                first_name = self.first_name_line.text()
                last_name = self.last_name_line.text()
                personSelectionWindow = PersonSelectionToChangeWindow(self)
                personSelectionWindow.show()
        else:
            show_alert(self, "Пожалуйста заполните все поля", False)


class PersonSelectionToChangeWindow(QtWidgets.QMainWindow,
                                    Ui_ChoosePersonWindow):
    def __init__(self, parent=None):
        super(PersonSelectionToChangeWindow, self).__init__(parent)
        self.setupUi(self)

        self.choose_person_button.setText("Изменить")
        self.choose_person_button.clicked.connect(self.change_person)
        self.parent = parent

        # Getting all people with the given name
        result = cur.execute("""SELECT p.first_name, p.last_name,
                                       p.picture, c.name, g.name, p.id
                                FROM people as p
                                LEFT JOIN companies as c
                                ON p.company = c.id
                                LEFT JOIN groups as g
                                ON p.group_id = g.id
                                WHERE p.first_name = ?
                                AND p.last_name = ?""",
                             (first_name, last_name,))
        self.people = [i for i in result]

        for person in self.people:
            item = QtWidgets.QListWidgetItem()
            icon = QIcon()
            icon.addPixmap(QtGui.QPixmap(person[2]))
            item.setIcon(icon)
            item.setText(f"{person[0]} {person[1]} {person[3]} {person[4]}")
            self.listWidget.setIconSize(QtCore.QSize(30, 30))
            self.listWidget.addItem(item)

        self.listWidget.setCurrentRow(0)

    def change_person(self):
        global company_, group_, person_id
        person_id = self.people[self.listWidget.currentRow()][5]
        company_, group_ = [i for i in cur.execute("""SELECT c.name, g.name
                                                      FROM people AS p
                                                      LEFT JOIN groups AS g
                                                      ON p.group_id = g.id
                                                      LEFT JOIN companies AS c
                                                      ON p.company = c.id
                                                      WHERE p.id = ?""",
                                                   (person_id,))][0]
        self.parent.close()
        self.close()
        changePerson = ChangePersonWindow(self)
        changePerson.show()


class StartFaceRecognitionWindow(QtWidgets.QMainWindow,
                                 Ui_StartFaceRecognitionWindow):
    def __init__(self, parent=None):
        super(StartFaceRecognitionWindow, self).__init__(parent)
        self.setupUi(self)

        self.companies = [i for i in cur.execute(
            """SELECT * FROM companies ORDER BY id""")]
        self.companies_box.currentTextChanged.connect(self.on_combobox_changed)
        self.companies_box.clear()
        for company in self.companies:
            self.companies_box.addItem(company[1])

        self.speed_box.addItems(["Быстро", "Медленно"])

        self.start_button.clicked.connect(self.start_face_recognition)

    def on_combobox_changed(self, value):
        cur_index = self.companies_box.currentIndex()
        res = cur.execute("""SELECT name
                             FROM groups
                             WHERE company_id = ?
                             ORDER BY id""",
                          (self.companies[cur_index][0],))
        self.groups_box.clear()
        self.groups_box.addItems([i[0] for i in res])

    def start_face_recognition(self):
        company_id = self.companies[self.companies_box.currentIndex()][0]
        group_id = [i for i in cur.execute("""SELECT id
                                              FROM groups
                                              WHERE company_id = ?""",
                                           (company_id,))][0][0]
        people = [i for i in cur.execute("""SELECT first_name, last_name,
                                                   picture
                                            FROM people
                                            WHERE company = ?
                                            AND group_id = ?""",
                                         (company_id, group_id,))]
        if self.speed_box.currentIndex() == 0:
            try:
                quickly_recognize_faces(people)
            except Exception:
                show_alert(self, "Не найдено подключенных камер", False)
        elif self.speed_box.currentIndex() == 1:
            try:
                slowly_recognize_faces(people)
            except Exception:
                show_alert(self, "Не найдено подключенных камер", False)


class AlertWindow(QtWidgets.QMainWindow, Ui_Alert):
    def __init__(self, parent=None):
        super(AlertWindow, self).__init__(parent)
        self.setupUi(self)

        self.alert_label.setText(alert_text)

        self.ok_button.clicked.connect(self.close)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    search_window = SearchWindow()
    search_window.show()
    app.exec_()
