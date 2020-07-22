import cv2
import os
import numpy as np
import faceRecognition as fr
from imaging.employee_dao import Employee_Dao
from imaging.employee_image_dao import EmployeeImage_Dao
from imaging.model.employee_image import EmployeeImage
from imaging.model.employee import Employee
from imaging.model.base import session_factory


def testerAuthorization():
    # This module takes images  stored in disk and performs face recognition
    # test_img = cv2.imread('TestImages/Kangana.jpg')  # test_img path
    # faces_detected, gray_img = fr.faceDetection(test_img)
    # print("faces_detected:", faces_detected)

    # Comment belows lines when running this program second time.Since it saves training.yml file in directory
    # faces, faceID = fr.labels_for_training_data('trainingImages')
    faces, faceID = fr.labels_for_training_data2()
    face_recognizer = fr.train_classifier(faces, faceID)
    face_recognizer.write('trainingData.yml')
    return True


def listUserInfoFunction(employee_data, images_data):
    session = session_factory()
    employee_dao = Employee_Dao()
    employeeImage_Dao = EmployeeImage_Dao()
    employee_rec = Employee(employee_data['Name'], employee_data['EmpCode'], True, None)
    employee_dao.create_record(session, employee_rec)
    employee = employee_dao.query_by_code(session, employee_data['EmpCode'])

    for image in images_data:
        employeeImage = EmployeeImage(image, employee)
        employeeImage_Dao.create_record(session, employeeImage)
    session.close()
    testerAuthorization()
    return True

    # Uncomment below line for subsequent runs
    # face_recognizer=cv2.face.LBPHFaceRecognizer_create()
    # face_recognizer.read('trainingData.yml')#use this to load training data for subsequent runs
