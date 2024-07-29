CREATE DATABASE viet;
ALTER DATABASE viet CHARACTER SET utf8 COLLATE utf8_unicode_ci;
USE viet;


CREATE TABLE noun (
    id INT NOT NULL AUTO_INCREMENT,
    eng VARCHAR (30),
    classifier NVARCHAR (10),
    viet NVARCHAR (30),
    PRIMARY KEY (id)
);

CREATE TABLE pronoun (
    id INT NOT NULL AUTO_INCREMENT,
    surface_form NVARCHAR (30),
    gender VARCHAR (10),
    person VARCHAR (10),
    number VARCHAR (10),
    relationship VARCHAR (50),
    PRIMARY KEY (id)
);

INSERT INTO noun
    (eng, classifier, viet)
VALUES
    ('dog', N'con', N'chó'),
    ('cat', N'con', N'mèo'),
    ('bird', N'con', N'chim'),
    ('book', N'quyển', N'sách'),
    ('chair', N'cái', N'ghế')
;

INSERT INTO pronoun
    (surface_form, gender, person, number, relationship)
VALUES
    (N'anh', 'masculine', 'second', 'singular', 'older brother age'),
    (N'chị', 'feminine', 'second', 'singular', 'older sister age'),
    (N'em', 'unisex', 'second', 'singular', 'younger sibling'),
    (N'bác', 'unisex', 'second', 'singular', 'older uncle/aunt age'),
    (N'chú', 'masculine', 'second', 'singular', 'younger uncle age'),
    (N'tôi', 'unisex', 'first', 'singular', 'formal')
;