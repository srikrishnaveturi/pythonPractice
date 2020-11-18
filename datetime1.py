from datetime import datetime

now = datetime.now()

print("Now it is", now)

# time formatting

print("Now Time is", now.strftime('%d %B %Y %H:%M'))
