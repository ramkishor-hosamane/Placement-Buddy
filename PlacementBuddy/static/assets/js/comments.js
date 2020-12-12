function send_comment(post_id){
    $.ajax({
        type: 'GET',
        url: "/newsfeed",
        dataType: 'json',
        data: {
            'post_id':post_id,
            'comment': $("#comment").val(),
        },
        success: function(data) {
            $('#all-comment-container').append('\
                                                <div class="row card comment-card">\
                                                    <div class="col-5 comment-user">\
                                                        <img class="card-profile-photo" src="'+data.profile_pic_url+'" alt="">\
                                                        <span>'+data.comment_user+'</span>\
                                                    </div>\
                                                    <div class="col-5 comment-user-comment">\
                                                        <span>'+$("#comment").val()+'</span>\
                                                    </div>\
                                                </div>\
                                              ')
            $("#comment").val('');
        }
    });
}



function star_post(btn,post_id){
        
    $.ajax({
        type: 'GET',
        url: "/newsfeed",
        dataType: 'json',
        data: {
            'post_id':post_id,
            'star': '',
        },
        success: function(data) {
           
            $(btn).find("span").toggleClass('checked');
        }
    });
    
}