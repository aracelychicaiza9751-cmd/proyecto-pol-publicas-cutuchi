# modelo_cutuchi.py
# Simulación Multiagente: Evaluación de Política de Saneamiento Ambiental en el Río Cutuchi

class AgenteIndustria:
    def __init__(self, id_agente, produccion, tasa_vertido):
        self.id_agente = id_agente
        self.produccion = produccion
        self.tasa_vertido = tasa_vertido
        self.capital = 1000.0  # Fondo de la empresa

    def producir_y_contaminar(self):
        contaminacion = self.produccion * self.tasa_vertido
        return contaminacion

    def pagar_multa(self, monto):
        self.capital -= monto


class AgenteGobierno:
    def __init__(self, tarifa_impuesto_ppm):
        self.tarifa_impuesto_ppm = tarifa_impuesto_ppm  # Multa por unidad de contaminación
        self.recaudacion_total = 0.0

    def aplicar_evaluacion_ambiental(self, industria, contaminacion_generada):
        multa = contaminacion_generada * self.tarifa_impuesto_ppm
        industria.pagar_multa(multa)
        self.recaudacion_total += multa
        return multa


class RioCutuchi:
    def __init__(self, nivel_contaminacion_inicial=100.0):
        self.nivel_contaminacion = nivel_contaminacion_inicial

    def recibir_vertidos(self, cantidad):
        self.nivel_contaminacion += cantidad

    def capacidad_regenerativa(self):
        # El río se autodepura un 5% en cada periodo
        self.nivel_contaminacion *= 0.95


def ejecutar_simulacion():
    print("=========================================================")
    print(" SIMULACIÓN DE POLÍTICA PÚBLICA: CUENCA RÍO CUTUCHI")
    print("=========================================================\n")
    
    rio = RioCutuchi(nivel_contaminacion_inicial=50.0)
    fábrica1 = AgenteIndustria(id_agente=1, produccion=50, tasa_vertido=0.8)
    municipio = AgenteGobierno(tarifa_impuesto_ppm=2.5)  # $2.5 de multa por unidad de PPM vertido
    
    meses = 6
    for mes in range(1, meses + 1):
        print(f"--- MES {mes} ---")
        vertido = fábrica1.producir_y_contaminar()
        multa = municipio.aplicar_evaluacion_ambiental(fábrica1, vertido)
        rio.recibir_vertidos(vertido)
        rio.capacidad_regenerativa()
        
        print(f"🏭 Vertido generado: {vertido:.1f} PPM | Multa cobrada: ${multa:.2f}")
        print(f"🌊 Contaminación Río Cutuchi: {rio.nivel_contaminacion:.2f} PPM\n")

    print(f"💰 Recaudación total del Municipio por multas: ${municipio.recaudacion_total:.2f}")

if __name__ == "__main__":
    ejecutar_simulacion()