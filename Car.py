class Car:
    def __init__(self, color, car_company, license_plate_number, owner_name):
        self.color = color
        self.car_company = car_company
        self.license_plate_number = license_plate_number
        self.owner_name = owner_name
        self.distance = 0

    def print_details(self):
        print(self.owner_name + "'s car: ", self.car_company, "\nlicense plate: ",
              self.license_plate_number, "\ncolor:", self.color, end=" ")