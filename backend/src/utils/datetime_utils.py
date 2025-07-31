from dateutil import parser


def format_iso_datetime(iso_str: str) -> str:
    """
    Converts an ISO 8601 datetime string to the format "HH:MM:SS DD.MM.YYYY".

    Args:
        iso_str (str): The ISO 8601 datetime string to format.

    Returns:
        str: The formatted datetime string in "hour:minute:second day.month.year" format.
    """
    dt = parser.isoparse(iso_str)
    return dt.strftime("%H:%M:%S %d.%m.%Y")
