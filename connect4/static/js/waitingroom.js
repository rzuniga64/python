/**
 * Created by John on 5/3/16.
 */

var socket = io();
var username = $('#waitingroom-wrapper').attr('data-username');

socket.on('connect', function() {
    console.log('Joining waiting room as ' + username);
    socket.emit('joinwaitingroom', username);
});

socket.on('foundmatch', function(resp) {
    var key = resp.key;
    console.log('Found a match with player ' + resp.user);
    console.log('Allow redirect to room ' + key);
    $('#join-button').prop('disabled', false);
    $('#key-input').attr('value', key);
    $('#user-input').attr('value', username);
});

socket.on('msg', function(msg) {
    console.log(msg);
});