#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: nandu
contact @ nandu.eng@gmail.com
"""


fileinput = str(input("Write typhoon name: "))
fileinput1 = str(input("Provide csv file name: "))
if not ".csv" in fileinput1:
  fileinput1 += ".csv"

import pandas as pd

rsmc = pd.read_csv(fileinput1, header=None)

yy = []
mm = []
dd = []
hh = []
for dt in range(len(rsmc)):
    yy.append(int(str(rsmc[0][dt])[:2]))
    mm.append(int(str(rsmc[0][dt])[2:4]))
    dd.append(int(str(rsmc[0][dt])[4:6]))
    hh.append(int(str(rsmc[0][dt])[6:8]))

year = 20
yyyy = [int(str(year)+str(yy[yd])) for yd in range(len(yy))]
hhhh = [str(int(hh[yd])) + ":00" for yd in range(len(hh))]

date = ['{}/{}/{}'.format(mm[dt],dd[dt],yyyy[dt]) for dt in range(len(yyyy))]
ddhh = ['{} {}'.format(date[dh], hhhh[dh]) for dh in range(len(date))]

lat = rsmc[3]*0.1
lon = rsmc[4]*0.1
lat_rev = [float(f'{lat[ltt]:.2f}') for ltt in range(len(lat))]
lon_rev = [float(f'{lon[0]:.2f}') for lot in range(len(lon))]
press = rsmc[5]
ws = rsmc[6]

typ_var = list(zip(ddhh, lat_rev, lon_rev, press, ws))
df = pd.DataFrame(typ_var, columns=['date', 'latitude', 'longitude', 'pressure', 'wind(kt)'])

df.to_csv(f'{fileinput}_RSMC_tokyo_track.csv', index=False)




