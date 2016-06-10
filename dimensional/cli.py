import argparse

def mock(args):
    output = '{0} {1}'.format(args.name, args)
    print(output)

def greet(args):
    output = '{0}, {1}!'.format(args.greeting, args.name)
    if args.caps:
        output = output.upper()
    print(output)

parser = argparse.ArgumentParser()
parser.add_argument('--version', action='version', version='0.0.1')

subparsers = parser.add_subparsers()

hello_parser = subparsers.add_parser('hello')
hello_parser.add_argument('name', help='name of the person to greet')
hello_parser.add_argument('--greeting', default='Hello', help='word to use for the greeting')
hello_parser.add_argument('--caps', action='store_true', help='uppercase the output')
hello_parser.set_defaults(func=greet)

goodbye_parser = subparsers.add_parser('goodbye')
goodbye_parser.add_argument('name', help='name of the person to greet')
goodbye_parser.add_argument('--greeting', default='Hello', help='word to use for the greeting')
goodbye_parser.add_argument('--caps', action='store_true', help='uppercase the output')
goodbye_parser.set_defaults(func=greet)

import_parser = subparsers.add_parser('import')
import_parser.add_argument('name', help='name of the ETL script to run')
import_parser.add_argument('--foo', default='bar', help='foo bar')
import_parser.set_defaults(func=mock)

"""
import
    --columns
fork
    --name
push (??? or register)
pr
pull
remove
update
upgrade
info
search
list
archive
verify


-- $ dimensional install zip_crime
-- $ dimensional install zip_income
​
SELECT
  ffl.*,
  zi.*,
  zc.*
FROM federal_firearm_licensees,
JOIN zip_income ON ffl.zip = zi.zipcode
JOIN zip_crime_stats ON ffl.zip = zc.zipcode
​
-- As I am going through the data I find something that I want to change
-- $ dimensional fork zip_income
​
-- I make the changes that I want
-- $ dimensional push zip_income
​
-- I want my changes to be integrated into the master
-- $ dimensional pr zip_income
​
-- I want to pull in 2016 data because this dimension is old
-- $ dimensional update zip_crime
​
-- I want to only download one column of the data set
-- $ dimensional install zip_crime --columns=2014,2015



"""

if __name__ == '__main__':
    args = parser.parse_args()
    args.func(args)