from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import BotData

# Create your views here.

@csrf_exempt
def receive_data(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            id = data.get("id")
            idsig = data.get("idsig")
            tipo_doc = data.get("tipo_doc")
            numero_doc = data.get("numero_doc")
            numero_tele = data.get("numero_tele")
            operadora = data.get("operadora")
            respuesta_bot = f"Hola, procesé el ID_SIG: {idsig}"

            # Guardar los datos en la base de datos
            BotData.objects.create(
                id=id,
                idsig=idsig,
                tipo_doc=tipo_doc,
                numero_doc=numero_doc,
                numero_tele=numero_tele,
                operadora=operadora,
                respuesta_bot=respuesta_bot
            )

            # Responder a la solicitud POST
            response = {"id": id, "respuesta_bot": respuesta_bot}
            return JsonResponse(response, status=201)
        except json.JSONDecodeError:
            return JsonResponse({"error": "JSON inválido"}, status=400)

def get_data(request):
    if request.method == "GET":
        # Obtener todos los campos del modelo
        data = list(BotData.objects.values(
            'id', 
            'idsig', 
            'tipo_doc', 
            'numero_doc', 
            'numero_tele', 
            'operadora', 
            'respuesta_bot'
        ))
        return JsonResponse(data, safe=False)