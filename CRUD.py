from models import Team, Player, Manager, session

#Create ops
def add_team (name, city):
    new_team = Team( name=name, city=city)
    session.add(new_team)
    session.commit()

def add_manager( First_name, Last_name, email, Team_id):
    new_manager = Manager(
        # managers_id = managers_id,
        First_name = First_name,
        Last_name = Last_name,
        email = email,
        # Hire_Date = Hire_Date,
        Team_id = Team_id
    )
    session.add(new_manager)
    session.commit()

def add_player(first_name, last_name, age, height, position, jersey_number, Team_id ):
    new_player = Player(
        # players_id = players_id,
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

#find queries

def show_player(jersey_number):
    query = session.query(Player) #will show all players

    # if last_name:
    #     query = query.filter(Player.last_name==last_name)

    if jersey_number:
        query = query.filter_by(jersey_number==jersey_number)
    
    players = query.all()

    if not player:
        print("playerdoes not exist")
    else:
        for player in players:
            print(f"last_name:{player.last_name}, jersey{player.jersey_number}")

    # return players
    #end session since its read only
    # session.close()

def show_teams(name):
    team=session.query(Team)
    team_name =team.filter(Team.name==name).first()

    # if teams_id:
    #     query = query.filter_by(teams_id==teams_id)
    

    if not team_name:
        print("Team is invalid!")
    else:
            print(f"id :{team_name.id}| team_name: {team_name.name}")

    #Delete Operators for player and managers

def delete_player(players_id):
    query = session.query(Player).where(id == players_id).first()

    session.delete(query)
    session.commit()

def delete_manager(managers_id):
    query = session.query(Manager).where(Manager.id==managers_id).one()

    if query is None:
        raise Exception (f"{managers_id } does not exist")

    session.delete(query)
    session.commit()