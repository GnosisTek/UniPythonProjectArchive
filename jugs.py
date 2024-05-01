'''
Created on 14/02/19
Martin Golding-Quigley
'''

class Jug():
    '''class describing a jug'''

    def __init__(self, max_capacity):
        self.max_capacity = max_capacity
        self.volume = 0
        self.temp = 0

    def pour_out(self, volume, into_jug=None):
        '''Pours out of jug'''
        # Checks if empty
        if volume == 'all' or volume > self.max_capacity:
            self.volume = 0
            if into_jug is not None:
                into_jug.pour_in(self.max_capacity, self.temp)
        #Changes volume
        else:
            self.volume -= volume
            if into_jug is not None:
                into_jug.pour_in(volume, self.temp)

    def pour_in(self, volume, temperature):
        '''Pours into jug'''
        # Finds temperature
        self.temp = self.temp_change (temperature, volume)
        # Finds volume
        if self.volume + volume > self.max_capacity:
            self.volume = self.max_capacity
        else:
            self.volume += volume
        
    def temperature(self):
        '''Returns temperature'''
        return self.temp
    
    def water_volume(self):
        '''Returns water volume'''
        return self.volume
    
    def capacity(self): 
        '''Return capacity'''
        return self.max_capacity
    
    def temp_change (self, temperature, volume): 
        '''Calculates temperature'''
        return (self.temp * self.volume + temperature * 
                volume) / (self.volume + volume)