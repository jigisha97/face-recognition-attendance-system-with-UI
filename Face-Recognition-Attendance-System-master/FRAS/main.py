import os  # accessing the os functions
import check_camera
import Capture_Image
import Train_Image
import Recognize

from flask import Flask,render_template,Response        # import flask
from flask import request

app = Flask(__name__)             # create an app instance
# templates = Jinja2Templates(directory='templates/')
@app.route("/",methods=['GET', 'POST'])                   # at the end point /
def hello():                      # call method hello
    return render_template('faceindex.html') 

@app.route("/abc", methods=['GET', 'POST'])                   # at the end point /
# def title_bar():
#     os.system('cls') # for windows
 
# def checkCamera():
#  check_camera.camer()
 


# def CaptureFaces():
#  Capture_Image.takeImages()


# # -----------------------------------------------------------------
# # calling the train images from train_images.py file
 
# def Trainimages():
#  Train_Image.TrainImages()

  
# # --------------------------------------------------------------------
# # calling the recognize_attendance from recognize.py file
 
# def RecognizeFaces():
#  Recognize.recognize_attendence()



def abc():                      # call method hello
    #title_bar()
    name = request.form['txtname']
    txtid=request.form['txtid']
    choice=int(request.form['choice'])
    print(choice)
    if choice == 1:
        check_camera.camer()
       
    elif choice == 2:
        Capture_Image.takeImages(txtid,name)
       
    elif choice == 3:
        Train_Image.TrainImages()
       
    elif choice == 4:
        Recognize.recognize_attendence()

    elif Choice == 5:
        os.system("py automail.py")
    

        
    return render_template('faceindex.html')     
if __name__ == "__main__":        # on running python app.py
    app.run()     
             
# creating the title bar function
# creating the title bar function
 

 # title of the program
 

# creating the user main menu function
 
# def mainMenu():
#  title_bar()
#  print()
#  print(10 * "*", "WELCOME MENU", 10 * "*")
#  print("[1] Check Camera")
#  print("[2] Capture Faces")
#  print("[3] Train Images")
#  print("[4] Recognize & Attendance")
#  print("[5] Auto Mail")
#  print("[6] Quit")
 
#  while True:
#  try:
#  choice = int(input("Enter Choice: "))
 
#  if choice == 1:
#  checkCamera()
#  break
#  elif choice == 2:
#  CaptureFaces()
#  break
#  elif choice == 3:
#  Trainimages()
#  break
#  elif choice == 4:
#  RecognizeFaces()
#  break
#  elif choice == 5:
#  os.system("py automail.py")
#  break
#  mainMenu()
#  elif choice == 6:
#  print("Thank You")
#  break
#  else:
#  print("Invalid Choice. Enter 1-4")
#  mainMenu()
#  except ValueError:
#  print("Invalid Choice. Enter 1-4\n Try Again")
#  exit
 
# ---------------------------------------------------------
# calling the camera test function from check camera.py file
 

 
# --------------------------------------------------------------
# calling the take image function form capture image.py file
 


 
# ---------------main driver ------------------
