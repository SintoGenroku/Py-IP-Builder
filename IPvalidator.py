
from index import IsValid, OutOfRange

subnet, host, broadcast = [ '', '', '', '' ], [ '', '', '', '' ], [ '', '', '', '' ]
print("IP: ") 
ip = (input().split('.'))
print("Mask: ") 
mask = (input().split('.'))

if len(ip)==4 and len(mask)==4:
    try:
        for i in range(0,4):
            ip[i] = int(ip[i])
            mask[i] = int(mask[i])

            if ip[i]>255 or mask[i]>255:
                raise OutOfRange("IP or mask octate value can't be more than 255")
            if  ip[i]<0 or mask[i]<0:    
                raise OutOfRange("IP or mask octate value can't be less than 0")

    except Exception as ex:
        print(f"Check your input: {ex}")           

for i in range(0,4):
    subnet[i] = str(ip[i]&mask[i])
    host[i] = str(ip[i]&~mask[i])
    broadcast[i] = str(ip[i] & mask[i] | ~mask[i]+256)

subnet = '.'.join(map(str,subnet))
host = '.'.join(map(str,host))
broadcast = '.'.join(map(str,broadcast))
IsValid(mask)
print(f"Subnet ID: {subnet}\nHost ID: {host}\nBroadcast adress: {broadcast}")

