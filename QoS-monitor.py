# -*- coding: utf-8 -*-
"""
Created on Sun Feb 2 20:39:25 2025

@author: IAN CARTER KULANI

"""

from colorama import Fore
import pyfiglet
import os
font=pyfiglet.figlet_format("QoS Monitor")
print(Fore.GREEN+font)


import socket
import time
import random
import threading

# QoS parameters (can be adjusted based on network conditions)
MAX_LATENCY = 200  # Maximum latency (ms)
MIN_BANDWIDTH = 500  # Minimum bandwidth (kbps)
PRIORITY_THRESHOLD = 10  # Priority threshold (1-10 scale)

# Traffic classes
HIGH_PRIORITY = 1
LOW_PRIORITY = 2

# Function to simulate sending a packet and monitoring QoS
def send_packet(ip, port, message, priority=LOW_PRIORITY, mac_address=None):
    # Simulate network behavior (latency, packet loss, bandwidth)
    latency = random.randint(50, 250)  # Simulate latency in ms
    packet_loss = random.randint(0, 10)  # Simulate packet loss chance (0-10%)

    if packet_loss < 3:  # 30% chance of packet loss for high-priority traffic
        print(f"Packet loss occurred (message: {message})")
        return False

    if latency > MAX_LATENCY:
        print(f"Packet with high latency ({latency}ms) for message: {message}")
        return False

    # Simulate transmission delay based on the message size (emulating bandwidth)
    bandwidth = random.randint(400, 1000)  # Random bandwidth in kbps

    if bandwidth < MIN_BANDWIDTH:
        print(f"Insufficient bandwidth for message: {message}")
        return False

    print(f"Sent message '{message}' with {latency}ms latency, {bandwidth}kbps bandwidth from MAC: {mac_address}")
    return True

# Function to simulate network client
def network_client(ip, port, mac_address, host_name):
    priority = random.randint(1, 10)
    message = f"Test message with priority {priority}"

    print(f"{host_name}: Sending message with priority {priority}")
    success = send_packet(ip, port, message, priority, mac_address)
    
    if not success:
        print(f"{host_name}: Failed to send message '{message}'")
    else:
        print(f"{host_name}: Message sent successfully '{message}'")

# Function to simulate network server
def network_server(ip, port):
    print(f"Server at {ip}:{port} is ready to receive messages...")
    while True:
        # Simulate receiving messages (In real case, would use sockets)
        time.sleep(3)
        print("Server: Listening for incoming traffic...")

# Main function to simulate the ad-hoc network and monitor QoS
def monitor_qos():
    # Prompting the user for necessary details
    mac_address = input("Enter MAC address of the device:")
    ip = input("Enter IP address for the device:")
    host_name = input("Enter host name:")

    # Validate IP address format (basic validation)
    try:
        socket.inet_aton(ip)
    except socket.error:
        print("Invalid IP address format.")
        return

    print(f"Starting network monitoring for host '{host_name}' with IP: {ip} and MAC address: {mac_address}")
    port = 8080  # Port for communication
    
    # Start server in a separate thread
    server_thread = threading.Thread(target=network_server, args=(ip, port))
    server_thread.daemon = True  # Daemonize server to stop when main thread exits
    server_thread.start()

    # Start clients in separate threads
    for i in range(5):  # Simulate 5 clients sending messages
        client_thread = threading.Thread(target=network_client, args=(ip, port, mac_address, host_name))
        client_thread.daemon = True  # Daemonize client threads
        client_thread.start()
        time.sleep(random.randint(1, 3))  # Random delay between clients sending messages

    # Monitor the QoS performance
    while True:
        print("\nQoS Monitoring - Current Performance Metrics:")
        print(f"Latency: {random.randint(50, MAX_LATENCY)} ms")
        print(f"Bandwidth: {random.randint(MIN_BANDWIDTH, 1000)} kbps")
        print(f"Packet Loss: {random.randint(0, 10)}%")
        print(f"Throughput: {random.randint(400, 1000)} kbps")
        print("=" * 50)
        time.sleep(5)  # Monitor every 5 seconds

if __name__ == "__main__":
    monitor_qos()
