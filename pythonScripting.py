import os
import time
from os import path
import smtplib

#How to find Current directory where we are working


# def current_directory():
#     cwd=os.getcwd()
#     print(cwd)
#
# current_directory()



#Another Example Retrive a File Path....


# def current_directory():
#     cwd=os.getcwd()
#     print(cwd)
#
# def file_path(filename):
#     path=os.path.abspath((filename))
#     print(path)
#
# current_directory()
# filename="sample.txt"
# file_path(filename)


#Another Example Time

# epc = time.time()
# print(epc)
# localtime=time.localtime(epc)
# print(localtime)
# print(localtime.tm_year)
#
# print(time.ctime(epc))



#Another Example creating file


# def createfile(dest):
#     if not (path.isfile(dest)):
#         f=open(dest, 'w')
#         f.write("Welcome to Python Scripting!")
#         f.close()
#
# dest = "D:\Python Course\Bignner/sample.txt"
#
# createfile(dest)
# print("File is created.")



#Send an Email



smtobj = smtplib.SMTP('smtp.gmail.com', 587)
smtobj.ehlo()
smtobj.starttls()
smtobj.login('arslanbalochry@gmail.com', 'Khan@9260')
smtobj.sendmail("arslanbalochry@gmail.com", "arslanbalochry@gmail.com", 'Subject: SMTP check. /n This is a test mail')
smtobj.quit()
