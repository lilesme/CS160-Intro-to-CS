def labs():
    num_labs=int(input("How many labs? "))
    points=int(input("How many points are each worth?"))
    y=1
    total_points_earned=0
    for x in range(num_labs):
        score=input("Points earned on Lab "+ str(y)+ ":")
        total_points_earned+=int(score)
        y+=1
    total_points= points* num_labs
    grade=total_points_earned/total_points
    percent= grade*100
    print("You earned a " + str(percent)+ "% in lab")
    return percent

def assignments():
    num_assignments=int(input("How many assignments? "))
    points=int(input("How many points are each worth?"))
    y=1
    total_points_earned=0
    for x in range(num_assignments):
        score=input("Points earned on Assignment "+ str(y)+ ":")
        total_points_earned+=int(score)
        y+=1
    total_points= points* num_assignments
    grade=total_points_earned/total_points
    percent= grade*100
    print("You earned a " + str(percent)+ "% on Assignments")
    return percent

def participation():
    num_exercises=int(input("How many exercises? "))
    points=int(input("How many points are each worth?"))
    y=1
    total_points_earned=0
    for x in range(num_exercises):
        score=input("Points earned on Exercise "+ str(y)+ ":")
        total_points_earned+=int(score)
        y+=1
    total_points= points* num_exercises
    grade=total_points_earned/total_points
    percent= grade*100
    print("You earned a " + str(percent)+ "% for Participation")
    return percent



def overall_grade(p_grade, a_grade, l_grade):
    overall=(p_grade*.10)+(a_grade*.65)+(l_grade*.25)
    print("You earned a " + str(overall)+ "% in CS 160")
    return overall


def letter(overall):
    if overall >= 93:
        print("You earned an A!")
    elif 90 <= overall <=92:
        print("You earned an A-")
    elif 87 <= overall <= 89:
        print("You earned a B+")
    elif 83 <= overall <= 86:
        print("You earned a B")
    elif 80 <= overall <= 82:
        print("You earned a B-")
    elif 77 <= overall <= 79:
        print("You earned a C+")
    elif 73 <= overall <= 76:
        print("You earned a C")
    elif 70 <= overall <= 72:
        print("You earned a C-")
    elif 67 <= overall <= 69:
        print("You earned a D+")
    elif 63 <= overall <= 66:
        print("You earned a D")
    elif 60 <= overall <= 62:
        print("You earned a D-")
    elif overall < 69:
        print("You earned a F!")


def main():

    p_grade=participation()
    a_grade=assignments()
    l_grade=labs()
    overall=overall_grade(p_grade, a_grade, l_grade)
    letter(overall)


main()
