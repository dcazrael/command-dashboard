commands = {'Dateiverwaltung': {
    'Datei kopieren': {'command': 'cp [source] [destination]', 'explanation': 'Kopiert Datei1 zu Datei2'},
    'Datei verschieben': {'command': 'mv [file] [directory]', 'explanation': 'Verschiebt Datei in verzeichnis/'},
    'Datei löschen': {'command': 'rm [file]', 'explanation': 'Löscht eine Datei'},
    'Verzeichnis erstellen': {'command': 'mkdir [directory]', 'explanation': 'Erstellt ein neues Verzeichnis'},
    'Datei erstellen': {'command': 'touch [file]',
        'explanation': 'Erstellt eine leere Datei oder aktualisiert Zeitstempel'},
    'Dateien suchen': {'command': "find / -name '*.txt'", 'explanation': 'Sucht nach .txt-Dateien im gesamten System'},
    'Dateien auflisten': {'command': 'ls -l',
        'explanation': 'Detaillierte Liste mit Berechtigungen, Besitzer, Größe etc.'}}, 'Systeminformationen': {
    'Systeminformationen': {'command': 'uname -a', 'explanation': 'Zeigt Systeminformationen (Kernel, Hostname etc.)'},
    'Speicherbelegung': {'command': 'df -h', 'explanation': 'Zeigt Speicherbelegung der Dateisysteme (human readable)'},
    'Speichernutzung': {'command': 'free -m', 'explanation': 'Zeigt Speichernutzung in MB'},
    'Prozessliste': {'command': 'top', 'explanation': 'Dynamische Anzeige der laufenden Prozesse'},
    'CPU-Informationen': {'command': 'lscpu', 'explanation': 'Zeigt CPU-Informationen'},
    'Systemlaufzeit': {'command': 'uptime', 'explanation': 'Zeigt Systemlaufzeit und Auslastung'}},
    'Prozesssteuerung': {'Prozessliste': {'command': 'ps aux', 'explanation': 'Zeigt alle laufenden Prozesse'},
        'Prozess beenden': {'command': 'kill -9 [PID]',
            'explanation': 'Beendet einen Prozess mit der angegebenen Prozess-ID'},
        'Prozess nach Name beenden': {'command': 'killall [processname]',
            'explanation': 'Beendet alle Prozesse mit diesem Namen'},
        'Priorität ändern': {'command': 'nice -n 10 [command]',
            'explanation': 'Startet einen Befehl mit angepasster Priorität'},
        'Hintergrundprozess': {'command': 'bg', 'explanation': 'Setzt einen gestoppten Prozess im Hintergrund fort'},
        'Vordergrundprozess': {'command': 'fg', 'explanation': 'Bringt einen Hintergrundprozess in den Vordergrund'}},
    'Netzwerkbefehle': {'Netzwerkkonfiguration': {'command': 'ifconfig',
        'explanation': 'Zeigt Netzwerkschnittstellen und Konfiguration'},
        'Verbindung testen': {'command': 'ping [host]', 'explanation': 'Sendet ICMP-Pakete zum angegebenen Host'},
        'Verbindungsweg': {'command': 'traceroute [host]', 'explanation': 'Zeigt den Weg der Pakete zum Zielhost'},
        'Offene Ports': {'command': 'netstat -tuln', 'explanation': 'Zeigt alle offenen Ports und Verbindungen'},
        'SSH Verbindung': {'command': 'ssh [user]@[host]',
            'explanation': 'Stellt eine SSH-Verbindung zum entfernten Host her'},
        'Dateien kopieren': {'command': 'scp [file] [user]@[host]:[path]', 'explanation': 'Kopiert Dateien über SSH'}},
    'Berechtigungen': {'Berechtigungen ändern': {'command': 'chmod 755 [file]',
        'explanation': 'Ändert Dateiberechtigungen (rwx für Owner, r-x für Gruppe und Andere)'},
        'Datei ausführbar machen': {'command': 'chmod +x [file]', 'explanation': 'Macht eine Datei ausführbar'},
        'Besitzer ändern': {'command': 'chown [user]:[group] [file]',
            'explanation': 'Ändert Besitzer und Gruppe einer Datei'},
        'Gruppe ändern': {'command': 'chgrp [group] [file]', 'explanation': 'Ändert die Gruppe einer Datei'},
        'Standard-Berechtigungen': {'command': 'umask 022',
            'explanation': 'Setzt Standard-Berechtigungen für neue Dateien'},
        'ACL anzeigen': {'command': 'getfacl [file]', 'explanation': 'Zeigt erweiterte ACL-Berechtigungen'}},
    'Paketverwaltung': {'Paketliste aktualisieren': {'command': 'apt update',
        'explanation': 'Aktualisiert die Paketliste (Debian/Ubuntu)'},
        'Paket installieren': {'command': 'apt install [package]', 'explanation': 'Installiert ein Paket'},
        'Paket entfernen': {'command': 'apt remove [package]', 'explanation': 'Deinstalliert ein Paket'},
        'Pakete aktualisieren': {'command': 'apt upgrade', 'explanation': 'Aktualisiert alle installierten Pakete'},
        'RPM-Paket installieren': {'command': 'yum install [package]',
            'explanation': 'Installiert ein Paket (RHEL/CentOS)'},
        'DEB-Paket installieren': {'command': 'dpkg -i [package.deb]', 'explanation': 'Installiert eine .deb-Datei'}},
    'Textverarbeitung': {
        'Datei kopieren': {'command': 'cp [source] [destination]', 'explanation': 'Kopiert datei1 zu datei2'},
        'Datei verschieben': {'command': 'mv [source] [directory]', 'explanation': 'Verschiebt datei1 in verzeichnis/'},
        'Datei löschen': {'command': 'rm [file]', 'explanation': 'Löscht eine Datei'},
        'Verzeichnis erstellen': {'command': 'mkdir [directory]', 'explanation': 'Erstellt ein neues Verzeichnis'},
        'Datei erstellen': {'command': 'touch [file]',
            'explanation': 'Erstellt eine leere Datei oder aktualisiert Zeitstempel'},
        'Dateien suchen': {'command': "find / -name '*.txt'",
            'explanation': 'Sucht nach .txt-Dateien im gesamten System'}, 'Dateien auflisten': {'command': 'ls -l',
            'explanation': 'Detaillierte Liste mit Berechtigungen, Besitzer, Größe etc.'}}, 'Festplattennutzung': {
        'Speicherbelegung': {'command': 'df -h', 'explanation': 'Zeigt Speicherbelegung aller Dateisysteme'},
        'Verzeichnisgröße': {'command': 'du -sh [directory]', 'explanation': 'Zeigt Gesamtgröße eines Verzeichnisses'},
        'Blockgeräte': {'command': 'lsblk', 'explanation': 'Listet alle Blockgeräte (Festplatten, Partitionen) auf'},
        'Partitionen': {'command': 'fdisk -l', 'explanation': 'Zeigt Partitionstabellen an'},
        'Eingehängte Dateisysteme': {'command': 'mount', 'explanation': 'Zeigt alle eingehängten Dateisysteme'},
        'Dateisystem aushängen': {'command': 'umount /mnt', 'explanation': 'Hängt ein Dateisystem aus'}},
    'Remote-Zugriff': {'SSH Verbindung': {'command': 'ssh [user]@[host]',
        'explanation': 'Stellt eine SSH-Verbindung zum entfernten Host her'},
        'SSH Schlüssel erstellen': {'command': 'ssh-keygen', 'explanation': 'Erstellt ein SSH-Schlüsselpaar'},
        'SSH Schlüssel kopieren': {'command': 'ssh-copy-id [user]@[host]',
            'explanation': 'Kopiert den öffentlichen Schlüssel zum Host'},
        'Dateien kopieren': {'command': 'scp [file] [user]@[host]:[path]', 'explanation': 'Kopiert Dateien über SSH'},
        'Verzeichnisse synchronisieren': {'command': 'rsync -avz src/ [user]@[host]:[destination]/',
            'explanation': 'Synchronisiert Verzeichnisse effizient'},
        'SSH Tunnel': {'command': 'ssh -L 8080:localhost:80 [user]@[host]',
            'explanation': 'Erstellt einen SSH-Tunnel'}}}
