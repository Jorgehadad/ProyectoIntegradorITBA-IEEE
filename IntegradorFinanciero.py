import pandas as pd
import requests
import matplotlib.pyplot as plt
import numpy as np

#-------------DESCARGA DE ARCHIVOS -------------------
def wget(url):
    r = requests.get(url, allow_redirects=True)
    with open(url[url.rfind('/') + 1::], 'wb') as f:
        f.write(r.content)


#wget ("https://raw.githubusercontent.com/IEEESBITBA/Curso-Python/master/Clase_4_datos/AMZN.csv")
#wget ("https://raw.githubusercontent.com/IEEESBITBA/Curso-Python/master/Clase_4_datos/GOOGLE.csv")


#------------- FIN DESCARGA DE ARCHIVOS -------------------


#--------------ASIGNACIÓN DE ARCHIVOS E INDEX --------------
archivoA= pd.read_csv("AMZN.BA.csv") 
archivoM = pd.read_csv("GOOGL.BA.csv")
archivoMic = pd.read_csv("MSFT.BA.csv")
archivoAp = pd.read_csv("AAPL.BA.csv")

archivoA= pd.DataFrame(archivoA)
archivoM= pd.DataFrame(archivoM)
archivoMic= pd.DataFrame(archivoMic)
archivoAp= pd.DataFrame(archivoAp)


pd.set_option("display.max_columns", 10)
data = archivoA.to_dict("list") 
# "list" significa que vamos a almacenar a cada columna como una lista con su contenido
#print (archivo)#archivo.info()
#--------------FIN ASIGNACIÓN DE ARCHIVOS E INDEX --------------


#------------------DICCIONARIOS--------------------------
empresas = {
    "Nombres" : ["Amazón", "Google", "Microsoft", "Apple"],
    "Abreviaciones": ["AMZN", "GOOGL","MSFT","AAPL"],
    "IdEmpresa": ["1", "2", "3", "4"],
    "Archivos": [archivoA, archivoM, archivoMic, archivoAp]
}

dicArch = {
    "1" : archivoA,
    "2" : archivoM,
    "3" : archivoMic,
    "4" : archivoAp
}

#...................FIN DICCIONARIOS------------

# ------------------------ MENU ---------------------------
print ("|----------------------------------------------------------------|")
print ("|-----------------------MENU-------------------------------------|")
print ("|Ingrese la opción segun lo que desea realizar :D                |")
print ("|OPCIONES:                                                       |")
print ("|1) Obtener analisis comparativo (+grafico) de dos empresas      |")
print ("|2) Calcular, graficar y guardar las intersecciones del precio   |")
print ("|de dos empresas.                                                |")
print ("|3) Graficar la derivada discreta de una empresa.                |")
print ("|4) Obtener excel de cuál empresa creció más y cuál menos en     |")
print ("|Octubre, septiembre y en los últimos 12 meses.                  |")
print ("|5) Obtener comparación de Amazón y Google con Intersecciones.   |")  
print ("|----------------------------------------------------------------|")



# ------------------------ MENU ---------------------------

opt= 5 #int(input ())

#-----------------------METODOS---------------------------

def op1CompararEmpresas(comp1, comp2, empresas):
    if comp1 in empresas["IdEmpresa"]:
        empresa1 = dicArch.get(comp1)
        valores1 = empresa1 [["Date", "Open", "Close", "High", "Low"]]
        print ("1ER EMPRESA SELECCIONADA: ")
        print (valores1.tail())                
        if comp2 in empresas["IdEmpresa"]:
            empresa2 = dicArch.get(comp2)
            valores2 = empresa2 [["Date", "Open", "Close", "High", "Low"]]
            print ("2DA EMPRESA SELECCIONADA: ")
            print (valores2.tail()) 
    generarGraficoDoble (empresa1, empresa2)
    return 

def op2Interseccion(comp1, comp2, empresas):
    if comp1 in empresas["IdEmpresa"]:
        empresa1 = dicArch.get(comp1)
        valores1 = empresa1 [["Date", "Open"]]               
        if comp2 in empresas["IdEmpresa"]:
            empresa2 = dicArch.get(comp2)
            valores2 = empresa2 [["Date", "Open"]]
    intersec = (valores1 [ (valores1["Open"]>0) & (valores2["Open"]>0) ])
    print ("Las intersecciones de precio entre ambas empresas son: \n")
    print (intersec)
    #llamamos a generar el excel
    generarExcel (intersec, "Interseccion2Empresas.xlsx")
    #ahora vamos a mostrar el grafico y guardar el jpg
    generarGraficoSimple (intersec)
    return


def generarExcel (archivo, texto):
    # Con pd.DataFrame podemos generar una variable tipo DataFrame
    # Recordemos que DataFrame es el tipo de dato que usa pandas
    dataFrame = pd.DataFrame(archivo) 
    #print(dataFrame)
    # Exportamos la información a un archivo llamado "personas.xlsx"
    dataFrame.to_excel(str (texto)) 
    return

