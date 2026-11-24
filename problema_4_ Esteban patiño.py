# Problema 4 - Videoteca Digital
# Estudiante: Esteban Patiño

# 1. Matriz con al menos 7 titulos
# Formato: [Titulo, Año, Calificacion 1-10, Genero]
videoteca = [
    ["Dune 2", 2024, 8.5, "Ciencia Ficcion"],
    ["Oppenheimer", 2023, 9.0, "Drama"],
    ["Avatar 2", 2022, 7.8, "Aventura"],
    ["Spider-Man No Way Home", 2021, 8.2, "Accion"],
    ["El Padrino", 1972, 9.5, "Crimen"],
    ["Interestelar", 2014, 8.8, "Ciencia Ficcion"],
    ["Joker", 2019, 8.4, "Drama"],
    ["Avengers Endgame", 2019, 8.6, "Accion"]
]

# 2. Modulo: funcion que cuenta los titulos que cumplen AMBAS condiciones
def contar_titulos(matriz, umbral_calificacion, anio_limite):
    """Cuenta los titulos con calificacion >= umbral y anio >= limite."""
    contador = 0
    for pelicula in matriz:
        anio = pelicula[1]
        calificacion = pelicula[2]
        # Logica de negocio: debe cumplir ambas condiciones
        if calificacion >= umbral_calificacion and anio >= anio_limite:
            contador += 1
    return contador

# 3. Criterios definidos
umbral = 8.0
anio_minimo = 2019

# 4. Salida
total = contar_titulos(videoteca, umbral, anio_minimo)
print(f"Umbral de calificacion: {umbral}")
print(f"Anio limite: {anio_minimo}")
print(f"El numero total de titulos que cumplen con ambos criterios es: {total}")