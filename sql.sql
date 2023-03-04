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




DROP TABLE IF EXISTS users;
CREATE TABLE users(
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL,   
    password_hash TEXT,
    admin boolean DEFAULT false
);

INSERT INTO users (name, email, password_hash, admin) VALUES ('Bon', 'bon@gmail.com','', true);
INSERT INTO users (name, email, password_hash, admin) VALUES ('Alice', 'alice@gmail.com','', true);
INSERT INTO users (name, email, password_hash, admin) VALUES ('Mike', 'mike@gmail.com','', false);
INSERT INTO users (name, email, password_hash, admin) VALUES ('AJ', 'aj@gmail.com','', false);


UPDATE users SET password_hash = 
'pbkdf2:sha256:260000$ntZqPanvtctOGV3a$05f5db9e2a537cd73d011b96dbfa7a38063afb4d8f0ee9ef2fb2eca9e5e1d74a'
WHERE id = 1;

UPDATE users SET password_hash = 
'pbkdf2:sha256:260000$O5K3Qlrcuq3R8yDy$7ab4e05aa4e7b83813a02260d6154c5e6873dc1b7af65944d8d5a9a66305dee0'
WHERE id = 2;

UPDATE users SET password_hash = 
'pbkdf2:sha256:260000$Jp4p9atQEtCagFfz$b2b1a270bb1db2d8df22979d87d918b3a63698831722587091db1612f1436371'
WHERE id = 3;

UPDATE users SET password_hash = 
'pbkdf2:sha256:260000$V1xgvntqn3yt9Lfu$fc6b99e9f1711373f2884d045518c1cba15fbd37023da62ebec40760f32afcf9'
WHERE id = 4;





