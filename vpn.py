import os
import random
loc=['US','CA','AT','BE','BG','HR','CY','CZ','DK','EE','FI','FR','DE','GR','HU','IS','IE','IL','LT','LV','NL'
,'IT','LV','LT','MD','NL','NO','PL','RO','SK','ES','SE','CH','TN','GB','IN','RU','ZA','AU','HK','ID','JP',
'MY','PH','KR','TH','BR','AR','MX','PE']
loc=loc[random.randint(0,len(loc)-1)]
os.system("windscribe connect "+'US')
os.system("windscribe status")