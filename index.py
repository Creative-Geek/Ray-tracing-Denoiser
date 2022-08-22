from PyQt5.QtWidgets import QMainWindow,QApplication,QMessageBox #*
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
from PyQt5.QtWidgets import QFileDialog
import sys
import PyQt5
import os
from os import path
import time, math, random
from random import seed
from random import randint
#import speedtest_cli #causing confliction without console

#FORM_CLASS,_=loadUiType(path.join(path.dirname(__file__), "main.ui"))
from main import Ui_MainWindow as FORM_CLASS



class MainWindow(QMainWindow, FORM_CLASS):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.HandleUI_Time()
        self.HandleButtons()
        self.HandleEvents()
        self.setAcceptDrops(True)
    
        


    def HandleUI_Time(self):
        self.setWindowTitle("Denoiser")



    def HandleButtons(self):
        self.Start_PB.clicked.connect(self.StartFunc)
        self.Browse_PB.clicked.connect(self.openFileNameDialog)
        self.Normal_PB.clicked.connect(self.openFileNameDialogNormal)
        self.Albedo_PB.clicked.connect(self.openFileNameDialogAlbedo)
        self.cls_PB.clicked.connect(self.closeApp)
        self.TestPB.clicked.connect(self.Testingfunc)
    
    def HandleEvents(self):
        #on text change reset color to black
        #self.input_SrcPth.textChanged.connect(self.resetAV_L)

        # on enter key while on any input, start calculation
        self.input_SrcPth.returnPressed.connect(self.StartFunc)

        #choose unit with keyboard
        #to be added later

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        file = ""
        files = [u.toLocalFile() for u in event.mimeData().urls()]
        file = '\n'.join(files)
        self.input_SrcPth.setText(file)
    
    def openFileNameDialog(self):
            options = QFileDialog.Options()
            #options |= QFileDialog.DontUseNativeDialog
            fileName, _ = QFileDialog.getOpenFileName(self,"Choose an image", "","Image files (*.jpg *.gif *.png)", options=options)
            
            if fileName:
                self.input_SrcPth.setText(fileName)
    
    def openFileNameDialogAlbedo(self):
            options = QFileDialog.Options()
            #options |= QFileDialog.DontUseNativeDialog
            fileName, _ = QFileDialog.getOpenFileName(self,"Choose an image", "","Image files (*.jpg *.gif *.png)", options=options)
            
            if fileName:
                self.input_SrcPth_Alb.setText(fileName)
                
    
    def openFileNameDialogNormal(self):
            options = QFileDialog.Options()
            #options |= QFileDialog.DontUseNativeDialog
            fileName, _ = QFileDialog.getOpenFileName(self,"Choose an image", "","Image files (*.jpg *.gif *.png)", options=options)
            
            if fileName:
                self.input_SrcPth_Nrm.setText(fileName)


    def keyPressEvent(self, event):
        key = event.key()
        if key == Qt.Key_Escape:
            sys.exit()
        
    #reset colors on event##############################

        
        
    def resetGlobal(self):
        pass
    
    ####################################################

    def Testingfunc(self):
        pass
    ###################
    def StartFunc(self):
        randomint = str(random.randint(0, 9999))
        self.label_Busy.show()
        #getting path from input:
        srcfile = self.input_SrcPth.text()
        srcfile_alb = self.input_SrcPth_Alb.text()
        srcfile_nrm = self.input_SrcPth_Nrm.text()
        #check for empty:
        if srcfile == "":
            self.label_Busy.hide()
            QMessageBox.critical(self, "Error", "Provide image path")
            return
        #check for frozen pack and get current path
        if getattr(sys, 'frozen', False):
            application_path = os.path.dirname(sys.executable)
        elif __file__:
            application_path = os.path.dirname(__file__)
        #get engine:
        Engindex = self.Eng_comboBox.currentIndex()
        if Engindex == 0:
            Eng = "N"
        if Engindex == 1:
            Eng = "O"
        #getting selected file name:
        imagefilename = os.path.basename(srcfile)
        #compiling command 1 for cmd:
        fullcmd1 = "".join(('cd /d ','"',application_path, "\Denoiser_",Eng,'"')) #kept on!
        #getting output folder
        if self.RB_Source.isChecked():
            outputpath = os.path.dirname(srcfile)
            #getting output full path (with edited image file name):
            outputdir = ''.join((outputpath,"/", "Denoised_",Eng, randomint , "_",imagefilename))
        if self.RB_Custom.isChecked():
            outputpath = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
            if outputpath =="": #check for cancelation
                self.label_Busy.hide()
                #QMessageBox.critical(self, "Error", "Provide output path")
                return 
            #getting output full path (with image file name):
            outputdir = ''.join((outputpath,"/","Denoised_",Eng,randomint, "_",imagefilename))




        #getting spinBox value:
        RPt = self.Repeat_spinBox.value()
        RPt = str(RPt)
        #compiling command 2 for cmd:
        if srcfile_alb =="" and srcfile_nrm == "":
            fullcmd2 = "".join(("Denoiser.exe -i " ,'"',srcfile,'"', " -repeat ",RPt," -o ",'"',outputdir,'"',))
        elif srcfile_alb != "" and srcfile_nrm == "":
            fullcmd2 = "".join(("Denoiser.exe -i " ,'"',srcfile,'"', " -repeat ",RPt," -a ",'"',srcfile_alb,'"'," -o ",'"',outputdir,'"',))
        elif srcfile_nrm != "" and srcfile_alb == "":
            QMessageBox.critical(self, "Error", "Normal requires albedo")
            return
        else:
            fullcmd2 = "".join(("Denoiser.exe -i " ,'"',srcfile,'"', " -repeat ",RPt," -a ",'"',srcfile_alb,'"'," -n ",'"',srcfile_nrm,'"'," -o ",'"',outputdir,'"',))
        #print (fullcmd1)
        #print (fullcmd2)
        self.label_Busy.show()
        #sending to cmd:
        sendcommand = "".join(('cmd /c ','"',fullcmd1," & ",fullcmd2))
        #print (sendcommand)
        os.system(sendcommand)
        self.label_Busy.hide()

        






    def HandleUI_Time(self):
        self.setWindowTitle('test')


    

    def closeApp(self):
        sys.exit()
    


    def mousePressEvent(self, event):
        
        if event.buttons() == Qt.LeftButton:
            self.dragPos = event.globalPos()
            event.accept()
    
    def mouseMoveEvent(self, event):
    
        if event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()




def main():
    
    app = QApplication(sys.argv)
    window = MainWindow()
    #app.setApplicationDisplayName('ES Time')
    window.setWindowTitle('Nvidia Denoiser')
    window.show()
    window.label_Busy.hide()
    window.TestPB.hide()
    app.exec_()
if __name__ == '__main__':
    main()
    