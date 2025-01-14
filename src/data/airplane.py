import uuid

class Airplane:
    def __init__(self, airplane_type, registration, model, power, price, fuel, tank_capacity, consumption, places, date):
        self.id = uuid.uuid4()
        self.type = airplane_type
        self.registration = registration
        self.model = model
        self.power = power
        self.price = price
        self.fuel = fuel
        self.tank_capacity = tank_capacity
        self.consumption = consumption
        self.places = places
        self.free_slots = [{"start": date.replace(hour=8, minute=0, second=0, microsecond=0), "end": date.replace(hour=20, minute=0, second=0, microsecond=0)}]
        self.reservations = []
        self.date = date

    def print(self):
        print(f"======={self.registration}========")
        print(f"Type: {self.type}")
        print(f"Registration: {self.registration}")
        print(f"Model: {self.model}")
        print(f"Power: {self.power}")
        print(f"Price: {self.price}")
        print(f"Fuel: {self.fuel}")
        print(f"Tank capacity: {self.tank_capacity}")
        print(f"Consumption: {self.consumption}")
        print(f"Places: {self.places}")
        print(f"Free slots: {self.free_slots}")
        print("===============" + self.registration.__len__() * "=")

    def push_reservation(self, reservation):
        self.free_slots = []
        self.reservations.append(reservation)
        self.reservations = sorted(self.reservations, key=lambda x: x.start.hour)

        current = self.date.replace(hour=8, minute=0, second=0, microsecond=0)
        end = self.date.replace(hour=20, minute=0, second=0, microsecond=0)
        for resa in self.reservations:
            if resa.start > current:
                self.free_slots.append({"start": current, "end": resa.start})
            current = resa.end
        if current < end:
            self.free_slots.append({"start": current, "end": end})

    def __str__(self):
        return f"{self.type} {self.registration} {self.model} {self.power} {self.price} {self.fuel} {self.tank_capacity} {self.consumption} {self.places}"

    @staticmethod
    def from_raw(data, date):
        airplane_type = data.get('<label style="font-weight', "")
        if not (airplane_type == ""):
            airplane_type = airplane_type.split(">")[1].split("<")[0]
        registration = data.get("Immatriculation", "")
        model = data.get("Modele", "")
        power = data.get("Puissance", "")
        price = data.get("Prix(€/h)", "")
        fuel = data.get("Carburant", "")
        tank_capacity = data.get("Capacité réservoir", "")
        consumption = data.get("Consommation", "")
        places = data.get("Places", "")
        return Airplane(airplane_type, registration, model, power, price, fuel, tank_capacity, consumption, places, date)
        