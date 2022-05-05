import PyQt5
from PyQt5 import QtSql, QtWidgets

import var


class Conexion():

    def db_connect(clientes):

        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName(clientes)
        if not db.open():
            QtWidgets.QMessageBox.critical(None, 'No se puede abrir la base de datos',
                                           'No se puede establecer conexión.\n ' 'Haz Click para Cancelar.',
                                           QtWidgets.QMessageBox.Cancel)
            return False
        else:
            print('Conexion Establecida')
        return True

    def cargarCli(clientes):
        query = QtSql.QSqlQuery()
        query.prepare('insert into clientes (dni, apellidos, nombre, direccion, provincia, sexo, formapago, fechaalta)'
                      'VALUES (:dni, :apellidos, :nombre, :direccion, :provincia, :sexo, :formapago, :fechaalta)')
        query.bindValue(':dni', str(clientes[0]))
        query.bindValue(':apellidos', str(clientes[1]))
        query.bindValue(':nombre', str(clientes[2]))
        query.bindValue(':direccion', str(clientes[3]))
        query.bindValue(':provincia', str(clientes[4]))
        query.bindValue(':sexo', str(clientes[5]))
        # pagos
        query.bindValue(':formapago', str(clientes[6]))
        query.bindValue(':fechaalta', str(clientes[7]))
        # print (pagos)
        if query.exec_():
            print("Inserción correcta")
            Conexion.mostrarClientes(clientes)
        else:
            print("Error: ", query.lastError().text())

    def mostrarClientes(self):
        index = 0
        query = QtSql.QSqlQuery()
        query.prepare('select dni, apellidos, nombre, direccion, provincia, sexo, formapago, fechaalta from clientes')
        if query.exec_():
            while query.next():
                dni = query.value(0)
                apellidos = query.value(1)
                nombre = query.value(2)
                direccion = query.value(3)
                provincia = query.value(4)
                sexo = query.value(5)
                formapago = query.value(6)
                fechaalta = query.value(7)
                var.ui.tableWidget.setRowCount(index + 1)
                var.ui.tableWidget.setItem(index, 0, QtWidgets.QTableWidgetItem(dni))
                var.ui.tableWidget.setItem(index, 1, QtWidgets.QTableWidgetItem(apellidos))
                var.ui.tableWidget.setItem(index, 2, QtWidgets.QTableWidgetItem(nombre))
                var.ui.tableWidget.setItem(index, 3, QtWidgets.QTableWidgetItem(direccion))
                var.ui.tableWidget.setItem(index, 4, QtWidgets.QTableWidgetItem(provincia))
                var.ui.tableWidget.setItem(index, 5, QtWidgets.QTableWidgetItem(sexo))
                var.ui.tableWidget.setItem(index, 6, QtWidgets.QTableWidgetItem(formapago))
                var.ui.tableWidget.setItem(index, 7, QtWidgets.QTableWidgetItem(fechaalta))
                index += 1
        else:
            Conexion.mostrarClientes(self)
            print("Error mostrar los clientes: ", query.lastError().text())

    def bajaCliente(dni):
        query = QtSql.QSqlQuery()
        query.prepare('delete from clientes where dni = :dni')
        query.bindValue(':dni', dni)

        if query.exec_():
            print('Baja de clientes')
            var.ui.label_2.setText('Cliente con dni ' + dni + ' dado de baja')
        else:
            print('Error mostrar putos clientes: ', query.lastError().text())

    def modificar(codigo, newdata):
        query = QtSql.QSqlQuery()
        codigo = int(codigo)
        query.prepare(
            'update clientes set dni=:dni, apellidos=:apellidos, nombre=:nombre, direccion=:direccion, provincia=:provincia, sexo=:sexo, '
            'formapago=:formapago, fechaalta=:fechaalta where codigo=:codigo')
        query.bindValue(':codigo', int(codigo))
        query.bindValue(':dni', str(newdata[0]))
        query.bindValue(':apellidos', str(newdata[1]))
        query.bindValue(':nombre', str(newdata[2]))
        query.bindValue(':direccion', str(newdata[3]))
        query.bindValue(':provincia', str(newdata[4]))
        query.bindValue(':sexo', str(newdata[5]))
        query.bindValue(':formapago', str(newdata[6]))
        query.bindValue(':fechaalta', str(newdata[7]))

        if query.exec_():
            print('Cliente modificado')
            var.ui.lblstatus.setText('Cliente con dni ' + str(newdata[0]) + ' modificado.')
        else:
            print("Error modificar cliente: ", query.lastError().text())

    def buscarCliente(self):
        dni = var.ui.CampoDNI.text()
        query = QtSql.QSqlQuery()
        query.prepare('select apellidos, nombre, direccion, provincia, sexo,'
                      'formapago, fecha from clients where dni=:dni')
        query.bindValue(':dni', dni)

        if query.exec_():
            while query.next():
                apellidos = query.value(1)
                nombre = query.value(2)
                direccion = query.value(3)
                provincia = query.value(4)
                sexo = query.value(5)
                formapago = query.value(6)
                fecha = query.value(7)

                var.ui.CampoNombre(nombre)
                var.ui.CampoApellidos(apellidos)
                var.ui.CampoApellidos_2(direccion)
                var.ui.comboBox(direccion)
                prov = ['Álava', 'Albacete', 'Alicante', 'Almería', 'Asturias', 'Ávila', 'Badajoz', 'Barcelona',
                        'Burgos', 'Cáceres', 'Cádiz', 'Cantabria', 'Castellón', 'Ceuta', 'Ciudad', 'Real', 'Córdoba',
                        'Cuenca', 'Girona', 'Las Palmas', 'Granada', 'Guadalajara', 'Guipúzcoa', 'Huelva', 'Huesca',
                        'Illes Balears', 'Jaén', 'A Coruña', 'La Rioja', 'León', 'Lleida', 'Lugo', 'Madrid', 'Málaga',
                        'Melilla', 'Murcia', 'Navarra', 'Ourense', 'Palencia', 'Pontevedra', 'Salamanca', 'Segovia',
                        'Sevilla', 'Soria', 'Tarragona', 'Santa Cruz de Tenerife', 'Teruel', 'Toledo', 'Valencia',
                        'Valladolid', 'Vizcaya', 'Zamora', 'Zaragoza']
                var.ui.ComboBox.setCurrentIndex.range(52)
                if (prov not in provincia):
                    print('Provincia no está en la lista')
                var.ui.horizontalLayout_2(sexo)
                var.ui.metodoPago_2(formapago)
                var.ui.CampoFecha(fecha)