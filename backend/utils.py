import gspread
from datetime import datetime

def get_sheet():
    gc = gspread.service_account(filename="service_account.json")
    return gc.open("QueueDuanDB").sheet1

def is_duplicate(user_id, dt):
    sheet = get_sheet()
    values = sheet.get_all_records()
    return any(v["userId"] == user_id and v["datetime"] == dt for v in values)

def append_booking(user_id, dt, service):
    sheet = get_sheet()
    sheet.append_row([datetime.now().isoformat(), user_id, dt, service])

def delete_booking(user_id, dt):
    sheet = get_sheet()
    records = sheet.get_all_records()
    for i, row in enumerate(records):
        if row["userId"] == user_id and row["datetime"] == dt:
            sheet.delete_rows(i + 2)  # +2 = header + 1-indexed
            return True
    return False

def get_summary_text():
    sheet = get_sheet()
    rows = sheet.get_all_records()
    today = datetime.now().date().isoformat()
    today_rows = [r for r in rows if r["datetime"].startswith(today)]
    return f"📅 คิววันนี้ ({today}) มีทั้งหมด {len(today_rows)} รายการ"
