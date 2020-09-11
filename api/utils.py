import time
from datetime import datetime

from .models import Document


def get_pubs_count(start, end):
    return Document.objects.raw("SELECT id, CAST(STRFTIME('%%Y', cover_date) AS INTEGER) AS year, "
                                "CAST(strftime('%%j', cover_date) AS INTEGER) / 7 AS week, "
                                "COUNT(*) as count "
                                "FROM api_document "
                                "WHERE year >= %s AND year <= %s "
                                "GROUP BY year, week ", [start, end])


def get_pubs(start, end):
    time_start = time.time()
    pubs = get_pubs_count(start, end)
    time_mid = time.time()
    weeks_per_year = 53
    result = {}
    # for year in range(start, end + 1):
    #     result[year] = [0] * weeks_per_year
    result = {year: [0] * weeks_per_year for year in range(start, end + 1)}
    for pub in pubs:
        result[pub.year][pub.week] = pub.count
    total = 0
    for year, weeks in result.items():
        for week, count in enumerate(weeks):
            total += count
            result[year][week] = total
    time_end = time.time()
    print(time_mid - time_start)
    print(time_end - time_mid)
    print(time_end - time_start)
    return result


def check_input(start, end):
    try:
        start = int(start)
        end = int(end)
    except ValueError:
        raise ValueError('Wrong year.')
    if start < 1900 or end < 1900:
        raise ValueError('Wrong year.')
    if start > end:
        raise ValueError('Wrong range.')
    return start, end
