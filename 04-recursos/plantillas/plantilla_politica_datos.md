# Plantilla: Política de Datos

## Metadatos de la Política

| Campo | Valor |
|-------|-------|
| **Nombre de la Política** | [Nombre descriptivo] |
| **Código/ID** | [POL-XXX] |
| **Versión** | [1.0.0] |
| **Fecha de Aprobación** | [YYYY-MM-DD] |
| **Aprobador** | [Governance Lead / Comité de Datos] |
| **Owner** | [Rol responsable] |
| **Siguiente Revisión** | [YYYY-MM-DD] |
| **Alcance** | [Empresa completa / Dominio específico / Sistema] |

---

## 1. Propósito

_Describe el objetivo de la política y el problema que resuelve._

**Ejemplo:**
Esta política establece los criterios y procedimientos para clasificar datasets según su nivel de sensibilidad, asegurando protección adecuada y cumplimiento normativo.

---

## 2. Alcance

_Define a qué datos, sistemas, roles o procesos aplica esta política._

**Aplica a:**
- [ ] Todos los datasets en la organización
- [ ] Datasets de dominio específico: [especificar]
- [ ] Sistemas: [listar]
- [ ] Roles afectados: [Data Owners, Stewards, Custodians, Consumers]

**No aplica a:**
- Datos personales de prueba en entornos aislados
- [Otras excepciones]

---

## 3. Definiciones Clave

| Término | Definición |
|---------|------------|
| [Término 1] | [Definición] |
| [Término 2] | [Definición] |

**Ejemplo:**
| PII | Información de identificación personal (nombre, email, DNI) |
| Regulado | Datos sujetos a GDPR, CCPA, PCI-DSS, etc. |

---

## 4. Política (Reglas)

_Enumera las reglas específicas de forma clara y accionable._

### 4.1. [Regla 1]
**Declaración:** [Qué se debe/no se debe hacer]

**Ejemplo:**
Todo dataset debe clasificarse en una de estas categorías: Público, Interno, Confidencial, Regulado.

**Excepciones:** [Si aplica]

---

### 4.2. [Regla 2]
**Declaración:** [...]

**Ejemplo:**
El acceso a datos clasificados como Regulados requiere aprobación explícita del Data Owner y del equipo de Seguridad.

---

## 5. Responsabilidades

| Rol | Responsabilidad |
|-----|-----------------|
| **Data Owner** | Clasificar datasets, aprobar accesos, revisar cumplimiento |
| **Data Steward** | Validar metadatos de clasificación, asistir en revisiones |
| **Data Custodian** | Implementar controles técnicos (RBAC, cifrado, masking) |
| **Governance Lead** | Monitorear cumplimiento, reportar métricas |
| **Consumers** | Cumplir restricciones de acceso y uso |

---

## 6. Procedimiento de Enforcement

_Cómo se aplica la política en la práctica._

**Controles Técnicos:**
- [ ] Automatización: [p.ej., tag obligatorio en catálogo]
- [ ] Validación: [p.ej., quality gate rechaza datasets sin clasificación]
- [ ] Monitoreo: [dashboard de cumplimiento]

**Controles de Proceso:**
- [ ] Revisión periódica: [trimestral/semestral]
- [ ] Auditoría: [logs de acceso, cambios de clasificación]
- [ ] Capacitación: [onboarding obligatorio para Data Owners]

**Gestión de Excepciones:**
- Proceso formal de solicitud y aprobación
- Registro en sistema de tracking
- Revisión en próxima auditoría

---

## 7. Métricas de Cumplimiento

| Métrica | Objetivo | Frecuencia |
|---------|----------|------------|
| % datasets clasificados | ≥ 95% | Semanal |
| Tiempo medio de clasificación (días) | ≤ 5 | Mensual |
| Excepciones pendientes | ≤ 3 | Mensual |
| Incidentes de no-cumplimiento | 0 | Mensual |

---

## 8. Consecuencias de No Cumplimiento

- Bloqueo de acceso/publicación de datasets no clasificados
- Escalación a Governance Committee
- [Otras medidas disciplinarias según política de empresa]

---

## 9. Documentos Relacionados

- [POL-XXX] Política de Acceso a Datos
- [PROC-YYY] Procedimiento de Solicitud de Acceso
- [STD-ZZZ] Estándar de Metadatos

---

## 10. Historial de Cambios

| Versión | Fecha | Autor | Cambios |
|---------|-------|-------|---------|
| 1.0.0 | YYYY-MM-DD | [Nombre] | Creación inicial |
| 1.1.0 | YYYY-MM-DD | [Nombre] | [Descripción de cambios] |

---

## Aprobaciones

| Rol | Nombre | Firma | Fecha |
|-----|--------|-------|-------|
| Governance Lead | | | |
| Legal / Compliance | | | |
| CISO / Seguridad | | | |
| Comité de Datos | | | |

---

**Notas:**
- Esta plantilla debe adaptarse al contexto organizacional.
- Almacenar versiones en sistema de gestión documental con control de cambios.
- Comunicar cambios a todos los roles afectados con al menos 2 semanas de antelación.
