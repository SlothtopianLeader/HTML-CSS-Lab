def get(): return """

<!DOCTYPE html>
<html>
<head>
<style>

div.dialog {
    
    border: 2px double black;
    background: white;
    padding-top: 0em;
    padding-left: 1em;
    padding-right: 1em;
    padding-bottom: 1em;

    /* center the div vertically and horizontally
       ref: https://stackoverflow.com/a/13356401 */
    position: absolute;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    margin: auto;

    /* set size of dialog */
    width: 40vw;
    height: 40vh;

    overflow: auto;

    /* offset x, offset y, blur radius, color*/
    box-shadow: 1em 1em 0.5em rgba(0,0,0,0.5);

    z-index: 10;
}

.title {
    font-weight: bold;
    text-align: center;
    margin-bottom: 1em;
    color: black;
    padding: 0.5em;
}

div.button {
    border: 3px outset;
    margin: 1em;
    padding: 1em;
    background: lightgrey;
    text-align: center;
}

</style>
<body>

<div class="dialog">
    <div class="title">Sign up</div>
    <hr>
    <div>Email</div>
    <input size=30>
    <div>Real Name</div>
    <input size=30>
    <div>Password</div>
    <input size=30>
    <div>Date of Birth</div>
    <div class="button">Sign Up</button>
</div>
     
</body>
</html>"""