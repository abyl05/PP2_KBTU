from datetime import datetime

date1 = datetime(2024, 1, 1, 12, 0, 0)
date2 = datetime(2024, 1, 2, 14, 30, 0)

difference = date2 - date1
seconds = difference.total_seconds()

print("Difference in seconds:", seconds)