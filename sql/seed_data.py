from datetime import date
from sqlalchemy.sql import table, column
from sqlalchemy import String, Integer, Date
from alembic import op

# Create an ad-hoc table to use for the insert statement.
accounts_table = table('account',
    column('id', Integer),
    column('name', String),
    column('create_date', Date)
)

op.bulk_insert(accounts_table,
    [
        {'id':1, 'name':'John Smith',
                'create_date':date(2010, 10, 5)},
        {'id':2, 'name':'Ed Williams',
                'create_date':date(2007, 5, 27)},
        {'id':3, 'name':'Wendy Jones',
                'create_date':date(2008, 8, 15)},
    ]
)