# Diccionario de libros: código -> (título, autor, copias, precio)
inventario_libros = {
    "L001": ("Cien Años de Soledad", "Gabriel García Márquez", 25, 45000),
    "L002": ("El Amor en los Tiempos del Cólera", "Gabriel García Márquez", 18, 42000),
    "L003": ("1984", "George Orwell", 30, 38000),
    "L004": ("Rebelión en la Granja", "George Orwell", 22, 35000),
    "L005": ("Don Quijote de la Mancha", "Miguel de Cervantes", 15, 50000),
    "L006": ("El Principito", "Antoine de Saint-Exupéry", 40, 28000),
    "L007": ("Crónica de una Muerte Anunciada", "Gabriel García Márquez", 12, 40000),
    "L008": ("La Metamorfosis", "Franz Kafka", 20, 32000)
}

# ===== FUNCIONES =====

def mostrar_todos_libros():
    """Muestra todo el inventario de libros"""
    if not inventario_libros:
        print("\n⚠ No hay libros en el inventario")
        return
    
    print("\n" + "=" * 90)
    print("📚 INVENTARIO COMPLETO DE LIBROS")
    print("=" * 90)
    print(f"{'Código':<10} {'Título':<35} {'Autor':<25} {'Copias':<10} {'Precio':<10}")
    print("-" * 90)
    
    for codigo, datos in inventario_libros.items():
        titulo, autor, copias, precio = datos
        print(f"{codigo:<10} {titulo:<35} {autor:<25} {copias:<10} ${precio:,}")
    
    print("=" * 90)

def buscar_libros_por_autor():
    """Muestra los libros disponibles de un autor específico"""
    print("\n--- BUSCAR LIBROS POR AUTOR ---")
    autor_buscar = input("Nombre del autor: ").strip()
    
    # Buscar libros del autor
    libros_encontrados = {}
    for codigo, datos in inventario_libros.items():
        titulo, autor, copias, precio = datos
        # Búsqueda no sensible a mayúsculas/minúsculas
        if autor_buscar.lower() in autor.lower():
            libros_encontrados[codigo] = datos
    
    if not libros_encontrados:
        print(f"\n❌ No se encontraron libros del autor '{autor_buscar}'")
        return
    
    # Mostrar resultados
    print("\n" + "=" * 90)
    print(f"📚 LIBROS DE: {autor_buscar}")
    print("=" * 90)
    print(f"{'Código':<10} {'Título':<35} {'Copias':<10} {'Precio':<10}")
    print("-" * 90)
    
    for codigo, datos in libros_encontrados.items():
        titulo, autor, copias, precio = datos
        disponibilidad = "✓ Disponible" if copias > 0 else "✗ Agotado"
        print(f"{codigo:<10} {titulo:<35} {copias:<10} ${precio:,}")
    
    print("=" * 90)
    print(f"Total de libros encontrados: {len(libros_encontrados)}")

def comprar_libro():
    """Permite al usuario comprar libros y actualiza el inventario"""
    print("\n--- COMPRAR LIBRO ---")
    codigo = input("Código del libro: ").strip().upper()
    
    if codigo not in inventario_libros:
        print(f"\n❌ El código '{codigo}' no existe en el inventario")
        return
    
    titulo, autor, copias, precio = inventario_libros[codigo]
    
    # Mostrar información del libro
    print("\n" + "=" * 70)
    print(f"📖 {titulo}")
    print(f"✍️  Autor: {autor}")
    print(f"💵 Precio: ${precio:,}")
    print(f"📦 Copias disponibles: {copias}")
    print("=" * 70)
    
    if copias == 0:
        print("\n❌ Lo sentimos, este libro está agotado")
        return
    
    try:
        cantidad = int(input("\n¿Cuántas copias deseas comprar?: "))
        
        if cantidad <= 0:
            print("❌ La cantidad debe ser mayor a 0")
            return
        
        if cantidad > copias:
            print(f"\n❌ Solo hay {copias} copias disponibles")
            print(f"¿Deseas comprar las {copias} copias disponibles? (s/n)")
            respuesta = input().strip().lower()
            if respuesta != 's':
                print("Compra cancelada")
                return
            cantidad = copias
        
        # Calcular total a pagar
        total_pagar = cantidad * precio
        
        # Mostrar resumen de compra
        print("\n" + "=" * 70)
        print("🛒 RESUMEN DE COMPRA")
        print("=" * 70)
        print(f"Libro: {titulo}")
        print(f"Cantidad: {cantidad} copias")
        print(f"Precio unitario: ${precio:,}")
        print(f"TOTAL A PAGAR: ${total_pagar:,}")
        print("=" * 70)
        
        confirmacion = input("\n¿Confirmar compra? (s/n): ").strip().lower()
        
        if confirmacion == 's':
            # Actualizar inventario (crear nueva tupla con las copias actualizadas)
            nuevas_copias = copias - cantidad
            inventario_libros[codigo] = (titulo, autor, nuevas_copias, precio)
            
            print("\n✓ ¡Compra realizada exitosamente!")
            print(f"  Copias restantes de '{titulo}': {nuevas_copias}")
            print(f"  Total pagado: ${total_pagar:,}")
        else:
            print("\n❌ Compra cancelada")
            
    except ValueError:
        print("❌ La cantidad debe ser un número entero")

