import sys
from PyQt5.QtSql import QSqlDatabase,QSqlTableModel,QSqlQuery
from PyQt5.QtWidgets import QMainWindow,QApplication,QWidget,QComboBox
from PyQt5 import QtCore, QtGui, QtWidgets
from GoodInvoice_addWindow import WindowAddGoodsInvoice


class addGoodsInvoice(WindowAddGoodsInvoice):
    def __init__(self,tableView_goods_invoice):
        super().__init__()
        self.setupUi(self)
        self.pb_add_goods_invoice.clicked.connect(self.add_goodsinvoice)
        self.goodsinvoice= tableView_goods_invoice
        
        
        
    def add_goodsinvoice(self):
         if self.lineEdit_col.text(): 
            queru_gn =QSqlQuery()
            queru_gn.exec(f"INSERT INTO public.goodsinvoice (name,price,count,cost) VALUES ('{self.comboBox.currentText()}',{str(1)},{self.lineEdit_col.text()},{str(1)})")
            queru3 =QSqlTableModel()
            queru3.setTable("goodsinvoice")
            queru3.select()
            self.goodsinvoice.setModel(queru3)
            
    
            
            
    
            
        