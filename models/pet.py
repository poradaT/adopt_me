from db import sql_select, sql_write, sql_select_one

def get_all_pets():
    pet_items = sql_select('SELECT id, image_url, name, type, breed, sex, size, colour, age FROM pet_list;')   
    return pet_items