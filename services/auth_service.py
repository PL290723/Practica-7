from dataclasses import dataclass

@dataclass(frozen=True)
class AuthResult:
    ok: bool
    message: str = ""
    role: str = ""  # New field to store the role

class AuthService:
    """
    Servicio de autenticación. Admite admin, estudiante, maestro.
    """
    # Hardcoded credentials for simplicity as requested
    USERS = {
        "admin": "1234",
        "estudiante": "1234",
        "maestro": "1234"
    }

    def login(self, username: str, password: str) -> AuthResult:
        if not username or not password:
            return AuthResult(False, "Usuario y contraseña son requeridos.")
        
        # Check if user exists and password matches
        if username in self.USERS and self.USERS[username] == password:
             # For this simple example, the role is the username itself (admin, estudiante, maestro)
             # In a real app, we would map username -> role
            return AuthResult(True, "Autenticación exitosa.", role=username)
            
        return AuthResult(False, "Usuario o contraseña incorrectos.")
