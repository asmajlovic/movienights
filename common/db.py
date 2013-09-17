import sqlite3

class Db(object):
    def __init__(self, db):
        self.conn = sqlite3.connect(db, check_same_thread=False)
        self.cur = self.conn.cursor()

    def __del__(self):
        self.conn.close()

    def execute(self, query, args=()):
        if ';' in query:
            return
        self.cur.execute(query, args)
        self.conn.commit()
        return self.cur.lastrowid

    def query(self, query, args=(), single=False):
        if ';' in query:
            return
        cur = self.cur.execute(query, args)
        rv = cur.fetchall()
        return (rv[0] if rv else None) if single else rv
