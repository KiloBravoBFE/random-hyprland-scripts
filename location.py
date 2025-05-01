#!/usr/bin/env python

from __future__ import print_function
import Geoclue
from datetime import datetime

print("Geoclue version %s" % Geoclue.VERSION)

dl = Geoclue.DiscoverLocation()
dl.init()
providers = dl.get_available_providers()

for provider in providers:
  pname = provider['name']
  dl.set_position_provider(pname)
  position = dl.get_location_info()

  print("\n%s\n%s" % (pname, "-"*len(pname)))
  for k, v in position.items():
    if k.endswith('_timestamp'):
      v = datetime.fromtimestamp(v)
    print("%-25s%s" % (k+':',v))

