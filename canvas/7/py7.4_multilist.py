# defining the list of student scores
studentencijfers = [ [95, 92, 86],[66, 75, 54],[89, 72, 100],[34, 0, 0] ]
# average for each student
def gemiddelde_per_student(studentencijfers):
    antw = []
    # looping throught all the students
    for student in studentencijfers:
        # defining the result 0 to count every student his total grade
        result = 0
        # looping every grade and counting it in result
        for cijfer in student:
            result = cijfer + result
        # calculating the average for each student
        gemiddelde = result / len(student)
        # dropping the average in the global list and
        antw.append(gemiddelde)
    return antw

def gemiddelde_van_alle_studenten(studentencijfers):
    # making the list of each student average
    studentgem = gemiddelde_per_student(studentencijfers)
    # result 0 because count every average to eachother
    result = 0
    # counting the total average highest
    for gemiddelde in studentgem:
        result = gemiddelde + result
    #calculating average
    antw = result / len(studentgem)
    return antw

print(gemiddelde_per_student(studentencijfers))

print(gemiddelde_van_alle_studenten(studentencijfers))