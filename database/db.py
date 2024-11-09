import sqlite3

def connect(db_path):
    con = sqlite3.connect(db_path)
    cursor = con.cursor()
    return con, cursor


def create_user_table():
    con, cursor = connect('../translator.db')

    sql = """
        create table if not exists users (
        user_id integer primary key autoincrement,
        chat_id bigint not null
        );
    """
    cursor.execute(sql)
    con.commit()
    con.close()

create_user_table()