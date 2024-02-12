
from PyQt5.QtSql import QSqlDatabase,QSqlTableModel,QSqlQuery
from PyQt5.QtWidgets import QTableView
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
            
    
class ProviderChange(WindowAddProvider):
    def __init__(self,tableView_provader:QTableView):
        super().__init__()
        self.setupUi(self)
        CurIndex = tableView_provader.currentIndex().row()
        id = tableView_provader.model()[CurIndex][0]
        OldName = tableView_provader[CurIndex][1]
        OldAddress = tableView_provader[CurIndex][2]
        self.id = id
        self.lineEdit_add.setText(OldName)
        self.lineEdit_add2.setText(OldAddress)
        self.pushButton_provader.clicked.connect(self.change_provider)
        self.tableView_provader = tableView_provader
        
    def change_provider(self):
        if self.lineEdit_add.text() and self.lineEdit_add2.text(): 
            queru_pr =QSqlQuery()
            SQL = f"UPDATE public.provider SET  name='{self.lineEdit_add.text()}', address='{self.lineEdit_add2.text()}' WHERE id="+str(self.id)
            queru_pr.exec(SQL)
            queru =QSqlTableModel()
            queru.setTable("provider")
            queru.select()
            self.tableView_provader.setModel(queru)            
    