# -*- coding: utf-8 -*-
COMMANDS = {
    'linux': {
        'Dateiverwaltung': {
            'Datei kopieren': {
                'command': 'cp [source] [destination]',
                'explanation': 'Kopiert Datei1 zu Datei2'
            },
            'Datei verschieben': {
                'command': 'mv [file] [directory]',
                'explanation': 'Verschiebt Datei in verzeichnis/'
            },
            'Datei löschen': {
                'command': 'rm [file]',
                'explanation': 'Löscht eine Datei'
            },
            'Verzeichnis erstellen': {
                'command': 'mkdir [directory]',
                'explanation': 'Erstellt ein neues Verzeichnis'
            },
            'Datei erstellen': {
                'command': 'touch [file]',
                'explanation': 'Erstellt eine leere Datei oder aktualisiert Zeitstempel'
            },
            'Dateien suchen': {
                'command': "find / -name '*.txt'",
                'explanation': 'Sucht nach .txt-Dateien im gesamten System'
            },
            'Dateien auflisten': {
                'command': 'ls -l',
                'explanation': 'Detaillierte Liste mit Berechtigungen, Besitzer, Größe etc.'
            }
        },
        'Systeminformationen': {
            'Systeminformationen': {
                'command': 'uname -a',
                'explanation': 'Zeigt Systeminformationen (Kernel, Hostname etc.)'
            },
            'Speicherbelegung': {
                'command': 'df -h',
                'explanation': 'Zeigt Speicherbelegung der Dateisysteme (human readable)'
            },
            'Speichernutzung': {
                'command': 'free -m',
                'explanation': 'Zeigt Speichernutzung in MB'
            },
            'Prozessliste': {
                'command': 'top',
                'explanation': 'Dynamische Anzeige der laufenden Prozesse'
            },
            'CPU-Informationen': {
                'command': 'lscpu',
                'explanation': 'Zeigt CPU-Informationen'
            },
            'Systemlaufzeit': {
                'command': 'uptime',
                'explanation': 'Zeigt Systemlaufzeit und Auslastung'
            }
        },
        'Prozesssteuerung': {
            'Prozessliste': {
                'command': 'ps aux',
                'explanation': 'Zeigt alle laufenden Prozesse'
            },
            'Prozess beenden': {
                'command': 'kill -9 [PID]',
                'explanation': 'Beendet einen Prozess mit der angegebenen Prozess-ID'
            },
            'Prozess nach Name beenden': {
                'command': 'killall [processname]',
                'explanation': 'Beendet alle Prozesse mit diesem Namen'
            },
            'Priorität ändern': {
                'command': 'nice -n 10 [command]',
                'explanation': 'Startet einen Befehl mit angepasster Priorität'
            },
            'Hintergrundprozess': {
                'command': 'bg',
                'explanation': 'Setzt einen gestoppten Prozess im Hintergrund fort'
            },
            'Vordergrundprozess': {
                'command': 'fg',
                'explanation': 'Bringt einen Hintergrundprozess in den Vordergrund'
            }
        },
        'Netzwerkbefehle': {
            'Netzwerkkonfiguration': {
                'command': 'ifconfig',
                'explanation': 'Zeigt Netzwerkschnittstellen und Konfiguration'
            },
            'Verbindung testen': {
                'command': 'ping [host]',
                'explanation': 'Sendet ICMP-Pakete zum angegebenen Host'
            },
            'Verbindungsweg': {
                'command': 'traceroute [host]',
                'explanation': 'Zeigt den Weg der Pakete zum Zielhost'
            },
            'Offene Ports': {
                'command': 'netstat -tuln',
                'explanation': 'Zeigt alle offenen Ports und Verbindungen'
            },
            'SSH Verbindung': {
                'command': 'ssh [user]@[host]',
                'explanation': 'Stellt eine SSH-Verbindung zum entfernten Host her'
            },
            'Dateien kopieren': {
                'command': 'scp [file] [user]@[host]:[path]',
                'explanation': 'Kopiert Dateien über SSH'
            }
        },
        'Berechtigungen': {
            'Berechtigungen ändern': {
                'command': 'chmod 755 [file]',
                'explanation': 'Ändert Dateiberechtigungen (rwx für Owner, r-x für Gruppe und Andere)'
            },
            'Datei ausführbar machen': {
                'command': 'chmod +x [file]',
                'explanation': 'Macht eine Datei ausführbar'
            },
            'Besitzer ändern': {
                'command': 'chown [user]:[group] [file]',
                'explanation': 'Ändert Besitzer und Gruppe einer Datei'
            },
            'Gruppe ändern': {
                'command': 'chgrp [group] [file]',
                'explanation': 'Ändert die Gruppe einer Datei'
            },
            'Standard-Berechtigungen': {
                'command': 'umask 022',
                'explanation': 'Setzt Standard-Berechtigungen für neue Dateien'
            },
            'ACL anzeigen': {
                'command': 'getfacl [file]',
                'explanation': 'Zeigt erweiterte ACL-Berechtigungen'
            }
        },
        'Paketverwaltung': {
            'Paketliste aktualisieren': {
                'command': 'apt update',
                'explanation': 'Aktualisiert die Paketliste (Debian/Ubuntu)'
            },
            'Paket installieren': {
                'command': 'apt install [package]',
                'explanation': 'Installiert ein Paket'
            },
            'Paket entfernen': {
                'command': 'apt remove [package]',
                'explanation': 'Deinstalliert ein Paket'
            },
            'Pakete aktualisieren': {
                'command': 'apt upgrade',
                'explanation': 'Aktualisiert alle installierten Pakete'
            },
            'RPM-Paket installieren': {
                'command': 'yum install [package]',
                'explanation': 'Installiert ein Paket (RHEL/CentOS)'
            },
            'DEB-Paket installieren': {
                'command': 'dpkg -i [package.deb]',
                'explanation': 'Installiert eine .deb-Datei'
            }
        },
        'Textverarbeitung': {
            'Datei kopieren': {
                'command': 'cp [source] [destination]',
                'explanation': 'Kopiert datei1 zu datei2'
            },
            'Datei verschieben': {
                'command': 'mv [source] [directory]',
                'explanation': 'Verschiebt datei1 in verzeichnis/'
            },
            'Datei löschen': {
                'command': 'rm [file]',
                'explanation': 'Löscht eine Datei'
            },
            'Verzeichnis erstellen': {
                'command': 'mkdir [directory]',
                'explanation': 'Erstellt ein neues Verzeichnis'
            },
            'Datei erstellen': {
                'command': 'touch [file]',
                'explanation': 'Erstellt eine leere Datei oder aktualisiert Zeitstempel'
            },
            'Dateien suchen': {
                'command': "find / -name '*.txt'",
                'explanation': 'Sucht nach .txt-Dateien im gesamten System'
            },
            'Dateien auflisten': {
                'command': 'ls -l',
                'explanation': 'Detaillierte Liste mit Berechtigungen, Besitzer, Größe etc.'
            }
        },
        'Festplattennutzung': {
            'Speicherbelegung': {
                'command': 'df -h',
                'explanation': 'Zeigt Speicherbelegung aller Dateisysteme'
            },
            'Verzeichnisgröße': {
                'command': 'du -sh [directory]',
                'explanation': 'Zeigt Gesamtgröße eines Verzeichnisses'
            },
            'Blockgeräte': {
                'command': 'lsblk',
                'explanation': 'Listet alle Blockgeräte (Festplatten, Partitionen) auf'
            },
            'Partitionen': {
                'command': 'fdisk -l',
                'explanation': 'Zeigt Partitionstabellen an'
            },
            'Eingehängte Dateisysteme': {
                'command': 'mount',
                'explanation': 'Zeigt alle eingehängten Dateisysteme'
            },
            'Dateisystem aushängen': {
                'command': 'umount /mnt',
                'explanation': 'Hängt ein Dateisystem aus'
            }
        },
        'Remote-Zugriff': {
            'SSH Verbindung': {
                'command': 'ssh [user]@[host]',
                'explanation': 'Stellt eine SSH-Verbindung zum entfernten Host her'
            },
            'SSH Schlüssel erstellen': {
                'command': 'ssh-keygen',
                'explanation': 'Erstellt ein SSH-Schlüsselpaar'
            },
            'SSH Schlüssel kopieren': {
                'command': 'ssh-copy-id [user]@[host]',
                'explanation': 'Kopiert den öffentlichen Schlüssel zum Host'
            },
            'Dateien kopieren': {
                'command': 'scp [file] [user]@[host]:[path]',
                'explanation': 'Kopiert Dateien über SSH'
            },
            'Verzeichnisse synchronisieren': {
                'command': 'rsync -avz src/ [user]@[host]:[destination]/',
                'explanation': 'Synchronisiert Verzeichnisse effizient'
            },
            'SSH Tunnel': {
                'command': 'ssh -L 8080:localhost:80 [user]@[host]',
                'explanation': 'Erstellt einen SSH-Tunnel'
            }
        }
    },
    'sql': {
        'Datenbanken verwalten': {
            'Datenbank erstellen': {
                'command': 'CREATE DATABASE [database]',
                'explanation': 'Erstellt eine neue Datenbank'
            },
            'Datenbank verwenden': {
                'command': 'USE [database]',
                'explanation': 'Wechselt zur angegebenen Datenbank'
            },
            'Datenbanken anzeigen': {
                'command': 'SHOW DATABASES',
                'explanation': 'Listet alle Datenbanken auf'
            },
            'Datenbank löschen': {
                'command': 'DROP DATABASE [database]',
                'explanation': 'Löscht eine Datenbank'
            },
            'Datenbank mit Zeichensatz': {
                'command': 'CREATE DATABASE [database] CHARACTER SET utf8mb4',
                'explanation': 'Erstellt DB mit UTF-8 Zeichensatz'
            }
        },
        'Tabellen verwalten': {
            'Tabelle erstellen': {
                'command': 'CREATE TABLE [table] (id INT, name VARCHAR(50))',
                'explanation': 'Erstellt eine neue Tabelle'
            },
            'Spalte hinzufügen': {
                'command': 'ALTER TABLE [table] ADD COLUMN [email] VARCHAR(100)',
                'explanation': 'Fügt eine Spalte hinzu'
            },
            'Tabelle löschen': {
                'command': 'DROP TABLE [table]',
                'explanation': 'Löscht eine Tabelle'
            },
            'Tabellenstruktur': {
                'command': 'DESCRIBE [table]',
                'explanation': 'Zeigt die Struktur einer Tabelle'
            },
            'Tabellen auflisten': {
                'command': 'SHOW TABLES',
                'explanation': 'Listet alle Tabellen in der aktuellen DB auf'
            }
        },
        'Daten bearbeiten': {
            'Daten einfügen': {
                'command': "INSERT INTO [table] VALUES (1, 'John')",
                'explanation': 'Fügt einen neuen Datensatz ein'
            },
            'Daten aktualisieren': {
                'command': "UPDATE [table] SET [name]='Mike' WHERE id=1",
                'explanation': 'Aktualisiert einen Datensatz'
            },
            'Daten löschen': {
                'command': 'DELETE FROM [table] WHERE id=1',
                'explanation': 'Löscht einen Datensatz'
            },
            'Alle Daten löschen': {
                'command': 'TRUNCATE TABLE [table]',
                'explanation': 'Löscht alle Daten in der Tabelle'
            },
            'Daten ersetzen': {
                'command': "REPLACE INTO [table] VALUES (1, 'John')",
                'explanation': 'Ersetzt oder fügt einen Datensatz ein'
            }
        },
        'Datenabfragen': {
            'Alle Daten auswählen': {
                'command': 'SELECT * FROM [table]',
                'explanation': 'Wählt alle Spalten und Zeilen aus'
            },
            'Spalten auswählen': {
                'command': 'SELECT [name], [email] FROM [table]',
                'explanation': 'Wählt bestimmte Spalten aus'
            },
            'Mit Bedingung': {
                'command': 'SELECT * FROM [table] WHERE id > 5',
                'explanation': 'Filtert Datensätze nach Bedingung'
            },
            'Sortieren': {
                'command': 'SELECT * FROM [table] ORDER BY [name] DESC',
                'explanation': 'Sortiert die Ergebnisse absteigend'
            },
            'Paginierung': {
                'command': 'SELECT * FROM [table] LIMIT 10 OFFSET 20',
                'explanation': 'Zeigt 10 Datensätze ab Position 20'
            }
        },
        'Joins': {
            'INNER JOIN': {
                'command': 'SELECT u.[name], o.[amount] FROM [table] u JOIN [table2] o ON u.id = o.user_id',
                'explanation': 'Nur übereinstimmende Datensätze'
            },
            'LEFT JOIN': {
                'command': 'SELECT u.[name], o.[amount] FROM [table] u LEFT JOIN [table2] o ON u.id = o.user_id',
                'explanation': 'Alle Benutzer, auch ohne Bestellungen'
            },
            'RIGHT JOIN': {
                'command': 'SELECT u.[name], o.[amount] FROM [table] u RIGHT JOIN [table2] o ON u.id = o.user_id',
                'explanation': 'Alle Bestellungen, auch ohne Benutzer'
            },
            'CROSS JOIN': {
                'command': 'SELECT u.[name], o.[amount] FROM [table] u CROSS JOIN [table2] o',
                'explanation': 'Alle möglichen Kombinationen'
            }
        },
        'Funktionen': {
            'Aggregatfunktionen': {
                'command': 'SELECT COUNT(*), AVG([column]), MAX([date]) FROM [table]',
                'explanation': 'Zählen, Durchschnitt, Maximum'
            },
            'Textfunktion': {
                'command': "SELECT CONCAT([first_name], ' ', [last_name]) AS full_name FROM [table]",
                'explanation': 'Text verkettung'
            },
            'Datumsfunktion': {
                'command': "SELECT DATE_FORMAT([created_at], '%Y-%m') AS month FROM [table2]",
                'explanation': 'Datumsformatierung'
            },
            'NULL-Behandlung': {
                'command': "SELECT IFNULL([email], 'no email') FROM [table]",
                'explanation': 'Behandlung von NULL-Werten'
            },
            'Gruppierung': {
                'command': 'SELECT SUM([amount]) FROM [table2] GROUP BY user_id',
                'explanation': 'Gruppierung und Summierung'
            }
        },
        'Index': {
            'Index erstellen': {
                'command': 'CREATE INDEX idx_name ON [table]([name])',
                'explanation': 'Erstellt einen Index auf die name-Spalte'
            },
            'Eindeutigen Index': {
                'command': 'CREATE UNIQUE INDEX idx_email ON [table]([email])',
                'explanation': 'Erstellt einen eindeutigen Index'
            },
            'Index löschen': {
                'command': 'DROP INDEX idx_name ON [table]',
                'explanation': 'Löscht einen Index'
            },
            'Indizes anzeigen': {
                'command': 'SHOW INDEX FROM [table]',
                'explanation': 'Zeigt alle Indizes einer Tabelle an'
            },
            'Abfrageplan': {
                'command': "EXPLAIN SELECT * FROM [table] WHERE [name] = 'John'",
                'explanation': 'Zeigt wie die Abfrage ausgeführt wird'
            }
        }
    },
    'datentypen': {
        'Numerische Typen': {
            'TINYINT': {
                'command': 'TINYINT',
                'explanation': 'Ganze Zahlen von -128 bis 127'
            },
            'SMALLINT': {
                'command': 'SMALLINT',
                'explanation': 'Ganze Zahlen von -32,768 bis 32,767'
            },
            'MEDIUMINT': {
                'command': 'MEDIUMINT',
                'explanation': 'Ganze Zahlen von -8,388,608 bis 8,388,607'
            },
            'INT': {
                'command': 'INT',
                'explanation': 'Ganze Zahlen von -2,147,483,648 bis 2,147,483,647'
            },
            'BIGINT': {
                'command': 'BIGINT',
                'explanation': 'Ganze Zahlen von -9,223,372,036,854,775,808 bis 9,223,372,036,854,775,807'
            },
            'BOOLEAN': {
                'command': 'BOOLEAN',
                'explanation': 'Boolesche Werte (true/false), Synonym für TINYINT(1)'
            },
            'DECIMAL': {
                'command': 'DECIMAL(p,s)',
                'explanation': 'Dezimalzahlen mit bis zu 65 Stellen (p=Gesamtstellen, s=Nachkommastellen)'
            },
            'FLOAT': {
                'command': 'FLOAT',
                'explanation': 'Gleitkommazahlen (±3.402823466E+38 bis ±1.175494351E-38)'
            },
            'DOUBLE': {
                'command': 'DOUBLE',
                'explanation': 'Gleitkommazahlen (±1.7976931348623157E+308 bis ±2.2250738585072014E-308)'
            },
            'BIT': {
                'command': 'BIT',
                'explanation': 'Ein einzelnes Bit (0 oder 1)'
            },
            'INTEGER': {
                'command': 'INTEGER',
                'explanation': 'Synonym für INT (Ganze Zahlen 32 Bit)'
            },
            'SERIAL': {
                'command': 'SERIAL',
                'explanation': 'Auto-increment Ganzzahl (Alias für BIGINT UNSIGNED NOT NULL AUTO_INCREMENT UNIQUE)'
            }
        },
        'Zeit/Datum Typen': {
            'DATE': {
                'command': 'DATE',
                'explanation': 'Speichert ein Datum (YYYY-MM-DD)'
            },
            'TIME': {
                'command': 'TIME',
                'explanation': 'Speichert eine Uhrzeit (HH:MM:SS)'
            },
            'DATETIME': {
                'command': 'DATETIME',
                'explanation': 'Speichert Datum und Uhrzeit (YYYY-MM-DD HH:MM:SS)'
            },
            'TIMESTAMP': {
                'command': 'TIMESTAMP',
                'explanation': 'Zeitstempel (automatische Aktualisierung möglich)'
            },
            'YEAR': {
                'command': 'YEAR',
                'explanation': 'Speichert ein Jahr (4-stellig)'
            },
            'INTERVAL': {
                'command': 'INTERVAL',
                'explanation': 'Zeitintervalle (z.B. für Berechnungen)'
            }
        },
        'String Typen': {
            'CHAR': {
                'command': 'CHAR(n)',
                'explanation': 'Feste Zeichenkette (0-255 Zeichen, mit Leerzeichen aufgefüllt)'
            },
            'VARCHAR': {
                'command': 'VARCHAR(n)',
                'explanation': 'Variable Zeichenkette (0-65.535 Zeichen)'
            },
            'BINARY': {
                'command': 'BINARY(n)',
                'explanation': 'Feste Länge binärer Daten (0-255 Bytes)'
            },
            'VARBINARY': {
                'command': 'VARBINARY(n)',
                'explanation': 'Variable Länge binärer Daten (0-65.535 Bytes)'
            },
            'TINYBLOB': {
                'command': 'TINYBLOB',
                'explanation': 'Binärobjekt bis 255 Bytes'
            },
            'BLOB': {
                'command': 'BLOB',
                'explanation': 'Binärobjekt bis 65.535 Bytes'
            },
            'MEDIUMBLOB': {
                'command': 'MEDIUMBLOB',
                'explanation': 'Binärobjekt bis 16.777.215 Bytes'
            },
            'LONGBLOB': {
                'command': 'LONGBLOB',
                'explanation': 'Binärobjekt bis 4.294.967.295 Bytes'
            },
            'TINYTEXT': {
                'command': 'TINYTEXT',
                'explanation': 'Text bis 255 Zeichen'
            },
            'TEXT': {
                'command': 'TEXT',
                'explanation': 'Text bis 65.535 Zeichen'
            },
            'MEDIUMTEXT': {
                'command': 'MEDIUMTEXT',
                'explanation': 'Text bis 16.777.215 Zeichen'
            },
            'LONGTEXT': {
                'command': 'LONGTEXT',
                'explanation': 'Text bis 4.294.967.295 Zeichen'
            },
            'ENUM': {
                'command': "ENUM('val1','val2',...)",
                'explanation': 'Aufzählungstyp (nur vordefinierte Werte)'
            },
            'SET': {
                'command': "SET('val1','val2',...)",
                'explanation': 'Menge unterschiedlicher Zeichenketten (kombinierbar)'
            }
        },
        'Räumliche Typen': {
            'GEOMETRY': {
                'command': 'GEOMETRY',
                'explanation': 'Basisklasse für räumliche Typen'
            },
            'POINT': {
                'command': 'POINT',
                'explanation': 'Punkt mit X/Y-Koordinaten'
            },
            'LINESTRING': {
                'command': 'LINESTRING',
                'explanation': 'Linie aus mehreren Punkten'
            },
            'POLYGON': {
                'command': 'POLYGON',
                'explanation': 'Geschlossene Fläche'
            },
            'MULTIPOINT': {
                'command': 'MULTIPOINT',
                'explanation': 'Mehrere Punkte'
            },
            'MULTILINESTRING': {
                'command': 'MULTILINESTRING',
                'explanation': 'Mehrere Linien'
            },
            'MULTIPOLYGON': {
                'command': 'MULTIPOLYGON',
                'explanation': 'Mehrere Polygone'
            },
            'GEOMETRYCOLLECTION': {
                'command': 'GEOMETRYCOLLECTION',
                'explanation': 'Sammlung verschiedener Geometrien'
            }
        },
        'Sonstige Typen': {
            'BLOB': {
                'command': 'BLOB',
                'explanation': 'Binäre Daten (z.B. Bilder, Audiodateien)'
            },
            'JSON': {
                'command': 'JSON',
                'explanation': 'Speichert JSON-Dokumente (ab MariaDB 10.2)'
            },
            'UUID': {
                'command': 'UUID',
                'explanation': 'Universally Unique Identifier (als String)'
            },
            'INET6': {
                'command': 'INET6',
                'explanation': 'IPv6-Adressen'
            },
            'BIT': {
                'command': 'BIT',
                'explanation': 'Bit-Felder'
            },
            'AUTO_INCREMENT': {
                'command': 'AUTO_INCREMENT',
                'explanation': 'Automatisch hochzählender Wert (für Primärschlüssel)'
            },
            'NULL': {
                'command': 'NULL',
                'explanation': 'Kein Wert vorhanden (kein eigener Datentyp)'
            }
        }
    }
}
