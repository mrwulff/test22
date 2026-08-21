(function () {

    console.log("ThinkRhino JS loaded");

    const button = document.getElementById("btnNewLogin");

    if (!button) {
        console.log("Button not found");
        return;
    }

    button.addEventListener("click", function (e) {

        e.preventDefault();
        e.stopPropagation();

        location.href = "schedulara://hello";

    }, true);

})();