from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets
from threading import Thread


class UI:

    def __init__(self):
        self.qt_app = QtWidgets.QApplication([])
        self.qt_view = QtWebEngineWidgets.QWebEngineView(self.qt_app.activeModalWidget())

    @staticmethod
    def thread(app):
        return Thread(target=app.run, daemon=True, kwargs={
            'debug': app.config['DEBUG'],
            'host': app.config['HOST'],
            'port': app.config['PORT'],
            'threaded': True,
            'use_reloader': False})

    def run(self, app):
        self.thread(app).start()
#        self.run_gui()

#    def run_gui(self, app):
        self.qt_view.load(QtCore.QUrl('{}://{}:{}'.format(app.config['PROTOCOL'], app.config['HOST'], app.config['PORT'])))

        change_setting = self.qt_view.page().settings().setAttribute
        settings = QtWebEngineWidgets.QWebEngineSettings
        change_setting(settings.LocalStorageEnabled, True)
        change_setting(settings.PluginsEnabled, True)

        self.qt_view.show()
        self.qt_app.exec_()
