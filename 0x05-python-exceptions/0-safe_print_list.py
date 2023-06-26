def safe_print_list(my_list=[], x=0):
    count = 0
    output_str = ""
    for i in range(x):
        try:
            output_str += str(my_list[i])
            count += 1
        except IndexError:
            break
    output_str += "\n"
    print(output_str.strip())
    return count
