class Strings:
    """
    Clase con métodos para manipulación y operaciones con cadenas de texto.
    Incluye funciones para manipular, validar y transformar strings.
    """
    
    def es_palindromo(self, texto):
        """
        Verifica si una cadena es un palíndromo (se lee igual de izquierda a derecha y viceversa).
        
        Args:
            texto (str): Cadena a verificar
            
        Returns:
            bool: True si es palíndromo, False en caso contrario
        """
        s = ''.join(ch.lower() for ch in texto if ch.isalnum())
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True  
    
    def invertir_cadena(self, texto):
        """
        Invierte una cadena de texto sin usar slicing ni reversed().
        
        Args:
            texto (str): Cadena a invertir
            
        Returns:
            str: Cadena invertida
        """
        res_chars = []
        i = len(texto) - 1
        while i >= 0:
            res_chars.append(texto[i])
            i -= 1
        return ''.join(res_chars)
    
    def contar_vocales(self, texto):
        """
        Cuenta el número de vocales en una cadena.
        
        Args:
            texto (str): Cadena para contar vocales
            
        Returns:
            int: Número de vocales en la cadena
        """
        if not texto:
            return 0
        vocales = set('aeiouáéíóúAEIOUÁÉÍÓÚ')
        conteo = 0
        for ch in texto:
            if ch in vocales:
                conteo += 1
        return conteo
    
    def contar_consonantes(self, texto):
        """
        Cuenta el número de consonantes en una cadena.
        
        Args:
            texto (str): Cadena para contar consonantes
            
        Returns:
            int: Número de consonantes en la cadena
        """
        if not texto:
            return 0
        vocales = set("aeiouáéíóúAEIOUÁÉÍÓÚ")
        conteo = 0
        for ch in texto:
            if ch.isalpha() and ch not in vocales:  # <- clave: NO es vocal
                conteo += 1
        return conteo
    
    def es_anagrama(self, texto1, texto2):
        """
        Verifica si dos cadenas son anagramas (contienen exactamente los mismos caracteres).
        
        Args:
            texto1 (str): Primera cadena
            texto2 (str): Segunda cadena
            
        Returns:
            bool: True si son anagramas, False en caso contrario
        """
        def normaliza(s: str):
            return sorted(ch.lower() for ch in s if ch.isalpha())
        return normaliza(texto1) == normaliza(texto2)
    
    def contar_palabras(self, texto):
        """
        Cuenta el número de palabras en una cadena.
        
        Args:
            texto (str): Cadena para contar palabras
            
        Returns:
            int: Número de palabras en la cadena
        """
        if not texto:
            return 0

        def es_alnum(c: str) -> bool:
            return c.isalpha() or c.isdigit()

        n = len(texto)
        i = 0
        conteo = 0

        while i < n:
            # saltar separadores
            while i < n and not es_alnum(texto[i]):
                i += 1
            if i >= n:
                break

            # encontramos inicio de palabra
            conteo += 1
            i += 1

            # consumir el resto de la palabra
            while i < n:
                c = texto[i]
                if es_alnum(c):
                    i += 1
                elif c in ("'", "-"):
                    # permitir '-' o "'" sólo si está ENTRE caracteres alfanuméricos
                    if i > 0 and i + 1 < n and es_alnum(texto[i - 1]) and es_alnum(texto[i + 1]):
                        i += 1
                    else:
                        break
                else:
                    break

        return conteo        
    
    def palabras_mayus(self, texto):
        """
        Pon en Mayuscula la primera letra de cada palabra en una cadena.
        
        Args:
            texto (str): Cadena
            
        Returns:
            str: Cadena con la primera letra de cada palabra en mayúscula
        """
        if texto is None:
            return ""
        res = []
        inicio_palabra = True  # inicio de cadena cuenta como inicio de palabra
        for ch in texto:
            if ch.isalpha():
                if inicio_palabra:
                    res.append(ch.upper())
                    inicio_palabra = False
                else:
                    res.append(ch.lower())
            else:
                res.append(ch)
                # solo el espacio ' ' marca nuevo inicio (no cambiamos por puntuación)
                inicio_palabra = (ch == ' ')
        return "".join(res)    
    
    def eliminar_espacios_duplicados(self, texto):
        """
        Elimina espacios duplicados en una cadena.
        
        Args:
            texto (str): Cadena con posibles espacios duplicados
            
        Returns:
            str: Cadena sin espacios duplicados
        """
        if texto == "":
            return ""
        out = []
        prev_space = False
        for c in texto:
            if c == ' ':
                if not prev_space:
                    out.append(' ')   # conserva un espacio
                    prev_space = True
                # si ya había espacio, no añadimos otro
            else:
                out.append(c)
                prev_space = False
        return ''.join(out)
    
    def es_numero_entero(self, texto):
        """
        Verifica si una cadena representa un número entero sin usar isdigit().
        
        Args:
            texto (str): Cadena a verificar
            
        Returns:
            bool: True si la cadena representa un número entero, False en caso contrario
        """
        if not texto:
            return False
        i = 0
        if texto[0] in "+-":
            if len(texto) == 1:
                return False
            i = 1
        for ch in texto[i:]:
            if ch < '0' or ch > '9':   # no usar isdigit()
                return False
        return True
    
    def cifrar_cesar(self, texto, desplazamiento):
        """
        Aplica el cifrado César a una cadena de texto.
        
        Args:
            texto (str): Cadena a cifrar
            desplazamiento (int): Número de posiciones a desplazar cada letra
            
        Returns:
            str: Cadena cifrada
        """
        if not texto:
            return ""
        k = desplazamiento % 26
        res = []
        for ch in texto:
            if 'a' <= ch <= 'z':
                res.append(chr((ord(ch) - ord('a') + k) % 26 + ord('a')))
            elif 'A' <= ch <= 'Z':
                res.append(chr((ord(ch) - ord('A') + k) % 26 + ord('A')))
            else:
                res.append(ch)
        return "".join(res)
    
    def descifrar_cesar(self, texto, desplazamiento):
        """
        Descifra una cadena cifrada con el método César.
        
        Args:
            texto (str): Cadena cifrada
            desplazamiento (int): Número de posiciones que se desplazó cada letra
            
        Returns:
            str: Cadena descifrada
        """
        if not texto:
            return ""
        k = desplazamiento % 26
        res = []
        for ch in texto:
            if 'a' <= ch <= 'z':
                res.append(chr((ord(ch) - ord('a') - k) % 26 + ord('a')))
            elif 'A' <= ch <= 'Z':
                res.append(chr((ord(ch) - ord('A') - k) % 26 + ord('A')))
            else:
                res.append(ch)
        return "".join(res)
        
    def encontrar_subcadena(self, texto, subcadena):
        """
        Encuentra todas las posiciones de una subcadena en un texto sin usar find() o index().
        
        Args:
            texto (str): Cadena principal
            subcadena (str): Subcadena a buscar
            
        Returns:
            list: Lista con las posiciones iniciales de cada ocurrencia
        """
        if not texto or not subcadena:
            return []
        n, m = len(texto), len(subcadena)
        if m > n:
            return []
        pos = []
        # Búsqueda ingenua O(n*m) con solapamientos
        for i in range(n - m + 1):
            j = 0
            while j < m and texto[i + j] == subcadena[j]:
                j += 1
            if j == m:
                pos.append(i)
        return pos