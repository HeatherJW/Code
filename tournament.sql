-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

CREATE TABLE players (
    id SERIAL primary key,
    name TEXT
    );

CREATE TABLE matches (
    player integer references players(id),
    wins integer default 0,
    losses integer default 0,
    matches integer default 0
    );
