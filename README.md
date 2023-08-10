INSTALL:
`pip install dnspython`

Create list txt of ip address, domain names, or ports.

EXAMPLE: 
- Batch ping: `python3 batch_ping.py ip_addresses.txt`
- Batch nslookup: `python3 batch_nslookup.py domain_names.txt`
- Multiple port check on single IP: `python3 batch_port_checker.py example.com ports.txt`
- Single port check on multiple domain/IPs: `python3 batch_port_checker.py domain_names.txt 22`
- SIngle port check on single domain/IP: `python3 port_checker.py example.com 22`