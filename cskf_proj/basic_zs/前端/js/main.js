
$(function () {
    //弹框js
    $("#add").click(function () {
        $(".alter_back").addClass('show');
    });
    $(".alter_quite").click(function () {
        $(".alter_back").removeClass('show');
    });
    //侧边菜单js
    $(".left_menu_list h3").click(function () {
        // $(this).next().toggleClass('show')
        //     .parent().siblings().children('ul').removeClass('show')
        $(this).next().toggle()
            .parent().siblings().children('ul').hide()
    })
});