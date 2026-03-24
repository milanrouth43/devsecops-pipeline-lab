def insecure_function(user_input):
    # This is a terrible idea and Semgrep hates it.
    eval(user_input)
