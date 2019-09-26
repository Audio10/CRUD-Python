import sys

clients = [
    {
        'name': 'Pablo',
        'company': 'Google',
        'email': 'pablo@google.com',
        'position': 'Software Engineer',
    },
    {
        'name': 'Ricardo',
        'company': 'Facebook',
        'email': 'ricardo@facebook.com',
        'position': 'Data Engineer',
    }
]


def create_client(client):
    global clients

    if client not in clients:
        clients.append(client)
    else:
        print('Client already is in the client\'s list')


def list_clients():
    global clients

    for idx, client in enumerate(clients):
        print('{uid} | {name} | {company} | {email} | {position}'.format(
            uid=idx,
            name=client['name'],
            company=client['company'],
            email=client['email'],
            position=client['position']
        ))


def update_client(client_name):
    global clients

    idx = search_client(client_name)

    if idx != None:
        updated_client = _get_new_client()
        clients[idx].update(updated_client)
    else:
        _client_found(idx, client_name)


def search_client(client_name):
    for idx, client in enumerate(clients):
        if client['name'] != client_name:
            continue
        else:
            return idx
    
    return None


def delete_client(client_name):
    global clients

    idx = search_client(client_name)

    if idx != None:
        del clients[idx]
    else:
        _client_found(idx, client_name)


def _get_new_client():
    client = {
        'name': _get_client_field('name'),
        'company': _get_client_field('company'),
        'email': _get_client_field('email'),
        'position': _get_client_field('position'),
    }

    return client


def _client_found(idx, client_name):
  
    if idx != None:
        print('The client is in the client\'s list')
    else:
        print('The client: {} is not in our client\'s list'.format(client_name))


def _print_welcome():
    print('WELCOME TO PLATZI VENTAS')
    print('*' * 50)
    print('What would you like to do day?')
    print('[C]reate client')
    print('[L]ist client')
    print('[U]pdate client')
    print('[D]elete client')
    print('[S]earch client')
    print('[E]xit')


def _get_client_field(field_name):
    field = None

    while not field:
        field = input('What is the client\'s {}?'.format(field_name))

        if field == 'exit':
            field = None
            break

    if not field:
        sys.exit()
    
    return field


def _not_found():
    print('Client is not in clients list')


if __name__ == '__main__':
    while (True):
        _print_welcome()

        command = input().upper()
        
        if command == 'C':
            client = {
                'name' : _get_client_field('name'),
                'company' : _get_client_field('company'),
                'email' : _get_client_field('email'),
                'position' : _get_client_field('position'),
            }

            create_client(client)
        elif command == 'L':
            list_clients()
        elif command == 'D':
            client_name = _get_client_field('name')
            delete_client(client_name)
        elif command == 'U':
            client_name = _get_client_field('name')
            update_client(client_name)
        elif command == 'S':
            client_name = _get_client_field('name')
            idx = search_client(client_name)
            _client_found(idx, client_name)
        elif command == 'E':
            sys.exit()
        else:
            print('Invalid command')
