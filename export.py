from flask import Blueprint, Response
from utils import get_sheet

import csv
import io

export_bp = Blueprint("export", __name__)

@export_bp.route("/csv", methods=["GET"])
def export_csv():
    sheet = get_sheet()
    data = sheet.get_all_values()

    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerows(data)

    response = Response(output.getvalue(), mimetype='text/csv')
    response.headers["Content-Disposition"] = "attachment; filename=queue_export.csv"
    return response
