import os.path
import csv
import json
from datetime import datetime
from itertools import accumulate

from django.http import HttpResponse
from django.shortcuts import render

from test_task.settings import BASE_DIR
from .utils import get_pubs, check_input


def get_csv(request):
    start = request.GET.get('start', 1965)
    end = request.GET.get('end', datetime.today().year)

    try:
        start, end = check_input(start, end)
    except ValueError as err:
        return HttpResponse(str(err))

    output_file = os.path.join(BASE_DIR, 'result.csv')
    with open(output_file, 'w') as file:
        writer = csv.writer(file)
        writer.writerow(['Год'] + ['Неделя ' + str(week) for week in accumulate([1] * 53)])
        pubs = get_pubs(start, end)
        writer.writerows([[year] + pubs[year] for year in pubs])
    data = open(output_file, 'r').read()
    print(data)
    resp = HttpResponse(data, content_type='text/csv')
    resp['Content-Disposition'] = 'attachment;filename=result.csv'
    return resp


def get_json(request):
    start = request.GET.get('start', 1965)
    end = request.GET.get('end', datetime.today().year)

    try:
        start, end = check_input(start, end)
    except ValueError as err:
        return HttpResponse(str(err))

    return HttpResponse(json.dumps(get_pubs(start, end)))

