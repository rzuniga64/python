/**
 * Created by John McAlmon on 4/14/16.
 */
$(document).ready(function() {
    $('#post-form').submit(function(event) {
        event.preventDefault(); // Prevents form from automatically sending POST request
        console.log('Clicked post button.');
        var button = $('#post-button');
        var state = button.attr('data-state');
        if (state == 'waiting') {
            console.log('request in progress, dropping second click');
            return;
        }
        button.text('Waiting...');
        button.attr('data-state', 'waiting');
        var textBox = $('#post-text');
        var urlBox = $('#url-text');
        var text = textBox.val(); // Get post text
        var url = urlBox.val(); //Retrieve URL text contents
        $.ajax('/api/post', {
            method: 'POST',
            data: {
                text: text,
                url: url,
                _csrf_token: csrfToken
            },
            success: function(result) {
                console.log('Submitted post.');
                textBox.val(''); // Clear text box
                urlBox.val(''); //Clear link text box
                button.text('Post!');
                button.attr('data-state', state);
                addPost(result);
            },
            error: function() {
                console.log('Post failed.');
                button.text('Post!');
                button.attr('data-state', state);
            }
         });
    });

    // Global mustache template for posts.
    var postTmpl = '<article class="post"> {{{ text }}}<br><a href="{{url}}">{{url}}</a><div class="author-info"><img class="post-avatar" src="https://www.gravatar.com/avatar/{{ grav_hash }}"> by <a href="/u/{{ creator }}">{{ creator }}</a><br> at &nbsp;{{ timestamp }}</div></article>';

    // Adds new post to top of timeline.
    function addPost(post) {
        var postElt = Mustache.render(postTmpl, post);
        console.log('generated HTML: %s', postElt);
        $('#timeline').prepend(postElt);
    }
});