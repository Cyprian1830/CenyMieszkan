from src.zajecia04.operations.incident import Incident


class IncidentQueue:
    __max_id = 0

    def __init__(self):
        IncidentQueue.__max_id += 1
        self.id = IncidentQueue.__max_id
        self.__queue = []

    def __getitem__(self, position):
        return self.__queue[position]

    def __setitem__(self, position, value):
        self.__queue[position] = value

    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        if self._index < len(self.__queue):
            result = self.__queue[self._index]
            self._index += 1
            return result
        else:
            raise StopIteration

    def __contains__(self, incident):
        return incident in self.__queue

    def __repr__(self):
        return f"IncidentQueue({self.__queue!r})"

    def __str__(self):
        if len(self):
            return "\n".join([
                f"{' ' * (4 * idx)}{incident}"
                for idx, incident in enumerate(self.__queue)
            ])
        else:
            return "Empty queue"

    def __add__(self, other):
        if isinstance(other, Incident):
            new__queue = IncidentQueue()
            new__queue.__queue = self.__queue[:]
            new__queue += other
            return new__queue
        else:
            return NotImplemented

    def __radd__(self, other):
        if isinstance(other, Incident):
            new__queue = IncidentQueue()
            new__queue += other
            new__queue.__queue += self.__queue
            return new__queue
        else:
            return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, Incident):
            self.__queue.append(other)
        return self

    def __call__(self, id):
        for incident in self.__queue:
            if incident.id == id:
                return incident
            pass
        raise ValueError("No incident found with the given ID")

    def __lt__(self, other):
        return len(self.__queue) < len(other.__queue)

    def __gt__(self, other):
        return len(self.__queue) > len(other.__queue)

    def __bool__(self):
        return bool(self.__queue)

    def __len__(self):
        return len(self.__queue)


if __name__ == "__main__":
    queue = IncidentQueue()
    #    incident1 = Incident("Power outage in sector 4", 1, time(20, 8, 12), dict(imie="Cyprian", naziwsko="Szot"))
    #   incident2 = Incident("Fire alarm in building 21", 3, time(14, 9, 18), dict(imie="Troy", nazwisko="Sivan"))
    #  incident4 = Incident("Fire alarm in building 129", 2, time(18, 10, 1), dict(imie="Kamil", nazwisko="Bednarek"))

    print("---------- wyświetlanie za pomocą __str__ ----------")
    #  print(queue)

    print("---------- dodanie za pomocą __iadd__ ----------")
    #  queue += incident1
    # queue += incident2
    # print(queue)
    print("---------- dodanie za pomocą __add__ ----------")
    #   queue = queue + incident4
    # print(queue)

    print("---------- dostęp za pomocą __getitem__ ----------")
    #    print(queue[0])
    print("---------- sprawdzenie za pomocą __contains__ ----------")
    # print(incident1 in queue)

    print("---------- iteracja za pomocą __iter__ i __next__ ----------")
    # for incident in queue:
    #      print(incident)

    print("---------- dodawanie prawostronne za pomocą __radd__ ----------")
    #    new_incident = Incident("Test incident", 1, time(20, 50, 19),
    #                             dict(imie="Zofia", nazwisko="Mrowiec"), Ambulance("car", "invalid", "Gdansk", "none"))
    # queue = new_incident + queue

    print("---------- test za pomocą __bool__ ----------")
    #   if queue:
    print("Queue is not empty.")

    print("---------- długość kolejki za pomocą __len__ ----------")
    #  print(len(queue))

    print("---------- wyszukiwanie za pomocą __call__ ----------")
    # print(queue(1))
