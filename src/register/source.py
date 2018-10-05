def check_registration_rules(**kwargs):
    cant_use = 'codecup', 'quera'

    final_list = []

    for user,password in kwargs.items():
        if str(user) in cant_use or len(str(user)) < 4 or len(str(password)) < 6 or str(password).isdigit():
            continue
        final_list.append(str(user))

    return final_list


