/*
                          In The Name Of God
                     Benyamin Bashari, Negar Layegh
                           9412430366, 9412430639
*/




DROP SCHEMA IF EXISTS `music_spot`;
CREATE SCHEMA IF NOT EXISTS `music_spot`;
USE `music_spot` ;

CREATE TABLE user(
  name VARCHAR(30) NOT NULL unique,
  email VARCHAR(30) NOT NULL unique,
  password VARCHAR(30) NOT NULL,
  p_question VARCHAR(100) NOT NULL,
  p_answer VARCHAR(50) NOT NULL,
  photo_path VARCHAR(100),
  type enum ('ordinary', 'composer', 'manager'),
  PRIMARY KEY(name)
);

CREATE view user_ordinary AS
  SELECT name, email, password, p_question, p_answer, photo_path FROM user WHERE type = 'ordinary';

CREATE view user_manager AS
  SELECT name, email, password, p_question, p_answer, photo_path FROM user WHERE type = 'manager';

CREATE view user_composer AS
  SELECT name, email, password, p_question, p_answer, photo_path FROM user WHERE type = 'composer';

CREATE TABLE tag(
  name VARCHAR(30),
  PRIMARY KEY (name)
);

CREATE TABLE user_tag(
  username VARCHAR (30) NOT NULL ,
  tag_name VARCHAR (30) NOT NULL ,
  PRIMARY KEY (username, tag_name),
  FOREIGN KEY (username) REFERENCES user(name) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (tag_name) REFERENCES tag(name) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE TABLE user_follow(
  follower VARCHAR (30) NOT NULL,
  following VARCHAR (30) NOT NULL,
  PRIMARY KEY (follower, following),
  FOREIGN KEY (follower) REFERENCES user(name) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (following) REFERENCES user(name) ON DELETE CASCADE ON UPDATE CASCADE
);


CREATE TABLE music(
    id INTEGER NOT NULL auto_increment,
    title VARCHAR(30) NOT NULL,
    songwriter VARCHAR(30),
    duration INTEGER NOT NULL,
    play_count INTEGER,
    lyrics VARCHAR(10000),
    photo VARCHAR(30),
    PRIMARY KEY(id)
);

CREATE TABLE user_music_like(
  username VARCHAR(30) NOT NULL,
  music_id INTEGER NOT NULL,
  PRIMARY KEY (username, music_id),
  FOREIGN KEY (username) REFERENCES user(name) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (music_id) REFERENCES music(id) ON DELETE CASCADE ON UPDATE CASCADE
);




CREATE TABLE music_tag(
  music_id INTEGER NOT NULL,
  tag_name VARCHAR (30) NOT NULL,
  PRIMARY KEY (music_id, tag_name),
  FOREIGN KEY (music_id) REFERENCES music(id) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (tag_name) REFERENCES tag(name) ON DELETE CASCADE ON UPDATE CASCADE
);


CREATE TABLE user_listen(
  username VARCHAR (30) NOT NULL,
  music_id INTEGER NOT NULL,
  PRIMARY KEY (username, music_id),
  FOREIGN KEY (username) REFERENCES user(name) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (music_id) REFERENCES music(id) ON DELETE CASCADE ON UPDATE CASCADE
);


CREATE TABLE music_list(
  id INTEGER NOT NULL auto_increment,
  title VARCHAR(30) NOT NULL,
  duration INTEGER NOT NULL,
  stars INTEGER,
  username VARCHAR (30) NOT NULL,
  type enum ('album','playlist'),
  public boolean NOT NULL,
  PRIMARY KEY (id)
);

CREATE view album AS
  SELECT id, title, duration, stars, username FROM music_list WHERE type = 'album';

CREATE view playlist AS
  SELECT id, title, duration, stars, username, public FROM music_list WHERE type = 'playlist';

CREATE TABLE music_list_tag(
  music_list_id INTEGER NOT NULL,
  tag_name VARCHAR(30) NOT NULL,
  PRIMARY KEY (tag_name, music_list_id),
  FOREIGN KEY (music_list_id) REFERENCES music_list(id) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (tag_name) REFERENCES tag(name) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE music_list_music(
  music_list_id INTEGER NOT NULL,
  music_id INTEGER NOT NULL,
  PRIMARY KEY (music_id, music_list_id),
  FOREIGN KEY (music_list_id) REFERENCES music_list(id) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (music_id) REFERENCES music(id) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE TABLE music_list_producer(
  username VARCHAR (30) NOT NULL,
  music_list_id INTEGER NOT NULL,
  published_date date NOT NULL,
  PRIMARY KEY (username, music_list_id),
  FOREIGN KEY (username) REFERENCES user(name) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (music_list_id) REFERENCES music_list(id) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE TABLE composer_music(
  username VARCHAR (30) NOT NULL,
  music_id INTEGER NOT NULL,
  published_date date NOT NULL,
  PRIMARY KEY (username, music_id),
  FOREIGN KEY (username) REFERENCES user(name) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (music_id) REFERENCES music(id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE music_list_follow(
  username VARCHAR (30) NOT NULL,
  music_list_id INTEGER NOT NULL,
  PRIMARY KEY (username, music_list_id),
  FOREIGN KEY (username) REFERENCES user(name) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (music_list_id) REFERENCES music_list(id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE request_music(
  username VARCHAR (30) NOT NULL,
  music_id INTEGER NOT NULL,
  PRIMARY KEY (username, music_id),
  FOREIGN KEY (username) REFERENCES user(name) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (music_id) REFERENCES music(id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE accept_music(
  manager_name VARCHAR (30) NOT NULL,
  music_id INTEGER NOT NULL,
  PRIMARY KEY (manager_name, music_id),
  FOREIGN KEY (manager_name) REFERENCES user(name) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (music_id) REFERENCES music(id) ON DELETE CASCADE ON UPDATE CASCADE
)





/*CREATE USER 'ordinary'@'localhost' IDENTIFIED BY 'ordinary';
CREATE USER 'manager'@'localhost' IDENTIFIED BY 'manager';
CREATE USER 'composer'@'localhost' IDENTIFIED BY 'composer';

GRANT SELECT ON music_spot.* TO 'ordinary'@'localhost', 'manager'@'localhost', 'composer'@'localhost';

GRANT INSERT ON music_spot.uesr_tag, music_spot.user_follow, music_spot.user_music_like, music_spot.user_listen, music_spot.music_list_follow  TO 'ordinary'@'localhost', 'manager'@'localhost', 'composer'@'localhost';

GRANT INSERT ON music_spot.music, music_spot.music_tag, music_spot.music_list, music_spot.music_list_tag, music_spot.music_list_music, music_spot.music_list_producer, music_spot.composer_music TO 'composer'@'localhost';

GRANT UPDATE ON music_spot.music, music_spot.music_list TO 'manager'@'localhost'

GRANT DELETE ON TO 'ordinary'@'localhost', 'manager'@'localhost', 'composer'@'localhost';
GRANT DELETE ON
GRANT DELETE ON
GRANT DELETE ON*/












