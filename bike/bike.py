
class Bike:
    def __init__(self,gear=1):
        self.__gear = gear
        self.is_on = False
        self.speed = 0

    def turned_on(self):
        self.is_on = True

    def turned_off(self):
        self.is_on = False

    def bike_state(self):
        return self.is_on

    def update_gear(self):
        if self.speed <= 20:
            self.__gear = 1
        elif self.speed <= 30:
            self.__gear = 2
        elif self.speed <= 40:
            self.__gear = 3
        else:
            self.__gear = 4
        return self.__gear

    def accelerate(self):
        if not self.is_on:
            raise ValueError("Bike is not turned on")
        self.update_gear()

        if self.__gear == 1:
            if self.speed <= 20:
                self.speed += 1
        elif self.__gear == 2:
            if self.speed <= 30:
                self.speed += 2
        elif self.__gear == 3:
            if 39 < self.speed <= 40:
                self.speed += 3
        elif self.__gear == 4:
            if self.speed > 50:
                self.speed += 4
        self.update_gear()

    def get_speed(self):
        if not self.is_on:
            raise ValueError("Bike is not turned on")

        else:
            print(self.__gear)
            return self.speed

    def decelerate(self):
        if not self.is_on:
            raise ValueError("Bike is not turned on")
        if self.speed > 0:
            self.speed -= 1
            self.update_gear()

    @property
    def gear(self):
        return self.__gear

    @gear.setter
    def gear(self, gea):
        if gea in [1, 2, 3, 4]:
            self.__gear = gea
        else:
            raise ValueError("Gear must be in the range of 1 to 4")
