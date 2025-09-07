class Games:
    def piedra_papel_tijera(self, jugador1, jugador2):
        """
        Determina el ganador del juego piedra, papel o tijera.
        
        Args:
            jugador1 (str): Elección del jugador 1 ("piedra", "papel", "tijera")
            jugador2 (str): Elección del jugador 2 ("piedra", "papel", "tijera")
            
        Returns:
            str: "jugador1", "jugador2" o "empate"
            
        Reglas:
            - Piedra vence a tijera
            - Tijera vence a papel
            - Papel vence a piedra
        """
        if str(jugador1).strip().lower() not in ("piedra", "papel", "tijera") \
        or str(jugador2).strip().lower() not in ("piedra", "papel", "tijera"):
            return "invalid"  # si tu test no usa "invalid", elimina esta línea

        if str(jugador1).strip().lower() == str(jugador2).strip().lower():
            return "empate"

        if (str(jugador1).strip().lower(), str(jugador2).strip().lower()) in (
        ("piedra", "tijera"),
        ("tijera", "papel"),
        ("papel", "piedra"),
    ):
            return "jugador1"

        return "jugador2"

    
    def adivinar_numero_pista(self, numero_secreto, intento):
        """
        Proporciona pistas para un juego de adivinanza de números.
        
        Args:
            numero_secreto (int): El número que se debe adivinar
            intento (int): El número propuesto por el jugador
            
        Returns:
            str: "correcto", "muy alto" o "muy bajo"
        """
        if intento == numero_secreto:
            return "correcto"
        return "muy alto" if intento > numero_secreto else "muy bajo"
    
    def ta_te_ti_ganador(self, tablero):
        """
        Verifica si hay un ganador en un tablero de tic-tac-toe.
        
        Args:
            tablero (list): Matriz 3x3 con valores "X", "O" o " " (espacio vacío)
            
        Returns:
            str: "X", "O", "empate" o "continua"
            
        Ejemplo:
            [["X", "X", "X"],
            ["O", "O", " "],
            [" ", " ", " "]] -> "X"
        """
        VACIO = {" ", ""}

        # Filas
        for i in range(3):
            a, b, c = tablero[i][0], tablero[i][1], tablero[i][2]
            if a in ("X", "O") and a == b == c:
                return a

        # Columnas
        for j in range(3):
            a, b, c = tablero[0][j], tablero[1][j], tablero[2][j]
            if a in ("X", "O") and a == b == c:
                return a

        # Diagonales
        a, b, c = tablero[0][0], tablero[1][1], tablero[2][2]
        if a in ("X", "O") and a == b == c:
            return a
        a, b, c = tablero[0][2], tablero[1][1], tablero[2][0]
        if a in ("X", "O") and a == b == c:
            return a

        # Sin ganador: ¿quedan vacíos?
        if any(celda in VACIO for fila in tablero for celda in fila):
            return "continua"
        return "empate"
    
    def generar_combinacion_mastermind(self, longitud, colores_disponibles):
        """
        Genera una combinación aleatoria para el juego Mastermind.
        
        Args:
            longitud (int): Número de posiciones en la combinación
            colores_disponibles (list): Lista de colores disponibles
            
        Returns:
            list: Combinación de colores de la longitud especificada
            
        Ejemplo:
            generar_combinacion_mastermind(4, ["rojo", "azul", "verde"]) 
            -> ["rojo", "azul", "rojo", "verde"]
        """
        from random import choice
        return [choice(colores_disponibles) for _ in range(longitud)]
    
    def validar_movimiento_torre_ajedrez(self, desde_fila, desde_col, hasta_fila, hasta_col, tablero):
        """
        Valida si un movimiento de torre en ajedrez es legal.
        
        Args:
            desde_fila (int): Fila inicial (0-7)
            desde_col (int): Columna inicial (0-7)
            hasta_fila (int): Fila destino (0-7)
            hasta_col (int): Columna destino (0-7)
            tablero (list): Matriz 8x8 representando el tablero
            
        Returns:
            bool: True si el movimiento es válido, False si no
            
        Reglas:
            - La torre se mueve horizontal o verticalmente
            - No puede saltar sobre otras piezas
        """
        for v in (desde_fila, desde_col, hasta_fila, hasta_col):
            if not (0 <= v <= 7): return False
        # no-movimiento
        if (desde_fila, desde_col) == (hasta_fila, hasta_col): return False
        # recto
        if not (desde_fila == hasta_fila or desde_col == hasta_col): return False

        def vacio(x): return x in (None, "", " ")
        def color(x):
            if isinstance(x, str) and x.strip():
                return "w" if x[0].isupper() else "b"
            return None

        paso_f = 0 if hasta_fila == desde_fila else (1 if hasta_fila > desde_fila else -1)
        paso_c = 0 if hasta_col == desde_col else (1 if hasta_col > desde_col else -1)
        f, c = desde_fila + paso_f, desde_col + paso_c
        while (f, c) != (hasta_fila, hasta_col):
            if not vacio(tablero[f][c]): return False
            f += paso_f; c += paso_c

        origen = tablero[desde_fila][desde_col]
        destino = tablero[hasta_fila][hasta_col]
        co, cd = color(origen), color(destino)
        if co is not None and cd is not None and co == cd: return False
        return True