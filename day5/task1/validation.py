def checking(data):
    name=data.filename
    
    if name is "":
        return True
    
def requered_colomn(data):
    col=["Name","Maths","English","Science"]
    for i in col:
        if i not in data.columns:
            return True

