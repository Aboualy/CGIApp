import sys
import grequests
import requests
from time import ctime
import csv
import os.path
from PyQt5.QtWidgets import QApplication
import ui_urls

headers = ["URL", "Check_time", "Response_time",
           "Response_status_code", "Response_headers"
           ]


def create_csv_file(data=None):
    if data is None:
        data = headers
    data = headers
    if not os.path.exists("output.csv"):
        with open('output.csv', 'w', newline='') as outcsv:
            writer = csv.writer(outcsv)
            writer.writerow(data)


def update_csv_file(obj):
    with open('output.csv', "a") as f:
        writer = csv.writer(f)
        for row in obj:
            writer.writerow(row)


def parse_urls(urls):

    rs = (grequests.get(u) for u in urls)
    r = grequests.map(rs)
    data = []
    for j, resp in enumerate(r):
        if resp is None:
            current_time = ctime()
            data.append((urls[j], current_time, "fetch data faileda", "fetch data failed"
                         , "fetch data failed"
                         ))
            continue
        # current_time = time.strftime("%Y%m%d")
        current_time = ctime()
        data.append((urls[j], current_time, resp.elapsed.total_seconds(), resp.status_code
                     , resp.headers
                     ))
    return data


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ui_urls.UiURLS()
    ui_urls.UiURLS()
    sys.exit(app.exec_())
