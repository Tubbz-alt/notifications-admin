from collections import OrderedDict

from flask import render_template

from app import service_api_client
from app.main import main
from app.utils import Spreadsheet, user_has_permissions


@main.route("/services/<uuid:service_id>/returned-letter-summary", methods=["GET"])
@user_has_permissions('view_activity')
def returned_letter_summary(service_id):
    summary = service_api_client.get_returned_letter_summary(service_id)
    return render_template(
        'views/returned-letter-summary.html',
        data=summary,
    )


@main.route("/services/<uuid:service_id>/returned-letters-csv/<reported_at>", methods=["GET"])
@user_has_permissions('view_activity')
def returned_letters_report(service_id, reported_at):
    returned_letters = service_api_client.get_returned_letters(service_id, reported_at)
    column_names = OrderedDict([
        ('notification_id', 'Notification ID'),
        ('client_reference', 'Reference'),
        ('created_at', 'Date sent'),
        ('email_address', 'Sent by'),
        ('template_name', 'Template name'),
        ('template_id', 'Template ID'),
        ('template_version', 'Template version'),
        ('original_file_name', 'Spreadsheet file name'),
        ('job_row_number', 'Spreadsheet row number'),
        ('uploaded_letter_file_name', 'Uploaded letter file name')
    ])

    # initialise with header row
    data = [[x for x in column_names.values()]]

    for row in returned_letters:
        data.append([row[key] for key in column_names.keys()])

    return Spreadsheet.from_rows(data).as_csv_data, 200, {
        'Content-Type': 'text/csv; charset=utf-8',
        'Content-Disposition': 'inline; filename="{} returned letters.csv"'.format(reported_at)
    }
