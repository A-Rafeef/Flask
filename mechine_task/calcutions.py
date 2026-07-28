def gradee(average):
    if average >= 90:
        return "A+","Outstanding"

    elif average >= 80:
        return "A","Excellent"
    elif average >= 70:
        return "B","Good"

    elif average >= 60:
        return "C","Average"

    else:
        return "Fail","Needs Improvement"




def calcutions(name,maths,science,eng):
    total=int(maths)+int(science)+int(eng)
    average=int(total)/3
    grade,remark=gradee(int(average))
    return name,total,average,grade,remark