def generarGraficoDiscreta (archivo):
    plt.plot (archivo["Date"], archivo["Open"])
    plt.title("Gráfico de DERIVADA DISCRETA de Empresa1")
    plt.xlabel('Fecha')
    plt.ylabel('Precio')
    plt.grid()
    plt.xticks(archivo["Date"][0::10], rotation=60)
    plt.savefig ("Grafico Derivada Discreta.jpg")
    plt.show ()
    return

def generarGraficoSimple (archivo):
    #ax= valores.plot(x = "Date" , y= "Open")
    plt.plot (archivo["Date"], archivo["Open"])
    plt.title("Gráfico INTERSECCIÓN Empresa1 y Empresa2")
    plt.xlabel('Fecha')
    plt.ylabel('Precio')
    plt.grid()
    plt.xticks(archivo["Date"][0::20], rotation=60)
    plt.savefig ("Grafico Intersección.jpg")
    plt.show ()
    return
   
def generarGraficoDoble (ArchEmpresa1, ArchEmpresa2):
    plt.figure(figsize=(12, 4))

    plt.subplot(1, 2, 1)
    plt.title("Gráfico Empresa1")
    plt.plot(ArchEmpresa1 ["Date"], ArchEmpresa1 ["Open"]) # graficamos función 1
    plt.xlabel('Fecha')
    plt.ylabel('Precio')
    plt.xticks(ArchEmpresa1["Date"][0::20], rotation=60)
    plt.grid()

    plt.subplot(1, 2, 2)
    plt.title("Gráfico Empresa2")
    plt.plot(ArchEmpresa2["Date"], ArchEmpresa2["Open"], 'r-.') # graficamos función 2
    plt.xlabel('Fecha')
    plt.ylabel('Precio')
    plt.xticks(ArchEmpresa2["Date"][0::20], rotation=60)
    #plt.axis([0, 3, -1, 1])
    plt.grid()
    plt.savefig ("Grafico Doble Comparación.jpg")
    plt.show()
    return

def graficarInterComplejo (google, amazon):
    maxG = len(google['Date'])-1
    maxA = len(amazon['Date'])-1
    plt.figure(figsize=(14, 6))
    crucex = []
    crucey = []
    gx = [google["Date"][0]]
    gy = [google["Open"][0]]
    ax = [amazon["Date"][0]]
    ay = [amazon["Open"][0]]

    # Empiezan con el valor del primer dia
    opc = input('Desea establecer fechas limite? s/n')

    if opc == 's':
        if google["Date"][0] > amazon["Date"][0]:
            print('La fecha inicial minima posible es: ', google["Date"][0])
        else:
            print('La fecha inicial minima posible es: ', amazon["Date"][0])
        fechai = str(input('Ingrese la fecha inicial (AAAA-MM-DD)'))


        if google["Date"][maxG] > amazon["Date"][maxA]:
            print('La fecha final maxima posible es: ', amazon["Date"][len(amazon["Date"])-1])
        else:
            print('La fecha final maxima posible es: ', google["Date"][len(google["Date"])-1])

        fechaf = str(input('Ingrese la fecha final (AAAA-MM-DD)'))
        we = int(0)
        x = int(0)
        while google["Date"][we] != fechai:
            we += 1
        while google["Date"][x] != fechaf:
            x += 1

        for y in range(we, x):
            gx.append(google["Date"][y])
            gy.append(google["Open"][y])
            ax.append(amazon["Date"][y])
            ay.append(amazon["Open"][y])

            if (ay[y] == gy[y]) or (ay[y] > gy[y] and ay[y - 1] < gy[y - 1]) or (ay[y] < gy[y] and ay[y - 1] > gy[y - 1]):
                crucex.append(gx[y])
                crucey.append(gy[y])



    else:

        for i in range(1, len(google["Date"])):  # range empieza desde 1 en vez de 0
            gx.append(google["Date"][i])
            gy.append(google["Open"][i])
            ax.append(amazon["Date"][i])
            ay.append(amazon["Open"][i])

        # Condicional de cruce (son iguales o invirtieron su orden)
            if (ay[i] == gy[i]) or (ay[i] > gy[i] and ay[i - 1] < gy[i - 1]) or (ay[i] < gy[i] and ay[i - 1] > gy[i - 1]):
                crucex.append(gx[i])
                crucey.append(gy[i])

    plt.plot(gx,gy, "b", label= "Google" )
    plt.plot(ax,ay,  "r", label= "Amazon")
    plt.plot(crucex,crucey, 'o')
    plt.xlabel('Fecha')
    plt.ylabel('Precio')
    plt.xticks(gx[::100], rotation=45)
    plt.title("Gráfico Google y Amazon con INTERSECCIONES marcadas")
    plt.legend()
    plt.savefig ("Grafico Complejo Amazon-Google2.jpg")
    plt.show()

#-----------------------------------------MAIN-----------------------------------------

if opt == 1:
    print ("|Se muestran debajo las empresas disponibles para el analisis|")
    print ("|--", empresas["Nombres"], "--|")
    print ("|--",empresas["IdEmpresa"], "--|")
    comp1= str (1) #input ("ingrese el ID de la primera empresa a comparar")
    comp2= str (2) #input ("ingrese el ID de la segunda empresa a comparar")
    op1CompararEmpresas(comp1, comp2, empresas)
    
            
