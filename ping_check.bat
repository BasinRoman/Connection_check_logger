ping -t 192.168.65.21 | cmd /q /v /c "(pause&pause)>nul & for /l %a in () do (set /p "data=" && echo(!date! !time! !data!)&ping -n 2 192.168.65.21>nul" > C:\Users\Administrator\Desktop\log.txt
