def print_chinese_list(names):
    for name in names:
        print name


def generate_urls(base_url):
    urls = []
    for i in range(1, 101):
        url = base_url + '-' + str(i)
        urls.append(url)
    return urls


def trim_text(line, new_lines=False, mid_bracket=False):
    temp = line
    if new_lines:
        temp = trim_new_lines(temp)

    if mid_bracket:
        temp = trim_mid_bracket(temp)

    temp = trim_beginning_space(temp)

    return temp


def trim_new_lines(line):
    return line.replace('\n', '')


def trim_mid_bracket(line):
    if '[' in line and ']' in line:
        begin_index = line.index('[')
        end_index = line.index(']')

        if begin_index < end_index:
            return line[:begin_index] + trim_mid_bracket(line[end_index+1:])
        else:
            return line[:end_index+1] + trim_mid_bracket(line[end_index+1:])

    return line


def trim_beginning_space(line):
    if line[0] == ' ':
        return line[1:]
    return line
