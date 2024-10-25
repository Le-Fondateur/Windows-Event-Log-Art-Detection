import win32evtlog
import pandas as pd
import os

def collect_security_events(output_path):
    server = 'localhost'  # Local machine
    logtype = 'Security'  # Security event logs
    handle = win32evtlog.OpenEventLog(server, logtype)

    flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ
    total = win32evtlog.GetNumberOfEventLogRecords(handle)

    events = []

    try:
        while True:
            records = win32evtlog.ReadEventLog(handle, flags, 0)
            if not records:
                break
            for event in records:
                events.append({
                    "EventID": event.EventID,
                    "SourceName": event.SourceName,
                    "TimeGenerated": event.TimeGenerated.strftime("%Y-%m-%d %H:%M:%S"),
                    "EventCategory": event.EventCategory,
                    "EventType": event.EventType,
                    "StringInserts": event.StringInserts
                })
    except Exception as e:
        print(f"Error while reading event log: {e}")

    # Convert the list of events to a DataFrame and save it as a CSV file
    df = pd.DataFrame(events)
    df.to_csv(output_path, index=False)
    print(f"Logs collected and saved to {output_path}")

if __name__ == "__main__":
    # Ensure the directory exists
    output_directory = "../event_log_collector"
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    output_path = os.path.join(output_directory, "security_logs.csv")
    collect_security_events(output_path)
