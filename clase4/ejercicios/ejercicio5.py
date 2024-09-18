# Ejercicio 5: Manejo de Matrículas en una Tupla
# Crea una tupla llamada matriculas con los siguientes números de matrícula: (101, 102, 103, 104, 105).
# Usa el método count para contar cuántas veces aparece el número de matrícula 102 en la tupla.
# Usa el método index para encontrar la posición del número de matrícula 104 en la tupla.

matriculas = (101, 102, 103, 104, 105, 102)

matricula_a_contar = 102
matricula_repite = matriculas.count(matricula_a_contar)
print(f"La matricula {matricula_a_contar} se repite {matricula_repite} veces en la tupla.")

matricula_a_buscar = 104
matricula_index = matriculas.index(matricula_a_buscar)
print(f"La matricula {matricula_a_buscar} se encuentra en la posición {matricula_index} en la tupla.")
