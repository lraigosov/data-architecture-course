# Checklist de Revisión de Arquitecturas y Data Products

Use esta lista para evaluar consistencia técnica, gobernanza y operación antes de aprobar un diseño o promover un data product.

## 1. Modelado y Contratos
- [ ] Modelo conceptual alineado a KPIs
- [ ] Modelo lógico y físico versionados
- [ ] Contrato de datos completo (schema + SLA frescura + reglas calidad + owner)
- [ ] Compatibilidad de esquema evaluada (backward / forward)

## 2. Calidad de Datos
- [ ] Reglas de calidad implementadas como código
- [ ] Métricas (nulls, duplicados, rangos, cardinalidad, frescura) registradas
- [ ] Plan de backfill documentado y aprobado
- [ ] Atributos críticos protegidos contra degradación

## 3. Seguridad y Privacidad
- [ ] Clasificación de datos (PII/PCI/PHI) completada
- [ ] Controles de acceso (RBAC/ABAC) definidos
- [ ] Cifrado in-transit y at-rest configurado
- [ ] Auditoría de accesos y cambios habilitada
- [ ] Plan de retención y derecho al olvido

## 4. Observabilidad
- [ ] Golden Signals monitoreados (Latency, Throughput, Errors, Saturation)
- [ ] Freshness y Completeness incluidos
- [ ] SLOs definidos y publicados
- [ ] Alertas con ownership y severidad
- [ ] Runbooks de incidentes presentes

## 5. Linaje y Metadatos
- [ ] Linaje table-level y column-level (si aplica) registrado
- [ ] Catálogo con metadatos de negocio y técnicos
- [ ] Steward asignado y visible
- [ ] Impacto de cambios evaluado (análisis de dependencias)

## 6. Costos y FinOps
- [ ] Etiquetado (tags) para imputación de costos
- [ ] Estimación de costos mensual documentada
- [ ] Plan de optimización (particionado, compaction, caching) definido
- [ ] Alertas de costo configuradas

## 7. Despliegue y Versionado
- [ ] Pipeline CI/CD con validaciones (calidad, schema, seguridad)
- [ ] Estrategia de despliegue definida (blue-green / canary / shadow)
- [ ] Versionado de datos, código y modelos (si ML) documentado
- [ ] ADRs presentes para decisiones clave

## 8. Data Product (si aplica Data Mesh)
- [ ] Owner y métricas de valor (uso, satisfacción)
- [ ] SLA frescura y calidad públicos
- [ ] API / interfaz de acceso definida
- [ ] Contratos público y semántica (glosario/ontología) enlazados

## 9. ML / IA (si aplica)
- [ ] Feature Store (offline/online) diseñado
- [ ] Registro de modelos con estados y métricas
- [ ] Monitoreo de drift y fairness configurado
- [ ] Plan de reentrenamiento y triggers definidos

## 10. Riesgos y Cumplimiento
- [ ] Riesgos identificados (performance, seguridad, costo, cumplimiento)
- [ ] Mitigaciones y responsables
- [ ] Normativas aplicables evaluadas (GDPR/CCPA/local)
- [ ] Evidencias de cumplimiento (logs, políticas, métricas)

---

Resultado de Revisión:
- Aprobado / Condicional / Rechazado
- Observaciones:

Última actualización: Noviembre 2025
