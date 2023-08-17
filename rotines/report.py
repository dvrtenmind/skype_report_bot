from database.db import DatabaseManager
from controllers.report_manager import ReportManager
from controllers.skype_manager import SkypeManager
from controllers.listener_bot import SkypeListener


class Report():
    def __init__(self, db_manager, skp_manager, report_manager):
        self.db_manager = db_manager
        self.skp_manager = skp_manager
        self.report_manager = report_manager
        self.status = self.report_manager.get_status_availables()
        self.funcionarios = self.report_manager.getFuncionariosAndEtapas()
        self.reports = {}

    def run(self):
        for funcionario in self.funcionarios.values():
            # if funcionario.nome == "Marcelo Junior":
            if funcionario.nome == "Emilly Barbieri":
                print("Funcionario encontrado")
                print("Iniciando")
                self.reports[funcionario.id] = self.report_manager.get_reports_by_func(funcionario, self.status)

if __name__ == "__main__":
    # initialize
    db_manager = DatabaseManager()
    skp_manager = SkypeManager()
    report_manager = ReportManager(db_manager, skp_manager)
    
    # initialize listener
    listener = SkypeListener(skp_manager)
    print(listener.run())
    
    #run
    report = Report(db_manager, skp_manager, report_manager)
    report.run()