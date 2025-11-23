# Rúbricas Comparativas Ejercicios Transversales

| Ejercicio | Nivel | Aspectos Clave | Pesos Totales | Enfoque Principal |
|-----------|-------|----------------|---------------|-------------------|
| Detección Calidad (sales_orders) | Junior Intro | Anomalías, Reglas, Formato almacenamiento, ADR, Presentación | 30/25/20/15/10 | Fundamentos de calidad y contratos iniciales |
| Calidad Avanzada (sales_orders) | Junior Calidad | Anomalías cuantificadas, Reglas, Flujo Bronze→Silver, Función checks, ADR | 25/25/25/15/10 | Profundizar perfilado y remediación |
| Modelado Normalización vs Desnormalización | Junior Modelado | Granularidad, Comparativa, Métricas, Contrato Wide, Escenarios | 25/25/20/20/10 | Decisiones estructurales de modelado |
| Selección Esquema (Star/Snowflake/Vault) | Junior Esquemas | Criterios elección, Mapeo entidades, Historización, Nuevas fuentes, ADR | 30/25/20/15/10 | Arquitectura de almacenes y auditabilidad |
| SCD Tipo 2 Dimensión Cliente | Junior Dimensional | Estructura SCD2, Algoritmo, Reglas calidad, Pseudocódigo, Métricas | 25/25/20/20/10 | Historización y confiabilidad del histórico |
| Streaming Features & FinOps (streaming_events) | Mid | Features definidas, Flujo arquitectura, Métricas dataset, Costos, ROI+ADR | 30/20/15/20/15 | Data para ML en tiempo real y costo/valor |
| Migración & KPI Scoring (customers_dim) | Senior | Anomalías impacto, ADR migración, Plan fases + KPIs, Scoring, Riesgos+Gobernanza | 20/25/20/20/15 | Estrategia y gobierno de transformación |

## Mapeo de Criterios Transversales
| Criterio Global | Junior Foco | Mid Foco | Senior Foco | Observación |
|-----------------|-------------|----------|-------------|-------------|
| Calidad Datos | Detección + Reglas | Validación en streaming | Impacto en KPIs | Aumenta profundidad y responsabilidad |
| Modelado | Fact/Dimensión + Esquemas | Features & Serving | Arquitectura Organizacional | Escala desde técnico a estratégico |
| Gobernanza | Contrato básico | Data contract eventos + lineage | Federated governance completo | Se incrementa formalización |
| Costos/FinOps | Nociones compresión/formato | Cálculo costo vs ROI | Optimización y eficiencia estratégica | Evoluciona de micro a macro visión |
| Riesgos & ADR | Pequeños ADR técnicos | Dual-store decisiones | Migración crítica + mitigaciones | Complejidad y alcance mayores |

## Normalización de Pesos
Para comparación global se puede normalizar cada rúbrica a 100 y mapear a categorías:
- Técnica Base (Calidad + Modelado): ~50%
- Arquitectura / Diseño (Decisiones, Esquemas): ~25%
- Operacional / Costos / ROI: ~15%
- Gobernanza / Riesgos: ~10%

## Uso Sugerido
1. Seleccionar ejercicio según nivel del participante.
2. Calificar cada aspecto con escala 1–5 y multiplicar por su peso relativo.
3. Sumar para score final y comparar progreso inter-nivel.
4. Identificar brechas (ej. baja puntuación en Gobernanza en nivel Senior).

## Futuras Extensiones
- Añadir rúbrica para Observabilidad y Drift (Mid/Senior).
- Incorporar dimensión Ética / Privacidad en nivel Senior IA.
- Automatizar cálculo en script `scripts/evaluate_rubrics.py`.
