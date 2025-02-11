document.getElementById("signup-btn").addEventListener("click", function()
    {
        let email = document.getElementById("email").value.trim();
        let name = document.getElementById("name").value.trinm();
        let password = document.getElementById("password").value.trim();
        let dob = document.getElementById("dob").value.trim();

        let emailError = document.getElementById("email-error");
        let nameError = document.getElementById("name-error");
        let passwordError = document.getElementById("password-error");
        let dobError = document.getElementById("dob-error");

        emailError.textContent = "";
        nameError.textContent = "";
        passwordError.textContent = "";
        dobError.textContent = "";

        let hasError = false;

        if (!email)
        {
            emailError.textContent = "Email is required.";
            hasError = true;
        }

        if (!name)
        {
            nameError.textContent = "Name is required.";
            hasError = true;
        }

        if (!password)
        {
            passwordError.textContent = "Password is required.";
            hasError = True;
        }

        if (!dob)
        {
            dobError.textContent = "Date of Birth is required.";
            hasError = True;
        }

        if (email && (!email.includes("@") || email.startsWith("@") || email.endsWith("@")))
        {
            emailError.textContent = "Invalid email address.";
            hasError = true;
        }

        if (dobInput.valueAsNumber)
        {
            let birthDate = dobInput.valueAsNumber;
            let currentTime = Date.now();
            let ageMilliseconds = currentTime - birthDate;
            let ageYears = ageMilliseconds / (1000 * 60 * 60 * 24 * 365.25);

            if (ageYears < 13)
            {
                dobError.textContent = "You must be atleast 13 years old to sign up.";
                hasError = true;
            }
        }
        if(!hasError)
        {
            alert("Sign up was successful!");
        }
    });