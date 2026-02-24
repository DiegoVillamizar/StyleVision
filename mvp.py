"""
StyleVision - MVP (Producto Mínimo Viable)
Prototipo de consola para selección y previsualización de cortes de cabello.
Asignatura: Diseño Funcional
"""

# ── Datos del sistema ─────────────────────────────────────────────

APP_NAME: str    = "StyleVision"
APP_VERSION: str = "1.0.0"

available_styles: list    = ["ST_001_FADE", "ST_002_UNDERCUT",
                              "ST_003_BUZZ_CUT", "ST_004_POMPADOUR"]
style_display_names: list = ["Fade Clásico", "Undercut Ejecutivo",
                              "Buzz Cut Militar", "Pompadour Moderno"]
style_prices: list        = [25000, 30000, 20000, 35000]
style_durations: list     = [30, 45, 20, 50]

session_history: list     = []

# ── Funciones del sistema ─────────────────────────────────────────

def mostrar_bienvenida(nombre: str) -> None:
    """Muestra el mensaje de bienvenida al usuario."""
    print("=" * 45)
    print(f"  Bienvenido a {APP_NAME} v{APP_VERSION}")
    print(f"  Hola, {nombre.strip().title()}!")
    print("=" * 45)


def mostrar_catalogo() -> None:
    """Muestra el catálogo de estilos disponibles."""
    print("\n📋 Estilos disponibles:\n")
    for i in range(len(available_styles)):
        print(f"  [{i + 1}] {style_display_names[i]}"
              f" — ${style_prices[i]:,} — {style_durations[i]} min")


def seleccionar_estilo(opcion: int) -> bool:
    """Valida que la opción seleccionada esté dentro del rango del catálogo."""
    return 1 <= opcion <= len(available_styles)


def calcular_precio_final(precio: int, descuento: float) -> float:
    """Calcula el precio final aplicando el porcentaje de descuento."""
    return precio - (precio * descuento)


def mostrar_resumen(indice: int, nombre: str) -> None:
    """Muestra el resumen del servicio seleccionado."""
    precio_final: float   = calcular_precio_final(style_prices[indice], 0.10)
    descuento_valor: float = style_prices[indice] * 0.10

    print("\n" + "=" * 45)
    print("  RESUMEN DEL SERVICIO")
    print("=" * 45)
    print(f"  Cliente      : {nombre.strip().title()}")
    print(f"  Estilo       : {style_display_names[indice]}")
    print(f"  Duración     : {style_durations[indice]} minutos")
    print(f"  Precio base  : ${style_prices[indice]:,}")
    print(f"  Descuento    : -${descuento_valor:,.0f} (10%)")
    print(f"  Precio final : ${precio_final:,.0f}")
    print("=" * 45)
    print("  ✅ Previsualización generada con éxito.")
    print("=" * 45)


# ── Ejecución principal ───────────────────────────────────────────

if __name__ == "__main__":

    # Entrada del usuario
    raw_nombre: str = input("\nIngresa tu nombre: ")

    # Validación del nombre
    nombre_valido: bool = len(raw_nombre.strip()) > 0
    if not nombre_valido:
        print("❌ Nombre no válido. Intenta de nuevo.")
    else:
        mostrar_bienvenida(raw_nombre)
        mostrar_catalogo()

        # Selección de estilo
        raw_opcion: str = input("\nSelecciona un estilo (número): ")

        # Validación de la opción
        opcion_valida: bool = raw_opcion.isdigit()
        if not opcion_valida:
            print("❌ Opción no válida. Debe ser un número.")
        else:
            opcion: int = int(raw_opcion)
            if seleccionar_estilo(opcion):
                indice: int = opcion - 1
                session_history.append(available_styles[indice])
                mostrar_resumen(indice, raw_nombre)
                print(f"\n  Estilos previsualizados en sesión: {len(session_history)}")
            else:
                print("❌ Opción fuera de rango. Elige entre 1 y 4.")