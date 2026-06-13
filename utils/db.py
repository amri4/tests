import sqlite3

# We leave these uninitialized here so they don't lock onto a single file name immediately
conn = None
cursor = None

# =========================================
# HELPER TO SWITCH DATABASE FILE DYNAMICALLY
# =========================================
def _connect_to(db_name):
    global conn, cursor
    conn = sqlite3.connect(f"{db_name}.db")
    cursor = conn.cursor()

# =========================================
# CREATE TABLE
# =========================================
def create_table(name, columns):
    _connect_to(name)  # Automatically connects to "tablename.db"

    cursor.execute(f"""
    CREATE TABLE IF NOT EXISTS {name} (
        {columns}
    )
    """)

    conn.commit()
    conn.close()

# =========================================
# INSERT
# =========================================
def insert(table, columns, values):
    _connect_to(table)

    placeholders = ", ".join(
        ["?"] * len(values)
    )

    cursor.execute(f"""
    INSERT INTO {table}
    ({columns})

    VALUES ({placeholders})
    """, values)

    conn.commit()
    conn.close()

# =========================================
# INSERT OR REPLACE
# =========================================
def insert_replace(table, columns, values):
    _connect_to(table)

    placeholders = ", ".join(
        ["?"] * len(values)
    )

    cursor.execute(f"""
    INSERT OR REPLACE INTO {table}
    ({columns})

    VALUES ({placeholders})
    """, values)

    conn.commit()
    conn.close()

# =========================================
# SELECT ONE
# =========================================
def fetchone(table, condition=None, values=()):
    _connect_to(table)

    query = f"SELECT * FROM {table}"

    if condition:
        query += f" WHERE {condition}"

    cursor.execute(query, values)
    result = cursor.fetchone()
    
    conn.close()
    return result

# =========================================
# SELECT ALL
# =========================================
def fetchall(table):
    _connect_to(table)

    cursor.execute(f"""
    SELECT * FROM {table}
    """)

    result = cursor.fetchall()
    
    conn.close()
    return result

# =========================================
# UPDATE
# =========================================
def update(table, set_values, condition, values):
    _connect_to(table)

    cursor.execute(f"""
    UPDATE {table}
    SET {set_values}
    WHERE {condition}
    """, values)

    conn.commit()
    conn.close()

# =========================================
# DELETE
# =========================================
def delete(table, condition, values):
    _connect_to(table)

    cursor.execute(f"""
    DELETE FROM {table}
    WHERE {condition}
    """, values)

    conn.commit()
    conn.close()

# =========================================
# EXISTS
# =========================================
def exists(table, condition, values):
    _connect_to(table)

    cursor.execute(f"""
    SELECT * FROM {table}
    WHERE {condition}
    """, values)

    result = cursor.fetchone() is not None
    
    conn.close()
    return result

# =========================================
# CLOSE
# =========================================
def close():
    if conn:
        conn.close()
