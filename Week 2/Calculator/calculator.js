function updateTextbox(value){
  document.getElementById("screen").value += value;
}


//result(), will evaluates all the text data written in the screen textbox using javascript's Eval function
function result(){
  document.getElementById("screen").value = eval(document.getElementById("screen").value);
}

//reset(), will clear's the screen textbox data
function reset(){
  document.getElementById("screen").value = '';
}
