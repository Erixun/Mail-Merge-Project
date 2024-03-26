path_names = "Input/Names/invitees.txt"
path_template = "Input/Letters/template.txt"
path_output = "Output/ReadyToSend"

with open(path_names) as names_file, open(path_template) as template_file:
    names, template = names_file.readlines(), template_file.read()

    for line in names:
        name = line.strip()
        output = template.replace("[name]", name)
        path_letter = f"{path_output}/{name}.txt"

        with open(path_letter, "w") as letter:
            letter.write(output)
