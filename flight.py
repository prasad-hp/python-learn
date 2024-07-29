class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
    def addpassanger(self,passenger):
        if not self.open_seats():
            print("There is no capacity")
            return False
        else:
            self.passengers.append(passenger)
            print(f"Passenger added {passenger}")
            return True
    def open_seats(self):
        return self.capacity - len(self.passengers)

passengers = ["asd", "dad", "asdasdas", "dadas"]
flight = Flight(3)
for per in passengers:
    flight.addpassanger(per)
