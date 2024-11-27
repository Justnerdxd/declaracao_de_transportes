from modules.database import buscar_cliente, buscar_transportadora

# Teste de cliente
print("=== Testando Cliente ===")
cliente = buscar_cliente("000837")
print(cliente)

# Teste de transportadora
print("=== Testando Transportadora ===")
transportadora = buscar_transportadora("000841")
print(transportadora)
