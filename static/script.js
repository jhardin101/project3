const form = document.getElementById("messageForm");
const input = document.getElementById("messageInput");
const messageList = document.getElementById("messageList");

async function loadMessages(){
    const response = await fetch("/messages");

    const messages = await response.json();

    messageList.innerHTML = "";

    messages.forEach(message => {
        const li = document.createElement("li");
        li.textContent = message;
        messageList.appendChild(li);
    });
}

form.addEventListener("submit", async (event) => {
    event.preventDefault();

    await fetch("/messages", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            message: input.value
        })
    });
    input.value = "";
    loadMessages();
});

loadMessages();