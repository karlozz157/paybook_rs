from prexto_paybook import User
from prexto_paybook import Transaction

user_manager = User()

# obtiene todos los usuarios
for user in user_manager.all():
    print(user.__dict__)

    try:
        # obtiene todas las transacciones de un usuario
        transaction_manager = Transaction(user.id_user)
        print(transaction_manager.all())
    except Exception as e:
        print(e.get_json())
