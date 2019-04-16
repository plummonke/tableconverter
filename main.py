import csv
import io
import re
import time

import formatter

def main():
    regexes = {
        "USDA": re.compile("USDA# (\d{4})"),
        "DOD": re.compile("AC-(\d{4})"),
        "state": re.compile("for the [\w\s]+?, (\w+)"),
        "date": re.compile("Effective Date: ([\w ]+)"),
        "grade": re.compile("(?=.*\d{1,3}\.\d{2}(?:[]\s\*]+)\d{1,3}\.\d{2})^.+?(?:WS-)?(\d{1,2})"),
        "rates": re.compile("(?:\s+?\d{1,2})? ?\*?([\d\.]+)\s+?\*?([\d\.]+)\s+?\*?([\d\.]+)\s+?\*?([\d\.]+)\s+?\*?([\d\.]+)\s+?")
    }

    plan_grades = {
        "WG": {
            1: {
                1: 0,
                2: 0,
                3: 0,
                4: 0,
                5: 0,
            },
            2: {
                1: 0,
                2: 0,
                3: 0,
                4: 0,
                5: 0,
            },
            3: {
                1: 0,
                2: 0,
                3: 0,
                4: 0,
                5: 0,
            },
            4: {
                1: 0,
                2: 0,
                3: 0,
                4: 0,
                5: 0,
            },
            5: {
                1: 0,
                2: 0,
                3: 0,
                4: 0,
                5: 0,
            },
            6: {
                1: 0,
                2: 0,
                3: 0,
                4: 0,
                5: 0,
            },
            7: {
                1: 0,
                2: 0,
                3: 0,
                4: 0,
                5: 0,
            },
            8: {
                1: 0,
                2: 0,
                3: 0,
                4: 0,
                5: 0,
            },
            9: {
                1: 0,
                2: 0,
                3: 0,
                4: 0,
                5: 0,
            },
            10: {
                1: 0,
                2: 0,
                3: 0,
                4: 0,
                5: 0,
            },
            11: {
                1: 0,
                2: 0,
                3: 0,
                4: 0,
                5: 0,
            },
            12: {
                1: 0,
                2: 0,
                3: 0,
                4: 0,
                5: 0,
            },
            13: {
                1: 0,
                2: 0,
                3: 0,
                4: 0,
                5: 0,
            },
            14: {
                1: 0,
                2: 0,
                3: 0,
                4: 0,
                5: 0,
            },
            15: {
                1: 0,
                2: 0,
                3: 0,
                4: 0,
                5: 0,
            },
        },
        "WL": {
            1: {
                1: 0,
                2: 0,
                3: 0,
                4: 0,
                5: 0,
            },
            2: {
                1: 0,
                2: 0,
                3: 0,
                4: 0,
                5: 0,
            },
            3: {
                1: 0,
                2: 0,
                3: 0,
                4: 0,
                5: 0,
            },
            4: {
                1: 0,
                2: 0,
                3: 0,
                4: 0,
                5: 0,
            },
            5: {
                1: 0,
                2: 0,
                3: 0,
                4: 0,
                5: 0,
            },
            6: {
                1: 0,
                2: 0,
                3: 0,
                4: 0,
                5: 0,
            },
            7: {
                1: 0,
                2: 0,
                3: 0,
                4: 0,
                5: 0,
            },
            8: {
                1: 0,
                2: 0,
                3: 0,
                4: 0,
                5: 0,
            },
            9: {
                1: 0,
                2: 0,
                3: 0,
                4: 0,
                5: 0,
            },
            10: {
                1: 0,
                2: 0,
                3: 0,
                4: 0,
                5: 0,
            },
            11: {
                1: 0,
                2: 0,
                3: 0,
                4: 0,
                5: 0,
            },
            12: {
                1: 0,
                2: 0,
                3: 0,
                4: 0,
                5: 0,
            },
            13: {
                1: 0,
                2: 0,
                3: 0,
                4: 0,
                5: 0,
            },
            14: {
                1: 0,
                2: 0,
                3: 0,
                4: 0,
                5: 0,
            },
            15: {
                1: 0,
                2: 0,
                3: 0,
                4: 0,
                5: 0,
            },
        },
        "WS": {
            1: {
                1: 0,
                2: 0,
                3: 0,
                4: 0,
                5: 0,
            },
            2: {
                1: 0,
                2: 0,
                3: 0,
                4: 0,
                5: 0,
            },
            3: {
                1: 0,
                2: 0,
                3: 0,
                4: 0,
                5: 0,
            },
            4: {
                1: 0,
                2: 0,
                3: 0,
                4: 0,
                5: 0,
            },
            5: {
                1: 0,
                2: 0,
                3: 0,
                4: 0,
                5: 0,
            },
            6: {
                1: 0,
                2: 0,
                3: 0,
                4: 0,
                5: 0,
            },
            7: {
                1: 0,
                2: 0,
                3: 0,
                4: 0,
                5: 0,
            },
            8: {
                1: 0,
                2: 0,
                3: 0,
                4: 0,
                5: 0,
            },
            9: {
                1: 0,
                2: 0,
                3: 0,
                4: 0,
                5: 0,
            },
            10: {
                1: 0,
                2: 0,
                3: 0,
                4: 0,
                5: 0,
            },
            11: {
                1: 0,
                2: 0,
                3: 0,
                4: 0,
                5: 0,
            },
            12: {
                1: 0,
                2: 0,
                3: 0,
                4: 0,
                5: 0,
            },
            13: {
                1: 0,
                2: 0,
                3: 0,
                4: 0,
                5: 0,
            },
            14: {
                1: 0,
                2: 0,
                3: 0,
                4: 0,
                5: 0,
            },
            15: {
                1: 0,
                2: 0,
                3: 0,
                4: 0,
                5: 0,
            },
            16: {
                1: 0,
                2: 0,
                3: 0,
                4: 0,
                5: 0,
            },
            17: {
                1: 0,
                2: 0,
                3: 0,
                4: 0,
                5: 0,
            },
            18: {
                1: 0,
                2: 0,
                3: 0,
                4: 0,
                5: 0,
            },
            19: {
                1: 0,
                2: 0,
                3: 0,
                4: 0,
                5: 0,
            },
        }
    }

    with io.open(input("What is the output filepath?"), "a+", newline="\n") as out:
        csv_writer = csv.writer(out)

        table_formatter = formatter.TableFormatter(
            plan_grades,
            csv_writer,
            **regexes
        )

        while True:
            with io.open(input("What is the file path for the current table?"), mode="r") as file:
                table_formatter.Run(file.readlines())
                print("Done")
                x = input("Do you want to format another table?").lower()

            if x in ("no", "n", "q", "quit"):
                break

    print("Goodbye.")
    time.sleep(5)

main()
