from models import Team, Player, Manager, session

def add_team (teams_id, name, city):
    new_team = Team(teams_id=teams_id, name=name, city=city)
    session.add(new_team)
    session.commit()

def add_manager(managers_id, First_name, Last_name, email, Hiring_Date, Team_id):
    new_manager = Manager(
        managers_id = managers_id,
        First_name = First_name,
        Last_name = Last_name,
        email = email,
        Hiring_Date = Hiring_Date,
        Team_id = Team_id
    )
    session.add(new_manager)
    session.commit()

def add_player(players_id, first_name, last_name, age, height, position, jersey_number, Team_id ):
    new_player = Player(
        players_id = players_id,
        first_name = first_name,
        last_name = last_name,
        age = age,
        height = height,
        position = position,
        jersey_number = jersey_number,
        Team_id = Team_id
    )
    session.add(new_player)
    session.commit()