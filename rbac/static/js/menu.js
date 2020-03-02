$('.item .title').click(function () {
    $(this).next().toggleClass('hide');
    $(this).parent().siblings().children(".body").addClass("hide")
});