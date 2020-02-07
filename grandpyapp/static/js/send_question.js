function xhr_request(xhr_object, method, url, ){
    xhr.onreadystatechange = function () {

        // Only run if the request is complete
        if (xhr.readyState !== 4) return;

        // Process our return data
        if (xhr.status >= 200 && xhr.status < 300) {
            // What do when the request is successful
            console.log(JSON.parse(xhr.responseText));
        }

    };
    xhr.open(method, url);
    xhr.send();
}





