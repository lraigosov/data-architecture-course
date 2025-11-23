package access.column

default allow = false

# Entrada ejemplo:
# {
#   "userRoles": ["analyst"],
#   "columnsRequested": ["email","total_amount"],
#   "piiColumns": ["email"],
#   "allowMasking": true
# }

allow {
  # Se permite si ninguna columna sensible es solicitada
  not contains_sensitive
}

# Si la columna sensible está solicitada y hay rol privilegiado y masking activo
allow {
  contains_sensitive
  input.allowMasking
  some r
  r := input.userRoles[r]
  r == "data_privileged"
}

contains_sensitive {
  some c
  c := input.columnsRequested[c]
  c == sensitive_column
}

sensitive_column = col {
  some p
  p := input.piiColumns[p]
  col := p
}
