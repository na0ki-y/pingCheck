import os

add_list=[]
for i in range(0,255):
    stream = os.popen('ping -c 1 -W 10 192.168.11.{}'.format(i))
    stream = os.popen('arp 192.168.11.{}'.format(i))
    output = stream.read()
    if "at" in output and not("(incomplete)" in output.split("at")[1]):#"Found"
        add_list.append(output.split("at")[1].split(" ")[1])
        
print("result",add_list)
    