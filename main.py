import click
from CRUD import add_team, add_manager, add_player, show_player, show_teams, delete_manager,delete_player

while True:
    click.secho("WELCOME TO MY BASKETBALL PROGRAM MANAGER", fg='bright_white')
    click.secho("Select an option to proceed", fg='yellow')
    click.secho("1. Teams", fg="green")
    click.secho("2. Manager", fg='green')
    click.secho("3. Player", fg="green")

    user_input = click.prompt("Select option", type=int)

    if user_input == 1:
        click.secho("1. Add new team", fg="yellow")
        click.secho("2.View teams", fg='yellow')

        team_option = click.prompt("Enter Team option", type=int)

        if team_option == 1:
            click.secho("Signing new Dawgs to the yard!...", fg="magenta")
            name = click.prompt("Enter teame name")
            city = click.prompt("State your hood")

            try:
                add_team(name, city)
                click.secho(f"Welcome to the Gulag {name}")
            except Exception as Dawgs:
                click.secho(f"Error adding Team {Dawgs}", fg='red')

        if team_option == 2:
            click.secho("Team list", fg='magenta')
            name = click.prompt("Team Name")
            show_teams(name)

            # try:
            #     show_teams(name)
            #     click.secho(f"{name}")

            # except Exception as err:
            #     click.secho("Team does not exist")

#manager options

    if user_input == 2:
        click.secho("1. Add to Manager", fg='green')
        click.secho("2. Delete Manager", fg='green')

        manager_option = click.prompt("Enter manager option", type=int)

        if manager_option==1:
            click.secho("Assign Manager....", fg='blue')
            First_name= click.prompt("Enter manager's First name")
            Last_name= click.prompt("Enter manager's Last name")
            email = click.prompt("Enter manager's email")
            # Hire_Date =click.prompt("Enter manager's hiring date")
            Team_id = click.prompt("Enter team id ")
            try:
                Team_id = int(Team_id)
                add_manager(First_name, Last_name, email, Team_id)
                click.secho(f"{First_name} added successfully")
            except Exception as err:
                click.secho(f"Error adding manager: {err}", fg='red')

        if manager_option==2:
            click.secho("Delete Manager", fg='red')
            manager_id = click.prompt("Enter manager's Id")
            try:
                delete_manager(manager_id)
                click.secho(f"DELETED {manager_id}")
            except Exception as e:
                click.secho(f"MANAGER DOES NOT EXIST: {e}", fg='red')




