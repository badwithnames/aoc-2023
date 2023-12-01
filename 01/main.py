def part_one():
    sum_values = 0
    with open('input.txt') as file:
        for line in file:
            value = []
            l, r = 0, len(line) - 1

            while not line[l].isdigit():
                l += 1
            value.append(line[l])

            while not line[r].isdigit():
                r -= 1
            value.append(line[r])

            sum_values += int(''.join(value))

    return sum_values


def part_two():
    digits = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    res = 0

    with open('input.txt') as file:
        for line in file:
            values = []
            l = 0
            while l < len(line):
                r = l
                while r < len(line):
                    if line[l:r + 1].isdigit():
                        values.append(line[l:r + 1])
                        l += 1
                        r = l
                    elif line[l:r + 1] in digits:
                        values.append(digits[line[l:r + 1]])
                        l = r
                    else:
                        r += 1
                l += 1
            if len(values) == 1:
                res += int(values[0] + values[0])
            else:
                res += int(values[0] + values[-1])

    return res


if __name__ == '__main__':
    print(part_two())
