#!/usr/bin/python3
"""script that takes in arguments and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument
that is safe from MySQL injections"""

if __name__ == '__main__':
    import sys
    import MySQLdb

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8"
        )

    cur = conn.cursor()
    query = """SELECT * FROM states WHERE name = %s ORDER BY states.id ASC"""
    cur.execute(query, (sys.argv[4],))
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    conn.close()
