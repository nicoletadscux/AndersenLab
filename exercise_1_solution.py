"""
Exercise: Python Coding

Objective:
Define functions that can apply a filter to supplied data

Notes:
Candidate can rename functions, create new ones as much as they want.
Candidate can import additional packages/modules if need be.
Candidate can change function definition if required.
"""

import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()

ACCEPT = "Accept"
DECLINE = "Decline"
REFER = "Refer"
EXPERIAN = "Experian"
TRANSUNION = "Transunion"
EQUIFAX = "Equifax"

data_sample: list = [
    {
        "Key": "A001",
        "Result": ACCEPT,
        "Service": EQUIFAX
    },
    {
        "Key": "A002",
        "Result": DECLINE,
        "Service": EQUIFAX
    },
    {
        "Key": "A003",
        "Result": ACCEPT,
        "Service": EQUIFAX
    },
    {
        "Key": "A004",
        "Result": REFER,
        "Service": EQUIFAX
    },
    {
        "Key": "A005",
        "Result": REFER,
        "Service": EQUIFAX
    },
    {
        "Key": "A006",
        "Result": DECLINE,
        "Service": EQUIFAX
    }
]


def get_matching_entries(data: list, filter_key: str, filter_value: str) -> list:
    """Function that applies a filter for the data entries.

    Returns all items that match the filter
    :param data: A list of dictionary values
    :type data: list
    :param filter_key: The matching key
    :type filter_key: string
    :returns filter_value: The matching filter
    :type filter_value: string
    """
    logger.info("Return all matching data for filter key: '%s' and filter value: '%s'", filter_key, filter_value)
    return [d for d in data if filter_key in d and d[filter_key] == filter_value]


def get_non_matching_entries(data: list, filter_key: str, filter_value: str) -> list:
    """Function that applies a filter for the data entries.

    Returns all items that do not match the filter
    :param data: A list of dictionary values
    :type data: list
    :param filter_key: The matching key
    :type filter_key: string
    :returns filter_value: The matching filter
    :type filter_value: string
    """
    logger.info("Return all non-matching data for filter key: '%s' and filter value: '%s'.", filter_key, filter_value)
    return [d for d in data if filter_key in d and d[filter_key] != filter_value]
