const historicContent = document.getElementById('historic-content');
const textarea = document.getElementById('textarea');

const createChatBox = (elt, valueToSave1, parent1) => {
    const para = document.createElement(elt); // create the main element p
    const node = document.createTextNode("~/.> " + valueToSave1); // write the text
    para.appendChild(node); // insert the text in the paragraphe html element
    parent1.appendChild(para); // insert the para element with text in the parent element
    return para // return the last paragraphe element created
};


// this function take an html object and class to remove in parameter 
const removeClass = (eltToModify, classToRemove) => {
    eltToModify.classList.remove(classToRemove);
};


/* this function take an html object and a list of
class in parameter and add the classes on the html object */
const addClass = (eltToModify, classesToAdd=[]) => {
    for (classToAdd of classesToAdd) {
        eltToModify.classList.add(classToAdd);
    }
};

const historicCreate = textarea.addEventListener("keyup", (e) => {
    if (e.keyCode === 13) {
        const historicElt = createChatBox("p", textarea.value, historicContent);
        let valueOfAnswer = textarea.value
        textarea.value = ''
        const p = historicElt;
        addClass(p, ['chatbox-text-wrap', 'chatbox-p', 'blue-text']);
        removeClass(historicContent, 'invisible');
        fetch('http://127.0.0.1:5000/send_answer?answer=' + valueOfAnswer, {
            method: 'GET'
            // body: json
        })
        .then(response => {console.log(response); return response.json()})
        .then(data => {
            console.log("data => ", data) // Prints result from `response.json()` in getRequest
             
            if (data.data_google.candidates[0]) {
                data_text = "Avant toute chose je tiens à préciser que je suis un peu sénile... \
                Le lieu nommé " + data.data_google.candidates[0].name + " se trouve " + data.data_google.candidates[0].formatted_address + "."
                if (data.data_wiki.wiki_response) {
                    data_text_wiki = " Tient j'oubliais, est ce que tu savais que " + data.data_wiki.wiki_response
                }
            } else {
                data_text = "La sénilité me guette ! J'ai rien trouvé p'tit"
            }

            console.log(data_text)
            const historicElt1 = createChatBox("p", data_text, historicContent);
            const historicElt2 = createChatBox("p", data_text_wiki, historicContent);
            const p = historicElt1;
            const p2 = historicElt2;
            addClass(p, ['chatbox-text-wrap', 'chatbox-p', 'green-text']);
            addClass(p2, ['chatbox-text-wrap', 'chatbox-p', 'green-text']);
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