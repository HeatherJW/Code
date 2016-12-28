#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    conn = connect()
    c = conn.cursor()
    sql = 'DELETE FROM matches *;'
    c.execute(sql)
    conn.commit()
    c.close()
    conn.close()


def deletePlayers():
    """Remove all the player records from the database."""
    conn = connect()
    c = conn.cursor()
    sql = 'DELETE FROM players *;'
    c.execute(sql)
    conn.commit()
    c.close()
    conn.close()


def clearMatches():
    """Remove all the match records from the database."""
    conn = connect()
    c = conn.cursor()
    sql = 'UPDATE matches SET losses = 0, matches = 0, wins = 0;'
    c.execute(sql)
    conn.commit()
    c.close()
    conn.close()


def countPlayers():
    """Returns the number of players currently registered."""
    conn = connect()
    c = conn.cursor()
    sql = 'SELECT COUNT(*) FROM players'
    c.execute(sql)
    results = c.fetchall()
    c.close()
    conn.close()
    return results[0][0]


def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    conn = connect()
    c = conn.cursor()
    sql = 'INSERT INTO players (name) VALUES (%s);'
    data = (name, )
    c.execute(sql, data)
    conn.commit()
    sql = 'SELECT id FROM players WHERE name = %s;'
    data = (name, )
    c.execute(sql, data)
    player_id = c.fetchall()
    sql = 'INSERT INTO matches (player) VALUES (%s);'
    data = (player_id[0][0], )
    c.execute(sql, data)
    conn.commit()
    c.close()
    conn.close()

def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    conn = connect()
    c = conn.cursor()
    sql = 'SELECT id, name, wins, matches FROM matches, players WHERE matches.player = players.id ORDER BY wins desc;'
    c.execute(sql)
    results = c.fetchall()
    c.close()
    conn.close()
    standings = [result for result in results]
    return standings


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    conn = connect()
    c = conn.cursor()
    sql = 'UPDATE matches SET wins = 1, matches = 1, losses = 0 WHERE (player) = (%s);'
    data = (winner, )
    c.execute(sql, data)
    conn.commit()
    c.close()
    c = conn.cursor()
    sql = 'UPDATE matches SET losses = 1, matches =1, wins = 0 WHERE (player) = (%s);'
    data = (loser, )
    c.execute(sql, data)
    conn.commit()
    c.close()
    conn.close()
 
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    standings = playerStandings()
    pairs = []
    for i in range(0, len(standings) - 1, 2):
        if i == 0:
            pairs.append((standings[0][0], standings[0][1], standings[1][0], standings[1][1]))
        else:
            pairs.append((standings[i][0], standings[i][1], standings[i+1][0], standings[i+1][1]))
    return pairs
