from jet_bridge.models import data_types

from sqlalchemy.sql import sqltypes

map_data_types = [
    {'query': sqltypes.VARCHAR, 'date_type': data_types.TEXT},
    {'query': sqltypes.TEXT, 'date_type': data_types.TEXT},
    {'query': sqltypes.BOOLEAN, 'date_type': data_types.BOOLEAN},
    {'query': sqltypes.INTEGER, 'date_type': data_types.INTEGER},
    {'query': sqltypes.SMALLINT, 'date_type': data_types.INTEGER},
    {'query': sqltypes.NUMERIC, 'date_type': data_types.FLOAT},
    {'query': sqltypes.DATETIME, 'date_type': data_types.DATE_TIME},
    {'query': sqltypes.TIMESTAMP, 'date_type': data_types.DATE_TIME},
    {'query': sqltypes.JSON, 'date_type': data_types.JSON},
]
default_data_type = data_types.TEXT

try:
    from geoalchemy2 import types
    map_data_types.extend(
        (
            {'query': types.Geometry, 'date_type': data_types.GEOMETRY},
            {'query': types.Geography, 'date_type': data_types.GEOGRAPHY},
        )
    )

except ImportError:
    pass


def map_data_type(value):
    return next(
        (
            rule['date_type']
            for rule in reversed(map_data_types)
            if isinstance(value, rule['query'])
        ),
        default_data_type,
    )
