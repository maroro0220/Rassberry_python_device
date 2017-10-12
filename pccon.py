import team1_DB_Control as dbc
import GUI_Server as gs
import team1_pcsend as ps1
class Pcon:
    def __init__(self):
        self.dc=dbc.tema1_DB()
        self.ps=ps1.PC()
    def dbin(self,data):
        self.dc.insert_data(data)
    def dipin(self,data):
        self.gs.insert(data)
    def pcsend(self, data):
        self.ps.Psend(data)
