const historicContent = document.getElementById('historic-content');
const textarea = document.getElementById('textarea1');

const createChatBox = (elt, valueToSave, parent1) => {
    const para = document.createElement(elt); // create the main element p
    const node = document.createTextNode("~/.> " + valueToSave); // write the text
    para.appendChild(node); // insert the text in the paragraphe html element
    parent1.appendChild(para); // insert the para element with text in the parent element
    return para // return the last paragraphe element created
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
        const historicElt = createChatBox("p", textarea.value, historicContent);
        const p = historicElt;
        console.log(p);
        addClass(p, ['chatbox-text-wrap', 'chatbox-p', 'green-text']);
        removeClass(historicContent, 'invisible');
        textarea.value = ""
    }
});