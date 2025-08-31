# project for Create a basic network scanner: Write a program to scan a network for active devices

import socket

def scan_target(target_ip, port_range):
    open_ports = []

    for port in range(port_range[0], port_range[1] + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        try:
            sock.connect((target_ip, port))
            open_ports.append(port)
        except (socket.timeout, socket.error):
            pass
        finally:
            sock.close()

    return open_ports

def main():
    target_ip = input("Enter the target IP address: ")
    start_port = int(input("Enter the start port: "))
    end_port = int(input("Enter the end port: "))

    port_range = (start_port, end_port)

    print(f"Scanning ports {start_port} to {end_port} on {target_ip}...")
    open_ports = scan_target(target_ip, port_range)

    if open_ports:
        print("Open ports:")
        for port in open_ports:
            print(port)
    else:
        print("No open ports found.")

if __name__ == "__main__":
    main()

