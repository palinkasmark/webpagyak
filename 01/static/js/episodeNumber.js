function episodeNumber() {
    const liElement = document.querySelectorAll("li");
    for(let element = 0; element < liElement.length; element++) {
        if(element % 2 === 0) {
            liElement[element].classList.add("light-green-background");
        }else {
            liElement[element].classList.add("light-blue-background");
        }
    }
}