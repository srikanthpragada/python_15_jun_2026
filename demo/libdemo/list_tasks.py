from datetime import datetime
f  = open("tasks.txt", "rt")

for line in f:
    parts = line.strip().split(',')
    if len(parts) < 2:
        continue

    task = parts[0].strip()
    try:
        start_date = datetime.strptime(parts[1].strip(),"%d-%m-%Y")
    except ValueError:
        continue

    if len(parts) > 2:
        try:
            end_date = datetime.strptime(parts[2].strip(),"%d-%m-%Y")
            days = (end_date - start_date).days
        except ValueError:
            continue
    else:
        days = "Incomplete"

    print(f"{task:40}  {start_date.strftime('%d-%m-%Y')}  {days}")
