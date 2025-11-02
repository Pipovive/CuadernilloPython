contraseña = input("Digita una contraseña: \n");

tiene_mayusculas = any(c.isupper() for c in contraseña)
tiene_minusculas = any(c.islower() for c in contraseña)
tiene_numero = any(c.isdigit() for c in contraseña)
longitud_validad = len(contraseña) >= 8

if tiene_mayusculas and tiene_minusculas and tiene_numero and longitud_validad:
    print("✅ Contraseña válida. Cumple con todos los requisitos.")
else:
    print("❌ Contraseña inválida. Debe cumplir con lo siguiente:")
    if not longitud_validad:
        print("- Tener al menos 8 caracteres.")
    if not tiene_mayusculas:
        print("- Incluir al menos una letra mayúscula.")
    if not tiene_minusculas:
        print("- Incluir al menos una letra minúscula.")
    if not tiene_numero:
        print("- Incluir al menos un número.")