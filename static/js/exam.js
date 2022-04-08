function getValue(radio) {
    if(radio.value=="Examdetails"){
        document.getElementById("divexam").style.visibility = "visible";
        document.getElementById("divseat").style.visibility = "hidden";
    } 
    else if(radio.value=="Seatno"){
        document.getElementById("divseat").style.visibility = "visible";
        document.getElementById("divexam").style.visibility = "hidden";
    }
    else{
        document.getElementById("divseat").style.visibility = "hidden";
        document.getElementById("divexam").style.visibility = "hidden";
    }
}