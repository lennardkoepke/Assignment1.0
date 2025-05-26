from sys import argv
import csv
import random


weeks = ['week1', 'week2', 'week3', 'week4', 'week5', 'week7'] + [f'week{i}' for i in range(8, 14)]

def read_csv(filename):
    try:
        with open(filename, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]
            return data, reader.fieldnames
    except FileNotFoundError:
        print(f" File not found: {filename}")
        exit(1)

def populate_scores(data):
    for row in data:
        for week in weeks:
            row[week] = str(random.choice([0, 1, 2, 3, '']))
    return data

def calculate_total(scores):
    best_10 = sorted(scores, reverse=True)[:10]
    total = sum(best_10)
    return min(total, 30)

def calculate_average(scores):
    return sum(scores) / len(scores) if scores else 0

def calculate_all(data):
    for row in data:
        scores = []
        for week in weeks:
            val = row.get(week, '').strip()
            try:
                score = float(val)
                scores.append(score)
            except ValueError:
                pass

        row['Total Points'] = f"{calculate_total(scores):.2f}"
        row['Average Points'] = f"{calculate_average(scores):.2f}"
    return data

def write_csv(filename, data, original_headers):
    extended_headers = original_headers.copy()
    for week in weeks:
        if week not in extended_headers:
            extended_headers.append(week)
    if 'Total Points' not in extended_headers:
        extended_headers.append('Total Points')
    if 'Average Points' not in extended_headers:
        extended_headers.append('Average Points')

    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=extended_headers)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

def print_analysis(data):
    stream_col = None
    for possible in ['Stream', 'Class', 'Group', 'Section']:
        if possible in data[0]:
            stream_col = possible
            break

    if stream_col:
        stream_data = {}
        for row in data:
            stream = row.get(stream_col, 'Unknown')
            total = float(row.get('Total Points', 0) or 0)
            stream_data.setdefault(stream, []).append(total)

        print("\n Average Total Points by Stream:")
        for stream, totals in stream_data.items():
            avg = sum(totals) / len(totals) if totals else 0
            print(f" - {stream}: {avg:.2f}")
    else:
        print("\n️ No stream column found (e.g., 'Stream', 'Class', 'Group').")

    print("\n Average Score per Week:")
    for week in weeks:
        scores = []
        for row in data:
            try:
                val = row.get(week, '').strip()
                if val:
                    scores.append(float(val))
            except ValueError:
                pass
        avg = sum(scores) / len(scores) if scores else 0
        print(f" - {week}: {avg:.2f}")

if __name__ == "__main__":
    if len(argv) < 2:
        print("Usage: python grade_calculator.py <input_csv_file>")
        exit(1)

    input_file = argv[1]
    output_file = "calculated_" + input_file.replace(" ", "_")

    print(f" Opening file: {input_file}")
    students, headers = read_csv(input_file)
    students = populate_scores(students)
    students = calculate_all(students)
    write_csv(output_file, students, headers)

    print(f"\n New file saved as: {output_file}")
    print_analysis(students)
