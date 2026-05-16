class Outfit:

    def __init__(self, top, bottom, shoes, style, event, weather):
        self.top = top
        self.bottom = bottom
        self.shoes = shoes
        self.style = style
        self.event = event
        self.weather = weather

    def to_dict(self):
        return {
            "top": self.top,
            "bottom": self.bottom,
            "shoes": self.shoes,
            "style": self.style,
            "event": self.event,
            "weather": self.weather
        }
    
class Outfit:

    def __init__(self, top, bottom, shoes, style, event, weather, image):
        self.top = top
        self.bottom = bottom
        self.shoes = shoes
        self.style = style
        self.event = event
        self.weather = weather
        self.image = image

    def to_dict(self):
        return {
            "top": self.top,
            "bottom": self.bottom,
            "shoes": self.shoes,
            "style": self.style,
            "event": self.event,
            "weather": self.weather,
            "image": self.image
        }
    
class CasualOutfit(Outfit):
    pass


class FormalOutfit(Outfit):
    pass


class SportOutfit(Outfit):
    pass