from exercise_1_solution import ACCEPT, DECLINE, data_sample, get_matching_entries, logger


def test_filter_matching_accept():
    results_list = get_matching_entries(data_sample, "Result", ACCEPT)
    logger.info("Matching entries for Result Accept are: %s", results_list)


def test_filter_matching_decline():
    results_list = get_matching_entries(data_sample, "Result", DECLINE)
    logger.info("Matching entries for Result Decline are: %s", results_list)


def test_filter_matching_non_existing_key():
    results_list = get_matching_entries(data_sample, "None", "ABC")
    logger.info("Matching entries for non existing key: %s", results_list)


def filter_matching_non_existing_value():
    results_list = get_matching_entries(data_sample, "Result", "ABC")
    logger.info("Matching entries for non existing value filter: %s", results_list)
