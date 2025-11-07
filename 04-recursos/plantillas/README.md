# Plantillas de Gobernanza y Documentación

Este directorio contiene plantillas reutilizables para gobierno de datos, documentación de políticas y casos de uso.

## Contenido

### Políticas de Datos

- **`plantilla_politica_datos.md`**: Plantilla completa en Markdown para crear políticas de datos.
  - Incluye: propósito, alcance, reglas, responsabilidades, enforcement, métricas, consecuencias.
  - Uso: Copiar y adaptar para crear políticas específicas (clasificación, acceso, retención, calidad).

- **`ejemplo_politica_clasificacion.yaml`**: Ejemplo funcional de política de clasificación en formato YAML.
  - Estructurado para parsing automático (governance-as-code).
  - Incluye: reglas, SLOs, controles técnicos, RACI implícito.

### Casos de Uso (referencia cruzada)

Los casos de uso completos están en `../casos-uso/`, incluyendo:
- `caso_integrador_gobierno_retail.md`: Ejercicio completo de aplicación de gobierno (roles, RACI, clasificación, lineage, políticas).

## Cómo Usar

### Para crear una nueva política:

1. Copia `plantilla_politica_datos.md` con nuevo nombre (ej. `politica_retencion_datos.md`).
2. Completa cada sección con contenido específico.
3. Revisa con stakeholders (Data Owners, Legal, Seguridad).
4. Obtén aprobaciones formales.
5. Publica en sistema de gestión documental.
6. Comunica a roles afectados.

### Para políticas ejecutables (automation):

- Usa formato YAML (ver `ejemplo_politica_clasificacion.yaml`).
- Integra con herramientas de gobierno (catálogo, quality suite, workflow engine).
- Ejemplo:
  ```python
  import yaml
  with open('ejemplo_politica_clasificacion.yaml') as f:
      politica = yaml.safe_load(f)
  
  # Validar dataset contra reglas
  for regla in politica['reglas']:
      if not validar_regla(dataset, regla):
          raise PolicyViolation(regla['id'])
  ```

## Extensiones Futuras

- Plantilla RACI matrix (CSV/Excel).
- Plantilla ADR (Architecture Decision Record).
- Plantilla contrato de datos (ya existe en `../contratos-datos/`).
- Checklist de compliance (GDPR, CCPA).

## Contribuciones

Si creas una política o plantilla útil, considera compartirla mediante PR para beneficiar a otros usuarios del curso.
