#codigo propio
from apps.profiles.models import *
from apps.profiles.serializers import *

#librerias de restframework
from rest_framework.decorators import *
from rest_framework import viewsets
from rest_framework.permissions import *
from rest_framework.response import Response

#librerias django
from django.contrib.auth.models import User
from django.http import JsonResponse

#librerias para enviar correos
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string, get_template
from django.utils.html import strip_tags

from django.utils.crypto import get_random_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator

@api_view(['POST'])
@permission_classes((AllowAny, ))
def send_code_sms(request):
    try:
        email = request.data['email']
        validation_email = User.objects.filter(email = email).exists()
        if validation_email:
            ramdom_verify=get_random_string(length=6, allowed_chars='1234567890')
            get_user = User.objects.get(email = email)
            #Almacenar la información en la tabla ubicaciones
            code_verify = CodeVerify(code = ramdom_verify, user_id = get_user.id, state_id=1)
            code_verify.save()

            send_mail('Restablecer contraseña Sapo', ' Tu código de verificacíon para restaurar la contraseña en nuestro sitio Sapo es '+ ramdom_verify, 'sapo@eurekadms.com', [email])
            data= JsonResponse({"Mensaje": "Se ha enviado un código al email registrado , por favor verifique en su correo", "usuario": get_user.id})
            return data
        else: #El email ya existe
            data = JsonResponse({"Mensaje": "El email no existe"})
            data.status_code = 404
            return data
    except Exception as e:
        data = JsonResponse({"Mensaje": "Revise su conexion a internet","error":str(e)})
        data.status_code = 500
        return data

@api_view(['POST'])
@permission_classes((AllowAny, ))
def validate_code_sms(request):
    try:
        user = request.data['user']
        code = request.data['code']
        print("Usuario: ",user,"codigo: ", code)
        code_verify = CodeVerify.objects.get(user_id=user)
        if code_verify.code == request.data['code'] and code_verify.state_id == 1:
            get_user = User.objects.get(id = user)
            code_verify.state_id=2
            code_verify.save()
            token_generator=default_token_generator.make_token(get_user)
            # en la versión 2.. funciona sin .decode() por actualizaciones
            encode_uid= urlsafe_base64_encode(force_bytes(get_user.id))
            data=JsonResponse({"Mensaje": "Código valido, proceda a cambiar la contraseña", "uid": encode_uid, "token": token_generator})
            # data= JsonResponse({"Mensaje": "Código valido, proceda a cambiar la contraseña", "usuario": encode_uid, "token": token_generator})
            return data
        else: #El email ya existe
            data=JsonResponse({"Mensaje": "Codigó no valido o caducado"})
            data.status_code = 404
            return data
    except Exception as e:
        print(e)
        data=JsonResponse({"Mensaje": "Usuario no valido"})
        data.status_code = 500
        return data