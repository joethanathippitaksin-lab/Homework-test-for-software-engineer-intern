import sqlite3

conn = sqlite3.connect(":memory:")  # temporary database in memory

conn.executescript("""
CREATE TABLE DEPARTMENT (
    departmentId   TEXT PRIMARY KEY,
    departmentName TEXT
);

CREATE TABLE STAFF (
    staffId      TEXT PRIMARY KEY,
    staffName    TEXT,
    salary       INTEGER,
    managerId    TEXT,
    departmentId TEXT
);

INSERT INTO DEPARTMENT VALUES ('D01', 'Commercial'), ('D02', 'Tech');

INSERT INTO STAFF VALUES
('S0001', 'Susan', 55000, NULL,    'D01'),
('S0002', 'John',  30000, 'S0001', 'D01'),
('S0003', 'Mike',  28000, 'S0001', 'D01'),
('S0004', 'Andy',  45000, NULL,    'D02'),
('S0005', 'Tom',   27000, 'S0004', 'D02');
""")

with open("q2.sql", encoding="utf-8") as f:
    query = f.read()

cursor = conn.execute(query)
print([col[0] for col in cursor.description])
for row in cursor.fetchall():
    print(row)