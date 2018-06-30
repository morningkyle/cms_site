function initialize_navigation_bar(bar_id)
{
    // Rename the class name of current clicked navigation item
    var nav = document.getElementById(bar_id);
    if (nav == null) {
        console.log("Failed to find id: " + bar_id);
        return;
    }
    var items = nav.getElementsByTagName("a");
    for (var i = 0; i < items.length; i++) {
        items[i].addEventListener("click", function() {
            var current = document.getElementsByClassName("active");
            current[0].className = current[0].className.replace("active", "");
            this.className = "active";
        });
    }
}

initialize_navigation_bar("top_nav_bar");
initialize_navigation_bar("bottom_nav_bar");


