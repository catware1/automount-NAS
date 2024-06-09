#
# Подставьте свои значения.
#
# 10.0.1.112 - узел с шарой NFS (понятие NAS там использовано всмысле Network Attached Storage)
#

# ./VK-notify.py --send "test-NAS: работаю"
if test -d /var/nfsshare/WWW-files; then
    echo "/var/nfsshare is already mounted. Aborting"
    exit
else
    echo "/var/nfsshare is not mounted. Checking M002-FBSD-NAS availability..."
    if ping 10.0.1.112 -c 4; then
        echo "M002-FBSD-NAS is working! Mounting NFS..."
        if mount 10.0.1.112:/var/nfsshare /var/nfsshare -o noauto; then
            echo "Successfull!";
            ./VK-notify.py --send "Примонтировал /var/nfsshare"
        else
            echo "Unable to mount NFS Share. :("
            ./VK-notify.py --send "/var/nfsshare не монтируется блять"
            exit
        fi
    else
        echo "M002-FBSD-NAS is not available. :("
    fi
fi
