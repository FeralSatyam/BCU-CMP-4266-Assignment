class Vehicle:
    def __init__(self, make, model):
        self.__make = make
        self.__model = model
        self.__state = "stoppped"
    
    def move(self):
        print("I am moving!")
        self.__state = "moving"
    
    def stop(self):
        print("I now stopped.")
        self.__state = "stopped"
        
    def get_make(self):
        return self.__make
    
    def get_model(self):
        return self.__model
    
    def get_state(self):
        return self.__state
    
    def __str__(self):
        return f"{self.get_make()} {self.get_model()} is {self.get_state()}"


class Bus(Vehicle):
    def __init__(self, make, model, ):
        Vehicle.__init__(self, make, model)
        self.route = ["New Street", "Bullring", "Moor Street", "BCU"]
        self.__state = "Not in use"
        self.current_stop = 0
    def get_route(self):
        return " - ".join(self.route)

    def move(self):
        if self.current_stop < len(self.route) - 1:
            self.previous_stop = self.current_stop
            self.current_stop += 1
            self.next_stop = self.current_stop
            print(f"The bus was at {self.route[self.previous_stop]} and is moving to {self.route[self.next_stop]}")
        else:
            print("I am finished for today!")
    def stop(self):
        print("I am a non-stop bus")


def main():
    v1 = Vehicle("BMW", "Z3")
    print(v1)
    v1.move()
    print(v1)
    v1.stop()
    print(v1)

    b1 = Bus("Mercedes", "1")
    print(f"Route: {b1.get_route()}")
    print(f"Initial bus state: {b1.get_state()}")

    b1.move()
    print(f"Bus state: {b1.get_state()}")
def main():
    v1 = Vehicle("BMW", "Z3")
    print(v1)
    v1.move()
    print(v1)
    v1.stop()
    print(v1)
    
    b1 = Bus("Mercedes", "1")
    print(f"Route: {b1.get_route()}")
    print(f"Initial bus state: {b1.get_state()}")

    b1.move()
    print(f"Bus state: {b1.get_state()}")
    b1.move()
    print(f"Bus state: {b1.get_state()}")
    b1.move()
    print(f"Bus state: {b1.get_state()}")
    b1.move()
    b1.stop()

    
if __name__ == '__main__':
    main()