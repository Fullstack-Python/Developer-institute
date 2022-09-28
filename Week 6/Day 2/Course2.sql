-- CREATE TABLE producers(
-- producers_id SERIAL,
-- producers_name VARCHAR (50) NOT NULL,
-- producers_number INTEGER,
-- FOREIGN KEY (producers_number) REFERENCES movies (movie_id)
-- );

-- INSERT INTO producers(producers_name,producers_id)
-- VALUES ('Kevin', 2)

SELECT movies.movie_title, producers.producers_name
FROM movies
INNER JOIN producers
ON movies.movie_id = producers.producers_id
