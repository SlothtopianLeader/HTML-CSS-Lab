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

    let tmp = document.createElement("div");
    tmp.classList.add("alert");
    document.body.appendChild(tmp);

    let Newtmp = document.createElement("div");
    Newtmp.classList.add("signIn");
    document.body.appendChild(Newtmp);
    
    if (emailX === "")
    {
        Newtmp.remove();
        tmp.appendChild(document.createTextNode("Email is required. "));
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
            Newtmp.remove();
            tmp.appendChild(document.createTextNode("Email must contain '@'. "));
            hasError = true;
        }
        else if (atIndex === 0)
        {
            Newtmp.remove();
            tmp.appendChild(document.createTextNode("Email cannot start with '@'. "));
            hasError = true;
        }
        else if (atIndex === emailX.length - 1)
        {
            Newtmp.remove();
            tmp.appendChild(document.createTextNode("Email cannot end with '@'. "));
            hasError = true;
        }
        else if (atIndex !== lastIndex)
        {
            Newtmp.remove();
            tmp.appendChild(document.createTextNode("Email can only contain one '@'. "));
            hasError = true;
        }
    }

    if (nameX === "")
    {
        Newtmp.remove();
        tmp.appendChild(document.createTextNode("Name is required. "));
        hasError = true;
    }

    if (passwordX === "")
    {
        Newtmp.remove();
        tmp.appendChild(document.createTextNode("Password is required. "));
        hasError = true;
    }

    if (dobX.value === "")
    {
        Newtmp.remove();
        tmp.appendChild(document.createTextNode("Date of Birth is required. "));
        hasError = true;
    }
    else
    {
        let birthDate = new Date(dobX);
        let ageMilliseconds = Date.now() - birthDate.getTime();
        let ageYears = ageMilliseconds / (1000 * 60 * 60 * 24 * 365.25);

        if (ageYears < 13)
        {
            Newtmp.remove();
            tmp.appendChild(document.createTextNode("You must be at least 13 years old to sign up. "));
            hasError = true;
        }
    }

    if (!hasError)
    {
        tmp.remove();
        Newtmp.appendChild(document.createTextNode("Welcome!"));
    }
};