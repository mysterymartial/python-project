class Tv:

    def __init__(self):
        self.channel: int = 1
        self.volume: int = 0
        self.is_on: bool = False
        self.previous_volume: int = 0



    def turn_on(self):
            self.is_on = True

    def turn_off(self):
         self.is_on =False

    def set_channel(self ,channel_number:int):
        if not self.is_on:
            raise ValueError("Tv is off, turn Tv on First")
        if channel_number < 1 or channel_number > 100:
            raise ValueError("channel number must be between 1 and 100")
        else:
            self.channel = channel_number



    def get_channel(self):
        if not self.is_on:
            raise ValueError("Tv is off, turn Tv on First")
        Tv.turn_on(self)
        return self.channel

    def set_volume(self, volume_number):
        Tv.turn_on(self)
        if volume_number < 0 or volume_number > 10:
            raise ValueError("volume must be between 0 to 10")
        else:
            self.volume = volume_number

    def get_volume(self):
        if not self.is_on:
            raise ValueError("Tv is off, turn Tv on First")
        return self.volume

    def channel_up(self):
        if not self.is_on:
            raise ValueError("Tv is off, turn Tv on First")
        self.channel += 1

    def channel_down(self):
        if not self.is_on:
            raise ValueError("Tv is off, turn Tv on First")
        self.channel -= 1

    def volume_up(self):
        if not self.is_on:
            raise ValueError("Tv is off, turn Tv on First")
        self.volume += 1

    def volume_down(self):
        if not self.is_on:
            raise ValueError("Tv is off, turn Tv on First")
        self.volume -= 1

    def mute(self):
        if not self.is_on:
            raise ValueError("Tv is off, turn Tv on First")
        self.previous_volume = self.volume
        self.volume= 0


    def un_mute(self):
        if not self.is_on:
            raise ValueError("Tv is off, turn Tv on First")
        self.volume = self.previous_volume





