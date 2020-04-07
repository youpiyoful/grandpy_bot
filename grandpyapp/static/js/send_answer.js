// const submit = document.getElementById('send');
const textareaToSubmit = document.getElementById('textarea');
const textareaToSubmitValue = textareaToSubmit.value;
// const baseUrl = 'http://127.0.0.1:5000/send_answer/'

const getResponseToAnswer = () => {
    const request = new XMLHttpRequest();
    // const url = baseUrl + textareaToSubmitValue;
    // console.log(url);
    request.open('GET', 'http://127.0.0.1:5000/send_answer/' + textareaToSubmitValue);
    console.log(request.responseType)
    console.log(request.responseText)
    return request.response
}

textarea.addEventListener("keydown", (event) => {
    if (event.keyCode == 13) {
        const response = getResponseToAnswer();
        console.log(response)
    }
})