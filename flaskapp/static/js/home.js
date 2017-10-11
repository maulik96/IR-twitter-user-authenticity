function tagUser (id, value) {
    $("#"+id).removeClass('no').removeClass('none').removeClass('yes');
    $("#"+id).addClass('pending');
    $.post("/tag/", {"user_id": id, "tag_value": value}, function(data, textStatus, xhr) {
        $("#"+id).removeClass('pending').addClass(value);
        console.log(data);
    });
}
