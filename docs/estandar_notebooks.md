# Estándar para Notebooks del Curso

Este estándar busca asegurar que todos los notebooks sean claros, reproducibles y evaluables. Aplica a `01-nivel-junior/`, `02-nivel-mid/` y `03-nivel-senior/`.

## Estructura Recomendada (Secciones)
Incluye, en este orden, como mínimo:
1. Título (H1)
2. Objetivos (H2)
3. Prerrequisitos (H2)
4. Preparación/Instalación (H2)
5. Índice/Mapa del contenido (H2)
6. Contenido principal por secciones numeradas (H2/H3)
7. Ejercicios (H2)
8. Evaluación o Criterios de logro (H2)
9. Referencias (H2)
10. Créditos/Versión (H3)

## Convenciones
- Títulos y secciones en español, con H2/H3 claros (##, ###).
- Celdas Markdown: explicaciones y enunciados; celdas de código separadas.
- Numeración de secciones: `01.`, `02.`, … para facilitar navegación.
- Nombres de archivos: `nn_titulo_descriptivo.ipynb` (snake_case; con prefijo numérico).
- Imágenes gráficas (si aplica): añade pie de figura y fuente.

## Reproducibilidad
- Fija semilla aleatoria (`numpy.random.seed`, etc.) y documenta entorno (Python y libs).
- Evita dependencias externas no listadas en `requirements.txt`.
- Mantén outputs clave visibles; limpia outputs ruidosos antes de guardar.
- Usa rutas relativas dentro del repo.

## Estilo de Código
- PEP8 básico, variables descriptivas, comentarios concisos.
- Funciones con docstring breve (propósito, entradas, salidas).
- Manejo de errores simple y mensajes amigables.

## Metadatos Recomendados (opcional)
- `authors`: lista de autores o responsables.
- `level`: {junior|mid|senior}.
- `last_update`: ISO date.
- `tags`: ["gobierno", "streaming", "ml", ...].

## Checklist Rápido por Notebook
- [ ] Secciones mínimas presentes (Objetivos, Prerrequisitos, Ejercicios, Referencias)
- [ ] Código ejecuta de inicio a fin sin errores
- [ ] Outputs relevantes incluidos
- [ ] Enlaces y rutas válidos
- [ ] Referencias a estándares o docs oficiales cuando aplican

---

Última actualización: Noviembre 2025
