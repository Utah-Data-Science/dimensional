
class Dataset(object):

    name = None
    source_url = None
    processing_notes = None  # What modifications to the original data set were done. Outliers, Imputation, etc?
    license = None  # Something about how this can be used CC/Apache/etc.
    columns = []

    def __str__(self):
        cols = "\n".join(['{} -\t{} - \t{}'.format(c.name, c.data_type, c.description) for c in self.columns])
        return 'Name: {}\nSource Url: {}\nLicense: {}\nNum. Observation {}\nNum. Columns: {}\n\n{}'.format(self.name,
                                                                                   self.source_url,
                                                                                   self.license,
                                                                                   len(self.columns[0].data),
                                                                                   len(self.columns), cols)


class Column(object):

    name = None
    data_type = None
    description = None  # I think it is very important to know how the data is calculated
    data = []


class PrimaryKey(Column):
    pass


zip = PrimaryKey()
zip.data = ['77379', '84064', '84003']
zip.data_type = str
zip.name = 'zipcodes'
zip.description = 'A 5 digit postal code used in the US'

city = Column()
city.data = ['Spring', 'Provo', 'Highland']
city.data_type = str
city.name = 'City'
city.description = 'Name of city'

state = Column()
state.data = ['TX', 'UT', 'UT']
state.data_type = str
state.name = 'State'
state.description = 'Name of State'

data_set = Dataset()
data_set.name = 'Places I have lived'
data_set.columns = [zip, state, city]
data_set.license = 'Creative Commons Share-Alike'
data_set.processing_notes = 'I removed cities that I haven\'t lived in'
data_set.source_url = 'jpotts18.github.io/datasets/zips.csv'

print(data_set)
