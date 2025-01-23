def get(): return """

<!DOCTYPE html>
<html>
<head>
<title>Posts</title>
</head>
<style>

div.box {
    
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

div.entry {
    
    border: 1px double black;
    background:  #cde5e5;
    padding-top: 0em;
    padding-left: 1em;
    padding-right: 1em;
    padding-bottom: 0em;

    /* center the div vertically and horizontally
       ref: https://stackoverflow.com/a/13356401 */
    position: relative;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    margin: auto;

    /* set size of dialog */
    width: 40vw;
    height: 10vh;

    overflow: auto;

    z-index: 10;
}

.title {
    font-weight: bold;
    text-align: center;
    margin-bottom: 1em;
    color: black;
    padding: 0.5em;
}

</style>
<body>

<div class='titlebar' align="center">
<font color="black" size=30>
    Posts
</font>
</div>

<div class="box">
    <div class="entry">
    <div>
    <img src="/html/Doge.png" width="64" height="64">
    </div>
    </div>
    
    <div class="entry">
    <div>
    <img src="/html/Sunset.png" width="64" height="64">
    </div>
    </div>
    
    <div class="entry">
    <div>
    <img src="/html/Stitch.png" width="64" height="64">
    </div>
    </div>
</div>
     
</body>
</html>"""