$(document).ready(function() {
    $("#menuButton").click(function(){
        if ($("#menu").hasClass("hidden")) {
            $(this).addClass("change");
            $("#menu").removeClass("hidden");
        } else {
            $(this).removeClass("change");
            $("#menu").addClass("hidden");
        }
    });
});
