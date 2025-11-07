import fetch from "node-fetch";

const API_URL = "http://127.0.0.1:8000/send-prompt";

async function sendPrompt() {
    const response = await fetch(API_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ prompt: "Сколько я потратил на сигареты в этом месяце?" }),
    });

    const data = await response.json();
    console.log("Response:", data);
}

sendPrompt().catch(console.error);
