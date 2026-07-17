def process_data(data):
    data["total"]=data["Maths"]+data["Science"]+data["English"]
    data["avarage"]=data["total"]/3
    return data