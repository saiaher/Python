def calculate_average_attendance(attendance_list):
    total_classes = len(attendance_list)
    total_present = sum(attendance_list)  # Counts how many times '1' appears in the list
    average_attendance = (total_present / total_classes) * 100  # Get the percentage
    return average_attendance

# Example usage:
attendance = [1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1]  # A sample attendance list for 75 classes

average = calculate_average_attendance(attendance)
print(f"Average attendance: {average:.2f}%")
