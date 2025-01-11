import win32evtlog
import re
# Lasīsim sistēmas log failu
log_tips = "System"  
# izmantosim regulāraās izteiksmes regex objektu, lai atrastu USB tekstā.
usb_pattern = re.compile(r'USB')
def read_windows_logs(log_tips, server=None):
    try:
        # mēģinam atvērt System log failu
        log_handle = win32evtlog.OpenEventLog(server, log_tips)
        print(f"Lasa {log_tips} logu...\n")
        # lasa ierakstus
        flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ
        events = []
        while True:
            records = win32evtlog.ReadEventLog(log_handle, flags, 0)
            if not records:
                break
            for event in records:
                # Pārliecinās, ka `StringInserts` nav None un ir string formāts
                if event.StringInserts:
                    # Apvieno visus elementus string formātā
                    event_message = " ".join(event.StringInserts)  
                    if usb_pattern.search(event_message):
                        events.append(event)
        
        # notikumu cikla izdruka
        if events:
            for event in events:
                print(f"Laiks: {event.TimeGenerated}")
                print(f"Serviss: {event.SourceName}")
                print(f"ID: {event.EventType}")
                print(f"Paziņojums: {event.StringInserts}")
                print("-" * 100)
        else:
            print("Pēc noteiktajiem kritērijiem, nav neviena LOG ieraksta!")
        
        # Aizveriet logu
        win32evtlog.CloseEventLog(log_handle)
    except Exception as e:
        print(f"Kļūda: {e}")

# Izsauciet funkciju, lai lasītu sistēmas logus
read_windows_logs(log_tips)