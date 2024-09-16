from django.contrib import messages
from django.contrib.auth.models import User
from django.db.utils import IntegrityError


def crear_usuario(request, username:str, first_name:str, email:str, password:str, pass_confirm:str ):
    if password != pass_confirm:
        messages.warning(request, 'Las Contraseñas no coinciden')
        return False
    # llega aqui es porque el password es igual
    if len(password) > 50:
        messages.warning(request, 'La contraseña no puede tener más de 50 caracteres')
        return False
    # llega aqui es porque el password es menor a 50
    try:
        user = User.objects.create_user(
            username=username, 
            first_name=first_name,            
            email=email, 
            password=password,            
        )
    # si hay un usuario duplicado    
    except IntegrityError:
        messages.warning(request, 'El usuario ya existe')
        return False
    except Exception:
        messages.warning(request, 'No se ha creado el usuario')
        return False
    # si llega aqui. es porque se creo el usuario
    messages.success(request, 'El usuario se ha creado correctamente, ya puede ingresar')
    return True