if opt == 2:
    print ("|Se muestran debajo las empresas disponibles para el analisis|")
    print ("|--", empresas["Nombres"], "--|")
    print ("|--",empresas["IdEmpresa"], "--|")
    comp1= str (1) #input ("ingrese el ID de la primera empresa a INTERSECCIONAR")
    comp2= str (2) #input ("ingrese el ID de la segunda empresa a INTERSECCIONAR")
    op2Interseccion(comp1, comp2, empresas)

if opt == 3: 
    print ("|Se muestran debajo las empresas disponibles para el analisis|")
    print ("|--", empresas["Nombres"], "--|")
    print ("|--",empresas["IdEmpresa"], "--|")
    comp1= str (1) #input ("ingrese el ID de la primera empresa a realizar la DERIVADA DISCRETA")
    if comp1 in empresas["IdEmpresa"]:
        empresa1 = dicArch.get(comp1)
        valores1 = empresa1 [["Date", "Open","Close"]]
    discreta1 = pd.DataFrame(empresa1 [["Date", "Open"]])
    discreta1["Open"] = (empresa1["Close"]) - (discreta1["Open"])
    print ("\nEl resultado de las derivadas discretas de la empresa seleccionada es: \n ")
    print (discreta1["Open"])
    generarGraficoDiscreta (discreta1)
    


if opt == 4: 
    print ("|Se muestran debajo las empresas a comparar minimos y máximos|")
    print ("|--", empresas["Nombres"], "--|")
    print ("|--",empresas["IdEmpresa"], "--|")

    archivo = pd.DataFrame(empresas) 
    data = archivo.to_dict("list") 
    # "list" significa que vamos a almacenar a cada columna como una lista con su contenido
    #print (data)
    #print (data['Nombres'])     # Accedemos a los datos de una columna
    #print (data['Nombres'][2])  # Accedemos al índice 2 de la columna 'Nombres'  
    mayorcre= 0
    mayorcreEm= ""
    cont = 0
    menorcre= 9999999
    menorcreEm= ""
    for archivo in dicArch:
        cont += 1
        empresita = dicArch.get(archivo)
        if (empresita["Open"].max()) - (empresita["Open"].min()) > mayorcre:
            mayorcre = ((empresita["Open"].max()) - (empresita["Open"].min()))
            mayorcreEm = str (cont)
        if (empresita["Open"].min()) < menorcre:
            menorcre = ((empresita["Open"].max()) - (empresita["Open"].min()) )
            menorcreEm = str (cont)
        if cont == 4:
                print ("El mayor crecimiento de las empresas es de ", mayorcre, " de la empresa con el ID: ", mayorcreEm ,data['Nombres'][int (mayorcreEm)-1])
                print ("El menor crecimiento de las empresas es de ", menorcre, " de la empresa con el ID: ", menorcreEm ,data['Nombres'][int (menorcreEm)-1])
    #generarExcel(empresita)
    #primer empresa mayor crecimiento
    Emp1ExcelMaCre= data['Archivos'][int (mayorcreEm)-1]

    valores1 = Emp1ExcelMaCre [["Date", "Open","Close"]]
    ArchEmprMayorCre = pd.DataFrame(Emp1ExcelMaCre [["Date", "Open"]])
    ArchEmprMayorCre["MaxCre"] = (Emp1ExcelMaCre["Open"].max()) - (ArchEmprMayorCre["Open"].min())
    print ("\nEl resultado de la empresa con mayor crecimiento con su máximo es:  ")
    print (ArchEmprMayorCre["MaxCre"][0])
    generarExcel (ArchEmprMayorCre, "EmpresaConMayCreci.xlsx")

    #segunda empresa menor crecimiento
    Emp2ExcelMenoCre= data['Archivos'][int (menorcreEm)-1]
    
    valores1 = Emp2ExcelMenoCre [["Date", "Open","Close"]]
    ArchEmprMenoCre = pd.DataFrame(Emp2ExcelMenoCre [["Date", "Open"]])
    ArchEmprMenoCre["MinCre"] = (Emp2ExcelMenoCre["Open"].max()) - (ArchEmprMenoCre["Open"].min())
    print ("\nEl resultado de la empresa con menor crecimiento con su mínimo es:  ")
    print (ArchEmprMenoCre["MinCre"][0])
    generarExcel (ArchEmprMenoCre, "EmpresaConMenorCreci.xlsx")


if opt == 5: 
    print ("Ahora se mostraran la comparativa entre las empresas de Amazon y Google")
    #wget ("https://raw.githubusercontent.com/LedesmaFran/python/master/GOOGLE.csv") 
    #wget  ("https://raw.githubusercontent.com/LedesmaFran/python/master/AMZN.csv")
    googlefile = pd.read_csv("GOOGLE.csv")
    amazonfile = pd.read_csv("AMZN.csv")
    google = googlefile.to_dict("list")
    amazon = amazonfile.to_dict("list")

    #print(google['Open'])
    #print(amazon['Open'])

    graficarInterComplejo (google, amazon)

    






#print (archivo["new_cases"].sum()/2)











