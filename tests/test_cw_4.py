from datetime import time, datetime
from src.zajecia04.fleet import *
from src.zajecia04.operations import *


def test_e2e_simulation():
    # Tworzenie instancji incydentów i karetek
    incident1 = Incident(
        "Power outage in sector 4",
        1,
        time(20, 8, 12),
        dict(imie="Cyprian", naziwsko="Szot"),
        location=(50, 14),
    )
    incident2 = Incident(
        "Fire alarm in building 21",
        3,
        time(14, 9, 18),
        dict(imie="Troy", nazwisko="Sivan"),
        location=(48, 9),
    )
    incident3 = Incident(
        "Fire alarm in building 129",
        2,
        time(16, 11, 41),
        dict(imie="Kamil", nazwisko="Bednarek"),
        location=(56, 18),
    )

    ambulance1 = Ambulance(
        vehicle_type="AZ124",
        status="Available",
        location=(50.095340, 19.920282),
        medical_equipment=["defibrillator", "stretcher"],
    )
    ambulance2 = Ambulance(
        vehicle_type="AZ2000",
        status="invalid",
        location=(59.095340, 12.920282),
        medical_equipment=["defibrillator", "stretcher"],
    )
    ambulance3 = Ambulance(
        vehicle_type="AZ2100",
        status="Available",
        location=(51.095340, 14.920282),
        medical_equipment=["defibrillator", "stretcher"],
    )

    incidents = [incident1, incident2, incident3]
    ambulances = [ambulance1, ambulance2, ambulance3]

    def testy_jednostkowe(karetka: Ambulance):
        assert karetka.location[0] >= 0 and karetka.location[1] >= 0, (
            "Karetka ma błędną lokalizację!"
        )
        assert isinstance(karetka.id, int), "ID karetki nie jest liczbą całkowitą!"

    def odleglosc(incident, ambulances):
        min_distance = float("inf")
        chosen_ambulance = None

        for ambulance in ambulances:
            testy_jednostkowe(ambulance)
            if ambulance.status == "invalid":
                continue

            # Obliczamy dystans euklidesowy między incydentem a karetką
            dist = (incident.location[0] - ambulance.location[0]) ** 2 + (
                incident.location[1] - ambulance.location[1]
            ) ** 2

            if dist < min_distance:
                min_distance = dist
                chosen_ambulance = ambulance

        return chosen_ambulance

    def czas(incident: Incident):
        actual_time = datetime.combine(datetime.today(), datetime.now().time())
        time2 = datetime.combine(datetime.today(), incident.application_time)
        difference = abs(actual_time - time2)
        print(f"Czas od zaistnienia incydentu '{incident.description}': {difference}")
        return difference

    def przypisanie(incident):
        chosen_ambulance = odleglosc(incident, ambulances)

        if chosen_ambulance is not None:
            ambulances.remove(chosen_ambulance)
            print(
                f"Wybrana karetka dla incydentu '{incident.description}' to {chosen_ambulance.vehicle_type}"
            )
        else:
            print(f"Brak dostępnych karetek dla incydentu: {incident.description}")
        return chosen_ambulance

    # Symulacja działania systemu
    for incident in incidents:
        assigned_ambulance = przypisanie(incident)
        incident_time_diff = czas(incident)

        # Walidacja wyników
        if incident.priority == 1:
            assert assigned_ambulance is not None, (
                "Nie przypisano karetki dla priorytetu 1!"
            )
        # elif incident.priority == 2:
        #     assert assigned_ambulance is not None, "Nie przypisano karetki dla priorytetu 2!"
        elif incident.priority == 3:
            assert assigned_ambulance is not None, (
                "Nie przypisano karetki dla priorytetu 3!"
            )

    print("Symulacja E2E zakończona sukcesem!")


# Uruchomienie symulacji E2E
test_e2e_simulation()
