echo a
for i in {2..10}; do ping -c 1 -W 10 192.168.11.$i ; done

for i in {2..10}; do arp 192.168.11.$i; done