# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1018, 724)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(30, 0, 981, 671))
        self.tabWidget.setObjectName("tabWidget")
        self.clientes = QtWidgets.QWidget()
        self.clientes.setObjectName("clientes")
        self.Salir = QtWidgets.QPushButton(self.clientes)
        self.Salir.setGeometry(QtCore.QRect(860, 600, 75, 23))
        self.Salir.setObjectName("Salir")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.clientes)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 310, 251, 22))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.sexo_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.sexo_2.setObjectName("sexo_2")
        self.horizontalLayout_2.addWidget(self.sexo_2)
        self.radioButtonFem_2 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radioButtonFem_2.setObjectName("radioButtonFem_2")
        self.grupoSexo = QtWidgets.QButtonGroup(MainWindow)
        self.grupoSexo.setObjectName("grupoSexo")
        self.grupoSexo.addButton(self.radioButtonFem_2)
        self.horizontalLayout_2.addWidget(self.radioButtonFem_2)
        self.radioButtonMas_2 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radioButtonMas_2.setObjectName("radioButtonMas_2")
        self.grupoSexo.addButton(self.radioButtonMas_2)
        self.horizontalLayout_2.addWidget(self.radioButtonMas_2)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.clientes)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(490, 310, 388, 22))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.metodosPago_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.metodosPago_2.setContentsMargins(0, 0, 0, 0)
        self.metodosPago_2.setObjectName("metodosPago_2")
        self.metodoPago_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.metodoPago_2.setObjectName("metodoPago_2")
        self.metodosPago_2.addWidget(self.metodoPago_2)
        self.checkEfect_2 = QtWidgets.QCheckBox(self.horizontalLayoutWidget_2)
        self.checkEfect_2.setObjectName("checkEfect_2")
        self.grupoPago = QtWidgets.QButtonGroup(MainWindow)
        self.grupoPago.setObjectName("grupoPago")
        self.grupoPago.addButton(self.checkEfect_2)
        self.metodosPago_2.addWidget(self.checkEfect_2)
        self.checkTarjeta_2 = QtWidgets.QCheckBox(self.horizontalLayoutWidget_2)
        self.checkTarjeta_2.setObjectName("checkTarjeta_2")
        self.grupoPago.addButton(self.checkTarjeta_2)
        self.metodosPago_2.addWidget(self.checkTarjeta_2)
        self.checkTransfe_2 = QtWidgets.QCheckBox(self.horizontalLayoutWidget_2)
        self.checkTransfe_2.setObjectName("checkTransfe_2")
        self.grupoPago.addButton(self.checkTransfe_2)
        self.metodosPago_2.addWidget(self.checkTransfe_2)
        self.DNI_2 = QtWidgets.QLabel(self.clientes)
        self.DNI_2.setGeometry(QtCore.QRect(550, 120, 111, 21))
        self.DNI_2.setObjectName("DNI_2")
        self.NOMBRE = QtWidgets.QLabel(self.clientes)
        self.NOMBRE.setGeometry(QtCore.QRect(540, 190, 51, 21))
        self.NOMBRE.setObjectName("NOMBRE")
        self.Aceptar = QtWidgets.QPushButton(self.clientes)
        self.Aceptar.setGeometry(QtCore.QRect(30, 590, 75, 23))
        self.Aceptar.setObjectName("Aceptar")
        self.Provincia = QtWidgets.QLabel(self.clientes)
        self.Provincia.setGeometry(QtCore.QRect(540, 250, 111, 21))
        self.Provincia.setObjectName("Provincia")
        self.CampoApellidos_2 = QtWidgets.QLineEdit(self.clientes)
        self.CampoApellidos_2.setGeometry(QtCore.QRect(110, 250, 221, 20))
        self.CampoApellidos_2.setObjectName("CampoApellidos_2")
        self.line_2 = QtWidgets.QFrame(self.clientes)
        self.line_2.setGeometry(QtCore.QRect(20, 340, 861, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.APELLIDOS = QtWidgets.QLabel(self.clientes)
        self.APELLIDOS.setGeometry(QtCore.QRect(40, 190, 111, 21))
        self.APELLIDOS.setObjectName("APELLIDOS")
        self.CampoApellidos = QtWidgets.QLineEdit(self.clientes)
        self.CampoApellidos.setGeometry(QtCore.QRect(110, 190, 221, 20))
        self.CampoApellidos.setObjectName("CampoApellidos")
        self.CampoNombre = QtWidgets.QLineEdit(self.clientes)
        self.CampoNombre.setGeometry(QtCore.QRect(600, 190, 161, 20))
        self.CampoNombre.setObjectName("CampoNombre")
        self.APELLIDOS_2 = QtWidgets.QLabel(self.clientes)
        self.APELLIDOS_2.setGeometry(QtCore.QRect(40, 250, 111, 21))
        self.APELLIDOS_2.setObjectName("APELLIDOS_2")
        self.CampoFecha = QtWidgets.QLineEdit(self.clientes)
        self.CampoFecha.setGeometry(QtCore.QRect(640, 120, 113, 20))
        self.CampoFecha.setObjectName("CampoFecha")
        self.GESTIONCLIENTES = QtWidgets.QLabel(self.clientes)
        self.GESTIONCLIENTES.setGeometry(QtCore.QRect(360, 20, 141, 21))
        self.GESTIONCLIENTES.setObjectName("GESTIONCLIENTES")
        self.DNI = QtWidgets.QLabel(self.clientes)
        self.DNI.setGeometry(QtCore.QRect(130, 120, 111, 21))
        self.DNI.setObjectName("DNI")
        self.CampoDNI = QtWidgets.QLineEdit(self.clientes)
        self.CampoDNI.setGeometry(QtCore.QRect(170, 120, 113, 20))
        self.CampoDNI.setObjectName("CampoDNI")
        self.comboBox = QtWidgets.QComboBox(self.clientes)
        self.comboBox.setGeometry(QtCore.QRect(620, 250, 141, 22))
        self.comboBox.setObjectName("comboBox")
        self.line = QtWidgets.QFrame(self.clientes)
        self.line.setGeometry(QtCore.QRect(20, 50, 861, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.tableWidget = QtWidgets.QTableWidget(self.clientes)
        self.tableWidget.setGeometry(QtCore.QRect(10, 360, 881, 221))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        self.label = QtWidgets.QLabel(self.clientes)
        self.label.setGeometry(QtCore.QRect(290, 120, 47, 16))
        font = QtGui.QFont()
        font.setFamily("Forte")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setObjectName("label")
        self.Calendario = QtWidgets.QPushButton(self.clientes)
        self.Calendario.setGeometry(QtCore.QRect(750, 120, 21, 21))
        self.Calendario.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Imagenes/calendar-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Calendario.setIcon(icon)
        self.Calendario.setObjectName("Calendario")
        self.tabWidget.addTab(self.clientes, "")
        self.facturacion = QtWidgets.QWidget()
        self.facturacion.setObjectName("facturacion")
        self.tabWidget.addTab(self.facturacion, "")
        self.productos = QtWidgets.QWidget()
        self.productos.setObjectName("productos")
        self.tabWidget.addTab(self.productos, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1018, 21))
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtWidgets.QMenu(self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSalir = QtWidgets.QAction(MainWindow)
        self.actionSalir.setObjectName("actionSalir")
        self.menuArchivo.addAction(self.actionSalir)
        self.menubar.addAction(self.menuArchivo.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Salir.setText(_translate("MainWindow", "Salir"))
        self.sexo_2.setText(_translate("MainWindow", "SEXO:"))
        self.radioButtonFem_2.setText(_translate("MainWindow", "Femenino"))
        self.radioButtonMas_2.setText(_translate("MainWindow", "Masculino"))
        self.metodoPago_2.setText(_translate("MainWindow", "METODOS DE PAGO:"))
        self.checkEfect_2.setText(_translate("MainWindow", "Efectivo"))
        self.checkTarjeta_2.setText(_translate("MainWindow", "Tarjeta"))
        self.checkTransfe_2.setText(_translate("MainWindow", "Transferencia"))
        self.DNI_2.setText(_translate("MainWindow", "FECHA ACTUAL:"))
        self.NOMBRE.setText(_translate("MainWindow", "NOMBRE"))
        self.Aceptar.setText(_translate("MainWindow", "Aceptar"))
        self.Provincia.setText(_translate("MainWindow", "PROVINCIA:"))
        self.APELLIDOS.setText(_translate("MainWindow", "APELLIDOS:"))
        self.APELLIDOS_2.setText(_translate("MainWindow", "DIRECCIÓN:"))
        self.GESTIONCLIENTES.setText(_translate("MainWindow", "GESTIÓN DE CLIENTES"))
        self.DNI.setText(_translate("MainWindow", "DNI:"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "dni"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "apellidos"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "nombre"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "direccion"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "provincia"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "sexo"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "formapago"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "fechaalta"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.clientes), _translate("MainWindow", "Clientes"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.facturacion), _translate("MainWindow", "Facturación"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.productos), _translate("MainWindow", "Productos"))
        self.menuArchivo.setTitle(_translate("MainWindow", "Archivo"))
        self.actionSalir.setText(_translate("MainWindow", "Salir"))
        self.actionSalir.setShortcut(_translate("MainWindow", "Ctrl+S, Alt+4"))
