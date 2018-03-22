def nested_sum(t):
    result = 0
    for k in t:
        result += sum(k)
    return result

