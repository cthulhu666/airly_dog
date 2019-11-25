import datadog
import os

datadog.initialize(api_key=os.environ['DD_API_KEY'],
                   app_key=os.environ['DD_APP_KEY'])

stats = datadog.ThreadStats()
stats.start()


def send(measurement, installation_id):
    pm25 = next(x['value'] for x in measurement['values'] if x['name'] == 'PM25')
    pm10 = next(x['value'] for x in measurement['values'] if x['name'] == 'PM10')
    stats.gauge('air.airly.pm25', pm25, tags=[f"installationId:{installation_id}"])
    stats.gauge('air.airly.pm10', pm10, tags=[f"installationId:{installation_id}"])
