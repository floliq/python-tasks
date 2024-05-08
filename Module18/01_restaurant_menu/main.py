def display_menu(user_menu):
    menu_res = user_menu.replace(";", ", ").strip()
    print("На данный момент в меню есть: {}".format(menu_res))


menu = input("Доступное меню: ")
display_menu(menu)
