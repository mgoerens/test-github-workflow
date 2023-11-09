import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument(
    "-a",
    "--chart-entry",
    dest="chart_entry",
    type=json.loads,
    required=True,
    help="Index entry to add",
)

args = parser.parse_args()

print(args)
print(args.chart_entry)
print(args.chart_entry["coucou"])
