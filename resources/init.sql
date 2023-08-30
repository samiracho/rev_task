CREATE TABLE IF NOT EXISTS users (
   username VARCHAR ( 50 ) PRIMARY KEY,
   birthday date
);

INSERT INTO users(username, birthday) VALUES ('pepe','1961-06-16'),('juan','1990-06-16');