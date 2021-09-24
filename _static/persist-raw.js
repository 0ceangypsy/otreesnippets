function persistInput(inp) {
    let isCheckboxOrRadio = ['checkbox', 'radio'].includes(inp.type);
    /*  checkboxes work differently from other form inputs.
        The 'checked' attribute stores whether it's checked or not.
        'valueInput' should generally be hardcoded to 1.
     */
    let valueAttr = isCheckboxOrRadio ? 'checked' : 'value';

    let key = `input-${pageNumber}-${inp.name}`;

    let storedValue = sessionStorage.getItem(key);

    if (storedValue != null) {
        inp[valueAttr] = storedValue;
    }

    inp.addEventListener('input', function () {
        let curValue = inp[valueAttr];
        // needed because sessionStorage implicitly converts true/false to strings
        if (isCheckboxOrRadio) curValue = curValue ? 'checked' : '';
        sessionStorage.setItem(key, curValue);
    });
}

// since sessionStorage persists across pages,
// we don't want to contaminate other pages in the same session
// whose fields happen to have the same name.
let urlParts = window.location.pathname.split('/');
let lastIndex = urlParts.length - 1
let pageNumber = urlParts[lastIndex];
// in case the path somehow has a trailing slash
if (pageNumber === '') pageNumber = urlParts[lastIndex - 1];

document.addEventListener("DOMContentLoaded", function (event) {
    for (let inp of document.getElementsByClassName('persist')) {
        persistInput(inp);
    }
});


