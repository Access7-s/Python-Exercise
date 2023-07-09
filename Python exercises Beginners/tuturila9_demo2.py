def function_c():
    print("Starting function_c")
    raise ValueError("An error occured in fuction_c")

def function_b():
    print("Starting fun_b")
    function_c()
    print("Finished fun_c")

def function_a():
    print("Starting function_a")
    try:
        function_b()
    except ValueError as e:
        print(f"Caught exception: {e}")
    print("Finished function_a")
function_a()
