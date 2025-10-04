from flask import jsonify

def is_correct_number(x):
    x.replace(",", ".")
    try:
        n = float(x)
        return int(n) if n.is_integer else n
    except ValueError:
        return None
    
def parseList(listString):

    listString = listString.replace("[", "")
    listString = listString.replace("]", "")
    data = listString.split(",")

    for i in range(len(data)):
        num = is_correct_number(data[i])
        if num is None:
            raise ValueError("Invalid number in list")
        data[i] = num
    return data
    
def reduce_operation(listString, operator):

    try:
        readDataList = parseList(listString) 
    except ValueError as e:
        return jsonify(error=str(e)), 400
    
    print(f"ReadDataList: {readDataList}")
    match operator:
        case '+':
            print(f"List: {readDataList}")
            result = sum(readDataList)
        
        case '-':
            result = readDataList[0]
            for i in range(1, len(readDataList)):
                result -= readDataList[i]
        case '*':
            result = 1
            for num in readDataList:
                result *= num
        case '/':
            result = readDataList[0]
            for i in range(1, len(readDataList)):
                if readDataList[i] == 0:
                    return None, "Division by zero error"
                result /= readDataList[i]
                print(f"Intermediate result: {result}")
        case _:
            return None, "Invalid operator"
    
    return result, None