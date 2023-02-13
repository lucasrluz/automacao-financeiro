from dotenv import load_dotenv
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtCore import QObject, Slot, QStandardPaths
from automacao_financeiro.service.run_service import run_service

load_dotenv()

class Bridge(QObject):
    @Slot(str, str, list, result=None)
    def start(self, initDate, endDate, banks):
        data = {
            'init_date': initDate,
            'end_date': endDate,
            'banks': banks 
        }

        data['init_date'] = '05/02/2023'
        data['end_date'] = '10/02/2023'

        run_service(data, banks)

def run_ui():
    app = QGuiApplication()

    QStandardPaths.writableLocation(QStandardPaths.StandardLocation.DownloadLocation)

    engine = QQmlApplicationEngine()
    engine.load('automacao_financeiro/ui/ui.qml')

    bridge = Bridge()
    context = engine.rootContext()
    context.setContextProperty('bridge', bridge)

    app.exec()

run_ui()