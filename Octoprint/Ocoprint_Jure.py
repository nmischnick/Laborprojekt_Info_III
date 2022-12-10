import json

json1 ='{"job":{"averagePrintTime":null,"estimatedPrintTime":null,"filament":null,"file":{"date":null,"display":"22167_Prusa_schwarz_0.3mm_PETG_MK3S_12h21m.gcode","name":"22167_Prusa_schwarz_0.3mm_PETG_MK3S_12h21m.gcode","origin":"sdcard","path":"22167_Prusa_schwarz_0.3mm_PETG_MK3S_12h21m.gcode","size":25178087},"lastPrintTime":null,"user":null},"progress":{"completion":33.51554865943548,"filepos":8438574,"printTime":15656,"printTimeLeft":31058,"printTimeLeftOrigin":"estimate"},"state":"Printing from SD"}'

json2= '{"error":"Too many consecutive timeouts, printer still connected and alive?","job":{"averagePrintTime":null,"estimatedPrintTime":null,"filament":null,"file":{"date":null,"display":null,"name":null,"origin":null,"path":null,"size":null},"lastPrintTime":null,"user":null},"progress":{"completion":null,"filepos":null,"printTime":null,"printTimeLeft":null,"printTimeLeftOrigin":null},"state":"Offline after error"}'
json3='{"files":[{"date":1655993823,"display":"Form-Kubus_0.2mm_PETG_MK3S_25m.gcode","gcodeAnalysis":{"dimensions":{"depth":104.754,"height":18.0,"width":101.754},"estimatedPrintTime":1415.1325518024532,"filament":{"tool0":{"length":1013.5587899999985,"volume":2.4378945872441}},"printingArea":{"maxX":101.754,"maxY":101.754,"maxZ":18.0,"minX":0.0,"minY":-3.0,"minZ":0.0}},"hash":"732bc17d3771299b1c86272d75e6fb1522f3bcd5","name":"Form-Kubus_0.2mm_PETG_MK3S_25m.gcode","origin":"local","path":"Form-Kubus_0.2mm_PETG_MK3S_25m.gcode","prints":{"failure":3,"last":{"date":1656241873.8742633,"success":false},"success":0},"refs":{"download":"http://141.41.42.192/downloads/files/local/Form-Kubus_0.2mm_PETG_MK3S_25m.gcode","resource":"http://141.41.42.192/api/files/local/Form-Kubus_0.2mm_PETG_MK3S_25m.gcode"},"size":498343,"statistics":{"averagePrintTime":{},"lastPrintTime":{}},"type":"machinecode","typePath":["machinecode","gcode"]},{"date":1655993549,"display":"y-belt-holder.gcode","gcodeAnalysis":{"dimensions":{"depth":29.25,"height":50.15,"width":41.0},"estimatedPrintTime":2695.4625377683983,"filament":{"tool0":{"length":4090.5442799998177,"volume":9.838912017223869}},"printingArea":{"maxX":120.5,"maxY":114.625,"maxZ":50.15,"minX":79.5,"minY":85.375,"minZ":0.0}},"hash":"9b6fb0eda020b99f5b689f14f0ec708aec8eccc6","name":"y-belt-holder.gcode","origin":"local","path":"y-belt-holder.gcode","prints":{"failure":1,"last":{"date":1655993626.970713,"success":false},"success":0},"refs":{"download":"http://141.41.42.192/downloads/files/local/y-belt-holder.gcode","resource":"http://141.41.42.192/api/files/local/y-belt-holder.gcode"},"size":969994,"statistics":{"averagePrintTime":{},"lastPrintTime":{}},"type":"machinecode","typePath":["machinecode","gcode"]},{"date":1644409213,"display":"3DBenchy_0.2mm_PETG_MK3S_1h31m.gcode","gcodeAnalysis":{"dimensions":{"depth":123.277,"height":48.0,"width":154.775},"estimatedPrintTime":3845.404587432485,"filament":{"tool0":{"length":4224.181309999737,"volume":10.160346743365588}},"printingArea":{"maxX":154.775,"maxY":120.277,"maxZ":48.0,"minX":0.0,"minY":-3.0,"minZ":0.0}},"hash":"0f608d71d0fe68f235044fe60fe0457f2e36eaa3","name":"3DBenchy_0.2mm_PETG_MK3S_1h31m.gcode","origin":"local","path":"3DBenchy_0.2mm_PETG_MK3S_1h31m.gcode","prints":{"failure":4,"last":{"date":1644421479.9018548,"success":false},"success":1},"refs":{"download":"http://141.41.42.192/downloads/files/local/3DBenchy_0.2mm_PETG_MK3S_1h31m.gcode","resource":"http://141.41.42.192/api/files/local/3DBenchy_0.2mm_PETG_MK3S_1h31m.gcode"},"size":3715604,"statistics":{"averagePrintTime":{"_default":5489.024685741999},"lastPrintTime":{"_default":5489.024685741999}},"type":"machinecode","typePath":["machinecode","gcode"]},{"date":1648568095,"display":"Test_0.2mm_PC_MK3S_44m.gcode","gcodeAnalysis":{"dimensions":{"depth":122.175,"height":22.0,"width":100.0},"estimatedPrintTime":2201.81331360901,"filament":{"tool0":{"length":1448.172510000022,"volume":3.483263090762363}},"printingArea":{"maxX":100.0,"maxY":119.175,"maxZ":22.0,"minX":0.0,"minY":-3.0,"minZ":0.0}},"hash":"8a45e9ad75c366b4b842e92b47ec8c2b34417f19","name":"Test_0.2mm_PC_MK3S_44m.gcode","origin":"local","path":"Test_0.2mm_PC_MK3S_44m.gcode","prints":{"failure":0,"last":{"date":1648570932.2885377,"printTime":2755.1466712969996,"success":true},"success":1},"refs":{"download":"http://141.41.42.192/downloads/files/local/Test_0.2mm_PC_MK3S_44m.gcode","resource":"http://141.41.42.192/api/files/local/Test_0.2mm_PC_MK3S_44m.gcode"},"size":1157348,"statistics":{"averagePrintTime":{"_default":2755.1466712969996},"lastPrintTime":{"_default":2755.1466712969996}},"type":"machinecode","typePath":["machinecode","gcode"]},{"date":1648737080,"display":"Grundtray_01_03-massiv_0.2mm_PC_MK3S_10h54m.gcode","gcodeAnalysis":{"dimensions":{"depth":212.775,"height":10.0,"width":237.377},"estimatedPrintTime":37148.25112485196,"filament":{"tool0":{"length":80500.73084997771,"volume":193.62694887028218}},"printingArea":{"maxX":237.377,"maxY":209.775,"maxZ":10.0,"minX":0.0,"minY":-3.0,"minZ":0.0}},"hash":"917e7a8286ed29fa78cbedba7aec5e82c8f79f47","name":"Grundtray_01_03-massiv_0.2mm_PC_MK3S_10h54m.gcode","origin":"local","path":"Grundtray_01_03-massiv_0.2mm_PC_MK3S_10h54m.gcode","prints":{"failure":1,"last":{"date":1648799918.512495,"success":false},"success":0},"refs":{"download":"http://141.41.42.192/downloads/files/local/Grundtray_01_03-massiv_0.2mm_PC_MK3S_10h54m.gcode","resource":"http://141.41.42.192/api/files/local/Grundtray_01_03-massiv_0.2mm_PC_MK3S_10h54m.gcode"},"size":2035551,"statistics":{"averagePrintTime":{},"lastPrintTime":{}},"type":"machinecode","typePath":["machinecode","gcode"]},{"date":1648706256,"display":"Halterung_01_03_0.2mm_PC_MK3S_5h8m.gcode","gcodeAnalysis":{"dimensions":{"depth":131.777,"height":76.4,"width":234.139},"estimatedPrintTime":12033.400206730463,"filament":{"tool0":{"length":13448.894939993323,"volume":32.34838324338772}},"printingArea":{"maxX":234.139,"maxY":128.777,"maxZ":76.4,"minX":0.0,"minY":-3.0,"minZ":0.0}},"hash":"7dcb3ca638aa0f4b27a8a068989add38eb5f3115","name":"Halterung_01_03_0.2mm_PC_MK3S_5h8m.gcode","origin":"local","path":"Halterung_01_03_0.2mm_PC_MK3S_5h8m.gcode","prints":{"failure":0,"last":{"date":1648726286.5610464,"printTime":18088.606299157982,"success":true},"success":1},"refs":{"download":"http://141.41.42.192/downloads/files/local/Halterung_01_03_0.2mm_PC_MK3S_5h8m.gcode","resource":"http://141.41.42.192/api/files/local/Halterung_01_03_0.2mm_PC_MK3S_5h8m.gcode"},"size":8652303,"statistics":{"averagePrintTime":{"_default":18088.606299157982},"lastPrintTime":{"_default":18088.606299157982}},"type":"machinecode","typePath":["machinecode","gcode"]}],"free":27833323520,"total":31119536128}'

