from netmiko import ConnectHandler
import getpass

# Ask for credentials and device IP
username = input("Enter your username: ")
password = getpass.getpass("Enter your password: ")   # hides typing
device_ip = input("Enter the device IP: ")

# Define the device
device = {
    "device_type": "cisco_ios",
    "host": device_ip,
    "username": username,
    "password": password,
}

try:
    # Connect
    print(f"\nConnecting to {device_ip}...")
    conn = ConnectHandler(**device)

    # Run some useful commands
    commands = [
        "show version",
        "show ip interface brief",
        "show vlan brief",
    ]

    for cmd in commands:
        print(f"\n--- {cmd} ---")
        output = conn.send_command(cmd)
        print(output)

    conn.disconnect()
    print("\nDisconnected.")

except Exception as e:
    print(f"Connection failed: {e}")
