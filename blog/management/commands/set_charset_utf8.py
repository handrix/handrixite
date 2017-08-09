# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand
import MySQLdb
import logging
from datetime import datetime

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    def set_charset_utf8(self, host, user, passwd, dbname):
        """
        :param host:
        :param user:
        :param passwd:
        :param dbname:
        :return:
        """
        db = MySQLdb.connect(host=host, user=user, passwd=passwd, db=dbname)
        cursor = db.cursor()

        cursor.execute("ALTER DATABASE `%s` CHARACTER SET 'utf8' COLLATE 'utf8_unicode_ci'" % dbname)

        sql = "SELECT DISTINCT(table_name) FROM information_schema.columns WHERE table_schema = '%s'" % dbname
        cursor.execute(sql)

        results = cursor.fetchall()
        for row in results:
            sql = "ALTER TABLE `%s` convert to character set DEFAULT COLLATE DEFAULT" % (row[0])
            cursor.execute(sql)
        db.close()
        pass

    def add_arguments(self, parser):
        parser.add_argument('-H', dest='host', type=str, default='localhost')
        parser.add_argument('-u', dest='user', type=str, default='root')
        parser.add_argument('-p', dest='passwd', type=str, default='')
        parser.add_argument('-d', dest='dbname', type=str)

    def handle(self, *args, **options):
        host = options['host']
        passwd = options['passwd']
        user = options['user']
        dbname = options['dbname']

        self.stdout.write("Begin at %s" % datetime.now())
        self.set_charset_utf8(host, user, passwd, dbname)
        self.stdout.write("Done at %s" % datetime.now())
        pass
    pass