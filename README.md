# chiralsol

![Python package](https://github.com/valentinafv96/chiralsol/workflows/Python%20package/badge.svg)
![Upload Python Package](https://github.com/valentinafv96/chiralsol/workflows/Upload%20Python%20Package/badge.svg)

Se encuentran las soluciones quirales (No Triviales) como se presentan en [arXiv:1905.13729](https://arxiv.org/abs/1905.13729) [PRL]:

Las soluciones son un conjunto de arreglos (`z`) de numpy de `n` enteros que satisfacen las ecuaciones diofánticas, i.e, los `z` tq:

```python
>>> z.sum()
0
>>> (z**3).sum()
0
```

Si se desea tener control sobre todos los parámetros del sistema, las entradas del programa son en orden: `n` (número de componentes de la solución), `N` (número de listas k-l generadas aleatoriamente en las que se corre el programa), `max` (rango sobre el que van a generar los valores de las componente de las listas k-l), `zmax` (rango entre el que se encuentran las componentes de las soluciones), `imax` (número de veces en que el programa va a correr las `N` listas aleatorias) y `output_name` (prefijo del archivo .json que se genera con todas las soluciones encontradas: output_name_n.json). 

NOTA: Como `output_name` es un string debe ponerse entre comillas.

La función se implementa a continuación como: `chiralsol.paralelo(n,N,max,zmax,imax,output_name)`, pero bien se prodría especificar solamente el n y los demás valores se toman por defecto en el programa como: 

  - `N` = 1000000
  - `max` = 9
  - `zmax` = 30
  - `imax` = $(10 * N_{uni}) // N, \quad N_{uni} = (2\times max +1)^{n-2}$
  - `output_name` = 'soluciones'
  
de tal forma que la función se implementa como: `chiralsol.paralelo(n)`

## Install
```bash
$ pip install -i https://test.pypi.org/simple/ chiralsol
```
## USAGE
```python
>>> from chiral import chiralsol
>>> chiralsol.paralelo(5,1000000,9,0,30,'soluciones')
Grid → [1000000, 3]
Tiempo ejecución → 0.013944939772288004 min
Soluciones únicas → 11
```

## Example
Una muestra del archivo que retorna el programa para los parámetros ingresados anteriormente se puede encontrar [acá](https://github.com/valentinafv96/chiralsol/blob/main/soluciones_5.json).
