#! /usr/bin/env python3
#  -*- coding: utf-8 -*-

# Database config, see https://docs.sqlalchemy.org/en/20/core/engines.html

# sqlite memory
#database_url = "sqlite:///:memory:"
# sqlite file
database_url = "sqlite:///database.db"

# default mysql
#database_url = 'mysql://user:pass@localhost:3306/dbname'
# mysqlcient
#database_url = 'mysql+mysqldb://user:pass@localhost:3306/dbname'
# PyMySQL
#database_url = 'mysql+pymysql://user:pass@localhost:3306/dbname'
#

# Print all requests in stdout
_DATABASE_DEBUG = True
# Don't autocommit in order to make manual transactions
_DATABASE_AUTOCOMMIT = False
