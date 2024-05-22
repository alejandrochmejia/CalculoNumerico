import flet as ft
import random
import funciones

#Definicion Pagina
def main(page: ft.Page): #Función que crea la página
    #Características de la página
    page.title = "1er Evaluación de Calculo Numérico - Alejandro Chávez (32.278.392)"
    page.bgcolor = '#06141B'
    page.window_resizable = False
    page.window_height = 1024
    page.window_width = 1440
    page.window_maximized = True
    page.horizontal_alignment = "CENTER"

    """
    CAMBIO DE PROGRAMA:
    Parte del código donde encuentras todo lo referente al display/botón y lista desplegable
    de la parte superior de la UI, donde se apoyará el cambio entre los dos programas: 'Gauss Seidel & Sistemas Numéricos'

    """

    def GaussSeidelEscenaCambio(e): #Función que apoya el cambio de programa, cuando el boton de Gauss Seidel es presionado
        if str(DisplayOpcionActual.value) == str(e.control.content.value) + " ▾":
            pass
        else:
            cambioDisplayOpcion(e)
            transicioncambio.content = filaPrincipal
            transicioncambio.update()
            page.update()

    def SistemasEscenaCambio(e): #Función que apoya el cambio de programa, cuando el boton de Sistemas Numéricos es presionado
        if str(DisplayOpcionActual.value) == str(e.control.content.value) + " ▾":
            pass
        else:
            cambioDisplayOpcion(e)
            transicioncambio.content = contenedorSistema
            transicioncambio.update()
            page.update()

    DisplayOpcionActual = ft.Text("Gauss Seidel ▾", #Texto de la parte superior donde se indica en que programa se está actualmente
                                  color="#9BA8AB",
                                  theme_style=ft.TextThemeStyle.TITLE_LARGE,
                                  weight=ft.FontWeight.BOLD,
                                  size=30
                                  )
    
    def cambioDisplayOpcion(e): #Función que cambia el texto del display de la parte superior izquierda
            DisplayOpcionActual.value = str(e.control.content.value) + " ▾"
            page.update()
            
    MenuOpciones = ft.SubmenuButton( #Botón que contiene el display + la lista ista desplegable para el cambio de programa entre 'Gauss Seidel/ Sistemas Numéricos'
                content= DisplayOpcionActual,
                controls=[
                    ft.MenuItemButton(
                        content=ft.Text("Gauss Seidel"),
                        on_click= GaussSeidelEscenaCambio
                    ),
                    ft.MenuItemButton(
                        content=ft.Text("Sistemas numéricos"),
                        on_click = SistemasEscenaCambio
                    )
                ]
    )

    BasemenuOpciones = ft.MenuBar( #Área donde se encuentra el menu de opciones para el cambio de página (Contiene el botón con el display + Lista desplegable)
        expand=True,
        style=ft.MenuStyle(
            ft.alignment.top_left,
            bgcolor='#06141B',
            mouse_cursor={
                ft.MaterialState.HOVERED: ft.MouseCursor.WAIT,
                ft.MaterialState.DEFAULT: ft.MouseCursor.ZOOM_OUT,
            }
        ),
        controls=[
            MenuOpciones
        ]

    )

    """
    SISTEMAS NUMÉRICOS:
    Parte del código donde encontrarás todo lo referente al programa de Traducción de Sistemas Numéricos

    """
    TituloSN = ft.Text("Traducción de Sistemas Numéricos", #Título principal de la interfaz
                       theme_style=ft.TextThemeStyle.TITLE_LARGE,
                       weight=ft.FontWeight.BOLD,
                       size=30,
                       color="#9BA8AB"
                       )
         

    def LimpiarSalida(e): #Función que limpia el texto escrito en el TextField de salida
         SalidaSN.value = ""
         page.update()

    EntradaSN = ft.TextField( #TextField para valores o números de entrada
         label="Número de Entrada",
         width= 370,
         border_color= "#4A5C6A",
         read_only= False,
         input_filter=ft.InputFilter(allow=True,regex_string=[0,1,2,3,4,5,6,7,8,9],replacement_string=""),
         on_change=LimpiarSalida
    )

    SalidaSN = ft.TextField( #TextField para valores o números de salida (Resultados)
         label="Número de Salida",
         width= 370,
         border_color= "#4A5C6A",
         read_only= True
    )

    def CambioDDEntrada(e): #Función que se ejecuta cuando hay un cambio de opción en el DropDown de entrada donde se eligen las bases de entrada
         EntradaSN.value = ""
         SalidaSN.value = ""
         if str(DDEntrada.value) == str(None):
              EntradaSN.read_only = True
              page.update()
         else:
              EntradaSN.read_only = False
              page.update()
              if str(DDEntrada.value) == "DEC":
                   EntradaSN.input_filter=ft.InputFilter(allow=True,regex_string=[0,1,2,3,4,5,6,7,8,9],replacement_string="")
                   page.update()
              elif str(DDEntrada.value) == "BIN":
                   EntradaSN.input_filter=ft.InputFilter(allow=True,regex_string=[0,1],replacement_string="")
                   page.update()
              elif str(DDEntrada.value) == "TER":
                   EntradaSN.input_filter=ft.InputFilter(allow=True,regex_string=[0,1,2],replacement_string="")
                   page.update()
              elif str(DDEntrada.value) == "CUA":
                   EntradaSN.input_filter=ft.InputFilter(allow=True,regex_string=[0,1,2,3],replacement_string="")
                   page.update()
              elif str(DDEntrada.value) == "OCT":
                   EntradaSN.input_filter=ft.InputFilter(allow=True,regex_string=[0,1,2,3,4,5,6,7],replacement_string="")
                   page.update()
              elif str(DDEntrada.value) == "HEX":
                   EntradaSN.input_filter=ft.InputFilter(allow=True,regex_string=[0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F','a','b','c','d','e','f'],replacement_string="")
                   page.update()

    DDEntrada = ft.Dropdown(width=100, #DropDown(Lista desplegable) para elegir las bases de entrada
                            border_color= "#4A5C6A",
                            options=[
                                ft.dropdown.Option("DEC"),
                                ft.dropdown.Option("BIN"),
                                ft.dropdown.Option("TER"),
                                ft.dropdown.Option("CUA"),
                                ft.dropdown.Option("OCT"),
                                ft.dropdown.Option("HEX"),
                                ],
                            label="Base",
                            on_change=CambioDDEntrada,
                            value="DEC"
                            )

    DDSalida = ft.Dropdown(width=100, #DropDown(Lista desplegable) para elegir las bases de salida
                           border_color= "#4A5C6A",
                           options=[
                                ft.dropdown.Option("DEC"),
                                ft.dropdown.Option("BIN"),
                                ft.dropdown.Option("TER"),
                                ft.dropdown.Option("CUA"),
                                ft.dropdown.Option("OCT"),
                                ft.dropdown.Option("HEX"),
                                ],
                            label="Base",
                            on_change= LimpiarSalida,
                            value="BIN"
                           )
    
    infoDialogSN = ft.AlertDialog(title=ft.Text("Bases de Sistemas Numéricos"), #Dialogo de alerta/información que se ejecuta al presionar botón de Información
                                  content=ft.Text("DEC = Decimal (Base 10)\nBIN = Binario (Base 2)\nTER = Terciario (Base 3)\nCUA = Cuaternario(Base 4)\nOCT = Octal (Base 8)\nHEX = Hexadecimal (Base 16)")
                                  )
    def abrirInfoSN(e): #Función que ejecuta y abre el dialogo de alerta/información
         page.dialog = infoDialogSN
         infoDialogSN.open = True
         page.update()

    infoSN = ft.IconButton( #Botón/Icono de información acerca del programa
         icon= ft.icons.INFO_ROUNDED,
         icon_color= "#4A5C6A",
         on_click= abrirInfoSN
    )

    def operacionSN(e): #Función que se ejecuta al dar click en el botón de operación
          baseEntrada = 0
          baseSalida = 0
          if EntradaSN.value == "": #Validación para cuando el textfield de entrada esté vacio
               requerimientosalerta = ft.AlertDialog(title=ft.Text("Falta el valor de entrada"),
                                  content=ft.Text("No se ha ingresado ningún número o valor de entrada.")
                                  )
               page.dialog = requerimientosalerta
               requerimientosalerta.open = True
               page.update()
          
          elif str(DDEntrada.value) == str(None) or str(DDSalida.value) == str(None): #Validación para cuando los Dropdown no tienen alguna base seleccionada
              requerimientosalerta = ft.AlertDialog(title=ft.Text("Faltan bases numéricas por definir."),
                                  content=ft.Text("Revisa las bases de entrada y salida.")
                                  )
              page.dialog = requerimientosalerta
              requerimientosalerta.open = True
              page.update()
          
          else:
               SalidaSN.value = funciones.SNexe(str(DDEntrada.value),str(DDSalida.value),EntradaSN.value)
               page.update()

    OperarSN = ft.ElevatedButton( #Botón de operar que al presionar se ejecutara la función anterior para la operación
         "Operar",
         bgcolor= "#4A5C6A",
         color= "#9BA8AB",
         on_click= operacionSN
    )

    def LimpiarSistemaNumerico(e): #Función que limpia los textfield de entrada y de salida
         EntradaSN.value = ""
         SalidaSN.value = ""
         page.update()

    LimpiarSN = ft.ElevatedButton( #Botón de limpiar que al presionar ejecutará la función anterior de limpieza
         "Limpiar",
         bgcolor= "#4A5C6A",
         color= "#9BA8AB",
         on_click= LimpiarSistemaNumerico
    )

    #Rows y Columns donde se encontrarán contenido todos los elementos a usar (Botones, Texfields, Dropdowns, etc)
    rsn1 = ft.Row(controls=[EntradaSN,DDEntrada],
                alignment="CENTER")
    rsn2 = ft.Row(controls=[SalidaSN,DDSalida],
                alignment="CENTER")
    rsn3 = ft.Row(controls=[TituloSN,infoSN],
                alignment="CENTER",
                spacing=0)
    rsn4 = ft.Row(controls=[OperarSN,LimpiarSN],
                alignment="CENTER",
                spacing= 40)
    csn1 = ft.Column(controls=[rsn3,rsn1,rsn2,rsn4],
                   alignment="CENTER",
                   spacing=80
                   )
    
    #Contenedor principal donde se encontrará todo el contenido del programa
    contenedorSistema = ft.Container(
         csn1,
         height=600,
         width=600,
         bgcolor= "#11212D",
         border_radius= 55,
         )

    """
    GAUSS SEIDEL:
    Parte del código que hace referencia al programa del sistema de ecuaciones resuelto por Gauss Seidel

    Este programa se dividió en 3 contenedores principales
    (uno para la matriz A, otro para el vector B y uno último para el Vector X de resultados)
    """
    
    "CONTENEDOR 1: Matriz A"

    titulomatrices = ft.Text("Ingreso de Matriz A", #Se define el titulo para el primer contenedor
                       theme_style=ft.TextThemeStyle.TITLE_LARGE,
                       weight=ft.FontWeight.BOLD,
                       size=30,
                       color="#9BA8AB")
    
    def cambiomatriza(e): #Función que se ejecuta cuando hay un cambio en el dropdown referente al tamaño de la matriz
         
         columnatemporal = disenomatriz(int(ddtam.value)) #Se obtiene la matriz A con el nuevo tamaño
         columnaMatrizA.controls = columnatemporal #Se muestra la matriz A con el nuevo tamaño

         vectorBtemporal = disenovector(int(ddtam.value),"#253745","9BA8AB",False) #Se obtiene el vector B con el nuevo tamaño
         vectorBcolumna.controls = vectorBtemporal #Se muestra el vector B con el nuevo tamaño

         vectorXtemporal = disenovector(int(ddtam.value),"#11212D","#9BA8AB",True) #Se obtiene el vector X con el nuevo tamaño
         vectorXcolumna.controls = vectorXtemporal #Se muestra el vector X con el nuevo tamaño

         page.update()
     
    ddtam = ft.Dropdown(width=75, #Se define el dropdown para la elección del tamaño de la matriz, al cambiar ejecutará la función anterior
                           options=[
                                ft.dropdown.Option("2"),
                                ft.dropdown.Option("3"),
                                ft.dropdown.Option("4"),
                                ft.dropdown.Option("5"),
                                ],
                            label="Tam",
                            border_color="#9BA8AB",
                            on_change=cambiomatriza,
                            value="3")
    
    filatitulo= ft.Row(controls=[titulomatrices,ddtam], #Se define el Row que se ubicará en la parte superior del Container 1 con el Titulo y el Dropdow para la elección del tamaño
                  alignment="CENTER",
                  spacing=80)
    
    def limitarcaracteres(e): #Función que se le otorgará a cada uno de los TextFields de la matriz y de los vectores para controlar el límite de caracteres de los mismos
         if len(e.control.value) > 3:
              e.control.value = e.control.value[:3]
         page.update()

    def disenomatriz(n): #Función donde se diseña según un número N todos los textfields donde serán ingresados los elementos de la matriz
         fila = [] #Fila que contendrá N textfields
         columna = [] #Columnas que contendrá N filas
         for i in range(n):
              fila = [] #Se vacia la lista fila
              for j in range(n):
                    fila.append(ft.TextField(border_radius=10000, #Se agregan N textfields a la lista
                        height = 60,
                        width = 100,
                        bgcolor="#9BA8AB",
                        color="#000000",
                        border_color="#9BA8AB",
                        on_change=limitarcaracteres,
                        cursor_color= "black",
                        input_filter=ft.InputFilter(allow=True,regex_string=[0,1,2,3,4,5,6,7,8,9],replacement_string="")
                        ))
              columna.append(ft.Row(controls=fila, #Se agregan N filas con N texfields a la lista
                                     alignment="CENTER"))
         return columna #Se retorna la lista de columnas
    
    columnatemporal = disenomatriz(3) #Se diseña por defecto una matriz 3x3
    columnaMatrizA = ft.Column(controls=columnatemporal, #Se muestra la matriz por defecto
                               alignment="CENTER",
                               height=400,)
    
    def verificacionMatriz(): #Función que verifica si todos los datos ingresados a la matriz son correctos
         for i in range(int(ddtam.value)):
             if vectorBcolumna.controls[i].value == "": return False
             try: float(vectorBcolumna.controls[i].value)
             except ValueError: return False
             for j in range(int(ddtam.value)):
                  if columnaMatrizA.controls[i].controls[j].value == "": return False
                  try: float(vectorBcolumna.controls[i].value)
                  except ValueError: return False
         return True
    
    def operacionMatriz(e): #Función que ejecutará el botón de operación, acá se llamaran todas las funciones para la operaciones de Gauss Seidel
         if verificacionMatriz(): #Si la verificación de valores de entrada retorna 'True' se ejecutara la operación correctamenta
               listamatriz = []
               listavector = []
               listaresultados = []
               for i in range(int(ddtam.value)):
                    listavector.append(float(vectorBcolumna.controls[i].value))
                    for j in range(int(ddtam.value)):
                         listamatriz.append(float(columnaMatrizA.controls[i].controls[j].value))
               resultadolista = []
               resultadolista = funciones.GaussSeidel(funciones.creacionMatriz(int(ddtam.value),listamatriz),funciones.creacionVector(int(ddtam.value),listavector))
               for i in range(len(resultadolista)):
                    stringtemporal = str(resultadolista[i])
                    stringtemporal = str(round(float(stringtemporal),1))
                    vectorXcolumna.controls[i].value = stringtemporal
               page.update()
         else: #Si la verificación de valores de entrada retorna 'False' se ejecutará el siguiente dialogo de alerta
              matrizalerta = ft.AlertDialog(title=ft.Text("Error en los valores de entrada."),
                                  content=ft.Text("Hay algún elemento de la 'matriz A' o de el 'Vector B' faltante o erróneo")
                                  )
              page.dialog = matrizalerta
              matrizalerta.open = True
              page.update()

    OperarMatriz = ft.ElevatedButton( #Botón que ejecutara la función anterior para realizar la operación Gauss Seidel
         "Operar",
         bgcolor= "#11212D",
         color= "#9BA8AB",
         on_click=operacionMatriz
    )

    def llenadoMatriz(e): #Función que será ejecutado por el botón 'Llenar' y llenará la matriz con valores aleatorios
         for i in range(int(ddtam.value)):
              vectorBcolumna.controls[i].value = round(random.randint(1,10),1)
              vectorXcolumna.controls[i].value = ""
              for j in range(int(ddtam.value)):
                   columnaMatrizA.controls[i].controls[j].value = round(random.randint(1,10),1)
         page.update()

    LlenarMatriz = ft.ElevatedButton( #Botón que ejecutará la función anterior para el llenado aleatorio de la matriz
         "Llenar",
         bgcolor= "#11212D",
         color= "#9BA8AB",
         on_click=llenadoMatriz
    )

    def limpiezaMatriz(e): #Función que limpiará todos los TEXTFIELDS que forman la matriz y los 2 vectores, será ejecutado por el botón de 'Limpiar'
         for i in range(int(ddtam.value)):
              vectorBcolumna.controls[i].value = ""
              vectorXcolumna.controls[i].value = ""
              for j in range(int(ddtam.value)):
                   columnaMatrizA.controls[i].controls[j].value = ""
         page.update()

    LimpiarMatriz = ft.ElevatedButton( #Botón que ejecuta la función anterior para la limpieza de la matriz
         "Limpiar",
         bgcolor= "#11212D",
         color= "#9BA8AB",
         on_click=limpiezaMatriz
    )

    infoDialogMatriz = ft.AlertDialog(title=ft.Text("Resolucion sistema de ecuaciones por metodo Gauss Seidel"), #Dialogo/Alerta que contiene información del programa Gauss Seidel
                                  content=ft.Text("Teniendo una operación 'Ax = B', siendo A una matriz de tamaño NxN y B un vector de tamaño N, se encontrarán los valores del 'vector X' de tamaño N a través del metodo Gauss Seidel")
                                  )
    
    def abrirInfoMatriz(e): #Función que ejecuta el botón de información para abrir el dialogo/alerta con toda la info del programa
         page.dialog = infoDialogMatriz
         infoDialogMatriz.open = True
         page.update()

    infoMatriz = ft.IconButton( #Botón de información que ejecutará la función anterior
         icon= ft.icons.INFO_ROUNDED,
         icon_color= "#11212D",
         on_click= abrirInfoMatriz
    )

    #Fila o 'Row' donde se encuentran todos los botones
    filabotones = ft.Row(controls=[infoMatriz,OperarMatriz,LlenarMatriz,LimpiarMatriz, ft.Container(padding=ft.padding.only,width=42,),],
                         alignment="CENTER",)
    
    "CONTENEDOR 2: Vector B"

    tituloc2 = ft.Text("Ingreso de Vector B", #Se define el titulo para el contenedor 2
                       theme_style=ft.TextThemeStyle.TITLE_LARGE,
                       weight=ft.FontWeight.BOLD,
                       size=30,
                       color="#9BA8AB",
                       text_align= ft.TextAlign.CENTER,
                       width=500)
    
    def disenovector(n,color,letra,bool): #Función que diseña un vector de textfields
         columna = []
         for i in range(n):
              columna.append(ft.TextField(border_radius=10000,
                        height = 60,
                        width = 250,
                        bgcolor=color,
                        color=letra,
                        border_color=color,
                        on_change=limitarcaracteres,
                        read_only= bool,
                        input_filter=ft.InputFilter(allow=True,regex_string=[0,1,2,3,4,5,6,7,8,9],replacement_string="")
                        ))
         return columna
    
    vectorBtemporal = disenovector(3,"#253745","#9BA8AB",False) #Se obtiene el vector de TextFields, para el vector B

    vectorBcolumna = ft.Column(controls=vectorBtemporal, #Se ingresa el vector de TextFields en un Column para despues mostrarse (Vector B)
                               alignment="CENTER",
                               height=450,
                               width=400,
                               horizontal_alignment= "CENTER")
    

    "CONTENEDOR 3: Vector X"

    tituloc3 = ft.Text("Resultados Vector X", #Titulo definido para el contenedor 3
                       theme_style=ft.TextThemeStyle.TITLE_LARGE,
                       weight=ft.FontWeight.BOLD,
                       size=30,
                       color="#9BA8AB",
                       text_align= ft.TextAlign.CENTER,
                       width=500)
    
    vectorXtemporal = disenovector(3,"#11212D","#9BA8AB",True) #Se obtiene el vector de Textfields, para el vector X, reutilizando la misma función del vector B

    vectorXcolumna = ft.Column(controls=vectorXtemporal, #Se ingresa el vector de TextFields en un Column para despues mostrarse (Vector X)
                               alignment="CENTER",
                               height=450,
                               width=400,
                               horizontal_alignment= "CENTER")
    
    "PARTE DEL CÓDIGO DEL PROGRAMA DE GAUSS SEIDEL DONDE SE DEFINIRÁN Y ACOMODARÁN LOS CONTENEDORES"

    columnaPrincipalContenedor1 = ft.Column(controls=[filatitulo,columnaMatrizA,filabotones], #Se define una columna donde estarán todos los elementos del contenedor 1
                          alignment="CENTER",
                          horizontal_alignment= "CENTER")
    
    contenedor1 = ft.Container( #Se define el contenedor 1 con todos sus elementos
         columnaPrincipalContenedor1,
         height=600,
         width=600,
         bgcolor= "#4A5C6A",
         border_radius= 55,
         )
    
    columnaC2 = ft.Column(controls=[tituloc2,vectorBcolumna], #Se define una columna donde estarán todos los elementos del contenedor 2
                          alignment="CENTER")
    
    contenedor2 = ft.Container( #Se define el contenedor 2 con todos sus elementos
         columnaC2,
         height=600,
         width=300,
         bgcolor= "#11212D",
         border_radius= 55,
         )
    
    columnaC3 = ft.Column(controls=[tituloc3,vectorXcolumna], #Se define una columna donde estarán todos los elementos del contenedor 3
                          alignment="CENTER")
    
    contenedor3 = ft.Container( #Se define el contenedor 3 con todos sus elementos
         columnaC3,
         height=600,
         width=300,
         bgcolor= "#253745",
         border_radius= 55,
         )
    
    filaPrincipal = ft.Row( #Se define la fila principal con todos los contenedores principales
         controls = [contenedor1,contenedor2,contenedor3],
         alignment="CENTER"
         )

    """
    ANIMACIÓN DE TRANSICIÓN:
    Parte del código donde se define la transición para el cambio entre los programas de 'Gauss Seidel' y 'Sistemas Numéricos'
    """
    transicioncambio = ft.AnimatedSwitcher( #Animación que su contenido va a variar entre los 2 programas, cuando se haga el cambio ejecutará la animación de desvanecimiento
        filaPrincipal,
        transition=ft.AnimatedSwitcherTransition.SCALE,
        duration=500,
        reverse_duration=200,
        switch_in_curve=ft.AnimationCurve.LINEAR,
        switch_out_curve=ft.AnimationCurve.LINEAR,
    )

    """
    AÑADIDOS DE LA INTERFAZ:
    Parte del código donde se hará el añadido de elementos a la interfaz
    """

    page.add(
        ft.Row([BasemenuOpciones]), #Se añade el botón/display/opciones desplegables para el cambio entre programas

        ft.Container( #Se añade una linea decorativa
             height=5,
             bgcolor= "#9BA8AB",
             border_radius=10,
        ),

        ft.Container( #Se añade un container invisible para dar un espaciado
         padding= ft.padding.only,
         height=35,
        ),

        transicioncambio #Se añade la animación que va a variar entre los programas de 'Gauss Seidel' y 'Sistemas Numéricos'
    )


    page.update() #Se hace la actualización de la interfaz

ft.app(target=main) #Se inicializa la aplicación
