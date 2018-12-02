class Flight:

    def __init__(self, id, startpoint, endpoint, departureTime, arrivalTime):
        self.id = id
        self.startpoint = startpoint
        self.description = description
        self.endpoint = endpoint
        self.departureTime = departureTime
        self.arrivalTime = arrivalTime
        
 
    

    def to_dict(self):
        return {
            'id': self.id,
            'startpoint': self.name,
            'endpoint': self.description,
            'departureTime': self.photo_url,
            'arrivalTime': self.team_uuid,
        }
###      0|id|INTEGER|1||1
###      1|startpoint|TEXT|1||0
###      2|endpoint|TEXT|1||0
###      3|departureTime|DATETIME|0||0
###      4|arrivalTime|DATETIME|0||0
