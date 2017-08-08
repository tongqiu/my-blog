$(document).ready(function() {
    $("#menuButton").click(function(){
        if ($("#menu").hasClass("hidden")) {
            $("#menu").removeClass("hidden");
        } else {
            $("#menu").addClass("hidden");
        }
    }); 
});
