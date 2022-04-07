function getValue(radio) {
    if(radio.value=="collage"){
        document.getElementById("divcollage").style.visibility = "visible";
        document.getElementById("divexam").style.visibility = "hidden";
    } 
    else if(radio.value=="exam"){
        document.getElementById("divexam").style.visibility = "visible";
        document.getElementById("divcollage").style.visibility = "hidden";
    }
    else{
        document.getElementById("divexam").style.visibility = "hidden";
        document.getElementById("divcollage").style.visibility = "hidden";
    }
}






