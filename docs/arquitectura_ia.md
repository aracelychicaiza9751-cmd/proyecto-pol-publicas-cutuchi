# Arquitectura Multiagente de IA y Prompts

## 1. Agentes del Sistema
- **AgenteIndustria**: Modela las decisiones de vertido de contaminantes según costos e incentivos.
- **AgenteGobierno**: Aplica multas por vertidos fuera de norma.
- **RioCutuchi**: Entorno hídrico que simula la acumulación de contaminantes y autodepuración (5% mensual).

## 2. Matriz de Prompts y Verificación Humana
- **Prompt**: "Diseñar un agente industrial en Python que modifique su comportamiento de vertido ante sanciones económicas."
- **Verificación Humana**: Revisión del balance de masa y validación de funciones con `pytest`.