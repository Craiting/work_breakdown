from Engineer import Engineer

class EngineerTeam(object):

    def __init__(self, team = []):
        self.team = team

    def get_team_availability(self):
        available_hours = 0
        for e in self.team:
            available_hours = available_hours + e.available_hours
        return available_hours
