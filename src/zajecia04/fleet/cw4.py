import datetime

from src.zajecia04.fleet.ambulance import Ambulance
from src.zajecia04.fleet.station import Station
from src.zajecia04.operations.incident import Incident
from src.zajecia04.operations.incident_queue import IncidentQueue
from src.zajecia04.personnel.employee import Employee
from src.zajecia04.personnel.driver import Driver
from datetime import time, datetime, timedelta
import numpy as np

# Zarządzanie incydentami

incident1 = Incident("Power outage in sector 4", 1, time(20, 8, 12), dict(imie="Cyprian", naziwsko="Szot"),
                     location=(50, 14))
incident2 = Incident("Fire alarm in building 21", 3, time(14, 9, 18), dict(imie="Troy", nazwisko="Sivan"),
                     location=(48, 9))
incident3 = Incident("Fire alarm in building 129", 2, time(16, 11, 41), dict(imie="Kamil", nazwisko="Bednarek"),
                     location=(56, 18))

ambulance1 = Ambulance(
    vehicle_type="AZ124",
    status="Available",
    location=(50.095340, 19.920282),
    medical_equipment=["defibrillator", "stretcher"]
)
ambulance2 = Ambulance(
    vehicle_type="AZ2000",
    status="invalid",
    location=(59.095340, 12.920282),
    medical_equipment=["defibrillator", "stretcher"]
)
ambulance3 = Ambulance(
    vehicle_type="AZ2100",
    status="Available",
    location=(51.095340, 14.920282),
    medical_equipment=["defibrillator", "stretcher"]
)

incidents = [incident1, incident2, incident3]
ambulances = [ambulance1, ambulance2, ambulance3]


def odleglosc(incident, ambulances):
    min_distance = float('inf')
    chosen_ambulance = None
    iter = 0

    for ambulance in ambulances:
        iter += 1
        if ambulance.status == "invalid":
            continue

        # Obliczamy dystans euklidesowy między incydentem a karetką
        dist = (incident.location[0] - ambulance.location[0]) ** 2 + (incident.location[1] - ambulance.location[1]) ** 2

        # Sprawdzamy, czy dystans jest mniejszy od aktualnego minimalnego
        if dist < min_distance:
            min_distance = dist
            chosen_ambulance = ambulance

    return chosen_ambulance


def czas(incident:Incident):
    actual_time = datetime.combine(datetime.today(), datetime.now().time())
    time2 = datetime.combine(datetime.today(), incident.application_time)
    difference = abs(actual_time - time2)

    print(f"Czas od zaistnienia incydentu: {difference}\n")


def przypisanie(incident):
    chosen_ambulance = odleglosc(incident, ambulances)

    if chosen_ambulance is not None:
        ambulances.remove(chosen_ambulance)
        print(f"Chosen ambulance for incident: {incident.description} is {chosen_ambulance.vehicle_type}")
    else:
        print(f"No available ambulance for incident: {incident.description}")


# Przypisanie najbliższej dostępnej karetki do incydentu o priorytecie 1
for incident in incidents:
    if incident.priority == 1:
        przypisanie(incident)
        czas(incident)
    elif incident.priority == 2:
        przypisanie(incident)
        czas(incident)
    elif incident.priority == 3:
        przypisanie(incident)
        czas(incident)

