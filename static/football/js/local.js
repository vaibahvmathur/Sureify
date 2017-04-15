$(document).ready(function(){
    $("#skill_1").click(function(){
        SortMe(1);
    });
    $("#skill_2").click(function(){
        SortMe(2);
    });
    $("#skill_3").click(function(){
        SortMe(3);
    });
    $("#skill_4").click(function(){
        SortMe(4);
    });
    $("#skill_4").click(function(){
        SortMe(4);
    });

    function SortMe(sort_with){
        $.ajax({
            url: "",
            type: 'POST',
            data: {
                "sort_with": sort_with
            },
            success: function(data) {
                $('.main-class').replaceWith(data);
            }
        });
    }

});