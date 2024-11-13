from datetime import time
from src.zajecia04.fleet.ambulance import Ambulance

class Incident:
    __max_id = 0

    def __init__(self, description, priority: int, application_time:time, applicant_info: dict, location):
        Incident.__max_id += 1
        self.id = Incident.__max_id
        self.description = description
        self.priority = priority
        self.application_time = application_time
        self.applicant_info = applicant_info
        self.location = location

    def __repr__(self):
        return (f"Incident(id={self.id!r}, description={self.description!r}, "
                f"priority={self.priority!r}, application_time={self.application_time!r},"
                f"applicant_info={self.applicant_info!r}")


    def __str__(self):
        return (f"Incident {self.id}: {self.description}, {self.priority}, {self.application_time}"
                f"{self.applicant_info}")
