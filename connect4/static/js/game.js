var socket = io();
var position = 'Z';
var shell = $('.shell');
var key = shell.attr('data-key');
var sid = shell.attr('data-sid');
var user = shell.attr('data-nick');


console.log(key);
console.log(sid);

socket.on('connect', function() {
    if(user) {
        console.log('joining room %s as %s', key, user);
        socket.emit('entergame', {
            sid: sid,
            room: key,
            name: user
        });
        console.log(user + ' is ready.');
        socket.emit('ready', {user: user, game: key})
    }
});

socket.on('user-joined', function(msg) {
    $('<li>').append($('<span>').addClass('user').text(msg.name))
        .append(' has joined the chat')
        .appendTo($('#messages'));
});

$('.chat-input').on('submit', function(event) {
    event.preventDefault();
    var msg = $('#message').val();
    if (!msg) return;

    console.log('submitting message');
    socket.emit('chat', {
        sid: sid,
        room: key,
        message: msg,
        name: user
    });
    $('#message').val('');
});

socket.on('new-chat', function(msg) {
    $('<li>').addClass('message')
        .append($('<span>').addClass('user').text(msg.sender))
        .append(': ')
        .append($('<span>').addClass('text').text(msg.message))
        .appendTo($('#messages'))
});

// ============== Game logic ================

socket.on('start-turn', function(evt) {
    // it is someone's turn
    console.log('player %s turn', evt.player.position);
    if (evt.player.position == position) {
        $('#board').attr('data-state', 'active');
        $('.piece').prop('disabled', false);
        $('#status').text('It is your turn!');
    } else {
        $('#status').text('It is ' + evt.player.name + '\'s turn.');
    }
});

socket.on('move', function(move) {
    console.log('received move');
    // a move has been made
    var pos = move.player.position;
    var col = move.col;
    var row = move.row;
    console.log('%s dropped a piece on row %d column %d', pos, row, col);
    $('#cell-' + row + '-' + col).removeClass('empty').addClass(pos.toLowerCase());
    $('#piece-' + row + '-' + col).addClass(pos.toLowerCase());
});

socket.on('game-over', function(over) {
    console.log('game over');
    $('.overlay').show();
    if (over.winner == 'draw') {
        $('#gameover-message').text('The game finished in a draw.');
    } else {
        $('#gameover-message').text(over.winner.name + " has won the game");
    }
});

$('.piece').on('click', function() {
    console.log('Clicked a piece');
    var col = parseInt($(this).parent().attr('data-col'));
    if ($('#board').attr('data-state') != 'active') {
        console.log('Board is not active.');
        return;
    }
    if (!$(this).parent().hasClass('empty')) {
        console.log('Not empty!');
        return;
    }

    console.log('dropping piece to column # %d', col);
    socket.emit('makemove', {
        game: key,
        name: user,
        col: col
    });
    console.log('move requested');
    $('#board').attr('data-state', 'waiting');
});

socket.on('position', function(pos) {
   position = pos;
    console.log('Player\'s position is ' + position);
});


$('#rematchbutton').on('click', function() {
    console.log('Clicked rematch button.');
    socket.emit('rematch', {
        player: user,
        game: key
    })
});

socket.on('noresponse', function(resp) {
    player = resp;
    console.log('Waiting on response from' + player) ;
    $('#overlay-message').text('Waiting on response from ' + player + '. Please wait a moment and try again.');
});

socket.on('reset', function(resp) {
    $('.overlay').hide();
    $('.cell').addClass('empty').removeClass('y').removeClass('x');
    $('.piece').removeClass('y').removeClass('x');
    $('#board').removeAttr('data-state');
    $('.piece').prop('disabled', true);
    $('#overlay-message').text('');
});

socket.on('noplayers', function(resp) {
    $('#overlay-message').text('There are currently no available players. Try again or pick another option.');
});

$(window).load(function() {
    $('.overlay').hide();
});
