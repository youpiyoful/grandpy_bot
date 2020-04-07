const form = document.getElementById('send');

const sendForm = () => {
    const request = new XMLHttpRequest();
    request.open('GET', 'http://127.0.0.1:5000/send_answer/<answer>')
}
form.addEventListener("click", (event) => {
    
})