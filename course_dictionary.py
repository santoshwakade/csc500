# Define the dictionaries
course_rooms = {
    'CSC101': '3004',
    'CSC102': '4501',
    'CSC103': '6755',
    'NET110': '1244',
    'COM241': '1411'
}

course_instructors = {
    'CSC101': 'Haynes',
    'CSC102': 'Alvarado',
    'CSC103': 'Rich',
    'NET110': 'Burke',
    'COM241': 'Lee'
}

course_times = {
    'CSC101': '8:00 a.m.',
    'CSC102': '9:00 a.m.',
    'CSC103': '10:00 a.m.',
    'NET110': '11:00 a.m.',
    'COM241': '1:00 p.m.'
}

# Function to display course details based on course number input
def display_course_details(course_num):
    if course_num in course_rooms and course_num in course_instructors and course_num in course_times:
        room = course_rooms[course_num]
        instructor = course_instructors[course_num]
        time = course_times[course_num]
        print(f"Course: {course_num}\nRoom: {room}\nInstructor: {instructor}\nMeeting Time: {time}")
    else:
        print("Course number not found.")

course_number = input("Enter course number: ")
if course_number and course_number.strip():
    display_course_details(course_number.upper())
else:
    print("Please enter valid course number")
