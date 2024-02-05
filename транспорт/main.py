import sys
from PyQt5.QtSql import QSqlDatabase,QSqlTableModel,QSqlQuery
from PyQt5.QtWidgets import QMainWindow,QApplication,QVBoxLayout, QComboBox, QCalendarWidget,QHeaderView
from PyQt5 import QtCore, QtGui, QtWidgets
from table import Ui_MainWindow 
from Provider import ProviderAdd
from invoicesadd import InvoicesAdd
from goodsinvoice import addGoodsInvoice
from delete_pv import Deleteprovader
from Window2 import addWindow2
from chanceProvader import AddProvaderchance
class MainWindow(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.db_connection()
        self.db_table1()
        self.db_table2()
        self.db_table3()
        
        self.tableView_provader.hideColumn(0)
        self.tableView_invoices.hideColumn(0)
        self.tableView_invoices.hideColumn(3)
        self.tableView_tovar_invoices.hideColumn(0)
        
        self.pushButton_add_provader.clicked.connect(self.open_provider)
        self.pushButton_add_invoices.clicked.connect(self.open_invoice)
        self.pushButton_add_tovar_invoices.clicked.connect(self.open_goods_invoices)
        
        self.pushButton_delete_provader.clicked.connect(self.delete_add_provider)
        self.pushButton_delete_invoices.clicked.connect(self.delete_add_invoice)
        
        self.pb_window.clicked.connect(self.open_window2)
        
        
        self.tableView_provader.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView_invoices.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView_tovar_invoices.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        
        
        
    def db_connection(self):
        db = QSqlDatabase.addDatabase("QPSQL")
        db.setUserName("postgres")
        db.setPassword("student")
        db.setPort(5432)
        db.setDatabaseName("transport")
        db.setHostName("localhost")
        db.open()
        


    def db_table1(self):
        stm =QSqlTableModel()
        stm.setTable('provider')
        stm.select()
        self.tableView_provader.setModel(stm)
        stm.setHeaderData(1, QtCore.Qt.Horizontal,"название")
        stm.setHeaderData(2, QtCore.Qt.Horizontal,"адрес")
        
        
        
    def db_table2(self):
        stm2 =QSqlTableModel()
        stm2.setTable('invoices')
        stm2.select()
        self.tableView_invoices.setModel(stm2)
        stm2.setHeaderData(1, QtCore.Qt.Horizontal,"номер накладных")
        stm2.setHeaderData(2, QtCore.Qt.Horizontal,"данные")
        
        
        
    def db_table3(self):
        stm3 =QSqlTableModel()
        stm3.setTable('goods_invoices')
        stm3.select()
        self.tableView_tovar_invoices.setModel(stm3)
        stm3.setHeaderData(1, QtCore.Qt.Horizontal,"Имя товара")
        stm3.setHeaderData(2, QtCore.Qt.Horizontal,"цена")
        stm3.setHeaderData(3, QtCore.Qt.Horizontal,"количества")
        stm3.setHeaderData(4, QtCore.Qt.Horizontal,"стоимость")
        
        
    
    #кнопка открытие окно 
    def open_provider(self):
        self.provider =ProviderAdd(tableView_provader=self.tableView_provader)
        self.provider.show()
        
        
    def open_invoice(self):
        self.invoice =InvoicesAdd(tableView_invoice=self.tableView_invoices)
        self.invoice.show()
        
    def open_goods_invoices(self):
        self.goods =addGoodsInvoice(tableView_goods_invoice=self.tableView_tovar_invoices)
        self.goods.show()
    
    def open_window2(self):
        self.window2 = addWindow2()
        self.setupUi(self.window2)
        self.window2.show()    
    
        
        
    #кнопка удаление данных  
    def delete_add_provider(self):
        selected_row = self.tableView_provader.selectedIndexes()[0].row()
        model = self.tableView_provader.model()
        model.removeRow(selected_row)
        
    def delete_add_invoice(self):
        selected_row = self.tableView_invoices.selectedIndexes()[0].row()
        model = self.tableView_invoices.model()
        model.removeRow(selected_row)
        
    def delete_add_goods(self):
        selected_row = self.tableView_tovar_invoices.selectedIndexes()[0].row()
        model = self.tableView_tovar_invoices.model()
        model.removeRow(selected_row)
        
        
    
        
  
        

app =QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()