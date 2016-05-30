// Create a socket.
var socket = io();

function scrollChat() {
    // a jQuery result is a list, get the first element
    var chat = $('#messages')[0];
    // figure out the height the *top* of window should scroll to
    var pos = chat.scrollHeight - chat.clientHeight;
    chat.scrollTop = pos;
}

$(document).ready(function() {
    var datakey = $('.chatwindow').attr("data-key");
    var datanick = $('.chatwindow').attr("data-nick");
    
    socket.on('connect', function () {
        var data = {
            room: datakey, 
            name: datanick
        }
        socket.emit('joined', data);
    });

    socket.on('status', function (data) {
        $('#messages').append($('<li>').addClass('received').text(data.msg));
        scrollChat();
    });

    /* Listen to new chats on the form */
    $('.chat-input').on('submit', function (event) {
        // don't really submit the form we handle in JS, a real submit would reload page
        event.preventDefault();

        // get the value of the message element
        var room = $('#room').text();
        var msg = $('#message').val();
        var data = {
            message:msg,
            room: datakey, 
            name: datanick
        }
        // reset the message input
        $('#message').val('');

        // send the message to the server
        //socket.send(msg);
        socket.send(data);
        scrollChat();
    });

    /* listen for replies */
    socket.on('message', function (event) {
        // add it to the list!
        $('#messages').append($('<li>').addClass('received').text(event.msg));
        scrollChat();
    });
    
    socket.on('disconnect', function () {
        var data = {
            room: datakey
        }
        socket.emit('disconnect', data);
    });

});