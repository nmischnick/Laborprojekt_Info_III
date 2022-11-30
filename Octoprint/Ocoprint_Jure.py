import pandas as pd

json_str = '{"job":{"averagePrintTime":null,"estimatedPrintTime":null,"filament":null,"file":{"date":null,"display":"22167_Prusa_schwarz_0.3mm_PETG_MK3S_12h21m.gcode","name":"22167_Prusa_schwarz_0.3mm_PETG_MK3S_12h21m.gcode","origin":"sdcard","path":"22167_Prusa_schwarz_0.3mm_PETG_MK3S_12h21m.gcode","size":25178087},"lastPrintTime":null,"user":null},"progress":{"completion":33.51554865943548,"filepos":8438574,"printTime":15656,"printTimeLeft":31058,"printTimeLeftOrigin":"estimate"},"state":"Printing from SD"}'
df = pd.read_json(json_str, orient='records')
#df.drop('job', inplace=True, axis=1)
#df.drop('progress', inplace=True, axis=1)
#df.drop('state', inplace=True, axis=1)
print(df)