from dotenv import load_dotenv
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtCore import QObject, Slot, QStandardPaths
from automacao_financeiro.service.run_service import run_service
from datetime import date

load_dotenv()

class Bridge(QObject):
    @Slot(str, str, str, list, result=None)
    def start(self, initDate, endDate, view_browser, banks):
        data = {
            'init_date': initDate,
            'end_date': endDate,
            'banks': banks 
        }

        if data['init_date'] == '' or data['end_date'] == '':
            today = str(date.today())

            year = today[0:4]
            mount = today[5:7]
            day = today[8:10]

            end_date = day + '/' + mount + '/' + year
            data['end_date'] = end_date

            new_day = int(day) - 5

            init_date = str(new_day) + '/' + mount + '/' + year
            data['init_date'] = init_date

        run_service(data, view_browser, banks)

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