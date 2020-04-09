const historicContent = document.getElementById('historic-content');
const textarea = document.getElementById('textarea');

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
        addClass(p, ['chatbox-text-wrap', 'chatbox-p', 'blue-text']);
        removeClass(historicContent, 'invisible');
        fetch('http://127.0.0.1:5000/send_answer/' + textarea.value, {
            method: 'GET'
            // body: json
        })
        .then(response => {console.log(response); textarea.value = ""; return response.json()})
        .then(data => {
            console.log("data => ", data) // Prints result from `response.json()` in getRequest
            data_text = " Avant toute chose je tiens à préciser que je suis un peu sénile... Je peux peut être raconter des grosses ******. \
             Le lieu nommé " + data.candidates[0].name + " se trouve " + data.candidates[0].formatted_address
            console.log(data_text)
            const historicElt2 = createChatBox("p", data_text, historicContent);
            const p = historicElt2;
            addClass(p, ['chatbox-text-wrap', 'chatbox-p', 'green-text']);
        })
        .catch(error => console.error("error => ", error))
    }
});

// textarea.addEventListener("keyup", (event) => {
//     if (event.keyCode == 13) {
//         fetch('http://127.0.0.1:5000/send_answer/' + textareaToSubmitValue)
//         .then(response => response.json())
//         .then(data => {
//           console.log(data) // Prints result from `response.json()` in getRequest
//         })
//         .catch(error => console.error(error))
//     }
// })