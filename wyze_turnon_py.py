
import os
import sys
from datetime import timedelta
from wyze_sdk import Client
from wyze_sdk.errors import WyzeApiError

client = Client(email='nischalkhadka11@gmail.com', password='Awesome1!!!!!')

try:
  plug = client.plugs.info(device_mac=sys.argv[1])



  client.plugs.turn_on(device_mac=plug.mac, device_model=plug.product.model)

  plug = client.plugs.info(device_mac=plug.mac)
  assert plug.is_on is True
except WyzeApiError as e:
    # You will get a WyzeApiError if the request failed
    print(f"Got an error: {e}")