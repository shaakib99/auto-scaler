import socket

async def get_open_port():
    # Create a socket and bind it to a random open port on localhost
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', 0))  # Binding to port 0 finds an open port
        port = s.getsockname()[1]  # Get the port number
    return port