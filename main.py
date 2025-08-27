import click
from CRUD import add_team, add_manager, add_player, show_players, show_teams, delete_manager,delete_player

while True:
    click.secho("WELCOME TO MY BASKETBALL PROGRAM MANAGER", fg='bright_white')
    click.secho("Select an option to proceed", fg='yellow')
    click.secho("1. Teams", fg="green")
    click.secho("2. Manager", fg='green')
    click.secho("3. Player", fg="green")

    user_input = click.prompt("Seleect option", type=int)

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
                click

            except Exception as Dawgs:
                click.secho(f"Error adding Team {Dawgs}", fg='red')

        if team_option == 2:
            click.secho("Team list", fg='magenta')
            name = click.prompt("Team Name:")

            try:
                show_teams(name)
                click.secho(f"{name}")

            except Exception as err:
                click.secho("Team does not exist")






