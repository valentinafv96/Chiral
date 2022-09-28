# chiralsol

![Python package](https://github.com/valentinafv96/chiralsol/workflows/Python%20package/badge.svg)
![Upload Python Package](https://github.com/valentinafv96/chiralsol/workflows/Upload%20Python%20Package/badge.svg)

Se encuentran las soluciones quirales (No Triviales) como se presentan en [arXiv:1905.13729](https://arxiv.org/abs/1905.13729) [PRL]:

Las soluciones totales son un conjunto de arreglos (z) de numpy de n enteros que satisfacen las ecuaciones diofánticas, i.e, los z tq:

```python
>>> z.sum()
0
>>> (z**3).sum()
0
```

Las entradas del programa son en orden: n (El número de componentes de la solución), N (número de listas k-l generadas aleatoriamente en las que se corre el programa), max (Rango sobre el que van a generar los valores de las componente de las listas k-l), imax (Número de veces en que el programa va a correr las N listas aleatorias), zmax (Rango de las componentes de las soluciones) y output_name (Prefijo del archivo .json que se genera con todas las soluciones encontradas).

La función se implementa a continuación como: chiralsol.paralelo(n,N,max,imax,zmax,output_name)

## Install
```bash
$ pip install --
```
## USAGE
```python
>>> from chiral import chiralsol
>>> chiralsol.paralelo(5,1000000,9,0,30,soluciones)
Grid → [1000000, 3]
Tiempo ejecución → 0.013944939772288004 min
Soluciones únicas → 11
```

## Example
Una muestra del archivo que retorna el programa para los parámetros ingresados anteriormente se puede encontrar [acá](https://github.com/valentinafv96/chiralsol/blob/main/soluciones_5.json) [JSON]
