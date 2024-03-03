#Esta funcion muestra el sudoku de una forma mas limpia
def print_sudoku(sudoku):
  for i in range(9):
    #Imprimimos la separación cada 3 filas
    if i == 3 or i == 6:
      print("|-------+-------+-------|")
    for j in range(9):
      #Separacion de cada 3 columnas
      if j%3 == 0:
        print("| ",end="")
      #Mostramos el numero, si no es cero
      if sudoku[i][j]:
        print(str(sudoku[i][j]) + " ", end="")
      else:
        print(". ",end="")
    print("|")

#Definimos el sudoku
sudoku1 = [
    [5,0,0,9,1,3,7,2,0],
    [3,0,0,0,8,0,5,0,9],
    [0,9,0,2,5,0,0,8,0],
    [6,8,0,4,7,0,2,3,0],
    [0,0,9,5,0,0,4,6,0],
    [7,0,4,0,0,0,0,0,5],
    [0,2,0,0,0,0,0,0,0],
    [4,0,0,8,9,1,6,0,0],
    [8,5,0,7,2,0,0,0,3],
]

sudoku2 = [
    [6,9,0,0,0,0,7,0,0],
    [0,0,0,0,9,6,0,0,0],
    [0,8,0,7,5,3,0,9,0],
    [0,2,0,3,7,4,5,6,1],
    [3,6,0,0,0,5,0,2,0],
    [0,0,0,9,6,0,3,7,8],
    [0,0,6,0,3,1,0,8,4],
    [0,4,5,8,0,7,6,0,0],
    [0,0,0,0,0,0,0,5,7]
]

#Metodo para validar si se puede agregar un numero a una casilla
def valido(sudoku,n,i,j):
  fila = sudoku[i]
  col = [f[j] for f in sudoku]
  #Metodo para recorrer el bloque completo de 3x3
  bloque = [sudoku[a][b]
            for a in range(9)
            for b in range(9)
            if i // 3 == a // 3
            and j // 3 == b // 3]
  return n not in fila and n not in col and n not in bloque

#Implementando la solución con backtraking
def resolver(sudoku):
  #Recorremos cada fila y cada columna
  for i in range(9):
    for j in range(9):
      #Unicamente nos centramos en las casillas vacias
      if sudoku[i][j] == 0:
        for n in range(1,10):
          if valido(sudoku,n,i,j):
            #Si el numero es valido se agrega a la casilla
            sudoku[i][j] = n
            #Utilizamos recursividad para verificar si el numero
            if resolver(sudoku):
              #Devuelve verdadero si es correcto y cumple con las condiciones
              return True
            else:
            #En caso de que no volvemos a blanquear la casilla
              sudoku[i][j] = 0
        #Aplicacion del Backtraking
        return False
  #Solucionado
  return True

#Aplicamos el metodo para solucionar sudoku
resolver(sudoku1)
resolver(sudoku2)
#Imprimimos el sudoku
print("Sudoku 1")
print_sudoku(sudoku1)
print("\n")
print("Sudoku 2")
print_sudoku(sudoku2)