from exercise_1_solution import ACCEPT, DECLINE, data_sample, get_non_matching_entries, logger


def test_filter_not_matching_accept():
    results_list = get_non_matching_entries(data_sample, "Result", ACCEPT)
    logger.info("Entries which do not match filter for Result Accept are: %s", results_list)


def test_filter_not_matching_decline():
    results_list = get_non_matching_entries(data_sample, "Result", DECLINE)
    logger.info("Entries which do not match filter for Result Decline are: %s", results_list)


def test_filter_not_matching_non_existing_key():
    results_list = get_non_matching_entries(data_sample, "WRONG_KEY", ACCEPT)
    logger.info("Checking no entries are return for non existing key filter: %s", results_list)


def test_filter_not_matching_non_existing_value():
    results_list = get_non_matching_entries(data_sample, "Result", "NONE")
    logger.debug("Checking no entries are return for non existing value filter: %s", results_list)
