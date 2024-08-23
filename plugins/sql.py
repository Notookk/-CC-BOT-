# import sqlite3
# # Function to create a table
# def create_table(db_path, table_name, columns):
#     with sqlite3.connect(db_path) as conn:
#         cursor = conn.cursor()
#         cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})")
#         conn.commit()

# # TASK 1/4: Create 'users' table
# user_columns = """
#     id TEXT NOT NULL UNIQUE,
#     username TEXT,
#     status TEXT,
#     plan TEXT,
#     expiry TEXT,
#     credit INTEGER,
#     antispam TEXT,
#     antispam_time INTEGER,
#     totalkey TEXT,
#     reg_at TEXT
# """
# create_table('plugins/xcc_db/users.db', 'users', user_columns)
# print("TASK 1/4 COMPLETED")

# # TASK 2/4: Create 'gc' table
# gc_columns = """
#     id TEXT NOT NULL UNIQUE,
#     status TEXT,
#     plan TEXT
# """
# create_table('plugins/xcc_db/giftcard.db', 'gc', gc_columns)
# print("TASK 2/4 COMPLETED")

# print("NOW THE BOT DATABASE IS CREATED AND BOT CAN EASILY RUN NOW ✅. NOW RUN run.py FILE")