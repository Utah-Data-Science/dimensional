When I have a column
I need to be able to inspect the contents of column
And label it as Continuous or Categorical
And disregard differences such as Time, Float, Int, etc.

When I have a Categorical column
I need to be able to count the number of categories
And generate a frequency table for each category
And generate a frequency percent for each category

When I have a column
I need to be able to count the data possibilities
And I need to count the NA values
ANd I need to count the non-NA values

When I have a Continuous column
I need to get the min
And I need the max
And I need the arithmetic mean
And I need the 25 percentile
And I need the 50 percentile
And I need the 75 percentile
And I need the standard deviation

When I have a dataset
Then I need each column evaluated

When I have a dataset evaluated
Then I need to store the meta data on each column

When I have multiple validated columns
Then I need to make continuous to continuous bivariate comparisons
And I need to make categorical to categorical bivariate comparisons
And I need to make continuous to categorical bivariate comparisons

When I have a column
And I try to evaluate it
And I get an error
Then I need to capture the error
And report that the data cannot be validated

When I have a chain of validation commands
And I have an error
Then I need to stop processing the chain
And report all of the successful and unsuccessful steps in the chain

When I have a chain
Then I need to interpret the whole chain as successful or not

When I have an unsuccessful chain
Then I need to report the problems in a useful way

