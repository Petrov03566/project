from PyQt5.QtSql import QSqlDatabase,QSqlTableModel,QSqlQuery
from Window2 import addWindow2

class Goodsadd(addWindow2):
    def __init__(self):
        super().__init__()
        self.setupUi()
        
        
    # def add_goods(self):
    #         queru_pr =QSqlQuery()
    #         queru_pr.exec(f"INSERT INTO public.goods (id_invoice, id_goods,quantity) VALUES ('{self.lineEdit_.text()}','{self.lineEdit_add2.text()}')")
    #         queru =QSqlTableModel()
    #         queru.setTable("provider")
    #         queru.select()
    #         self..setModel(queru)