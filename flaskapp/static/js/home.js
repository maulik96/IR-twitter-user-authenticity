function tagUser (id, handle, value) {
    $("#"+handle).removeClass('untagged').removeClass('no').removeClass('yes').removeClass('unsure');
    $("#"+handle).addClass('pending');
    $.post("/tag/", {"user_handle": handle, "tag_value": value}, function(data, textStatus, xhr) {
        $("#"+handle).removeClass('pending').addClass(value);
        console.log(data);
    });
}
