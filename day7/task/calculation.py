def calcutions(data):
    
    data["total"]=data["Maths"]+data["Science"]+data["English"]
    data["avarage"]=data["total"]/3
    
    
    data["grade"]=data["avarage"].apply(grade)
    return data
def grade(avarage):
        if avarage>=90:
            return "A"
        else :
            return "B"  
        
def total(data):
    classavarge=data["avarage"].mean()
    top_index=data["total"].idxmax()
     
    class_topper=data.loc[top_index,"Name"]
    return classavarge,class_topper