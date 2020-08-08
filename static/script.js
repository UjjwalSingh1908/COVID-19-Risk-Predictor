const a = document.getElementById('p');
let n = a.innerHTML.length;
if(n==22) {
a.classList.add('green-background');
}
else if(n==25){
  a.classList.add('orange-background');  
}
else if(n==23 || n==28){
  a.classList.add('red-background');  
}
else{
    a.classList.add('white-background');
}