import json
import os
import time

import requests

import dog


api_key = os.environ['AIRLY_API_KEY']
installation_id = os.environ['AIRLY_INSTALLATION_ID']

outputs = [
    dog.send,
]


def get_measurement():
    rs = requests.get(f"https://airapi.airly.eu/v2/measurements/installation?installationId={installation_id}",
                      headers={'apikey': api_key})
    if rs.status_code != 200:
        raise RuntimeError(f"Http error, status: {rs.status_code}")
    data = json.loads(rs.content)['current']
    return data


def process():
    measurement = get_measurement()
    print(measurement)

    for out in outputs:
        try:
            out(measurement, installation_id)
        except RuntimeError as e:
            print(e)


while True:
    try:
        process()
    except (RuntimeError, IOError) as e:
        print(e)

    time.sleep(60*15)
