import socket


def hostname() -> str:
    return socket.gethostname()
