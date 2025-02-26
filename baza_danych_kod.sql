USE ceny_mieszkañ

CREATE TABLE ceny_mieszkañ (
    city NVARCHAR(100),
    squareMeters FLOAT,
    rooms nvarchar(10),
    floor nvarchar(10) NULL,
    buildYear nvarchar(10) NULL,
    latitude FLOAT,
    longitude FLOAT,
    price INT
);

INSERT INTO ceny_mieszkañ (city, squareMeters, rooms, floor, buildYear, latitude, longitude, price)
SELECT city, squareMeters, rooms, floor, buildYear, latitude, longitude, price
FROM dbo.apartments_pl_2023_08;

Select * from ceny_mieszkañ


SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'ceny_mieszkañ';



