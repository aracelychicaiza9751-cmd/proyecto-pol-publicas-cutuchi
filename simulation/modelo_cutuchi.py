# modelo_cutuchi.py
# Simulación Multiagente: Evaluación de Política de Saneamiento Ambiental en el Río Cutuchi

import matplotlib.pyplot as plt
import pandas as pd

class AgenteIndustria:
    def __init__(self, id_agente, produccion, tasa_vertido):
        self.id_agente = id_agente
        self.produccion = produccion
        self.tasa_vertido = tasa_vertido

    def producir_y_contaminar(self, tasa_ajustada=None):
        tasa = tasa_ajustada if tasa_ajustada is not None else self.tasa_vertido
        return self.produccion * tasa


class RioCutuchi:
    def __init__(self, nivel_inicial=50.0):
        self.nivel_contaminacion = nivel_inicial

    def recibir_vertidos(self, cantidad):
        self.nivel_contaminacion += cantidad

    def autodepuracion(self):
        self.nivel_contaminacion *= 0.95


def simular_escenario(aplicar_politica=False, meses=12):
    rio = RioCutuchi(nivel_inicial=50.0)
    fabrica = AgenteIndustria(id_agente=1, produccion=50, tasa_vertido=0.8)
    
    historial = []
    
    for mes in range(1, meses + 1):
        tasa_efectiva = 0.3 if aplicar_politica else 0.8
        
        vertido = fabrica.producir_y_contaminar(tasa_ajustada=tasa_efectiva)
        rio.recibir_vertidos(vertido)
        rio.autodepuracion()
        
        historial.append({
            "Mes": mes,
            "Contaminacion_PPM": rio.nivel_contaminacion
        })
        
    return pd.DataFrame(historial)


def generar_evaluacion_y_grafico():
    print("=========================================================")
    print(" EVALUACIÓN DE POLÍTICA PÚBLICA EN EL RÍO CUTUCHI")
    print("=========================================================\n")
    
    df_sin_politica = simular_escenario(aplicar_politica=False)
    df_con_politica = simular_escenario(aplicar_politica=True)
    
    print("--- RESULTADOS A 12 MESES ---")
    print(f"🌊 Nivel final SIN regulación: {df_sin_politica['Contaminacion_PPM'].iloc[-1]:.2f} PPM")
    print(f"🌱 Nivel final CON regulación: {df_con_politica['Contaminacion_PPM'].iloc[-1]:.2f} PPM\n")
    
    plt.figure(figsize=(9, 5))
    plt.plot(df_sin_politica["Mes"], df_sin_politica["Contaminacion_PPM"], label="Sin Regulación (Business as Usual)", color="red", linestyle="--", marker="o")
    plt.plot(df_con_politica["Mes"], df_con_politica["Contaminacion_PPM"], label="Con Regulación Ambiental (Impuesto / Incentivo)", color="green", marker="s")
    
    plt.title("Evaluación Ex-Ante de Política Pública: Cuenca Río Cutuchi", fontsize=12)
    plt.xlabel("Meses de simulación")
    plt.ylabel("Nivel de Contaminación (PPM)")
    plt.grid(True, linestyle=":", alpha=0.6)
    plt.legend()
    
    nombre_grafico = "grafico_politica_cutuchi.png"
    plt.savefig(nombre_grafico)
    print(f"📊 ¡Gráfico generado exitosamente y guardado como '{nombre_grafico}'!")

if __name__ == "__main__":
    generar_evaluacion_y_grafico()