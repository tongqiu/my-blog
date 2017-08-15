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

    $("#homepageName").click(function(){
        if ($("#homepageQuote").hasClass("hidden")) {
            $("#homepageQuote").removeClass("hidden");
            $(this).text("quoting");
            $(this).removeClass("homepage-name");
        }
    });
});
