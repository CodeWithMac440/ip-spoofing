import subprocess
import random

def change_mac(interface, new_mac):
    """
    Change the MAC address of the speci5fied network interface.

    Args:
        interface (str): Name of the network interface (e.g., eth0, wlan0).
        new_mac (str): New MAC address to assign to the interface.
    """
    # Bring down the interface
    subprocess.call(["sudo", "ifconfig", interface, "down"])
    # Set the new MAC address
    subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", new_mac])
    # Bring up the interface
    subprocess.call(["sudo", "ifconfig", interface, "up"])

def change_ip(interface, new_ip):
    """
    Change the IP address of the specified network interface.

    Args:
        interface (str): Name of the network interface (e.g., eth0, wlan0).
        new_ip (str): New IP address to assign to the interface.
    """
    # Set the new IP address for the interface
    subprocess.call(["sudo", "ifconfig", interface, new_ip])

def get_interface():
    """
    Prompt the user to input the name of the network interface.

    Returns:
        str: Name of the network interface entered by the user.
    """
    interface = input("Enter the name of the interface (e.g., eth0, wlan0): ")
    return interface

def generate_random_mac():
    """
    Generate a random MAC address.

    Returns:
        str: Randomly generated MAC address in the format XX:XX:XX:XX:XX:XX.
    """
    random_mac = [0x00, 0x16, 0x3e,
                  random.randint(0x00, 0x7f),
                  random.randint(0x00, 0xff),
                  random.randint(0x00, 0xff)]
    mac_address = ':'.join(map(lambda x: "%02x" % x, random_mac))
    return mac_address

def generate_random_ip():
    """
    Generate a random IP address.

    Returns:
        str: Randomly generated IP address in the format 192.168.XX.XX.
    """
    ip_address = "192.168." + str(random.randint(0, 255)) + "." + str(random.randint(0, 255))
    return ip_address

# Generate 10 random MAC addresses
random_mac_addresses = [generate_random_mac() for _ in range(10)]

# Print the list of MAC addresses for user selection
print("Select a MAC address:")
for i, mac_address in enumerate(random_mac_addresses):
    print(f"{i+1}. {mac_address}")

# Prompt user to select a MAC address
selection = int(input("Enter the number corresponding to the MAC address you want to use: "))
selected_mac = random_mac_addresses[selection - 1]

# Get the interface from the user
interface = get_interface()

# Apply the selected MAC address to the interface
change_mac(interface, selected_mac)

# Generate a random IP address
random_ip = generate_random_ip()

# Apply the random IP address to the interface
change_ip(interface, random_ip)

print(f"MAC address changed to: {selected_mac}")
print(f"IP address changed to: {random_ip}")
