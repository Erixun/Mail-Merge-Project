from constant import PATH_NAMES, PATH_OUTPUT, PATH_TEMPLATE, PLACEHOLDER

with open(PATH_NAMES) as names_file, open(PATH_TEMPLATE) as template_file:
    names, template = names_file.readlines(), template_file.read()

    for line in names:
        name = line.strip()
        output = template.replace(PLACEHOLDER, name)
        path_letter = f"{PATH_OUTPUT}/{name}.txt"

        with open(path_letter, "w") as letter:
            letter.write(output)
