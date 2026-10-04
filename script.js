const apiUrl = "http://127.0.0.1:8000/messages";

fetch(apiUrl)
    .then(response => response.json())
    .then(data => {
        console.log("Messages:", data);
    });

fetch(apiUrl, {
    method: "POST",
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify({
        message: "Hello from the browser"
    })
})
.then(response => response.json())
.then(data => {
    console.log("Posted:", data);
});