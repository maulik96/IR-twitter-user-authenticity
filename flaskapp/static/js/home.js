function tagUser (id, value) {
    $("#"+id).removeClass('untagged').removeClass('no').removeClass('yes').removeClass('unsure');
    $("#"+id).addClass('pending');
    $.post("/tag/", {"user_handle": id, "tag_value": value}, function(data, textStatus, xhr) {
        $("#"+id).removeClass('pending').addClass(value);
        console.log(data);
    });
}
