for test in ('isalnum','isalpha','isdigit','islower','isupper'):
    any(eval('c. '+test+'()') for c in str)