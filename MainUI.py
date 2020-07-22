from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime
from imaging.employee_dao import Employee_Dao
from imaging.in_out_time_dao import InOutTime_Dao
from imaging.model.base import session_factory
from imaging.model.in_out_time import InOutTime
from tester import listUserInfoFunction
import faceRecognition as fr
import cv2


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1084, 869)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.objMain = QtWidgets.QTabWidget(self.centralwidget)
        self.objMain.setGeometry(QtCore.QRect(0, 0, 1081, 831))
        self.objMain.setToolTip("")
        self.objMain.setObjectName("objMain")
        self.tabAuthOut = QtWidgets.QWidget()
        self.tabAuthOut.setObjectName("tabAuthOut")
        self.lblAuthWebcamScreenOut = QtWidgets.QLabel(self.tabAuthOut)
        self.lblAuthWebcamScreenOut.setGeometry(QtCore.QRect(160, 30, 761, 571))
        self.lblAuthWebcamScreenOut.setFrameShape(QtWidgets.QFrame.Box)
        self.lblAuthWebcamScreenOut.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lblAuthWebcamScreenOut.setLineWidth(5)
        self.lblAuthWebcamScreenOut.setText("")
        self.lblAuthWebcamScreenOut.setObjectName("lblAuthWebcamScreenOut")
        self.btnWebcamOut = QtWidgets.QPushButton(self.tabAuthOut)
        self.btnWebcamOut.setGeometry(QtCore.QRect(460, 640, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(13)
        self.btnWebcamOut.setFont(font)
        self.btnWebcamOut.setObjectName("btnWebcamOut")
        self.btnExitAuthOut = QtWidgets.QPushButton(self.tabAuthOut)
        self.btnExitAuthOut.setGeometry(QtCore.QRect(890, 740, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.btnExitAuthOut.setFont(font)
        self.btnExitAuthOut.setObjectName("btnExitAuthOut")
        self.objMain.addTab(self.tabAuthOut, "")
        self.tabAuthIn = QtWidgets.QWidget()
        self.tabAuthIn.setObjectName("tabAuthIn")
        self.lblAuthWebcamScreen = QtWidgets.QLabel(self.tabAuthIn)
        self.lblAuthWebcamScreen.setGeometry(QtCore.QRect(160, 30, 761, 571))
        self.lblAuthWebcamScreen.setFrameShape(QtWidgets.QFrame.Box)
        self.lblAuthWebcamScreen.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lblAuthWebcamScreen.setLineWidth(5)
        self.lblAuthWebcamScreen.setText("")
        self.lblAuthWebcamScreen.setObjectName("lblAuthWebcamScreen")
        self.btnWebcamIn = QtWidgets.QPushButton(self.tabAuthIn)
        self.btnWebcamIn.setGeometry(QtCore.QRect(460, 640, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(13)
        self.btnWebcamIn.setFont(font)
        self.btnWebcamIn.setObjectName("btnWebcamIn")
        self.btnExitAuthIn = QtWidgets.QPushButton(self.tabAuthIn)
        self.btnExitAuthIn.setGeometry(QtCore.QRect(890, 740, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.btnExitAuthIn.setFont(font)
        self.btnExitAuthIn.setObjectName("btnExitAuthIn")
        self.objMain.addTab(self.tabAuthIn, "")
        self.tabSetup = QtWidgets.QWidget()
        self.tabSetup.setObjectName("tabSetup")
        self.txtUserMessages = QtWidgets.QTextBrowser(self.tabSetup)
        self.txtUserMessages.setGeometry(QtCore.QRect(160, 10, 731, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.txtUserMessages.setFont(font)
        self.txtUserMessages.setFrameShape(QtWidgets.QFrame.Box)
        self.txtUserMessages.setFrameShadow(QtWidgets.QFrame.Raised)
        self.txtUserMessages.setLineWidth(3)
        self.txtUserMessages.setObjectName("txtUserMessages")
        self.lblWebcamScreen = QtWidgets.QLabel(self.tabSetup)
        self.lblWebcamScreen.setGeometry(QtCore.QRect(150, 70, 751, 511))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.lblWebcamScreen.setFont(font)
        self.lblWebcamScreen.setFrameShape(QtWidgets.QFrame.Box)
        self.lblWebcamScreen.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lblWebcamScreen.setLineWidth(5)
        self.lblWebcamScreen.setText("")
        self.lblWebcamScreen.setObjectName("lblWebcamScreen")
        self.btnStartWebcam = QtWidgets.QPushButton(self.tabSetup)
        self.btnStartWebcam.setGeometry(QtCore.QRect(270, 590, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.btnStartWebcam.setFont(font)
        self.btnStartWebcam.setObjectName("btnStartWebcam")
        self.btnCaptureImage = QtWidgets.QPushButton(self.tabSetup)
        self.btnCaptureImage.setGeometry(QtCore.QRect(640, 590, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.btnCaptureImage.setFont(font)
        self.btnCaptureImage.setObjectName("btnCaptureImage")
        self.lblUserName = QtWidgets.QLabel(self.tabSetup)
        self.lblUserName.setGeometry(QtCore.QRect(160, 650, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.lblUserName.setFont(font)
        self.lblUserName.setObjectName("lblUserName")
        self.lblUserCode = QtWidgets.QLabel(self.tabSetup)
        self.lblUserCode.setGeometry(QtCore.QRect(160, 690, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.lblUserCode.setFont(font)
        self.lblUserCode.setObjectName("lblUserCode")
        self.txtBoxUserName = QtWidgets.QLineEdit(self.tabSetup)
        self.txtBoxUserName.setGeometry(QtCore.QRect(280, 650, 461, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.txtBoxUserName.setFont(font)
        self.txtBoxUserName.setObjectName("txtBoxUserName")
        self.txtBoxUserCode = QtWidgets.QLineEdit(self.tabSetup)
        self.txtBoxUserCode.setGeometry(QtCore.QRect(280, 690, 461, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.txtBoxUserCode.setFont(font)
        self.txtBoxUserCode.setObjectName("txtBoxUserCode")
        self.btnSave = QtWidgets.QPushButton(self.tabSetup)
        self.btnSave.setGeometry(QtCore.QRect(450, 730, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(13)
        self.btnSave.setFont(font)
        self.btnSave.setObjectName("btnSave")
        self.btnCancel = QtWidgets.QPushButton(self.tabSetup)
        self.btnCancel.setGeometry(QtCore.QRect(890, 740, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.btnCancel.setFont(font)
        self.btnCancel.setObjectName("btnCancel")
        self.objMain.addTab(self.tabSetup, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1084, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.objMain.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # For setup tab
        self.txtUserMessages.setText('Kindly Press "Start Webcam" Button To Connect With Webcam.')
        self.btnCancel.clicked.connect(self.loadcancelmode)
        self.btnStartWebcam.clicked.connect(self.loadstartwebcammode)
        self.btnCaptureImage.clicked.connect(self.loadCapturedImageMode)
        self.btnSave.clicked.connect(self.loadsaveUserInfo)
        self.btnSave.setEnabled(False)
        self.btnCaptureImage.setEnabled(False)

        # For Authentication In tab
        self.btnWebcamIn.clicked.connect(self.WebcamActivity)
        self.btnExitAuthIn.clicked.connect(self.loadExitAuthInMode)

        # For Authentication Out tab
        self.btnWebcamOut.clicked.connect(self.WebcamActivityOut)
        self.btnExitAuthOut.clicked.connect(self.loadExitAuthOutMode)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Home Window"))
        self.btnWebcamOut.setText(_translate("MainWindow", "Start Webcam"))
        self.btnExitAuthOut.setToolTip(_translate("MainWindow", "Exit application"))
        self.btnExitAuthOut.setText(_translate("MainWindow", "Exit"))
        self.objMain.setTabText(self.objMain.indexOf(self.tabAuthOut),
                                _translate("MainWindow", "Authentication Out Time"))
        self.btnWebcamIn.setText(_translate("MainWindow", "Start Webcam"))
        self.btnExitAuthIn.setToolTip(_translate("MainWindow", "Exit application"))
        self.btnExitAuthIn.setText(_translate("MainWindow", "Exit"))
        self.objMain.setTabText(self.objMain.indexOf(self.tabAuthIn),
                                _translate("MainWindow", "Authentication In Time"))
        self.txtUserMessages.setToolTip(_translate("MainWindow", "Prompt user messages"))
        self.btnStartWebcam.setToolTip(_translate("MainWindow", "Connect to webcam"))
        self.btnStartWebcam.setText(_translate("MainWindow", "Start Webcam"))
        self.btnCaptureImage.setToolTip(_translate("MainWindow", "Capture images from webcam video"))
        self.btnCaptureImage.setText(_translate("MainWindow", "Capture Image"))
        self.lblUserName.setText(_translate("MainWindow", "User Name"))
        self.lblUserCode.setText(_translate("MainWindow", "User Code"))
        self.btnSave.setToolTip(_translate("MainWindow", "Save the user info"))
        self.btnSave.setText(_translate("MainWindow", "Save"))
        self.btnCancel.setToolTip(_translate("MainWindow", "Exit application"))
        self.btnCancel.setText(_translate("MainWindow", "Exit"))
        self.objMain.setTabText(self.objMain.indexOf(self.tabSetup), _translate("MainWindow", "Setup"))

    #  ************************************* For Setup Tab ******************************************* #

    global text
    text = ["Please Look left", "Please Look right", "Please Look Up",
            "Please Look 45 degree right", "Please Look 45 degree left", "Please Look 45 degree Up",
            "Please Look Straight", "Please E-Smile",
            "Please Look Straight", "Please Bigger E-Smile", "Please Make your eyes bigger", "Please E-Smile"]

    def loadstartwebcammode(self):
        self.btnStartWebcam.setEnabled(False)
        self.btnSave.setEnabled(True)
        self.btnCaptureImage.setEnabled(True)
        self.tabAuthIn.setEnabled(False)
        self.tabAuthOut.setEnabled(False)
        self.logic = 0
        self.value = 0
        img_counter = 1
        self.txtUserMessages.setText('Kindly Press "Capture Image" To take the image. '
                                     'Please Look straight')
        cap = cv2.VideoCapture(0)
        while True:
            while img_counter < 13:
                ret, frame = cap.read()
                self.displayImage(frame)
                cv2.waitKey()

                if self.logic == 2:
                    # self.value = self.value + 1
                    img_name = "Image_{}.png".format(img_counter)
                    cv2.imwrite(img_name, frame)
                    self.logic = 1
                    self.txtUserMessages.setText(text[img_counter - 1])
                    img_counter += 1
            cap.release()
            self.btnCaptureImage.setEnabled(False)
            self.txtUserMessages.setText('You have reached the limit. Kindly Press "Start Webcam" Button To '
                                         'Connect With Webcam.')
            break

    def displayImage(self, img):
        qformat = QImage.Format_Indexed8
        if len(img.shape) == 3:
            if (img.shape[2]) == 4:
                qformat = QImage.Format_RGBA888
            else:
                qformat = QImage.Format_RGB888
        img = QImage(img, img.shape[1], img.shape[0], qformat)
        img = img.rgbSwapped()
        self.lblWebcamScreen.setPixmap(QPixmap.fromImage(img))
        self.lblWebcamScreen.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

    def loadCapturedImageMode(self):
        self.logic = 2

    def loadsaveUserInfo(self):
        self.btnSave.setEnabled(False)
        self.btnStartWebcam.setEnabled(True)
        self.btnCaptureImage.setEnabled(False)
        self.tabAuthIn.setEnabled(True)
        self.tabAuthOut.setEnabled(True)
        self.lblWebcamScreen.clear()
        images_data = []
        lstCapturedImages = ["Image_1.png", "Image_2.png", "Image_3.png", "Image_4.png",
                             "Image_5.png", "Image_6.png", "Image_7.png", "Image_8.png",
                             "Image_9.png", "Image_10.png", "Image_11.png", "Image_12.png"]
        for name in lstCapturedImages:
            with open(name, 'rb') as file:
                binaryData = file.read()
                images_data.append(binaryData)
        user_info = {"Name": self.txtBoxUserName.text(), "EmpCode": self.txtBoxUserCode.text()}
        self.txtBoxUserName.clear()
        self.txtBoxUserCode.clear()
        success_message = listUserInfoFunction(user_info, images_data)
        # print(success_message)
        self.txtUserMessages.setText("Kindly Press 'Start Webcam' Button To Connect With Webcam.")
        if success_message:
            # print("Employee added successfully !")
            self.success_messagebox()

    def success_messagebox(self):
        success = QMessageBox()
        success.setWindowTitle('Saved !')
        success.setText('User Info has saved successfully.')
        success.setIcon(QMessageBox.Information)
        success.setStandardButtons(QMessageBox.Ok)
        success.setDefaultButton(QMessageBox.Ok)
        xy = success.exec_()

    def loadcancelmode(self):
        reply = QMessageBox()
        reply.setWindowTitle('Warning..')
        reply.setText('Are you sure you want to exit ?')
        reply.setIcon(QMessageBox.Warning)
        reply.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        reply.setDefaultButton(QMessageBox.No)
        x = reply.exec_()
        if x == QMessageBox.Yes:
            if cv2.VideoCapture(0):
                cap.release()
            MainWindow.close()
        else:
            reply.close()

    #  ****************************** For Authentication In Mode Tab ************************************ #

    def WebcamActivity(self):
        InFlag = 1
        if self.btnWebcamIn.text() == "Start Webcam":
            self.btnWebcamIn.setText("Stop Webcam")
            self.btnExitAuthIn.setEnabled(False)
            self.AuthorizationFunction1(InFlag)
        elif self.btnWebcamIn.text() == "Stop Webcam":
            self.btnWebcamIn.setText("Start Webcam")
            self.btnExitAuthIn.setEnabled(True)
            self.CloseWebcamIn()

    def AuthorizationFunction1(self, Flag):
        self.WebCamValue = 0
        if Flag == 1:
            self.tabSetup.setEnabled(False)
            self.tabAuthOut.setEnabled(False)
        else:
            self.tabSetup.setEnabled(False)
            self.tabAuthIn.setEnabled(False)

        # This module captures images via webcam and performs face recognition
        face_recognizer = cv2.face.LBPHFaceRecognizer_create()
        face_recognizer.read('trainingData.yml')  # Load saved training data

        session = session_factory()
        employee_dao = Employee_Dao()
        employees = employee_dao.query_records(session)
        name = {}
        for employee in employees:
            name[employee.id] = employee.name

        # print('Names in DB : ', name)
        counter = 1
        flag = 0
        global predicted_name, employeeId
        global test_img
        global cap
        cap = cv2.VideoCapture(0)

        while True:
            ret, test_img = cap.read()  # captures frame and returns boolean value and captured image
            self.displayImage_In(test_img, Flag)
            faces_detected, gray_img = fr.faceDetection(test_img)
            for (x, y, w, h) in faces_detected:
                cv2.rectangle(test_img, (x, y), (x + w, y + h), (255, 0, 0), thickness=5)

            cv2.waitKey(10)
            if self.WebCamValue == 1:
                self.WebCamValue = 2
                cap.release()
                if Flag == 1:
                    self.lblAuthWebcamScreen.clear()
                else:
                    self.lblAuthWebcamScreenOut.clear()
                break
            for face in faces_detected:
                if counter < 31:
                    (x, y, w, h) = face
                    roi_gray = gray_img[y:y + w, x:x + h]
                    label, confidence = face_recognizer.predict(roi_gray)  # predicting the label of given image
                    # print("confidence:", confidence)
                    # print("label:", label)
                    fr.draw_rect(test_img, face)
                    predicted_name = name[label]
                    employeeId = label
                    if confidence < 39:  # If confidence less than 37 then don't print predicted face text on screen
                        # fr.put_text(test_img, predicted_name, x, y)
                        # fr.put_text(test_img, str(confidence), x, y + h + 50)
                        flag = 1
                        counter += 1
                    elif confidence > 39:
                        counter += 1
                elif flag == 1:
                    cap.release()
                    flag = 0
                    counter = 1
                    if Flag == 1:
                        self.InInsertion(current_time, DateToday)
                    else:
                        self.OutInsertion(current_time, DateToday)
                    granted = QMessageBox()
                    granted.setWindowTitle('Granted !')
                    granted.setText('Authentication successful. Access granted.'
                                    ' Welcome : ' + predicted_name)
                    granted.setIcon(QMessageBox.Information)
                    granted.setStandardButtons(QMessageBox.Ok)
                    granted.setDefaultButton(QMessageBox.Ok)
                    xy = granted.exec_()
                    if xy == QMessageBox.Ok:
                        cap = cv2.VideoCapture(0)
                elif flag == 0:
                    cap.release()
                    counter = 1
                    granted = QMessageBox()
                    granted.setWindowTitle('Denied !')
                    granted.setText('Authentication unsuccessful. Access denied.')
                    granted.setIcon(QMessageBox.Question)
                    granted.setStandardButtons(QMessageBox.Ok)
                    granted.setDefaultButton(QMessageBox.Ok)
                    xy = granted.exec_()
                    if xy == QMessageBox.Ok:
                        cap = cv2.VideoCapture(0)

    def displayImage_In(self, img, Flag):
        faces_detected, gray_img = fr.faceDetection(img)
        for (x, y, w, h) in faces_detected:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), thickness=5)
        qformat = QImage.Format_Indexed8
        if len(img.shape) == 3:
            if (img.shape[2]) == 4:
                qformat = QImage.Format_RGBA888
            else:
                qformat = QImage.Format_RGB888
        img = QImage(img, img.shape[1], img.shape[0], qformat)
        img = img.rgbSwapped()
        if Flag == 1:
            self.lblAuthWebcamScreen.setPixmap(QPixmap.fromImage(img))
            self.lblAuthWebcamScreen.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        else:
            self.lblAuthWebcamScreenOut.setPixmap(QPixmap.fromImage(img))
            self.lblAuthWebcamScreenOut.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

    now = datetime.now()
    global current_time
    global DateToday
    current_time = now.strftime("%H:%M:%S")
    today = datetime.today()
    DateToday = today.strftime("%d/%m/%Y")

    def loadExitAuthInMode(self):
        # cap.release()
        self.loadcancelmode()

    def InInsertion(self, currentTime, dateToday):
        session = session_factory()
        employee_dao = Employee_Dao()
        in_out_time_Dao = InOutTime_Dao()
        employee = employee_dao.query_by_id(session, employeeId)
        employeeInOut = InOutTime(dateToday, currentTime, None, employee)
        in_out_time_Dao.create_record(session, employeeInOut)

    def CloseWebcamIn(self):
        self.WebCamValue = 1
        self.tabSetup.setEnabled(True)
        self.tabAuthOut.setEnabled(True)

    #  ****************************** For Authentication Out Mode Tab ************************************ #

    def WebcamActivityOut(self):
        OutFlag = 2
        if self.btnWebcamOut.text() == "Start Webcam":
            self.btnWebcamOut.setText("Stop Webcam")
            self.btnExitAuthOut.setEnabled(False)
            self.AuthorizationFunction1(OutFlag)
        elif self.btnWebcamOut.text() == "Stop Webcam":
            self.btnWebcamOut.setText("Start Webcam")
            self.btnExitAuthOut.setEnabled(True)
            self.CloseWebcamOut()

    def OutInsertion(self, currentTime, dateToday):
        session = session_factory()
        employee_dao = Employee_Dao()
        in_out_time_Dao = InOutTime_Dao()
        employee = employee_dao.query_by_id(session, employeeId)
        employeeInOut = InOutTime(dateToday, None, currentTime, employee)
        in_out_time_Dao.create_record(session, employeeInOut)

    def CloseWebcamOut(self):
        self.WebCamValue = 1
        self.tabSetup.setEnabled(True)
        self.tabAuthIn.setEnabled(True)

    def loadExitAuthOutMode(self):
        # cap.release()
        self.loadcancelmode()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    wi = Ui_MainWindow()
    wi.setupUi(MainWindow)
    MainWindow.showNormal()
    sys.exit(app.exec_())
