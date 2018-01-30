create database store;
use store;

CREATE TABLE category(
id INT auto_increment PRIMARY KEY, 
name VARCHAR(30) unique
);

CREATE TABLE product(
category INT,
description VARCHAR(50),
price DOUBLE,
title VARCHAR (50),
favorite boolean default false,
img_url VARCHAR(500),
id INT auto_increment PRIMARY KEY
);
SET FOREIGN_KEY_CHECKS=0;

INSERT INTO category (name) VALUES
('Snacks'),('Fruits'),('Vegetables');

INSERT INTO product (category, price, title,img_url) VALUES
(1, 7.5,'Chilli Crackers','./images/chilli.jpg'),
(1, 9.0,'Dried Fruit','./images/dried.jpg'),
(1, 6.0,'Trail Mix','./images/nuts.jpg'),
(1, 7.5,'Nuts Mix','./images/nuts2.jpg'),
(2, 7.5,'Apples','./images/apples.png'),
(2, 9.0,'Dragon Fruit','./images/dragonfruit.jpg'),
(2, 6.0,'Pear','./images/pear.jpg'),
(2, 7.5,'Watermelon','./images/watermelon.jpg'),
(3, 9.0,'Carrot','./images/carrot.jpg'),
(3, 8.0,'Cucumbers','./images/cucumbers.png'),
(3, 8.0,'Tomatoes','./images/tomatoes.png'),
(3, 9.0,'Cauliflower','./images/cauli.jpg');