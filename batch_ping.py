import subprocess
import sys

def is_ip_reachable(ip_address):
    try:
        # Execute the ping command with a single ping packet and a timeout of 2 seconds
        subprocess.check_output(["ping", "-c", "1", "-W", "2", ip_address], stderr=subprocess.STDOUT, universal_newlines=True)
        return True
    except subprocess.CalledProcessError:
        return False

def main():
    input_file = sys.argv[1]

    try:
        with open(input_file, 'r') as file:
            ip_addresses = file.read().splitlines()

        for ip_address in ip_addresses:
            reachable = is_ip_reachable(ip_address)
            state = "UP" if reachable else "DOWN"
            print(f"{ip_address} is {state}")

    except FileNotFoundError:
        print(f"File '{input_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
