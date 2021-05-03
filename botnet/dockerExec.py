import docker
import threading
import sys

ips = list()
threadjobs = list()
img = 'jieliau/ping'
cmd = 'ping 8.8.8.8'

def dockerexec(ipaddr, img, command):
    client = docker.APIClient(base_url='tcp://'+ ipaddr +':2375', tls=False)
    container = client.create_container(image=img, command=cmd)
    client.start(container=container.get('Id'))

try:
    with open('./iplist.txt') as iplist:
        ips = iplist.read().split('\n')
    ips.pop()

    for i in range(len(ips)):
        threadjobs.append(threading.Thread(target = dockerexec(ips[i], img, cmd)))
        threadjobs[i].start()

    for i in range(len(ips)):
        threadjobs[i].join()

except Exception as e:
    print('Error: %s' % e)
    sys.exit(1)
