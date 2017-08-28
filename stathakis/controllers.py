import logging

import dateutil
import flask

from .measurements import available_grids

logger = logging.getLogger(__name__)


def stations() -> list:
    logger.info("request: %s", flask.request)
    return [{
        "id": 1
    }]


def grid_info(id) -> list:
    return []


def grid_measurements(id, quantity, lat, lon, start_time, end_time) -> list:
    quantity = str(quantity)
    start_time = dateutil.parser.parse(start_time)
    end_time = dateutil.parser.parse(end_time)
    lat = float(lat)
    lon = float(lon)
    fun = available_grids[id]
    # get the data directory from the configuration
    data_dir = flask.current_app.config["%s_DATA_DIR" % (id.upper(), )]
    records = fun(
        quantity=quantity,
        lat=lat,
        lon=lon,
        start_time=start_time,
        end_time=end_time,
        data_dir=data_dir
    )
    return records


def grids() -> list:
    return list(available_grids.keys())


def station_info(id) -> str:
    return 'do some magic!'


def station_measurements(id, quantity, startDate, endDate) -> str:
    return 'do some magic!'
