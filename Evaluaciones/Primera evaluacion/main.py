import flet as ft
import random
import funciones

#Definicion Pagina
def main(page: ft.Page):
    #Caracteristicas pagina
    page.title = "1er Evaluación de Calculo Numérico - Alejandro Chávez (32.278.392)"
    page.bgcolor = '#06141B'
    page.window_resizable = False
    page.window_height = 1024
    page.window_width = 1440
    page.window_maximized = True
    page.horizontal_alignment = "CENTER"

    ########################## FUNCIONES DE CAMBIO DE PROGRAMA ###############################

    def MatricesEscenaCambio(e):
        if str(DisplayOpcionActual.value) == str(e.control.content.value) + " ▾":
            pass
        else:
            cambioDisplayOpcion(e)
            transicioncambio.content = filaPrincipal
            transicioncambio.update()
            page.update()

    def SistemasEscenaCambio(e):
        if str(DisplayOpcionActual.value) == str(e.control.content.value) + " ▾":
            pass
        else:
            cambioDisplayOpcion(e)
            transicioncambio.content = contenedorSistema
            transicioncambio.update()
            page.update()

    

    ################# MENUBAR DE CAMBIO DE PROGRAMA ########################################

    DisplayOpcionActual = ft.Text("Gauss Seidel ▾",
                                  color="#9BA8AB",
                                  theme_style=ft.TextThemeStyle.TITLE_LARGE,
                                  weight=ft.FontWeight.BOLD,
                                  size=30
                                  )
    
    def cambioDisplayOpcion(e):
            DisplayOpcionActual.value = str(e.control.content.value) + " ▾"
            page.update()
    MenuOpciones = ft.SubmenuButton(
                content= DisplayOpcionActual,
                controls=[
                    ft.MenuItemButton(
                        content=ft.Text("Gauss Seidel"),
                        on_click= MatricesEscenaCambio
                    ),
                    ft.MenuItemButton(
                        content=ft.Text("Sistemas numéricos"),
                        on_click = SistemasEscenaCambio
                    )
                ]
    )

    BasemenuOpciones = ft.MenuBar(
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

    ######################################################################################
    ###################### SISTEMAS NUMERICOS ############################################
    ######################################################################################
    TituloSN = ft.Text("Traducción de Sistemas Numéricos",
                       theme_style=ft.TextThemeStyle.TITLE_LARGE,
                       weight=ft.FontWeight.BOLD,
                       size=30,
                       color="#9BA8AB"
                       )
         

    def CambioDDSalida(e):
         SalidaSN.value = ""
         page.update()
    EntradaSN = ft.TextField(
         label="Número de Entrada",
         width= 370,
         border_color= "#4A5C6A",
         read_only= False,
         input_filter=ft.InputFilter(allow=True,regex_string=[0,1,2,3,4,5,6,7,8,9],replacement_string=""),
         on_change=CambioDDSalida
    )

    SalidaSN = ft.TextField(
         label="Número de Salida",
         width= 370,
         border_color= "#4A5C6A",
         read_only= True
    )

    def CambioDDEntrada(e):
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
    DDEntrada = ft.Dropdown(width=100,
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

    DDSalida = ft.Dropdown(width=100,
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
                            on_change= CambioDDSalida,
                            value="BIN"
                           )
    
    infoDialogSN = ft.AlertDialog(title=ft.Text("Bases de Sistemas Numéricos"),
                                  content=ft.Text("DEC = Decimal (Base 10)\nBIN = Binario (Base 2)\nTER = Terciario (Base 3)\nCUA = Cuaternario(Base 4)\nOCT = Octal (Base 8)\nHEX = Hexadecimal (Base 16)")
                                  )
    def abrirInfoSN(e):
         page.dialog = infoDialogSN
         infoDialogSN.open = True
         page.update()
    infoSN = ft.IconButton(
         icon= ft.icons.INFO_ROUNDED,
         icon_color= "#4A5C6A",
         on_click= abrirInfoSN
    )

    def operacionSN(e):
          baseEntrada = 0
          baseSalida = 0
          if EntradaSN.value == "":
               requerimientosalerta = ft.AlertDialog(title=ft.Text("Falta el valor de entrada"),
                                  content=ft.Text("No se ha ingresado ningún número o valor de entrada.")
                                  )
               page.dialog = requerimientosalerta
               requerimientosalerta.open = True
               page.update()
          elif str(DDEntrada.value) == str(None) or str(DDSalida.value) == str(None):
              requerimientosalerta = ft.AlertDialog(title=ft.Text("Faltan bases numéricas por definir."),
                                  content=ft.Text("Revisa las bases de entrada y salida.")
                                  )
              page.dialog = requerimientosalerta
              requerimientosalerta.open = True
              page.update()
          else:
               if str(DDEntrada.value) == "DEC":
                   baseEntrada = 10
                   valorEntrada = EntradaSN.value
               elif str(DDEntrada.value) == "BIN":
                   baseEntrada = 2
                   valorEntrada = EntradaSN.value
               elif str(DDEntrada.value) == "TER":
                   baseEntrada = 3
                   valorEntrada = EntradaSN.value
               elif str(DDEntrada.value) == "CUA":
                   baseEntrada = 4
                   valorEntrada = EntradaSN.value
               elif str(DDEntrada.value) == "OCT":
                   baseEntrada = 8
                   valorEntrada = EntradaSN.value
               elif str(DDEntrada.value) == "HEX":
                   baseEntrada = 16
                   valorEntrada = EntradaSN.value

               if str(DDSalida.value) == "DEC":
                    baseSalida = 10
               elif str(DDSalida.value) == "BIN":
                   baseSalida = 2
               elif str(DDSalida.value) == "TER":
                   baseSalida = 3
               elif str(DDSalida.value) == "CUA":
                   baseSalida = 4
               elif str(DDSalida.value) == "OCT":
                   baseSalida = 8
               elif str(DDSalida.value) == "HEX":
                   baseSalida = 16

               if baseEntrada == 10:
                    if baseSalida == 10:
                         SalidaSN.value = str(valorEntrada)
                         page.update()
                    elif baseSalida == 16:
                         cadena = hex(int(valorEntrada))
                         cadena = cadena[2:]
                         cadena = cadena.upper()
                         SalidaSN.value = cadena
                         page.update()
                    else:
                        SalidaSN.value = funciones.fromDEC(valorEntrada,baseSalida)
                        page.update()
               else:
                    valorEntrada = funciones.toDEC(valorEntrada,baseEntrada)
                    if baseSalida == 10:
                         SalidaSN.value = str(valorEntrada)
                         page.update()
                    elif baseSalida == 16:
                         cadena = hex(int(valorEntrada))
                         cadena = cadena[2:]
                         cadena = cadena.upper()
                         SalidaSN.value = cadena
                         page.update()
                    else:
                        SalidaSN.value = funciones.fromDEC(valorEntrada,baseSalida)
                        page.update()
               
               
               page.update()
    OperarSN = ft.ElevatedButton(
         "Operar",
         bgcolor= "#4A5C6A",
         color= "#9BA8AB",
         on_click= operacionSN
    )

    def LimpiarSistemaNumerico(e):
         EntradaSN.value = ""
         SalidaSN.value = ""
         page.update()
    LimpiarSN = ft.ElevatedButton(
         "Limpiar",
         bgcolor= "#4A5C6A",
         color= "#9BA8AB",
         on_click= LimpiarSistemaNumerico
    )

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

    contenedorSistema = ft.Container(
         csn1,
         height=600,
         width=600,
         bgcolor= "#11212D",
         border_radius= 55,
         )

    ######################################################################################
    ############################# MATRICES ###############################################
    ######################################################################################
    ### Contenedor 1
    #Fila del titulo
    titulomatrices = ft.Text("Ingreso de Matriz A",
                       theme_style=ft.TextThemeStyle.TITLE_LARGE,
                       weight=ft.FontWeight.BOLD,
                       size=30,
                       color="#9BA8AB")
    def cambiomatriza(e):
         columnatemporal = disenotamano(int(ddtam.value))
         columnaMatrizA.controls = columnatemporal
         vectorBtemporal = disenovector(int(ddtam.value),"#253745","9BA8AB",False)
         vectorBcolumna.controls = vectorBtemporal
         vectorXtemporal = disenovector(int(ddtam.value),"#11212D","#9BA8AB",True)
         vectorXcolumna.controls = vectorXtemporal
         page.update()
    ddtam = ft.Dropdown(width=75,
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
    filatitulo= ft.Row(controls=[titulomatrices,ddtam],
                  alignment="CENTER",
                  spacing=80)
    #Diseño de Matriz
    def limitarcaracteres(e):
         if len(e.control.value) > 7:
              e.control.value = e.control.value[:7]
         page.update()

    def disenotamano(n):
         filas = []
         columnas = []
         for i in range(n):
              filas = []
              for j in range(n):
                    filas.append(ft.TextField(border_radius=10000,
                        height = 60,
                        width = 100,
                        bgcolor="#9BA8AB",
                        color="#000000",
                        border_color="#9BA8AB",
                        on_change=limitarcaracteres,
                        cursor_color= "black",
                        input_filter=ft.InputFilter(allow=True,regex_string=["-",".",0,1,2,3,4,5,6,7,8,9],replacement_string="")
                        ))
              columnas.append(ft.Row(controls=filas,
                                     alignment="CENTER"))
         return columnas
    columnatemporal = disenotamano(3)
    columnaMatrizA = ft.Column(controls=columnatemporal,
                               alignment="CENTER",
                               height=400,)
    
    #Fila de botones
    def verificacionMatriz():
         for i in range(int(ddtam.value)):
             if vectorBcolumna.controls[i].value == "": return False
             try: float(vectorBcolumna.controls[i].value)
             except ValueError: return False
             for j in range(int(ddtam.value)):
                  if columnaMatrizA.controls[i].controls[j].value == "": return False
                  try: float(vectorBcolumna.controls[i].value)
                  except ValueError: return False
         return True
    def operacionMatriz(e):
         if verificacionMatriz():
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
         else:
              matrizalerta = ft.AlertDialog(title=ft.Text("Error en los valores de entrada."),
                                  content=ft.Text("Hay algún elemento de la 'matriz A' o de el 'Vector B' faltante o erróneo")
                                  )
              page.dialog = matrizalerta
              matrizalerta.open = True
              page.update()
    OperarMatriz = ft.ElevatedButton(
         "Operar",
         bgcolor= "#11212D",
         color= "#9BA8AB",
         on_click=operacionMatriz
    )
    def llenadoMatriz(e):
         for i in range(int(ddtam.value)):
              vectorBcolumna.controls[i].value = round(random.randint(1,10),1)
              vectorXcolumna.controls[i].value = ""
              for j in range(int(ddtam.value)):
                   columnaMatrizA.controls[i].controls[j].value = round(random.randint(1,10),1)
         page.update()
    LlenarMatriz = ft.ElevatedButton(
         "Llenar",
         bgcolor= "#11212D",
         color= "#9BA8AB",
         on_click=llenadoMatriz
    )
    def limpiezaMatriz(e):
         for i in range(int(ddtam.value)):
              vectorBcolumna.controls[i].value = ""
              vectorXcolumna.controls[i].value = ""
              for j in range(int(ddtam.value)):
                   columnaMatrizA.controls[i].controls[j].value = ""
         page.update()
    LimpiarMatriz = ft.ElevatedButton(
         "Limpiar",
         bgcolor= "#11212D",
         color= "#9BA8AB",
         on_click=limpiezaMatriz
    )

    infoDialogMatriz = ft.AlertDialog(title=ft.Text("Resolucion sistema de ecuaciones por metodo Gauss Seidel"),
                                  content=ft.Text("Teniendo una operación 'Ax = B', siendo A una matriz de tamaño NxN y B un vector de tamaño N, se encontrarán los valores del 'vector X' de tamaño N a través del metodo Gauss Seidel")
                                  )
    def abrirInfoMatriz(e):
         page.dialog = infoDialogMatriz
         infoDialogMatriz.open = True
         page.update()
    infoMatriz = ft.IconButton(
         icon= ft.icons.INFO_ROUNDED,
         icon_color= "#11212D",
         on_click= abrirInfoMatriz
    )

    filabotones = ft.Row(controls=[infoMatriz,OperarMatriz,LlenarMatriz,LimpiarMatriz, ft.Container(padding=ft.padding.only,width=42,),],
                         alignment="CENTER",)
    
    #### Contenedor 2
    tituloc2 = ft.Text("Ingreso de Vector B",
                       theme_style=ft.TextThemeStyle.TITLE_LARGE,
                       weight=ft.FontWeight.BOLD,
                       size=30,
                       color="#9BA8AB",
                       text_align= ft.TextAlign.CENTER,
                       width=500)
    def disenovector(n,color,letra,bool):
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
                        input_filter=ft.InputFilter(allow=True,regex_string=["-",".",0,1,2,3,4,5,6,7,8,9],replacement_string="")
                        ))
         return columna
    vectorBtemporal = disenovector(3,"#253745","#9BA8AB",False)
    vectorBcolumna = ft.Column(controls=vectorBtemporal,
                               alignment="CENTER",
                               height=450,
                               width=400,
                               horizontal_alignment= "CENTER")
    

    #Contenedor 3
    tituloc3 = ft.Text("Resultados Vector X",
                       theme_style=ft.TextThemeStyle.TITLE_LARGE,
                       weight=ft.FontWeight.BOLD,
                       size=30,
                       color="#9BA8AB",
                       text_align= ft.TextAlign.CENTER,
                       width=500)
    
    vectorXtemporal = disenovector(3,"#11212D","#9BA8AB",True)
    vectorXcolumna = ft.Column(controls=vectorXtemporal,
                               alignment="CENTER",
                               height=450,
                               width=400,
                               horizontal_alignment= "CENTER")
    #Contenedores principales
    columnaPrincipalContenedor1 = ft.Column(controls=[filatitulo,columnaMatrizA,filabotones],
                          alignment="CENTER",
                          horizontal_alignment= "CENTER")
    contenedor1 = ft.Container(
         columnaPrincipalContenedor1,
         height=600,
         width=600,
         bgcolor= "#4A5C6A",
         border_radius= 55,
         )
    
    columnaC2 = ft.Column(controls=[tituloc2,vectorBcolumna],
                          alignment="CENTER")
    contenedor2 = ft.Container(
         columnaC2,
         height=600,
         width=300,
         bgcolor= "#11212D",
         border_radius= 55,
         )
    
    columnaC3 = ft.Column(controls=[tituloc3,vectorXcolumna],
                          alignment="CENTER")
    contenedor3 = ft.Container(
         columnaC3,
         height=600,
         width=300,
         bgcolor= "#253745",
         border_radius= 55,
         )
    filaPrincipal = ft.Row(
         controls = [contenedor1,contenedor2,contenedor3],
         alignment="CENTER"
         )

    ##################################### Animacion
    transicioncambio = ft.AnimatedSwitcher(
        filaPrincipal,
        transition=ft.AnimatedSwitcherTransition.FADE  ,
        duration=1000,
        reverse_duration=200,
        switch_in_curve=ft.AnimationCurve.LINEAR,
        switch_out_curve=ft.AnimationCurve.LINEAR,
    )

    ######################################################################################
    ################## AÑADIDOS A LA PAGINA ##############################################
    ######################################################################################

    page.add(
        ft.Row([BasemenuOpciones]),

        ft.Container(
             height=5,
             bgcolor= "#9BA8AB",
             border_radius=10,
        ),

        ft.Container(
         padding= ft.padding.only,
         height=35,
        ),

        transicioncambio
    )


    page.update()  

ft.app(target=main)