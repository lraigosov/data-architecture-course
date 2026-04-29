# Checklist de Revisión de Arquitecturas y Data Products

Use esta lista para evaluar consistencia técnica, gobernanza y operación antes de aprobar un diseño o promover un data product. No reemplaza una revisión humana; ayuda a que las decisiones importantes queden visibles y comparables.

## 1. Modelado y Contratos
- [ ] Modelo conceptual alineado a KPIs
- [ ] Modelo lógico y físico versionados
- [ ] Contrato de datos completo: schema, semántica, calidad, SLA, owner, términos de uso y estado
- [ ] Compatibilidad de esquema evaluada (backward / forward / full, según el caso)
- [ ] Cambios breaking con plan expand-contract, fecha objetivo y consumidores impactados
- [ ] Glosario o capa semántica enlazada para métricas críticas

## 2. Calidad de Datos
- [ ] Reglas de calidad implementadas como código y versionadas
- [ ] Métricas de schema, missingness, unicidad, rangos, integridad, volumen y frescura registradas
- [ ] Plan de backfill documentado y aprobado
- [ ] Atributos críticos protegidos contra degradación
- [ ] Resultado de validaciones visible para consumidores o stewards

## 3. Seguridad y Privacidad
- [ ] Clasificación de datos (PII/PCI/PHI) completada
- [ ] Controles de acceso (RBAC/ABAC) definidos
- [ ] Cifrado in-transit y at-rest configurado
- [ ] Auditoría de accesos y cambios habilitada
- [ ] Plan de retención y derecho al olvido
- [ ] Usos permitidos y prohibidos documentados para datos sensibles o regulados

## 4. Observabilidad
- [ ] Golden Signals monitoreados (Latency, Throughput, Errors, Saturation)
- [ ] Freshness y Completeness incluidos
- [ ] SLOs definidos y publicados
- [ ] Alertas con ownership y severidad
- [ ] Runbooks de incidentes presentes
- [ ] Alertas separan fallas técnicas de impacto real en productos de datos
- [ ] MTTD/MTTR o métricas equivalentes registradas para incidentes relevantes

## 5. Linaje y Metadatos
- [ ] Linaje table-level y column-level (si aplica) registrado
- [ ] Catálogo con metadatos de negocio y técnicos
- [ ] Steward asignado y visible
- [ ] Impacto de cambios evaluado (análisis de dependencias)
- [ ] Consumidores críticos identificados: dashboards, modelos, APIs, reportes regulatorios

## 6. Costos y FinOps
- [ ] Etiquetado (tags) para imputación de costos
- [ ] Estimación de costos documentada con supuestos claros
- [ ] Plan de optimización (particionado, compaction, caching) definido
- [ ] Alertas de costo configuradas
- [ ] Costos de egress, retención y reprocesos incluidos en la decisión

## 7. Despliegue y Versionado
- [ ] Pipeline CI/CD con validaciones (calidad, schema, seguridad)
- [ ] Estrategia de despliegue definida (blue-green / canary / shadow / expand-contract)
- [ ] Versionado de datos, código y modelos (si ML) documentado
- [ ] ADRs presentes para decisiones clave
- [ ] Plan de rollback o replay probado para cambios de alto impacto

## 8. Data Product (si aplica Data Mesh)
- [ ] Owner y métricas de valor (uso, satisfacción)
- [ ] SLA frescura y calidad públicos
- [ ] API / interfaz de acceso definida
- [ ] Contratos público y semántica (glosario/ontología) enlazados
- [ ] Soporte y canal de contacto definidos
- [ ] Métricas de adopción revisadas con consumidores

## 9. ML / IA (si aplica)
- [ ] Feature Store (offline/online) diseñado
- [ ] Registro de modelos con estados y métricas
- [ ] Monitoreo de drift y fairness configurado
- [ ] Plan de reentrenamiento y triggers definidos
- [ ] Procedencia y consentimiento de datos de entrenamiento documentados
- [ ] Evaluación de riesgos de IA registrada para casos sensibles
- [ ] Restricciones de uso del dataset o modelo comunicadas

## 10. Riesgos y Cumplimiento
- [ ] Riesgos identificados (performance, seguridad, costo, cumplimiento)
- [ ] Mitigaciones y responsables
- [ ] Normativas aplicables evaluadas (GDPR/CCPA/local)
- [ ] Evidencias de cumplimiento (logs, políticas, métricas)
- [ ] Decisiones aceptadas por dueños de negocio y tecnología
- [ ] Próxima revisión agendada o gatillada por cambios relevantes

---

Resultado de Revisión:
- Aprobado / Condicional / Rechazado
- Observaciones:

Última actualización: Abril 2026
