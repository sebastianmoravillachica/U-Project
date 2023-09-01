import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
#from Menuprincipal import Ui_MainWindow


from Login import Ui_MainWindow
from Menuprincipal import Menu

#crear una clase anejadora de la aplicación
class mdiApp(QMainWindow):
    def __init__(self):
        super().__init__() #crea el objeto QmainWindow, solo abra no y las demas ventanas principales se renderizaran sobre el
        self.login = Ui_MainWindow() #instancio el login
        self.login.setupUi(self) #pinto los componentes
        self.login.btnIngresar.clicked.connect(self.acceso)
        self.show() #se meustra la vetana principal
        self.user_role = None


    def acceso(self):
        # Obtener los datos ingresados por el usuario
        username = self.login.lineEditUsuario.text()
        password = self.login.lineEditPassword.text()

        # Verificar si los campos están vacíos
        if not username or not password:
            self.login.labelMjs.setText("Por favor, ingrese el usuario y la contraseña.")
            return

        # Verificar el rol seleccionado
        selected_role = self.login.comboBox.currentText()
        if selected_role not in ["Administrador", "Encuestador"]:
            self.login.labelMjs.setText("Rol de usuario no válido.")
            return

        # Verificar las credenciales del usuario y permitir o denegar el acceso
        if selected_role == "Encuestador":
            if username in ["Daniela Solano Garita", "Maryssa Cañas Cruz","Mario Cascante Vargas "] and password == "DSG11" or  password == "MCC2304" or password == "Mario123" :
                self.login.labelMjs.setText("Acceso correcto,Bienvenido Encuestador")
                self.user_role = "Encuestador"
            else:
                self.login.labelMjs.setText("Acceso denegado")
                self.user_role = None
        elif selected_role == "Administrador":
            if username in ["Sebastian Mora Villachica","Rolando Sequeira Victor"] and password == "SMV08" or password =="Rolando888":
                self.login.labelMjs.setText("Acceso correcto,Bienvenido Administrador")
                self.user_role = "Administrador"
            else:
                self.login.labelMjs.setText("Acceso denegado")
                self.user_role = None

        # Si se pudo acceder, mostrar la ventana principal
        if self.user_role:
            # metodo para abrir la sibventana en este caso el mdi
            self.sub_window = Menu()  # instanciar la clase que contiene el mdi
            self.sub_window.setupUi(self)  # pintar los componentes
            # no se debe llamar a show, pq la ventana se renderizara sobre el QmainWindow ya creado
class winMDI(QWidget): #esta clase permite renderizar la nueva ventana
    def __init__(self):
        super(winMDI, self).__init__() #se instancia la clase Qwidget
        # instanciar la ventana
        self.ui = Menu()
        # generar los componetes
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = mdiApp()
    win.show()
    sys.exit(app.exec())
