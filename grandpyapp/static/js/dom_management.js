const historicContent = document.getElementById('historic-content');
const textarea = document.getElementById('textarea');
const loader = document.querySelector('loader');
const baseUrl = "https://grandpy-bot-2001.herokuapp.com/"; // in dev use http://127.0.0.1:5000

const createChatBox = (elt, valueToSave1, parent1) => {
    const para = document.createElement(elt); // create the main element p
    const node = document.createTextNode("~/.> " + valueToSave1); // write the text
    para.appendChild(node); // insert the text in the paragraphe html element
    parent1.appendChild(para); // insert the para element with text in the parent element
    return para // return the last paragraphe element created
};

// loader.innerHTML = 
// '<div class="preloader-wrapper small active">\
//     <div class="spinner-layer spinner-green-only">\
//         <div class="circle-clipper left">\
//             <div class="circle"></div>\
//         </div>\
//         <div class="gap-patch">\
//             <div class="circle"></div>\
//         </div>\
//         <div class="circle-clipper right">\
//             <div class="circle"></div>\
//         </div>\
//     </div>\
// </div>'

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
        const valueOfAnswer = textarea.value;
        const historicElt = createChatBox("p", textarea.value, historicContent);
        textarea.value = '';
        const p = historicElt;
        addClass(p, ['chatbox-text-wrap', 'chatbox-p', 'blue-text']);
        removeClass(historicContent, 'invisible');
        console.log("VALUE OF ANSWER : ", valueOfAnswer);
        console.log("if value", /[A-z]/.test(valueOfAnswer));
        if (/[A-z]/.test(valueOfAnswer)){
            console.log("value of answer is not null");
            fetch(baseUrl + '/send_answer?answer=' + valueOfAnswer, {
                method: 'GET'
                // body: json
            })
            .then(response => {
                console.log(response);
                if (response.status == 200) return response.json(); else return response.status;
            })
            .then(data => {
                console.log("data => ", data); // Prints result from `response.json()` in getRequest
                console.log("type of data => ", typeof(data));
                if (typeof(data) != "number" && data.data_google.candidates[0]) {
                    data_text = "Avant toute chose je tiens à préciser que je suis un peu sénile... \
                    Le lieu nommé " + data.data_google.candidates[0].name + " se trouve " + data.data_google.candidates[0].formatted_address + "."
                    if (data.data_wiki.wiki_response) {
                        data_text_wiki = " Tient j'oubliais, est ce que tu savais que " + data.data_wiki.wiki_response
                    }
                    else {
                        data_text_wiki = " Oups, j'ai rien a te dire à ce sujet... Même moi je ne sais pas tout !";
                    }
                } else {
                    data_text = "La sénilité me guette ! J'ai rien trouvé p'tit";
                    data_text_wiki = "";
                }

                console.log("data_text =", data_text)
                const historicElt1 = createChatBox("p", data_text, historicContent);
                const p = historicElt1;
                addClass(p, ['chatbox-text-wrap', 'chatbox-p', 'green-text']);
                if (data_text_wiki){
                    const historicElt2 = createChatBox("p", data_text_wiki, historicContent);
                    const p2 = historicElt2;
                    addClass(p2, ['chatbox-text-wrap', 'chatbox-p', 'green-text']);
                }
                
            })
            .catch(error => console.error("error => ", error))
        } else {
            console.log("value of answer is null");
            const textIsEmpty = createChatBox("p", "Ne soyez pas si timide !", historicContent);
            const p = textIsEmpty;
            addClass(p, ['chatbox-text-wrap', 'chatbox-p', 'green-text']);
        }
    }
});

// TODO: gérer les cas ou wiki et google ne retourne pas la même chose
// TODO mettre en place la sécurité avec google


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