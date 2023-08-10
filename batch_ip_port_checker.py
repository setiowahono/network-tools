import socket
import sys
import dns.resolver

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
    dns_resolver = dns.resolver.Resolver()
    print(f"DNS: {dns_resolver.nameservers[0]}")
    print('--------')

    # target = sys.argv[1]
    input_file = sys.argv[1]
    port = sys.argv[2]

    try:
    
        with open(input_file, 'r') as file:
            items = file.read().splitlines()
            
        for item in items:
            ip_address = socket.gethostbyname(item)
            if check_port(ip_address, int(port)):
                print(f"Port {port} is open on {ip_address} ({ip_address})")
            else:
                print(f"Port {port} is closed on {ip_address} ({ip_address})")
    except socket.gaierror:
        print(f"Could not resolve {ip_address}")
    except ValueError:
        print("Invalid port number")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()