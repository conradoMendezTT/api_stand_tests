class User():
    is_registered = True

    def __init__(self, name, login):
        self.user_name = name
        self.user_login = login

    def describe(self):  # Método para describir el objeto User
        return f'Nombre: {self.user_name}, Iniciar sesión: {self.user_login}'


user_1 = User('Mark', 'supermarkus94')
user_2 = User('Bob', 'bobisthebest')
user_3 = User('Paula', 'pauline888')




class Group():
    def __init__(self,name): # El grupo tiene un nombre
        self.name = name
        self.members = [] # Inicializar la lista de miembros como vacía

    def add_member(self, user): # El método agrega un usuario o usuaria
        if user not in self.members: # Verificar que el usuario no está ya en el grupo
            print('Nuevo miembro agregado')
            self.members.append(user) # Agregar un nuevo usuario o usuaria al grupo

    def print_member_descriptions(self):  # El método muestra la información de todos los miembros del grupo
        print(f'Información sobre los miembros del grupo {self.name}:')
        for member in self.members:  # Recorremos cada miembro en la lista
            print(member.describe())  # Llamamos al método 'describe()' del usuario


user1 = User('Mark', 'supermarkus94') # Crear un usuario o usuaria
user2 = User('Bob', 'bobisthebest') # Crear otro usuario o usuaria
group1 = Group('Dog Lovers') # Crear un grupo de amantes de los perros
group1.add_member(user1) # Agregar un nuevo usuario o usuaria al grupo
group1.add_member(user2) # Agregar un segundo usuario o usuaria al grupo
group1.print_member_descriptions() # Mostrar información sobre los usuarios y usuarias






