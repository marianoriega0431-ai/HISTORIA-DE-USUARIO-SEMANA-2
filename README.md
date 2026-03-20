# 📦 Sistema de Inventario

## 📌 Descripción
Este proyecto consiste en un sistema básico de inventario desarrollado en Python.  
Permite al usuario agregar productos, ver el inventario y calcular estadísticas de forma sencilla mediante un menú interactivo.

El programa utiliza listas, diccionarios, estructuras condicionales y bucles.

##  Objetivo
Aplicar conceptos básicos de programación en Python como:
- Condicionales (`if`, `elif`, `else`)
- Bucles (`while` y `for`)
- Listas y diccionarios
- Validación de datos ingresados por el usuario
  
##  Funcionalidades

El programa cuenta con un menú que permite:

1. **Agregar producto**
   - Solicita nombre, precio y cantidad
   - Valida que los datos sean correctos
   - Guarda el producto en el inventario

2. **Mostrar inventario**
   - Muestra todos los productos registrados
   - Indica si el inventario está vacío

3. **Calcular estadísticas**
   - Calcula el valor total del inventario (precio × cantidad)
   - Muestra la cantidad total de productos

4. **Salir**
   - Finaliza el programa

##  Estructura del programa

- `inventario`: lista donde se guardan los productos  
- Cada producto es un diccionario con:
  - `nombre`
  - `precio`
  - `cantidad`

Funciones utilizadas:
- `agregar_producto()`
- `mostrar_inventario()`
- `calcular_estadisticas()`
##  Cómo ejecutar el programa
1. Abrir el archivo en un entorno de Python (VS Code, PyCharm o terminal)
2. Ejecutar el archivo
3. Usar el menú escribiendo el número de la opción deseada
##  Aprendizajes
En este proyecto aprendí a:
- Usar ciclos para repetir procesos
- Validar datos ingresados por el usuario
- Organizar información con listas y diccionarios
- Dividir el programa en funciones para hacerlo más ordenado

---

## 📌 Nota final
Este es un proyecto básico enfocado en el aprendizaje de los fundamentos de Python y la lógica de programación.
