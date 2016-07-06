import petl as etl

class Column(object):
    """Description of a single column.
    A Column and a PrimaryKey in a Dataset make a dimension,
    or a minimally deliverable dataset for this tool.
    """

    name = None
    data_type = None
    description = None
    data = []

    def __repr__(self):
        return "Column({})".format(self.name)

class PrimaryKey(Column):
    """Merge key for a Column or set of Columns.
    A PrimaryKey must be included in a DataSet before
    it can be published successfully.
    """

    def __repr__(self):
        return "PrimaryKey({})".format(self.name)

class Dataset(etl.Table):
    """The core data entity in dimensional.
    This is columnar data that takes on a header and rows.
    It inherits from Petl's Table, which gives us quite a
    few ways to simply import and export data in a lazy way.
    There is no reason to have to use Petl for your ETL.
    """

    name = None
    source_url = None
    processing_notes = None  # What modifications to the original data set were done. Outliers, Imputation, etc?
    license = None  # Something about how this can be used CC/Apache/etc.
    header = None

    def __init__(self, rows):
        self.rows = rows

    def __iter__(self):
        yield self.header
        for row in self.rows:
            yield(row)

    def __str__(self):
        cols = "\n".join(['{} -\t{} - \t{}'.format(c.name, c.data_type, c.description) for c in self.columns])
        return 'Name: {}\nSource Url: {}\nLicense: {}\nNum. Observation {}\nNum. Columns: {}\n\n{}'.format(self.name,
            self.source_url,
            self.license,
            len(self.columns[0].data),
            len(self.columns), cols)

    def __repr__(self):
        return "Dataset({})".format(self.name)

