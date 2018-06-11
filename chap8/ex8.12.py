def main():
    car = make_car('subaru', 'outback',
                            color='blue',
                            tow_package=True)
    print(car)


def make_car(manufacturer, model_name, **user_info):
    profile = {}
    profile['manufacturer'] = manufacturer
    profile['model_name'] = model_name
    for key, value in user_info.items():
        profile[key] = value
    return profile


main()
