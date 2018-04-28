#!/usr/bin/env python
# coding: utf-8

import json
import MySQLdb


class Db_mysql(object):
    """ test connect with mysql """

    def __init__(self):
        self.db = MySQLdb.connect(host='localhost',
                        user='jovi',
                        passwd='mwq1992414',
                        db='test')

    def get_multi(self, id):

        def iter(cur):
            for row in cur.fetchall():
                yield row

        def flat(arr):
            show_list = []
            for per in arr:
                show_list.append(per)
            return show_list

        cur = self.db.cursor()
        sql = "select * from foo where id='%s'" % id
        print '---', sql, '+++'
        cur.execute(sql)

        generator = iter(cur)
        res = flat(generator)

        return json.dumps(res)

    def get_one(self, name):
        cur = self.db.cursor()
        sql = 'select * from foo where id=%s' % name
        print '---', sql, '+++'
        try:
            cur.execute(sql)
        except:
            return 'nobody actually'
        res = cur.fetchone()
        return json.dumps(res)
