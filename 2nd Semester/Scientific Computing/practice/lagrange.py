def lagrange(x_vals, y_vals, val):
    assert len(x_vals) == len(y_vals), "Length should be equal"

    result = 0

    for i, y_val in enumerate(y_vals):
        l_i = y_val
        for j, x_val in enumerate(x_vals):
            if i != j:
                l_i *= (val - x_vals[j]) / (x_vals[i] - x_vals[j])

        result += l_i

    return result


if __name__ == "__main__":
    x_vals: list = [300, 304, 305, 307]
    y_vals: list = [2.4771, 2.4829, 2.4843, 2.4871]

    val: int = 301

    # result
    # rslt = lagrange_func(x_vals, y_vals, val)
    rslt = lagrange(x_vals, y_vals, val)

    print(f"For X: {val} the value of Y: {rslt:0.6f}")
