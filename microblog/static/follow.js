/**
 * Created by Raul Zuniga on 4/10/2016.
 * Modfied by John McAlmon on 4/14/2016.
 */
$(document).ready(function(){
    $('.widget.follow-button').click(function() {
        var elt = $(this);
        if (state == 'waiting') {
            console.log('request in progress, dropping second click');
            return;
        }
        var state = elt.attr('data-state');
        var following  = state == 'following';
        var nextState = following ? 'not-following' : 'following';
        elt.attr('data-state', 'waiting');
        elt.text('Waiting...');
        $.ajax('/api/update-follow', {
            method: 'POST',
            data: {
                _csrf_token: csrfToken,
                followee_id: $('.user-profile').attr('data-followee-id'),
                followed: !following
            },
            success: function () {
                /* called when post succeeds */
                elt.attr('data-state', nextState);
                if ( !following ) {
                    console.log('Followed user');
                    elt.text('Unfollow');
                } else {
                    console.log('unfollowed');
                    elt.text('Follow');
                }
            },
            error: function () {
                /* called when post fails */
                elt.attr('data-state', state);
            }
        });
    });
});


