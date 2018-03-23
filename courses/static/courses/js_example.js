
//https://www.youtube.com/watch?v=zPHerhks2Vg
var newItemCounter = 1;
var ourList = document.querySelector('#our-list');//document.getElementById('our-list');
var ourButton = document.getElementById('our-button');
var ourHeadline = document.getElementById('our-headline');
var listItems = document.getElementById("our-list").getElementsByTagName("LI");
                //document.querySelectorAll('our-list li');


ourList.addEventListener('click', activateItem);
function activateItem(xx){
    if(xx.target.nodeName == 'LI'){
    ourHeadline.innerHTML = xx.target.innerHTML;
    for (i = 0; i < xx.target.parentNode.children.length; i++){
        xx.target.parentNode.children[i].classList.remove('active');
    }
    xx.target.classList.add('active');
    }
}
//for (i = 0; i < listItems.length; i++){
//    listItems[i].addEventListener('click', activateItem)
//}
//function activateItem(){
//    ourHeadline.innerHTML = this.innerHTML;
//    for (i = 0; i < listItems.length; i++){
//swap our listItems for xx.target.parentNode.children b/c we want reference to element we clicked on 'xx.target'
// then select its parent so add .parentNode, then select children of that element...
//        listItems[i].classList.remove('active');
//    }
//    this.classList.add('active');
//}


ourButton.addEventListener('click', createNewItem);
function createNewItem(){
    ourList.innerHTML += '<li>new stoof ' + newItemCounter + '</li>'
    newItemCounter++;
}
