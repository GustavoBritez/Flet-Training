from Login.ORM.ORM import obtener_sesion
from Login.Be.UsuarioBE import UsuarioBE

class UsuarioService:
    @staticmethod
    def registrar_usuario(usuario_be: UsuarioBE):
        """
        Recibe una entidad de negocio y la persiste en SQL Server 
        usando una transacción.
        """
        # Obtenemos la sesión del ORM (Equivalente al DbContext)
        session = obtener_sesion()
        
        try:
            # 1. Validaciones de Negocio (BLL)
            if "@" not in usuario_be.email:
                raise Exception("El formato del correo no es válido.")
            
            if len(usuario_be.password) < 4:
                raise Exception("La contraseña es demasiado corta.")

            # 2. Iniciar Transacción y Agregar
            session.add(usuario_be)
            
            # 3. Confirmar cambios (Commit)
            session.commit()
            return {"success": True, "message": "Usuario registrado con éxito."}
            
        except Exception as e:
            # 4. Si algo falla, deshacemos todo (Rollback)
            session.rollback()
            return {"success": False, "message": str(e)}
            
        finally:
            # 5. Siempre cerramos la conexión
            session.close()