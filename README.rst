dimensional
==========

A project for sharing and collaborating on data collection.  This includes features to:

* package: collect ETL and data set parameters into a distributable package
* validate: confirm the package and the data in their columns
* publish: share a discoverable package
* import: bring the data set into your workflow with various formats supported

Principles
----------

There are a few principles that are guiding the project so far.

**Collaboration**: This is a tool to make data collaboration easier.  We also collaborate as we work.  If you have ideas, please reach out to us on Slack or the Issues board.  Of course, the best collaboration is pull requests, if you have concrete ideas you are ready to share.

**Idiomatic Python**: We're writing this in as clean a format as we can...

**Lazy Evaluation**: We bring in an ETL script and expect it to be evaluated only when necessary.  Petl is great for this.  We treat our own packaging, validating, publishing, and sharing tasks in the same way.

**Dependency Indifference**: You can write your ETL scripts in any way that suits you.  We like petl, but if it produces high quality data, we want what you use.  This is also true of our destination. You can write to CSV files, databases, or other formats.

