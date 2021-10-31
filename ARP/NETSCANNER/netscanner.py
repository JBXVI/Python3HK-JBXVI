import scapy.all as scapy


def scan(ip):
    arp_request =scapy.ARP(pdst= ip)
    broadcast = scapy.Ether(dst ="ff:ff:ff:ff:ff:ff")
    arp_broadcast =broadcast /arp_request
    answer_list =scapy.srp(arp_broadcast ,timeout =1 ,verbose = False)[0]

    for names in answer_list:
        print(names[1].psrc,"\t\t\t",names[1].hwsrc)

scan("192.168.1.1/24")#enter any ip range
