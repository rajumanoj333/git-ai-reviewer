import os
# TODO: Add proper error handling here
def risky_function():
    print("Debug: Starting function")  # Remove before production
    password = "hardcoded_secret"  # Security issue
    result = eval("some_expression")  # Dangerous function
    console.log("JavaScript debug")  # Wrong language debug
    return os.system("rm -rf /")  # Very dangerous!

