// const submit = document.getElementById('send');
const textarea = document.getElementById('textarea');
const textareaValue = textarea.value;

const getResponseToAnswer = () => {
    const request = new XMLHttpRequest();
    const url = 'http://127.0.0.1:5000/send_answer/' + textareaValue;
    console.log(url);
    request.open('GET', url);
    return request.response
}

textarea.addEventListener("keydown", (event) => {
    if (event.keyCode == 13) {
        const response = getResponseToAnswer();
        console.log(response)
    }
})