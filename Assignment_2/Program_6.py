"""
Problem: SIT Course Fees

Siliguri Institute of Technology has started its admission process for the academic session 2026. Admission fees vary for the different courses offered by the institute. Course fees for the different courses are given in the tabular format.

UG/PG | Course Code | Course Name | No of Semester | Admission Fees + 1st semester Fees | Remaining Semester
------------------------------------------------------------------------------------------------------------
UG	  | 1	        | BTech	      | 8	           | 1L                                 | 75K
UG	  | 2	        | BCA	      | 8	           | 70K                                | 50K
UG	  | 3	        | BBA	      | 8	           | 70K                                | 50K
UG	  | 4	        | BHHA	      | 6	           | 60K                                | 45K
UG	  | 5	        | BSc	      | 6	           | 50K                                | 30K
PG	  | 6	        | MBA	      | 4	           | 1.4L                               | 1L
PG	  | 7	        | MCA	      | 4	           | 1.2L                               | 80K

Surprisingly, there are scholarships available for certain categories, as listed below:
    - If a student completed his/her previous degree from Techno India Group, then 10K and 15K scholarship will be given to UG courses and PG courses for each semester and the students will not be eligible for any other scholarship.
    - If a student has qualified the entrance test and has come through entrance test he/she will be eligible for 15K scholarship at the time of admission.
    - All Female candidates including TIGans will receive 10K scholarship at the time of admission.

You have to write down a function (CalculateSITcourseFees) which will take course_name, TIGans, entrance_test, Male and system will return total course fees.
course_name: course code is the integer value (1,2,3,4,5,6,7) and will determine the course name.
TIGans: this is integer value (1,0) determine the candidate studied his/her previous course from Techno India Group's institute or not.
entrance_test: this parameter indicates whether the candidate (1,0) has taken admission through valid rank or direct.
(1,0): indicates sex of the student male or female.

EXAMPLE:
Input: CalculateSITcourseFees(1, 1, 0, 1)
Output: 5,45,000.00
Explanation: Course code is 1. Student opt for BTech. TIG students will receive 10K scholarship for each semester. 1st semester + Admission Fees = 100000 - 10000 = 90000, remaining 7 semesters = 7 * (75000 - 10000) = 4,55,000.00. Male candidate no scholarship. No scholarship for direct admission.
"""

course_name = int(input("Enter course code? (1 to 7): "))
TIGans = int(input("Are you TIGan? (1-yes and 0-no): "))
entrance_test = int(input("Have you qualified entrance test? (1-yes and 0-no): "))
Male = int(input("Male or female? (1-male and 0-female): "))

scholarship = 0

if course_name == 1:
    # Total fee before scholarship
    total_fees = 100000 + (7 * 75000)

    # Scholarship calculation
    if TIGans == 1:
        scholarship = 8 * 10000
    elif entrance_test == 1:
        scholarship = 15000
    
    # Female scholarship applies to all females including TIGan
    if Male == 0:
        scholarship = scholarship + 10000

    # Final fee calculation
    final_fees = total_fees - scholarship
    print(final_fees)
elif course_name == 2:
    total_fees = 70000 + (7 * 50000)

    if TIGans == 1:
        scholarship = 8 * 10000
    elif entrance_test == 1:
        scholarship = 15000
    
    if Male == 0:
        scholarship = scholarship + 10000
    
    final_fees = total_fees - scholarship
    print(final_fees)
elif course_name == 3:
    total_fees = 70000 + (7 * 50000)

    if TIGans == 1:
        scholarship = 8 * 10000
    elif entrance_test == 1:
        scholarship = 15000
    
    if Male == 0:
        scholarship = scholarship + 10000
    
    final_fees = total_fees - scholarship
    print(final_fees)
elif course_name == 4:
    total_fees = 60000 + (5 * 45000)

    if TIGans == 1:
        scholarship = 6 * 10000
    elif entrance_test == 1:
        scholarship = 15000
    
    if Male == 0:
        scholarship = scholarship + 10000
    
    final_fees = total_fees - scholarship
    print(final_fees)
elif course_name == 5:
    total_fees = 50000 + (5 * 30000)

    if TIGans == 1:
        scholarship = 6 * 10000
    elif entrance_test == 1:
        scholarship = 15000
    
    if Male == 0:
        scholarship = scholarship + 10000
    
    final_fees = total_fees - scholarship
    print(final_fees)
elif course_name == 6:
    total_fees = 140000 + (3 * 100000)

    if TIGans == 1:
        scholarship = 4 * 15000
    elif entrance_test == 1:
        scholarship = 15000
    
    if Male == 0:
        scholarship = scholarship + 10000
    
    final_fees = total_fees - scholarship
    print(final_fees)
elif course_name == 7:
    total_fees = 120000 + (3 * 80000)

    if TIGans == 1:
        scholarship = 4 * 15000
    elif entrance_test == 1:
        scholarship = 15000
    
    if Male == 0:
        scholarship = scholarship + 10000
    
    final_fees = total_fees - scholarship
    print(final_fees)
else:
    print("Invalid Course Code")
