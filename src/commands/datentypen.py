commands = {'Numerische Typen': {'TINYINT': {'command': 'TINYINT', 'explanation': 'Ganze Zahlen von -128 bis 127'},
    'SMALLINT': {'command': 'SMALLINT', 'explanation': 'Ganze Zahlen von -32,768 bis 32,767'},
    'MEDIUMINT': {'command': 'MEDIUMINT', 'explanation': 'Ganze Zahlen von -8,388,608 bis 8,388,607'},
    'INT': {'command': 'INT', 'explanation': 'Ganze Zahlen von -2,147,483,648 bis 2,147,483,647'},
    'BIGINT': {'command': 'BIGINT',
        'explanation': 'Ganze Zahlen von -9,223,372,036,854,775,808 bis 9,223,372,036,854,775,807'},
    'BOOLEAN': {'command': 'BOOLEAN', 'explanation': 'Boolesche Werte (true/false), Synonym für TINYINT(1)'},
    'DECIMAL': {'command': 'DECIMAL(p,s)',
        'explanation': 'Dezimalzahlen mit bis zu 65 Stellen (p=Gesamtstellen, s=Nachkommastellen)'},
    'FLOAT': {'command': 'FLOAT', 'explanation': 'Gleitkommazahlen (±3.402823466E+38 bis ±1.175494351E-38)'},
    'DOUBLE': {'command': 'DOUBLE',
        'explanation': 'Gleitkommazahlen (±1.7976931348623157E+308 bis ±2.2250738585072014E-308)'},
    'BIT': {'command': 'BIT', 'explanation': 'Ein einzelnes Bit (0 oder 1)'},
    'INTEGER': {'command': 'INTEGER', 'explanation': 'Synonym für INT (Ganze Zahlen 32 Bit)'},
    'SERIAL': {'command': 'SERIAL',
        'explanation': 'Auto-increment Ganzzahl (Alias für BIGINT UNSIGNED NOT NULL AUTO_INCREMENT UNIQUE)'}},
    'Zeit/Datum Typen': {'DATE': {'command': 'DATE', 'explanation': 'Speichert ein Datum (YYYY-MM-DD)'},
        'TIME': {'command': 'TIME', 'explanation': 'Speichert eine Uhrzeit (HH:MM:SS)'},
        'DATETIME': {'command': 'DATETIME', 'explanation': 'Speichert Datum und Uhrzeit (YYYY-MM-DD HH:MM:SS)'},
        'TIMESTAMP': {'command': 'TIMESTAMP', 'explanation': 'Zeitstempel (automatische Aktualisierung möglich)'},
        'YEAR': {'command': 'YEAR', 'explanation': 'Speichert ein Jahr (4-stellig)'},
        'INTERVAL': {'command': 'INTERVAL', 'explanation': 'Zeitintervalle (z.B. für Berechnungen)'}}, 'String Typen': {
        'CHAR': {'command': 'CHAR(n)', 'explanation': 'Feste Zeichenkette (0-255 Zeichen, mit Leerzeichen aufgefüllt)'},
        'VARCHAR': {'command': 'VARCHAR(n)', 'explanation': 'Variable Zeichenkette (0-65.535 Zeichen)'},
        'BINARY': {'command': 'BINARY(n)', 'explanation': 'Feste Länge binärer Daten (0-255 Bytes)'},
        'VARBINARY': {'command': 'VARBINARY(n)', 'explanation': 'Variable Länge binärer Daten (0-65.535 Bytes)'},
        'TINYBLOB': {'command': 'TINYBLOB', 'explanation': 'Binärobjekt bis 255 Bytes'},
        'BLOB': {'command': 'BLOB', 'explanation': 'Binärobjekt bis 65.535 Bytes'},
        'MEDIUMBLOB': {'command': 'MEDIUMBLOB', 'explanation': 'Binärobjekt bis 16.777.215 Bytes'},
        'LONGBLOB': {'command': 'LONGBLOB', 'explanation': 'Binärobjekt bis 4.294.967.295 Bytes'},
        'TINYTEXT': {'command': 'TINYTEXT', 'explanation': 'Text bis 255 Zeichen'},
        'TEXT': {'command': 'TEXT', 'explanation': 'Text bis 65.535 Zeichen'},
        'MEDIUMTEXT': {'command': 'MEDIUMTEXT', 'explanation': 'Text bis 16.777.215 Zeichen'},
        'LONGTEXT': {'command': 'LONGTEXT', 'explanation': 'Text bis 4.294.967.295 Zeichen'},
        'ENUM': {'command': "ENUM('val1','val2',...)", 'explanation': 'Aufzählungstyp (nur vordefinierte Werte)'},
        'SET': {'command': "SET('val1','val2',...)",
            'explanation': 'Menge unterschiedlicher Zeichenketten (kombinierbar)'}},
    'Räumliche Typen': {'GEOMETRY': {'command': 'GEOMETRY', 'explanation': 'Basisklasse für räumliche Typen'},
        'POINT': {'command': 'POINT', 'explanation': 'Punkt mit X/Y-Koordinaten'},
        'LINESTRING': {'command': 'LINESTRING', 'explanation': 'Linie aus mehreren Punkten'},
        'POLYGON': {'command': 'POLYGON', 'explanation': 'Geschlossene Fläche'},
        'MULTIPOINT': {'command': 'MULTIPOINT', 'explanation': 'Mehrere Punkte'},
        'MULTILINESTRING': {'command': 'MULTILINESTRING', 'explanation': 'Mehrere Linien'},
        'MULTIPOLYGON': {'command': 'MULTIPOLYGON', 'explanation': 'Mehrere Polygone'},
        'GEOMETRYCOLLECTION': {'command': 'GEOMETRYCOLLECTION', 'explanation': 'Sammlung verschiedener Geometrien'}},
    'Sonstige Typen': {'BLOB': {'command': 'BLOB', 'explanation': 'Binäre Daten (z.B. Bilder, Audiodateien)'},
        'JSON': {'command': 'JSON', 'explanation': 'Speichert JSON-Dokumente (ab MariaDB 10.2)'},
        'UUID': {'command': 'UUID', 'explanation': 'Universally Unique Identifier (als String)'},
        'INET6': {'command': 'INET6', 'explanation': 'IPv6-Adressen'},
        'BIT': {'command': 'BIT', 'explanation': 'Bit-Felder'}, 'AUTO_INCREMENT': {'command': 'AUTO_INCREMENT',
            'explanation': 'Automatisch hochzählender Wert (für Primärschlüssel)'},
        'NULL': {'command': 'NULL', 'explanation': 'Kein Wert vorhanden (kein eigener Datentyp)'}}}
