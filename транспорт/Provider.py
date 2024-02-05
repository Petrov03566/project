import sys
from PyQt5.QtSql import QSqlDatabase,QSqlTableModel,QSqlQuery
from PyQt5.QtWidgets import QMainWindow,QApplication,QWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from provader_add import WindowAddProvider

class ProviderAdd(WindowAddProvider):
    def __init__(self,tableView_provader):
        super().__init__()
        self.setupUi(self)
        self.pushButton_provader.clicked.connect(self.add_provider)
        self.tableView_provader = tableView_provader
        
        
    
        
    def add_provider(self):
        if self.lineEdit_add.text() and self.lineEdit_add2.text(): 
            queru_pr =QSqlQuery()
            queru_pr.exec(f"INSERT INTO public.provider (name, address) VALUES ('{self.lineEdit_add.text()}','{self.lineEdit_add2.text()}')")
            queru =QSqlTableModel()
            queru.setTable("provider")
            queru.select()
            self.tableView_provader.setModel(queru)
            
    
            
    