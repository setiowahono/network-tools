import socket

def check_port(ip_address, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        sock.connect((ip_address, port))
        sock.close()
        return True
    except (socket.timeout, ConnectionRefusedError):
        return False

def main():
    target = input("Enter IP address or domain name: ")
    port = int(input("Enter port number: "))

    try:
        ip_address = socket.gethostbyname(target)
        if check_port(ip_address, port):
            print(f"Port {port} is open on {target} ({ip_address})")
        else:
            print(f"Port {port} is closed on {target} ({ip_address})")
    except socket.gaierror:
        print(f"Could not resolve {target}")
    except ValueError:
        print("Invalid port number")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()