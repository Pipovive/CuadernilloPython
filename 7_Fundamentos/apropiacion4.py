import random

adjetivos_positivos = [
    "luminoso",
    "sabio",
    "valiente",
    "armonioso",
    "místico",
    "resplandeciente",
    "sereno",
    "poderoso",
    "visionario",
    "radiante",
    "honorable",
    "enérgico",
    "trascendental",
    "intuïtivo",
    "destinado al éxito"
]

destinos = [
    "los astros se alinearán a tu favor muy pronto",
    "una energía ancestral te guiará hacia nuevas oportunidades",
    "un cambio inesperado abrirá caminos llenos de abundancia",
    "el universo está conspirando para darte buenas noticias",
    "una revelación transformará tu manera de ver la vida",
    "un encuentro especial te traerá claridad espiritual",
    "un ciclo poderoso está por comenzar para ti",
    "las fuerzas cósmicas te protegerán en los próximos días",
    "una sorpresa mística llegará cuando menos lo esperes",
    "tu energía atraerá prosperidad y crecimiento"
]

nombre = input("Digita tu nombre: ")

def generar_mensaje_animo(nombre):
    if nombre.strip() == "":
        nombre = "Hola"
    
    adjetivo = random.choice(adjetivos_positivos)
    destino = random.choice(destinos)

    print(f"{nombre}, eres una persona {adjetivo}, y {destino}.")

generar_mensaje_animo(nombre)
