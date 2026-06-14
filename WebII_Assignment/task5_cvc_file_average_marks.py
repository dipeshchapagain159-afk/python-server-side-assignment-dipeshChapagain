import csv
def calculate_average_marks(filename):
    total_marks = 0
    student_count = 0

    # Open CSV file
    with open(filename, mode='r') as file:
        csv_reader = csv.reader(file)


        header = next(csv_reader)
        for row in csv_reader:
            marks = float(row[1])
            total_marks += marks
            student_count += 1
    # Calculating average
    if student_count > 0:
        average = total_marks / student_count
        return average
    else:
        return 0

filename = "student_marks.csv"
average_marks = calculate_average_marks(filename)
print(f"Average Marks: {average_marks:.2f}")
