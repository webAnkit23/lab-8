def decode(roll) :
    program = {
        "1" : "UG",
        "2" : "PG",
        "3" : "PHD"
    }
    course = {
        "1" : "B.TECH",
        "2" : "M.TECH",
        "3" : "MBA",
        "4" : "BCA",
        "5" : "MCA"
    }
    return {
        "program" : program.get(roll[0], "unknown"),
        "course" : course.get(roll[1:3]),
        "admission_year" : f"20{roll[4:6]}",
        "Roll_No" : roll[6:]
    }

print(decode(input("enter your roll no : ")))