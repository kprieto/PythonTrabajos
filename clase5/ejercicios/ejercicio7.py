# Ejercicio 7: Contar Ocurrencias de Elementos en un Diccionario 
# Anidado 
# 1. Crea un diccionario que contenga información sobre tres clubes 
# deportivos, cada uno con una lista de jugadores. 
# o Cada jugador es un diccionario con las claves: nombre y edad. 
# 2. Cuenta cuántos jugadores en total tienen cada uno de los clubes 

clubes = {
    "Real Madrid": {
        "país": "España",
        "fundación": 1902,
        "jugadores": [{"nombre":"Thibaut Courtois", "edad": 25},
                    {"nombre":"Dani Carvajal", "edad": 25},
                    {"nombre":"Luka Modrić", "edad": 26},
                    {"nombre":"Vinícius Júnior", "edad": 26}
                    ]
    },
    "Manchester United": {
        "país": "Inglaterra",
        "fundación": 1878,
        "jugadores": [{"nombre":"David de Gea", "edad": 25},
                    {"nombre":"Harry Maguire", "edad": 28},
                    {"nombre":"Bruno Fernandes", "edad": 27}
                    ]
    },
    "FC Bayern Munich": {
        "país": "Alemania",
        "fundación": 1900,
        "jugadores": [{"nombre":"Manuel Neuer", "edad": 25},
                    {"nombre":"Joshua Kimmich", "edad": 25},
                    {"nombre":"Leon Goretzka", "edad": 26},
                    {"nombre":"Thomas Müller", "edad": 25},
                    {"nombre":"Leroy Sané", "edad": 25}                    
                    ]
    }
    }

print("Datos del club: \n")
for clave,datos in clubes.items():
    print(clave, ": \n")
    
        
    for c,d in datos.items():
        
        if c == "jugadores":
            print("JUGADORES \n") 
            for j in d:     
                print("Jugador: ",j.get("nombre"),"- Edad: ",j.get("edad"),"\n") 
            print("Total de jugadores: ", len(d))   
        else:
            print(c, ": ",d ,"\n")
