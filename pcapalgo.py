from scapy.all import *
from scapy.utils import *
# Include standard modules
import argparse
import json
from pprint import pprint


dic = {}		 
# required arg
parser = argparse.ArgumentParser()
#action='store_true',
parser.add_argument('-p','--pcap',help="el nombre de su archivo pcap incluyendo la extension", required=True)
parser.add_argument('-d','--dominio',help="el nombre de su dominio a analizar", required=True)

args = parser.parse_args()

host = args.dominio
pcap = args.pcap

pkts = rdpcap(pcap)
#25 tcp
ports = [80,443]
filtered = (pkt for pkt in pkts if TCP in pkt and (pkt[TCP].sport in ports or pkt[TCP].dport in ports))
wrpcap('filtered.pcap', filtered)

packets = rdpcap('filtered.pcap')
packets = rdpcap(pcap)
for packet in packets:
    temp = packet.sprintf("%IP.dst%  test")
    dic[temp] = 1

for ip in dic.keys():
    print(ip)