class Temperature:
    def __init__(self, temperature):
        self.temperature = temperature

    def to_fahrenheit(self):
        return self.temperature * 1.8 +32
        
    @classmethod
    def from_fahrenheit(cls, far):
        temp = (far - 32) / 1.8
        return cls(temp)
    
    def __str__(self):
        return f'{round(self.temperature, 2)}°C'
    
    def __bool__(self):
        return self.temperature > 0 
    
    def __int__(self):
        return int(self.temperature)
    
    def __float__(self):
        return float(self.temperature)
