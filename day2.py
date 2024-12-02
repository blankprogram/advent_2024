def safe(report):
    increasing = True
    decreasing = True

    for i in range(len(report) - 1):
        diff = report[i + 1] - report[i]

        if not (1 <= abs(diff) <= 3):
            return False

        if diff > 0:
            decreasing = False
        elif diff < 0:
            increasing = False

    return increasing or decreasing



safe_count = 0

with open('day2in.txt', 'r') as file:
    for line in file:
        report = list(map(int, line.split()))

        if safe(report):
            safe_count += 1
            continue

        for i in range(len(report)):
            modified_report = report[:i] + report[i+1:]
            if safe(modified_report):
                safe_count += 1
                break

print("safe:", safe_count)
