function tagUser (id, handle, value) {
    $("#"+id).removeClass('untagged').removeClass('no').removeClass('yes').removeClass('unsure');
    $("#"+id).addClass('pending');
    $.post("/tag/", {"user_handle": handle, "tag_value": value}, function(data, textStatus, xhr) {
        $("#"+id).removeClass('pending').addClass(value);
        console.log(data);
    });
}
