import socket


def hostname() -> str:
    return socket.gethostname()


def defaulttimeout() -> float:
    return socket.getdefaulttimeout()
