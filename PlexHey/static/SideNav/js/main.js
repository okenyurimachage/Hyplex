'use strict';

window.onload = () => {
    var doc = document;

    // /form divs
    var firstForm = doc.getElementById('first-form'),
        secondForm = doc.getElementById('second-form');

    // next buttons
    var nextBtn = doc.getElementById('nextBtn');

    //submit cotainer
    var submitCntr = doc.getElementById('submit-container');

    //Links
    var firstLink = doc.getElementById('first-link'),
        secondLink = doc.getElementById('second-link');

    nextBtn.addEventListener('click', (event) => {
        event.preventDefault();

        firstForm.classList.add('hidden');
        secondForm.classList.remove('hidden');
        submitCntr.classList.remove('hidden');
        nextBtn.classList.add('hidden');

        //links
        firstLink.classList.remove('active');
        secondLink.classList.add('active');
    });
}