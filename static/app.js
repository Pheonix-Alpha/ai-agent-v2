async function sendMessage() {
    const input = document.getElementById("query");
    const chat = document.getElementById("chat");

    const query = input.value;

    if (!query) return;

    chat.innerHTML += `
        <div class="user">
            ${query}
        </div>
    `;

    input.value = "";

    const response = await fetch("/ask", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            query
        })
    });

    const data = await response.json();

    chat.innerHTML += `
        <div class="bot">
            ${data.answer}
            <div class="route">
                ${data.route}
            </div>
        </div>
    `;

    chat.scrollTop = chat.scrollHeight;
}