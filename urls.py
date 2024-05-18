from django.urls import path
from piPlant import views

urlpatterns = [
	path("", views.home),
	path("Startseite", views.Startseite),
	path("EmailsVerwalten", views.verwaltung),
	path("Einstellungen", views.einstellungen),
	path("SensorDatenEmpfang", views.sensor_data_receiver),	
]
