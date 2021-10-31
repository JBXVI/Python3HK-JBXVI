#this program will print MAC Address of the given IP
import scapy.all as scapy


def scan(ip):
  arp_request =scapy.ARP(pdst =ip)
  broadcast = scapy.Ether(dst ="ff:ff:ff:ff:ff:ff")
  arp_broadcast=broadcast /arp_request 
  answers_list =scapy.srp(arp_broadcast , timeout =1 ,verbose =False)[0]
  
  print(answers_list[0][1].hwsrc)

scan("192.168.1.1")#enter the IP
