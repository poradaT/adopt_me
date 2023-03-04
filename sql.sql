DROP TABLE IF EXISTS pet_list;

CREATE TABLE pet_list (
    id SERIAL PRIMARY KEY,
    image_url TEXT,
    name VARCHAR(50) NOT NULL,
    type TEXT,
    breed TEXT,
    sex VARCHAR(50) NOT NULL,
    size VARCHAR(50) NOT NULL,
    colour TEXT,
    age TEXT    
);



INSERT INTO pet_list(image_url, name, type, breed, sex, size, colour, age)
VALUES (
'https://www.adoptapet.com.au/img/animals/7451439.jpeg', 
'Hazel',
'Dog',
'Medium Cross Breed',
'Female',
'Unknown',
'Brindle/White',
'1 year and 5 months'
);


