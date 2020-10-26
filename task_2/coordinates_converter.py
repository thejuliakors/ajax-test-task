def dd_to_ddm(dd):
    """
    Converts Decimal Degrees (DD) to Degrees Decimal Minutes (DDM)

    Parameters:
    dd -- Decimal Degrees (float)

    Returns:
    Degrees Decimal Minutes (str)
    """
    dd_abs = abs(dd)
    degrees = int(dd_abs // 1)
    minutes = (dd_abs - degrees) * 60.
    minutes_trailing = str((dd_abs - degrees)).split(".")[-1]
    minutes = round(minutes, 3) if len(minutes_trailing) > 3 else minutes
    minutes = round(minutes) if minutes.is_integer() else minutes
    ddm = f'{degrees}^{minutes}' 
    return ddm


def convert_latitude(dd):
    """
    Converts the latitude in DD to latitude in DDM

    Parameters:
    dd -- Latitude in Decimal Degrees (float)

    Returns:
    Latitude in Degrees Decimal Minutes (str)
    """
    if -90 <= dd <= 90:
        hemishere = 'S' if dd < 0 else 'N'
        return f"{dd_to_ddm(dd)}{hemishere}"
    else:
        raise ValueError("Latitude should be between -90 and 90")


def convert_longitude(dd):
    """
    Converts the longitude Decimal Degrees (DD) to Degrees Decimal Minutes (DDM)

    Parameters:
    dd -- Decimal Degrees (float)

    Returns:
    Longitude in Degrees Decimal Minutes (str)
    """
    if -180 <= dd <= 180:
        hemishere = 'W' if dd < 0 else 'E'
        return f"{dd_to_ddm(dd)}{hemishere}"
    else:
        raise ValueError("Longitude should be between -180 and 180")
