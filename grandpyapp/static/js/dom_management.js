const historicContent = document.getElementById('historic-content');
const textarea = document.getElementById('textarea1');
// const textareaContainer = document.getElementById('textarea_container');
// const nodeContainer = document.getElementById('test');

const createChatBox = (elt, elt2, br, valueToSave, parent1) => {
    const para = document.createElement(elt);
    const span = document.createElement(elt2); //create main element
    const breakLine = document.createElement(br); // add a breakline
    const node = document.createTextNode(valueToSave); // write the text
    span.appendChild(node); // insert the text into main element
    para.appendChild(span);
    parent1.appendChild(para); // insert the span element with text in the parent element
    parent1.appendChild(breakLine); // insert the breakline in the parent element
    return [para, span] // return the last paragraphe element created
};


const removeClass = (eltToModify, classToRemove) => {
    eltToModify.classList.remove(classToRemove);
};

const addClass = (eltToModify, classesToAdd=[]) => {
    for (classToAdd of classesToAdd) {
        eltToModify.classList.add(classToAdd);
    }
};

const historicCreate = textarea.addEventListener("keyup", (e) => {
    if (e.keyCode === 13) {
        const historicElt = createChatBox("p", "span", 'br', textarea.value, historicContent);
        // console.log(historicContent)
        const p = historicElt[0];
        const sp = historicElt[1];
        console.log(p);
        console.log(sp);
        // addClass(p, ['grey']);
        addClass(sp, ['white-text']);
        removeClass(historicContent, 'invisible');
        textarea.value = ""
    }
});