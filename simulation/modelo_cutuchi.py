# modelo_cutuchi.py
# Simulación Multiagente: Evaluación de Política de Saneamiento Ambiental en el Río Cutuchi

class AgenteIndustria:
    def __init__(self, id_agente, produccion, tasa_vertido):
        self.id_agente = id_agente
        self.produccion = produccion
        self.tasa_vertido = tasa_vertido  # Nivel de contaminación por unidad producida

    def producir_y_contaminar(self):
        contaminacion_generada = self.produccion * self.tasa_vertido
        return contaminacion_generada


class RioCutuchi:
    def __init__(self, nivel_contaminacion_inicial=100.0):
        self.nivel_contaminacion = nivel_contaminacion_inicial

    def recibir_vertidos(self, cantidad):
        self.nivel_contaminacion += cantidad

    def mostrar_estado(self):
        print(f"🌊 Estado actual del Río Cutuchi - Nivel de contaminación: {self.nivel_contaminacion:.2f} PPM")


def ejecutar_simulacion():
    print("--- INICIANDO SIMULACIÓN DE LA CUENCA DEL RÍO CUTUCHI ---")
    
    rio = RioCutuchi()
    fábrica1 = AgenteIndustria(id_agente=1, produccion=50, tasa_vertido=0.8)
    
    rio.mostrar_estado()
    
    # Simular 1 periodo de vertidos
    vertido = fábrica1.producir_y_contaminar()
    print(f"🏭 La Industria 1 ha generado {vertido} unidades de residuos.")
    
    rio.recibir_vertidos(vertido)
    rio.mostrar_estado()

if __name__ == "__main__":
    ejecutar_simulacion()