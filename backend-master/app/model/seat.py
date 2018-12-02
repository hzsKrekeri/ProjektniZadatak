class Seat:

    def __init__(self, id, flight_id, team_member_id, seat_number):
        self.id = id
        self.startpoint = startpoint
        self.flight_id = flight_id
        self.team_member_id = team_member_id
        self.seat_number = seat_number
        
        
 
    

    def to_dict(self):
        return {
            'id': self.id,
            'flight_id': self.flight_id,
            'team_member_id': self.team_member_id,
            'seat_number': self.seat_number,
        }
###      0|id|INTEGER|1||1
###      1|flight_id|INTEGER|1||0
###      2|team_member_id|INTEGER|1||0
###      3|seat_number|INTEGER|1||0
