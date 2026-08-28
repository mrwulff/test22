//
// Schedulara Rhino Login Helper
//

window.schedulara = {

    loginFailed: function () {

        const button = document.getElementById("btnNewLogin");

        if (button) {
            button.disabled = false;
            button.value = "Login with Schedulara";
        }

        let error = document.getElementById("schedularaError");

        if (!error) {

            error = document.createElement("div");

            error.id = "schedularaError";

            error.style.background = "#ffe5e5";
            error.style.color = "#b00020";
            error.style.padding = "10px";
            error.style.marginBottom = "12px";
            error.style.borderRadius = "6px";
            error.style.fontWeight = "bold";

            const form = document.querySelector(".upperform");

            form.parentNode.insertBefore(error, form);
        }

        error.innerHTML =
            "Login failed. Please check your email and password.";
    }

};


(function waitForLogin() {

    //
    // Wait until Rhino finishes loading
    //

    const button = document.getElementById("btnNewLogin");

    if (!button) {
        setTimeout(waitForLogin, 250);
        return;
    }

    //
    // Remove any old error message
    //

    const oldError = document.getElementById("schedularaError");

    if (oldError)
        oldError.remove();

    //
    // Disable the alternate login
    //

    //
    // Disable SSN login only
    //

    [
        "socialsecuritynumber",
        "city",
        "zipcode",
        "btnSearch"
    ].forEach(function(id) {

        const el = document.getElementById(id);

        if (el) {
            el.disabled = true;
            el.style.opacity = "0.5";
            el.style.cursor = "not-allowed";
        }

    });

    const btnSearch = document.getElementById("btnSearch");

    if (btnSearch) {
        btnSearch.value = "Use Email Login Above";
    }

    //
    // Customize login button
    //

    button.value = "Login with Schedulara";
    button.style.fontWeight = "bold";

    //
    // Focus email field
    //

    const email = document.getElementById("emailaddress");

    if (email)
        email.focus();

    //
    // Override Rhino login
    //

    button.onclick = function (e) {

        e.preventDefault();
        e.stopPropagation();

        button.disabled = true;
        button.value = "Signing In...";

        const payload = {

            email:
                document.getElementById("emailaddress").value,

            password:
                document.getElementById("mypassword").value,

            url:
                location.href
        };

        location.href =
            "schedulara://login?"
            + encodeURIComponent(JSON.stringify(payload));

        return false;
    };

})();