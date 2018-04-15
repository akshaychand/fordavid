from flask_script import Command, Option

from server.core.globals import db
from server.core.services import users, roles


class CreateDbCommand(Command):
    """
    Creates the db tables.
    """
    def run(self):
        db.create_all(bind=['prizm_admin'])


class DropDbCommand(Command):
    """
    Drops the db tables.
    """
    def run(self):
        db.drop_all(bind=['prizm_admin'])


class AddUserCommand(Command):
    """
    Adds a user to the db.
    """

    option_list = (
      Option('--email', '-u',
             dest='email',
             help='Email of the user to add.'),
      Option('--password', '-p',
             dest='password',
             help='Password for the user.')
    )

    def run(self, email, password):
        user_exist = users.first(email=email)
        if user_exist:
            print('User already exists!')
            return
        users.create(email=email, password=password)


class DeleteUserCommand(Command):
    """
    Deletes a user from the db.
    """

    option_list = (
      Option('--email', '-e',
             dest='email',
             help='Email of the user to delete'),
    )

    def run(self, email):
        user_exist = users.first(email=email)
        if not user_exist:
            print('User does not exist')
            return
        users.delete(user_exist)


class AddRoleCommand(Command):
    """
    Adds a role to the db.
    """
    option_list = (
      Option('--role', '-r',
             dest='role',
             help='Name of the role to add.'),
      Option('--description', '-d',
             dest='description',
             help='Description of the role (e.g. System Administrator, Power User, etc.).'),
    )

    def run(self, role, description):
        role_exist = roles.first(role_name=role)
        if role_exist:
            print('Role already exists!')
            return
        roles.create(role_name=role, role_description=description)


class DeleteRoleCommand(Command):
    """
    Deletes a role from the db.
    """
    option_list = (
      Option('--role', '-r',
             dest='role',
             help='Name of the role to remove.'),
    )

    def run(self, role):
        role_exist = roles.first(role_name=role)
        if not role_exist:
            print('Role does not exist')
            return
        roles.delete(role_exist)


class AddUserToRoleCommand(Command):
    """
    Adds a user to a role
    """
    option_list = (
      Option('--email', '-u',
             dest='email',
             help='Email of the user.'),
      Option('--role', '-r',
             dest='role',
             help='Name of the role to add to.'),
    )

    def run(self, email, role):
        user_exist = users.first(email=email)
        if not user_exist:
            print('User does not exist!')
            return
        role_exist = roles.first(role_name=role)
        if not role_exist:
            print('Role does not exist!')
            return
        user_exist.roles.append(role_exist)
        users.save(user_exist)


class RemoveUserFromRoleCommand(Command):
    """
    Removes a user from a role
    """

    option_list = (
      Option('--email', '-u',
             dest='email',
             help='Email of the user.'),
      Option('--role', '-r',
             dest='role',
             help='Name of the role to remove from.'),
    )

    def run(self, email, role):
        user_exist = users.first(email=email)
        if not user_exist:
            print('User does not exist!')
            return
        role_exist = users.first(role_name=role)
        if not role_exist:
            print('Role does not exist!')
            return
        user_exist.roles.remove(role_exist)
        users.save(user_exist)
