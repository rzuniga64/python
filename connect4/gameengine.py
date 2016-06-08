import base64
import os
import flask
import random
import routes
from flask_socketio import emit, join_room

from init import app, socketio

games = {}


class Player:
    position = None
    rematch = False

    def __init__(self, name):
        self.name = name


class Game:
    player_x = None
    player_y = None
    current = None
    finished = False
    winner = None


    def __init__(self, key):
        self.key = key
        self.board = [
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None]
        ]

    def reset(self):
        self.board = [
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None]
        ]
        self.finished = False
        self.winner = None

    def find_player(self, name):
        if self.player_y:
            if self.player_y.name == name:
                if name in routes.usernames:
                    return self.player_y
                else:
                    self.player_y = None
        if self.player_x:
            if self.player_x.name == name:
                if name in routes.usernames:
                    return self.player_x
                else:
                    self.player_x = None
        return None

    def find_other_player(self, name):
        if self.player_y:
            if self.player_y.name != name:
                if self.player_y.name in routes.usernames:
                    return self.player_y
                else:
                    self.player_y = None
        if self.player_x:
            if self.player_x.name != name:
                if self.player_x.name in routes.usernames:
                    return self.player_x
                else:
                    self.player_x = None
        return None

    def get_player(self, pos):
        if pos == 'X':
            return self.player_x
        elif pos == 'Y':
            return self.player_y
        else:
            return None

    def add_player(self, player):
        if self.player_x is None:
            self.player_x = player
            player.position = 'X'
            self.current = player
            return 'X'
        elif self.player_y is None:
            self.player_y = player
            player.position = 'Y'
            return 'Y'
        else:
            raise RuntimeError('game full')

    def remove_player(self, name):
        player = self.find_player(name)
        if player is not None:
            pos = player.position
            if pos is 'X':
                self.player_x = None
            else:
                self.player_y = None
            del player
            return True
        return False

    def is_empty(self):
        if self.player_x is None and self.player_y is None:
            return True
        return False


    @property
    def ready(self):
        return self.player_x is not None and self.player_y is not None

    #We do not need the row because conceptually we are placing pieces on top of a stack of columns
    def make_move(self, player, col):
        #We need row and maxRows to have a local variable because technically we have no control over exactly where pieces are being placed
        row = None
        maxRows = 5
        for j in range(6):
            if self.board[j][col] is None:
                row = j #Find the empty row-spot area where the piece will land
        #Checks to make sure the right player is making a move
        if player != self.current:
            raise RuntimeError('bad player')
        #Checks to see if the column the piece is dropped is already full by seeing if 'row' has updated from the previous for-loop above
        if row is None:
            raise RuntimeError('this column is already full.')

        self.board[row][col] = player.position
        self._check_for_winner(player.position)
        if self.current == self.player_x:
            self.current = self.player_y
        else:
            self.current = self.player_x

        return row

    def _check_for_winner(self, position):
        # count empty cells
        rAdjacents = 0
        cAdjacents = 0
        dlAdjacents = 0
        drAdjacents = 0
        pos = position
        empties = sum(((1 if cell is None else 0) for maxRows in self.board for cell in maxRows))

        #This algorithm brute forces a check on every possible row, column, and diagonal
        #This algorithm assumes that [0][0] is the top left corner and can possibly check for Connect 4+
        #and even multiple connect-4's.

        # check the rows for winners
        for i in range(6):
            if rAdjacents >= 4:
                break
            rAdjacents = 0
            for j in range(7):
                #For every row, check to see how many of the player's pieces in a sequence are there
                if self.board[i][j] is pos:
                    rAdjacents += 1 #Keep tallying up sequential pieces.
                else:
                    if rAdjacents >= 4: #If we reached the end of a chain and we got 4+, quickly leave the search algorithm
                        break
                    rAdjacents = 0 #Else just reset the adjacency counter and hope we can count another 4+ sequence
                if rAdjacents >= 4:
                    break

        # check the columns for winning condidtions
        for j in range(7):
            if cAdjacents >= 4:
                break
            cAdjacents = 0
            for i in range(6):
                #For every column, check to see how many of the player's pieces in a sequence are there
                if self.board[i][j] is pos:
                    cAdjacents += 1 #Keep tallying up sequential pieces.
                    print('[{}][{}] is {}'.format(i, j, pos))
                else:
                    if cAdjacents >= 4: #If we reached the end of a chain and we got 4+, quickly leave the search algorithm
                        break
                    cAdjacents = 0 #Else just reset the adjacency counter and hope we can count another 4+ sequence
                if cAdjacents >= 4: #Quickly break out of the for loop if connection is found
                    break

        # check diagonals along the the down-right '\' directions
        for a in range(6):
            if drAdjacents >= 4:
                break
            drAdjacents = 0
            i = 0
            j = 0
            #This if-else chain forcefully changes the starting position to the beginning of each '\' diagonal
            if a is 0:
                i = 2
            elif a is 1:
                i = 1
            elif a is 2:
                i = 0
            elif a is 3:
                j = 1
            elif a is 4:
                j = 2
            elif a is 5:
                j = 3

            while i < 6 and j < 7:
            #For piece along the down-right diagonal, check to see how many of the player's pieces in a sequence are there
                if self.board[i][j] is pos:
                    drAdjacents += 1 #Keep tallying up sequential pieces.
                else:
                    if drAdjacents >= 4: #If we reached the end of a chain and we got 4+, quickly leave the search algorithm
                        break
                    drAdjacents = 0 #Else just reset the adjacency counter and hope we can count another 4+ sequence
                if drAdjacents >= 4:
                    break
                i += 1
                j += 1

        # check along the down-left '/' diagonals
        for b in range(6):
            if dlAdjacents >= 4:
                break
            dlAdjacents = 0
            i = 0
            j = 6
            if b is 0:
                j = 3
            elif b is 1:
                j = 4
            elif b is 2:
                j = 5
            elif b is 3:
                j = 6
            elif b is 4:
                i = 1
            elif b is 5:
                i = 2

            while i < 6 and j >= 0:
            #For piece along the down-left diagonal, check to see how many of the player's pieces in a sequence are there
                if self.board[i][j] is pos:
                    dlAdjacents += 1 #Keep tallying up sequential pieces.
                else:
                    if dlAdjacents >= 4: #If we reached the end of a chain and we got 4+, quickly leave the search algorithm
                        break
                    dlAdjacents = 0 #Else just reset the adjacency counter and hope we can count another 4+ sequence
                if dlAdjacents >= 4:
                    break
                i += 1
                j -= 1


        if rAdjacents >= 4 or cAdjacents >= 4 or drAdjacents >= 4 or dlAdjacents >= 4:
            self.winner = self.get_player(pos)

        if not self.winner and empties == 0:
            self.winner = 'draw'

        if self.winner:
            self.finished = True


