// This function changes the class value of table cells in accordance with the pattern of a 7 segment display. Refer hints 
function illuminate(num){
    num = Number(num);
    var pattern=["yyyyyyn","nyynnnn","yynyyny","yyyynny",
                 "nyynnyy","ynyynyy","ynyyyyy","yyynnn","yyyyyyy","yyyynyy"];
    return pattern[num];
        // REPLACE THIS CODE WITH YOUR illuminate() METHOD
}

// This function extracts digits from an input text and illuminates based on the digits based
function getDigits(text){
    //var text = document.getElementById("inputString").value;
    res=[];
    for (var i=0; i<text.length; i++){
        var ch =text[i]
        if (ch >='0' && ch <='9'){
            res.push(illuminate(ch))
        }
    }
     return res 
}
        // REPLACE THIS CODE WITH YOUR getDigits() METHOD