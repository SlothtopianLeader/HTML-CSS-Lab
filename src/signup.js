function SignUp()
    {
        "use strict";

        let email = document.getElementById("email");
        let emailX = email.value.trim();
        let name = document.getElementById("name");
        let nameX = name.value.trim();
        let password = document.getElementById("password");
        let passwordX = name.value;
        let dob = document.getElementById("dob");
        let dobX = dob.value;

        let emailError = document.getElementById("email-error");
        let nameError = document.getElementById("name-error");
        let passwordError = document.getElementById("password-error");
        let dobError = document.getElementById("dob-error");

        emailError.textContent = "";
        nameError.textContent = "";
        passwordError.textContent = "";
        dobError.textContent = "";

        let hasError = false;

        if (!emailX)
        {
            emailError.textContent = "Email is required.";
            hasError = true;
        }
        else if (!emailX.includes("@") || emailX.startsWith("@") || emailX.endsWith("@"))
        {
            emailError.textContent = "Invalid email address.";
            hasError = true;
        }

        if (!nameX)
        {
            nameError.textContent = "Name is required.";
            hasError = true;
        }

        if (!passwordX)
        {
            passwordError.textContent = "Password is required.";
            hasError = true;
        }

        if (!dobX)
        {
            dobError.textContent = "Birth Date is required.";
            hasError = true;
        }
        else
        {
            let birthDate = new Date(dobX).getTime();
            let currentTime = Date.now();
            let ageMilliseconds = currentTime - birthDate;
            let ageYears = ageMilliseconds / (1000 * 60 * 60 * 24 * 365.25);

            if (ageYears < 13)
            {
                dobError.textContent = "You have to be at least 13 years old to sign up.";
                hasError = true;
            }
        }

        if (!hasError)
            alert("Sign up was successful!");

    };