def create_game(player: Player, key) -> Game:
    xy = random.choice(['X', 'Y'])
    player.position = xy
    game = Game(key)
    if xy == 'X':
        game.player_x = player
        game.current = player
    else:
        game.player_y = player

    print('Created game ' + key)

    return game


@socketio.on('ready')
def on_player_ready(evt):
    user = evt['user']
    key = evt['game']
    game = games[key]
    print('ready to start ' + game.key)
    player = game.find_player(user)
    if player is None:
        app.logger.warn('player %s is not in game %s', user, key)
        return

    print('Player {} is ready'.format(player.name))
    print('Current player is ' + game.current.name)
    print('Position is ' + game.current.position)
    if game.ready:
        emit('start-turn', {'player': {
            'name': game.current.name,
            'position': game.current.position
        }}, room=key)
    for i, row in enumerate(game.board):
        for j, cell in enumerate(row):
            if cell is not None:
                emit('move', {'row': i, 'col': j, 'player': {'position': cell}})


@socketio.on('makemove')
def on_move(evt):
    app.logger.debug('received move request')
    name = evt['name']
    key = evt['game']
    game = games[key]
    player = game.find_player(name)
    if player is None:
        app.logger.warn('player %s is not in game %s', name, key)
        return
    if player != game.current or game.finished:
        app.logger.warn('move from non-current player')
        return # ignore the move

    col = evt['col']
    print('player {} moved to {}'.format(player.name, col))
    # make the move
    row = game.make_move(player, col)
    # notify the players
    emit('move', {
        'player': {
            'position': player.position,
            'name': player.name
        },
        'col': col,
        'row': row
    }, room=key)

    if game.finished:
        # game over
        winner = game.winner
        if winner is None:
            emit('game-over', {'winner': 'draw'}, room=key)
        else:
            emit('game-over', {'winner': {
                'name': winner.name,
                'position': winner.position
            }}, room=key)
    else:
        # new player
        emit('start-turn', {'player': {
            'name': game.current.name,
            'position': game.current.position
        }}, room=key)


@socketio.on('entergame')
def enter_game(json):
    sid = flask.session['sid']
    room = json['room']
    name = json['name']

    app.logger.debug('user %s joined %s', name, room)

    join_room(room)
    join_room(name)
    emit('user-joined', {'name': name}, room=room)
    game = games[room]
    player = game.find_player(name)
    # Send the player their position.
    emit('position', player.position, room=name)


@socketio.on('chat')
def on_chat(json):
    app.logger.info('received chat')
    sid = flask.session['sid']
    if json['sid'] != sid:
        return

    message = json['message']
    room = json['room']
    sender = json['name']

    app.logger.debug('user %s posted in %s', sender, room)

    emit('new-chat', {
        'message': message,
        'sender': sender
    }, room=room)


@socketio.on('rematch')
def on_rematch(json):
    key = json['game']
    username = json['player']
    game = games[key]
    print('{} requested a rematch for game {}'.format(username, key))
    player = game.find_player(username)
    if player is not None:
        player.rematch = True
        other_player = game.find_other_player(username)
        if other_player is None:
            if not routes.waitingroom.empty():
                print('Resetting game.')
                game.reset()
                emit('reset', 'reset', room=key)
                player.rematch = False
                new_player = routes.waitingroom.get()
                routes.matches[new_player] = {'this_user': new_player, 'other_user': username, 'key': key}
                emit('foundmatch', {'key': key, 'user': new_player}, room=new_player)
            else:
                emit('noplayers', 'noplayers', room=username)
        else:
            if other_player.rematch is True:
                player.rematch = False
                other_player.rematch = False
                print('Initiating rematch.')
                game.reset()
                emit('reset', 'reset', room=key)
                emit('start-turn', {'player': {
                    'name': game.current.name,
                    'position': game.current.position
                    }}, room=key)
            else:
                emit('noresponse', other_player.name, room=username)