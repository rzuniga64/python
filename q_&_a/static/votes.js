/**
 * Created by John on 3/29/16.
 */
$(window).on('load', function() {
    console.log('the page is loaded');
});
$('.widget.upvote').on('click', function() {
    console.log('upvote was clicked');
    var state = $(this).attr('data-state');
    var down = 'down';
    var ansid = $(this).attr('data-aid');
    var downid = down.concat(ansid);
    var downvote = document.getElementById(downid);
    var downstate = $(downvote).attr('data-state');
    var score = 'score';
    var scoreid = score.concat(ansid);
    var scorefield = document.getElementById(scoreid);
    var intscore = parseInt($(scorefield).text());
    var checked  = state === 'checked';
    var nextState = checked ? 'unchecked' : 'checked';
    var elt = $(this);
    $.ajax('/api/update-upvote', {
        method: 'POST',
        data: {
            answer_id: $(this).attr('data-aid'),
            want_upvote: !checked,
            _csrf_token: csrfToken
        },
        success: function(data) {
            /* called when post succeeds */
            console.log('post succeeded with result %s', data.result);
            elt.attr('data-state', nextState);
            if (downstate == 'checked') {
                $(downvote).attr('data-state', 'unchecked');
            }
            if (nextState == 'checked' && downstate == 'checked') {
                intscore += 2;
                var newscore = intscore.toString();
                $(scorefield).text(newscore);
            }
            else if (nextState == 'checked' && downstate == 'unchecked') {
                intscore += 1;
                var newscore = intscore.toString();
                $(scorefield).text(newscore);
            }
            else {
                intscore -= 1;
                var newscore = intscore.toString();
                $(scorefield).text(newscore);
            }
        },
        error: function() {
            /* called when post fails */
            console.log('post failed');
            elt.attr('data-state', state);
        }
    });
});

$('.widget.downvote').on('click', function() {
    console.log('downvote was clicked');
    var state = $(this).attr('data-state');
    var up = 'up';
    var ansid = $(this).attr('data-aid');
    var upid = up.concat(ansid);
    var upvote = document.getElementById(upid);
    var upstate = $(upvote).attr('data-state');
    var score = 'score';
    var scoreid = score.concat(ansid);
    var scorefield = document.getElementById(scoreid);
    var intscore = parseInt($(scorefield).text());
    var checked  = state === 'checked';
    var nextState = checked ? 'unchecked' : 'checked';
    var elt = $(this);
    $.ajax('/api/update-downvote', {
        method: 'POST',
        data: {
            answer_id: $(this).attr('data-aid'),
            want_downvote: !checked,
            _csrf_token: csrfToken
        },
        success: function(data) {
            /* called when post succeeds */
            console.log('post succeeded with result %s', data.result);
            elt.attr('data-state', nextState);
            if (upstate == 'checked') {
                $(upvote).attr('data-state', 'unchecked');
            }
            if (nextState == 'checked' && upstate == 'checked') {
                intscore -= 2;
                var newscore = intscore.toString();
                $(scorefield).text(newscore);
            }
            else if (nextState == 'checked' && upstate == 'unchecked') {
                intscore -= 1;
                var newscore = intscore.toString();
                $(scorefield).text(newscore);
            }
            else {
                intscore += 1;
                var newscore = intscore.toString();
                $(scorefield).text(newscore);
            }
        },
        error: function() {
            /* called when post fails */
            console.log('post failed');
            elt.attr('data-state', state);
        }
    });
});
