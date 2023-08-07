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
    
    target = sys.argv[1]
    input_file = sys.argv[2]

    try:
        ip_address = socket.gethostbyname(target)
        with open(input_file, 'r') as file:
            common_ports = file.read().splitlines()

        for common_port in common_ports:
            if check_port(ip_address, int(common_port)):
                print(f"Port {common_port} is OPEN on {target} ({ip_address})")
            else:
                print(f"Port {common_port} is closed on {target} ({ip_address})")

    except socket.gaierror:
        print(f"Could not resolve {target}")
    except ValueError:
        print("Invalid port number")
    except FileNotFoundError:
        print(f"File '{input_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()