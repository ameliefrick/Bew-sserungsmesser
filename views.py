from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
import os
from django.conf import settings
from datetime import datetime, date
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
	return render(request, 'piPlant/Startseite.html')

def Startseite(request):
	return render(request, 'piPlant/Startseite.html')


def verwaltung(request):
	return render(request, 'piPlant/EmailsVerwalten.html')

def einstellungen(request):
	return render(request, 'piPlant/Einstellungen.html')

@csrf_exempt
def sensor_data_receiver(request):
	if request.method == 'GET':
		return render(request, 'piPlant/Startseite.html')

	if request.method == 'POST':
		sensordaten = {}
		try:
			with open("/home/ubuntu/django-test/piPlant/templates/piPlant/sensordata/aktuelleSensorDaten.json", "r") as datei:
				sensordaten = datei.read()

			neueData = json.loads(request.body.decode("utf-8"))
			sensordaten.append(neueData)
			with open("/home/ubuntu/django-test/piPlant/templates/piPlant/sensordata/aktuelleSensorDaten.json", "w") as datei:
				datei.write(json.dumps(sensordaten))
			return JsonResponse({'success': True})

		except Exception as fehlermeldung:
			return JsonResponse({'success': False, 'error': str(fehlermeldung)}, status=400)
	else:
		return JsonResponse({'error': 'Unsupported method'}, status=405)
		return HttpResponse("Hier werden Sensordaten empfangen")


