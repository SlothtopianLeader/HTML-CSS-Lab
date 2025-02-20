function SignUp()
    {
        "use strict";

        let email = document.getElementById("email");
        let emailX = email.value;
        let name = document.getElementById("name");
        let nameX = name.value;
        let password = document.getElementById("password");
        let passwordX = password.value;
        let dob = document.getElementById("dob");
        let dobX = dob.value;

        let hasError = false;


        if (emailX === "")
        {
            alert("Email is required.");
            hasError = true;
        }
        /*
        reference: https://www.geeksforgeeks.org/applications-of-string-indexof-method-in-java/
        */
        else
        {
            let atIndex = emailX.indexOf("@");
            let lastIndex = emailX.lastIndexOf("@");

            if (atIndex === -1)
            {
                alert("Email must contain '@'.");
                hasError = true;
            }
            else if (atIndex === 0)
            {
                alert("Email cannot start with '@'.");
                hasError = true;
            }
            else if (atIndex === emailX.length - 1)
            {
                alert("Email cannot end with '@'.");
                hasError = true;
            }
            else if (atIndex !== lastIndex)
            {
                alert("Email can only contain one '@'.");
                hasError = true;
            }
        }

        if (nameX === "")
        {
            alert("Name is required.");
            hasError = true;
        }

        if (passwordX === "")
        {
            alert("Password is required.");
            hasError = true;
        }

        if (dobX.value === "")
        {
            alert("Date of birth required.");
            hasError = true;
        }
        else
        {
            let birthDate = new Date(dobX);
            let ageMilliseconds = Date.now() - birthDate.getTime();
            let ageYears = ageMilliseconds / (1000 * 60 * 60 * 24 * 365.25);

            if (ageYears < 13)
            {
                alert("You must be at least 13 years old to sign up.");
                hasError = true;
            }
        }

        if (!hasError)
        {
            alert("Sign Up was successsful!");
        }
    };