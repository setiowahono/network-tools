import socket
import sys
import dns.resolver

def resolve_domain(domain_name):
    try:
        ip_address = socket.gethostbyname_ex(domain_name)
        return ip_address
    except socket.gaierror:
        return None

def main():
    dns_resolver = dns.resolver.Resolver()
    print(f"DNS: {dns_resolver.nameservers[0]}")
    print('--------')

    input_file = sys.argv[1]

    try:
        with open(input_file, 'r') as file:
            domain_names = file.read().splitlines()

        for domain_name in domain_names:
            ip_address = resolve_domain(domain_name)
            if ip_address:
                print(f"{domain_name} is resolved to {', '.join(ip_address[2])}")
            else:
                print(f"{domain_name} could not be resolved")

    except FileNotFoundError:
        print(f"File '{input_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()