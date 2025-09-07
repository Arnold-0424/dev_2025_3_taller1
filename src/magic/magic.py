class Magic:
    """
    Clase con métodos para juegos matemáticos, secuencias especiales y algoritmos numéricos.
    Incluye implementaciones de Fibonacci, números perfectos, triangulo de pascal etc.
    """
    
    def fibonacci(self, n):
        """
        Calcula el n-ésimo número de la secuencia de Fibonacci.
        
        Args:
            n (int): Posición en la secuencia (empezando desde 0)
            
        Returns:
            int: El n-ésimo número de Fibonacci
        """
        def fibonacci(self, n: int) -> int:
            if n < 0:
                raise ValueError("n debe ser >= 0")
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a
    
    def secuencia_fibonacci(self, n):
        """
        Genera los primeros n números de la secuencia de Fibonacci.
        
        Args:
            n (int): Cantidad de números a generar
            
        Returns:
            list: Lista con los primeros n números de Fibonacci
        """
        if n < 0:
            raise ValueError("n debe ser >= 0")
        seq = []
        a, b = 0, 1
        for _ in range(n):
            seq.append(a)
            a, b = b, a + b
        return seq
    
    def es_primo(self, n):
        """
        Verifica si un número es primo.
        
        Args:
            n (int): Número a verificar
            
        Returns:
            bool: True si n es primo, False en caso contrario
        """
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    
    def generar_primos(self, n):
        """
        Genera una lista de números primos hasta n.
        
        Args:
            n (int): Límite superior para generar primos
            
        Returns:
            list: Lista de números primos hasta n
        """
        if n < 2:
            return []
        primos = []
        for i in range(2, n + 1):  # <-- aquí el cambio
            es_primo = True
            for j in range(2, int(i**0.5) + 1):
                if i % j == 0:
                    es_primo = False
                    break
            if es_primo:
                primos.append(i)
        return primos

    
    def es_numero_perfecto(self, n):
        """
        Verifica si un número es perfecto (igual a la suma de sus divisores propios).
        
        Args:
            n (int): Número a verificar
            
        Returns:
            bool: True si n es un número perfecto, False en caso contrario
        """
        if n < 2:
            return False
        suma = 1
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                suma += i
                if i != n // i:
                    suma += n // i
        return suma == n
    
    def triangulo_pascal(self, filas):
        """
        Genera las primeras n filas del triángulo de Pascal.
        
        Args:
            filas (int): Número de filas a generar
            
        Returns:
            list: Lista de listas que representa el triángulo de Pascal
        """
        if filas <= 0:
            return []
        tri = [[1]]
        for i in range(1, filas):
            fila = [1]
            for j in range(1, i):
                fila.append(tri[i - 1][j - 1] + tri[i - 1][j])
            fila.append(1)
            tri.append(fila)
        return tri
    
    def factorial(self, n):
        """
        Calcula el factorial de un número.
        
        Args:
            n (int): Número para calcular su factorial
            
        Returns:
            int: El factorial de n
        """
        if n < 0:
            raise ValueError("n debe ser >= 0")
        r = 1
        for i in range(2, n + 1):
            r *= i
        return r
    
    def mcd(self, a, b):
        """
        Calcula el máximo común divisor de dos números.
        
        Args:
            a (int): Primer número
            b (int): Segundo número
            
        Returns:
            int: El máximo común divisor de a y b
        """
        a, b = abs(a), abs(b)
        if a == 0 and b == 0:
            return 0
        while b:
            a, b = b, a % b
        return a
    
    def mcm(self, a, b):
        """
        Calcula el mínimo común múltiplo de dos números.
        
        Args:
            a (int): Primer número
            b (int): Segundo número
            
        Returns:
            int: El mínimo común múltiplo de a y b
        """
        if a == 0 or b == 0:
            return 0
        return abs(a * b) // self.mcd(a, b)
    
    def suma_digitos(self, n):
        """
        Calcula la suma de los dígitos de un número.
        
        Args:
            n (int): Número para sumar sus dígitos
            
        Returns:
            int: La suma de los dígitos de n
        """
        return sum(int(d) for d in str(abs(n)))
    
    def es_numero_armstrong(self, n):
        """
        Verifica si un número es de Armstrong (igual a la suma de sus dígitos elevados a la potencia del número de dígitos).
        
        Args:
            n (int): Número a verificar
            
        Returns:
            bool: True si n es un número de Armstrong, False en caso contrario
        """
        str_n = str(n)
        num_digs = len(str_n)
        return sum(int(d) ** num_digs for d in str_n) == n
    
    def es_cuadrado_magico(self, matriz):
        """
        Verifica si una matriz es un cuadrado mágico (suma igual en filas, columnas y diagonales).
        
        Args:
            matriz (list): Lista de listas que representa una matriz cuadrada
            
        Returns:
            bool: True si es un cuadrado mágico, False en caso contrario
        """
        n = len(matriz)
        if any(len(fila) != n for fila in matriz):
            return False  # No es cuadrada

        suma_ideal = sum(matriz[0])

        # Suma de filas
        for fila in matriz:
            if sum(fila) != suma_ideal:
                return False

        # Suma de columnas
        for col in range(n):
            if sum(matriz[fila][col] for fila in range(n)) != suma_ideal:
                return False

        # Diagonal principal
        if sum(matriz[i][i] for i in range(n)) != suma_ideal:
            return False

        # Diagonal secundaria
        if sum(matriz[i][n - 1 - i] for i in range(n)) != suma_ideal:
            return False

        return True