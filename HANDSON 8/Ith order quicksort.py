def r_a( a, s, e):
    p = a[e]
    p_i = s - 1
    for c in range(s,e):
        if a[c] < p:
            p_i += 1
            a[p_i], a[c] = a[c], a[p_i]
    a[p_i + 1], a[e] = a[e], a[p_i + 1]
    return p_i + 1
def ith_el(a, s, e, t_i):
    if s <= e:
        p_i = r_a(a, s, e)
        if p_i == t_i:
            return a[p_i]
        elif p_i < t_i:
            return ith_el(a, p_i + 1, e, t_i)
        else:
            return ith_el(a, s, p_i - 1, t_i)
    return -1
def main():
    o_a = [8, 11, 25, 99, 26, 58, 33, 71, 49, 19]
    s_a = o_a.copy()  
    try:
        ith_o = int(input("Enter the ith order : "))
        if ith_o < 1 or ith_o > len(o_a):
            print(f"Invalid input. ith_order must be between 1 and {len(o_a)}")
            return
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return
    ith_v = ith_el(o_a, 0, len(o_a) - 1, ith_o - 1)
    if ith_v == -1:
        print("Invalid index or array size.")
    else:
        print(f"The {ith_o}th order statistic: {ith_v}")
    s_a.sort()
    if s_a[ith_o - 1] == ith_v:
        print("Validation successful: ith Order matches with the sorted array.")
    else:
        print("Validation failed: Invalid result.")
if __name__ == "__main__":
    main()
