from db import sql_select, sql_write, sql_select_one

def get_all_pets(sort_by):
    if sort_by == 'dog':
        pet_items = sql_select("SELECT id, image_url, name, type, breed, sex, size, colour, age FROM pet_list WHERE type='dog';") 
    elif sort_by == 'cat':
        pet_items = sql_select("SELECT id, image_url, name, type, breed, sex, size, colour, age FROM pet_list WHERE type='cat';") 
    elif sort_by == 'all' :
        pet_items = sql_select('SELECT id, image_url, name, type, breed, sex, size, colour, age FROM pet_list;')
    else :
        pet_items = sql_select('SELECT id, image_url, name, type, breed, sex, size, colour, age FROM pet_list;')   
    return pet_items
  
def insert_pet(image_url, name, type, breed, sex, size, colour, age):
    sql_write(
        "INSERT INTO pet_list(image_url, name, type, breed, sex, size, colour, age) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", 
        [image_url, name, type, breed, sex, size, colour, age])

def get_pet(id):
    pet_item = sql_select(f"SELECT id, image_url, name, type, breed, sex, size, colour, age FROM pet_list WHERE id={id};")
    return pet_item

def update_pet(id, image_url, name, type, breed, sex, size, colour, age):
    sql_write(
        f"UPDATE pet_list SET image_url = %s, name = %s, type = %s, breed = %s, sex = %s, size = %s, colour = %s, age = %s WHERE id={id}",
        [image_url, name, type, breed, sex, size, colour, age])

def delete_pet(id):
    delete_item = sql_write(f"DELETE FROM pet_list WHERE id={id};",
        [id])
    return delete_item