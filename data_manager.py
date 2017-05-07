def add_to_file(form_data_list):

    form_data_list = [prop.replace('\r\n', '') for prop in form_data_list]

    with open('stories.csv', 'a+') as file:
        file.write(','.join(form_data_list) + "\n")


def write_to_file(list_of_forms):

    with open('stories.csv', 'w') as file:
        for form in list_of_forms:
            form_data_list = ["{}:{}".format(key, form[key]) for key in form]
            add_to_file(form_data_list)


def get_data_from_file(path):
    '''Returns list of dictionaries containing form data read from file. Each dict is an entire user story.
    '''
    with open(path, 'r') as file:
        data = [line.split(',') for line in file.readlines()]

        data_final = []
        for i, form_data in enumerate(data):
            data_dict = {}
            for pair in form_data:
                data_dict[pair.split(':')[0]] = pair.split(':')[1].strip()
            data_dict['id'] = str(i + 1)
            data_final.append(data_dict)

        return data_final
