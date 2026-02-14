from dataclasses import dataclass

@dataclass(frozen=True)
class AuthResult:
    ok: bool
    message: str = ""
    role: str = ""

class AuthService:
    """
    Servicio de autenticación. Admite admin, estudiante, maestro.
    """
    USERS = {
        "admin": "1234",
        "estudiante": "1234",
        "maestro": "1234"
    }

    def login(self, username: str, password: str) -> AuthResult:
        if not username or not password:
            return AuthResult(False, "Usuario y contraseña son requeridos.")
        
        if username in self.USERS and self.USERS[username] == password:
            return AuthResult(True, "Autenticación exitosa.", role=username)
            
        return AuthResult(False, "Usuario o contraseña incorrectos.")