def json_into_dic(json_str):
    y = json.loads(json_str)
    job= y["job"]
    file = job["file"]
    state = y["state"]
    progress = y["progress"]
    averagePrintTime = job['averagePrintTime']
    lastPrintTime = job['lastPrintTime']
    date=file['date']
    display = file['display']
    state = state
    completion = progress['completion']
    printTime = progress['printTime']
    werte = {'date':date,'state':state,'averagePrintTime':averagePrintTime,'lastPrintTime':lastPrintTime,'display':display,'completion':completion,'printTime':printTime}

    return werte

def json_server_dateien(json_str,i):
    y = json.loads(json_str)
    files = y['files']
    free = y['free']
    total = y['total']
    file = files[i]
    date = file['date']
    display = file['display']
    tool0 = file['gcodeAnalysis']['filament']['tool0']
    volume = file['gcodeAnalysis']['filament']['tool0']['volume']
    averagePrintTime = file['statistics']['averagePrintTime']
    hash = file['hash']
    download = file['refs']['download']
    werte = {'date':date,'display':display,'tool0':tool0,'volume':volume,'averagePrintTime':averagePrintTime,'hash':hash,'download':download,'free':free,'total':total}
    return werte


liste1 = json_into_dic(json1)
liste2 = json_into_dic(json2)
i = 0
list = json_server_dateien(json3,i)
i = i+1
list1 = json_server_dateien(json3,i)
i = i+1
list3 = json_server_dateien(json3,i)
i = i+1
list4 = json_server_dateien(json3,i)
i = i+1
list5 = json_server_dateien(json3,i)
i = i+1
list6 = json_server_dateien(json3,i)
