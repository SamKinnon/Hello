# class Point():
#     def __init__(self,input1,input2):
#         self.x = input1
#         self.y = input2
# p = Point(2,3)
# print(p.x)
# print(p.y)
class Flight():
    def __init__(self,capacity):
        self.capacity = capacity
        self.passengers = []
    def add_passenger(self,name):
        if not self.open_seates():
            return False 
        self.passengers.append(name)
        return True
    def open_seates(self):
        return self.capacity - len(self.passengers)
flight = Flight(3)
people = input["Sam","Kalisa","Jane","Anitha"]

for person in people:
    success = flight.add_passenger(person)
    if success:
        print(f"Added {person} to flight Sucessfully")
    else:
        print(f"No available seat for {person}")

