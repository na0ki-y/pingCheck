echo a

netstat -rn | grep /32 | grep -F -v '.1/32' | grep -v -E '^f|255' | cut -d/ -f1

for i in {2..10}; do ping -c 1 -W 10 192.168.11.$i ; done

for i in {2..10}; do arp 192.168.11.$i; done