def compute_bmi(weight, height):
    bmi = weight / height ** 2
    if bmi < 18.5:
        result = 'undrweight'
    elif bmi > 25:
        result = 'overweight'
    else:
        result = 'normal'
    return result


if __name__ == '__main__':
    user_weight = float(input('Your weight [kg]: '))
    user_height = float(input('Your height [m]: '))
    user_result = compute_bmi(user_weight, user_height)
    print(f'You are {user_result}')

    print('You are ' + user_result)

    print('You are {}'.format(user_result))


