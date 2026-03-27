def add_setting(settings, key_value_pair):

    key = key_value_pair[0].lower()
    value = key_value_pair[1].lower()

    if key in settings:
        return (
            f"Setting '{key}' already exists! Cannot add a new setting with this name."
        )

    settings[key] = value

    return f"Setting '{key}' added with value '{value}' successfully!"


def update_setting(settings, key_value_pair):

    key = key_value_pair[0].lower()

    value = key_value_pair[1].lower()

    if key not in settings:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

    settings[key] = value

    return f"Setting '{key}' updated to '{value}' successfully!"


def delete_setting(settings, key_setting):

    key = key_setting.lower()

    if key in settings:
        del settings[key]
        return f"Setting '{key}' deleted successfully!"

    return "Setting not found!"


def view_settings(settings):

    if not settings:
        return "No settings available."

    output = "Current User Settings:"

    for key, value in settings.items():
        output += f"\n{key.capitalize()}: {value}"
    return output + "\n"


# this was made for me to see app in action
def start_app():

    moje_data = {}

    while True:
        print("\n                    --- MY APP ---")
        print("\n1. Add | 2. Update | 3. Delete | 4. View | 5. Quit")
        volba = input("Choose from the menu: ")

        if volba == "1":
            k = input("Enter setting: ")
            v = input("Enter value: ")

            print(add_setting(moje_data, (k, v)))

        elif volba == "2":
            k = input("Enter setting: ")
            v = input("Enter value: ")

            print(update_setting(moje_data, (k, v)))

        elif volba == "3":
            k = input("Enter setting: ")

            print(delete_setting(moje_data, (k)))

        elif volba == "4":
            print(view_settings(moje_data))

        elif volba == "5":
            print("Bye!")
            break



if __name__ == "__main__":
    start_app()
