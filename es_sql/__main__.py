import json
import sys
import logging
import urllib.error
import sys

from . import es_query


def main():
    logging.basicConfig(level=logging.DEBUG)
    sql = sys.stdin.read()
    result_map = es_query.execute_sql(sys.argv[1], sql)
    print('=====')
    for result_name, rows in list(result_map.items()):
        for row in rows:
            print json.dumps(row)


if __name__ == "__main__":
    try:
        main()
    except urllib.error.HTTPError as e:
        print(e.read())
        sys.exit(1)

