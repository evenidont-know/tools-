import socket

def scan_ports(target, port_range):
    open_ports = []

    for port in port_range:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Set a timeout for the connection attempt

        result = sock.connect_ex((target, port))
        if result == 0:
            open_ports.append(port)

        sock.close()

    return open_ports

if __name__ == "__main__":
    target_host = input("Enter the target website or IP address: ")
    port_start = int(input("Enter the starting port: "))
    port_end = int(input("Enter the ending port: "))
    
    ports = list(range(port_start, port_end + 1))
    open_ports = scan_ports(target_host, ports)

    if open_ports:
        print(f"Open ports on {target_host}: {open_ports}")
    else:
        print(f"No open ports found on {target_host}")
