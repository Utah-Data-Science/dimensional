import petl as etl

def export(exporter, table, *args, **kwargs):
    return exporter(table, *args, **kwargs)

def export_csv(table, *args, **kwargs):
    return export(etl.tocsv, table, *args, **kwargs)

def append_csv(table, *args, **kwargs):
    return export(etl.appendcsv, table, *args, **kwargs)

def export_db(table, connection, tablename, *args, **kwargs):
    return export(etl.todb, table, connection, tablename, *args, **kwargs)

def append_db(table, connection, tablename, *args, **kwargs):
    return export(etl.appenddb, table, connection, tablename, *args, **kwargs)