def agregar_libro():
    """Agrega un nuevo libro al inventario"""
    print("\n--- AGREGAR NUEVO LIBRO ---")
    codigo = input("Código del libro (ej: L009): ").strip().upper()
    
    if codigo in inventario_libros:
        print(f"❌ El código '{codigo}' ya existe")
        return
    
    titulo = input("Título del libro: ").strip()
    autor = input("Autor: ").strip()
    
    try:
        copias = int(input("Número de copias: "))
        precio = float(input("Precio del libro: $"))
        
        if copias < 0 or precio < 0:
            print("❌ Las copias y el precio deben ser positivos")
            return
        
        inventario_libros[codigo] = (titulo, autor, copias, precio)
        print(f"\n✓ Libro '{titulo}' agregado correctamente")
    except ValueError:
        print("❌ Valores inválidos")

def buscar_libro_por_codigo():
    """Busca un libro por su código"""
    print("\n--- BUSCAR LIBRO POR CÓDIGO ---")
    codigo = input("Código del libro: ").strip().upper()
    
    if codigo not in inventario_libros:
        print(f"\n❌ El código '{codigo}' no existe")
        return
    
    titulo, autor, copias, precio = inventario_libros[codigo]
    
    print("\n" + "=" * 70)
    print(f"📖 INFORMACIÓN DEL LIBRO")
    print("=" * 70)
    print(f"Código: {codigo}")
    print(f"Título: {titulo}")
    print(f"Autor: {autor}")
    print(f"Copias disponibles: {copias}")
    print(f"Precio: ${precio:,}")
    print(f"Valor total en inventario: ${copias * precio:,}")
    print("=" * 70)

def libros_agotados():
    """Muestra los libros que están agotados"""
    print("\n" + "=" * 70)
    print("⚠️  LIBROS AGOTADOS (0 copias)")
    print("=" * 70)
    
    agotados = {cod: dat for cod, dat in inventario_libros.items() if dat[2] == 0}
    
    if not agotados:
        print("✓ No hay libros agotados")
    else:
        for codigo, datos in agotados.items():
            titulo, autor, copias, precio = datos
            print(f"{codigo}: {titulo} - {autor}")
    
    print("=" * 70)

def actualizar_copias():
    """Actualiza el número de copias de un libro"""
    print("\n--- ACTUALIZAR COPIAS ---")
    codigo = input("Código del libro: ").strip().upper()
    
    if codigo not in inventario_libros:
        print(f"\n❌ El código '{codigo}' no existe")
        return
    
    titulo, autor, copias, precio = inventario_libros[codigo]
    print(f"\nLibro: {titulo}")
    print(f"Copias actuales: {copias}")
    
    try:
        nuevas_copias = int(input("Nuevas copias: "))
        
        if nuevas_copias < 0:
            print("❌ Las copias no pueden ser negativas")
            return
        
        inventario_libros[codigo] = (titulo, autor, nuevas_copias, precio)
        print(f"\n✓ Copias actualizadas: {copias} → {nuevas_copias}")
    except ValueError:
        print("❌ Debe ser un número entero")

def mostrar_menu():
    """Muestra el menú principal"""
    print("\n" + "=" * 70)
    print("              📚 SISTEMA DE INVENTARIO DE LIBROS 📚")
    print("=" * 70)
    print("1.  Mostrar todos los libros")
    print("2.  Buscar libros por autor")
    print("3.  Comprar libro")
    print("4.  Buscar libro por código")
    print("5.  Agregar nuevo libro")
    print("6.  Actualizar copias de un libro")
    print("7.  Ver libros agotados")
    print("8.  Salir")
    print("=" * 70)

# ===== PROGRAMA PRINCIPAL =====

def main():
    print("\n¡Bienvenido a la Librería!")
    
    while True:
        mostrar_menu()
        
        try:
            opcion = int(input("\nSelecciona una opción (1-8): "))
        except ValueError:
            print("\n❌ Por favor ingresa un número válido")
            continue
        
        if opcion == 1:
            mostrar_todos_libros()
            
        elif opcion == 2:
            buscar_libros_por_autor()
            
        elif opcion == 3:
            comprar_libro()
            
        elif opcion == 4:
            buscar_libro_por_codigo()
            
        elif opcion == 5:
            agregar_libro()
            
        elif opcion == 6:
            actualizar_copias()
            
        elif opcion == 7:
            libros_agotados()
            
        elif opcion == 8:
            print("\n¡Gracias por visitar la librería! 📚👋")
            break
            
        else:
            print("\n❌ Opción no válida. Elige entre 1 y 8")

# Ejecutar el programa
if __name__ == "__main__":
    main()