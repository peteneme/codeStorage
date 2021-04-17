REM TEST CLI, NO CSV FILE
call python srvlookup.py --serial=sn1006

REM REM TEST CLI, EXISTENT SERIAL, CSV FILE INSERTED
call python srvlookup.py --csvfile=newservers.csv --serial=sn1006

REM TEST CLI, NON EXISTENT SERIAL
call python srvlookup.py --csvfile=newservers.csv --serial=sn100X || echo %ERRORLEVEL%

REM TEST CLI , ERRORNESS SERIAL
call python srvlookup.py --serial=sn1027 || echo %ERRORLEVEL%

REM TEST REST 
START /B call python srvlookup.py --csvfile=newservers.csv --rest

REM TEST REST, EXISTENT SERIAL 
call curl get http://127.0.0.1:8888/server/sn1006

REM REST, NON EXISTENT SERIAL
call curl get http://127.0.0.1:8888/server/sn100X

REM TEST CLI , ERRORNESS SERIAL
call curl get http://127.0.0.1:8888/server/sn1027