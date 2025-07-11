
productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
 '2175HD': ['Acer', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
 'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
 'fgdxFHD': ['HP', 15.6, '12GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
 'GF75HD': ['Asus', 15.6, '12GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
 '123FHD': ['Acer', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
 '342FHD': ['Acer', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
 'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
 } 

stock = {'8475HD': [387990,10],#hp
    '2175HD': [327990,4],#acer
    'JjfFHD': [424990,1],
    'fgdxFHD': [664990,21],#hp
    '123FHD': [290890,32],#acer
     '342FHD': [444990,7],#acer
    'GF75HD': [749990,2],
    'UWU131HD': [349990,1],#dell
 }

stock_por_marca = {
    'HP' : [31],
    'Acer' : [43],
    'Asus' : [3],
    'Dell' : [1]
}

#me estoy poniendo ansioso y estresando con esto

def stock_marca(marca):
    if marca in stock_por_marca.keys():
        resultado = stock_por_marca[marca][0]
        print(f'El stock de esa marca es de {resultado}')
    else:
        print('No hay stock de esa marca: ')
    return resultado

def precio_rango(p_min, p_max):
    



    while True:
        print('***MENU PRINCIPAL***')
        print('1. Stock marca.')
        print('2. Búsqueda por precio.')
        print('3. Eliminar producto.')
        print('4. Salir.')
        try:
            opc = int(input('ingrese una opcion: '))
        except ValueError:
            print('ingrese solo numeros')
            if opc == 1 or 2 or 3 or 4 or 5:
                continue
            else:
                print('ingrese una opcion valida: ')
        if opc == 1:
            try:
                marca = input('Ingrese marca a consultar: ').lower
            except ValueError:
                print('ingrese solo letras')
                continue
            stock_marca(marca)

    
        elif opc == 2:
            p_min = int(input('Ingrese precio mínimo: '))
            p_max = int(input('Ingrese precio maximo: '))
            precio_rango(p_min, p_max)

        

        
            

       
 
