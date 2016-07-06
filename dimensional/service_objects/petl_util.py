from __future__ import absolute_import, print_function, division
from dimensional.entities.entities import (Column, PrimaryKey, Dataset)
import petl as etl

def table_container_from(dataset):
    return etl.fromcolumns(dataset.columns, dataset.header)

def from_csv(source=None, encoding=None, errors='strict', description=None,
        **csvargs):
    table = etl.fromcsv(source, encoding, errors, **csvargs)
    dataset = Dataset()
    dataset.header = table.header
    dataset.rows = table.records
    # FIXME: configure name, etc.
    return dataset

# For Petl familiarity
fromcsv = from_csv

