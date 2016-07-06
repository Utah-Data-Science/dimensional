When I have a CSV file in a package
I need to have an executable wrap on that file
So that when I export I can get the table in memory.

When I have a package to export
And I ask for a Pandas DataFrame in memory
Then I get a new DataFrame with my data loaded

When I have a package
And I ask for a column of it in Pandas format
Then I get a Pandas Series
And I get the Primary Key for the Series index

When I have a package
And I ask for multiple columns in Pandas format
Then I get a Pandas DataFrame
And the index is set to the Primary Key

When I have a package
And I ask for it in CSV format and provide a destination
Then that file gets written with the data

When I have a package
And I select a subset of columns
And I ask for an export in CSV format with a destination
Then I get a file written with the subset of columns
And the PrimaryKey is always the first column

When I have a package
And I ask for an export to a database
Then I should verify a database connection
And push to a new table on that database

When I have a package
And I ask for an export to a database
And that table already exists
Then I should verify a database connection
And replace the table on that database

When I have a package
And I ask for an export to a database with append
And that table already exists
Then I should verify a database connection
And add rows to the table
And I use a transaction so that primary key constraints work

