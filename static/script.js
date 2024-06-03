// script.js

const socket = io();

socket.on('connect', () => {
    console.log('Connected to WebSocket');
});

socket.on('agent_status', (data) => {
    console.log('Received status update:', data);
    const agentCard = document.getElementById(data.agent);
    if (agentCard) {
        agentCard.querySelector('.prompt').textContent = data.prompt || 'N/A';
        agentCard.querySelector('.response').innerHTML = formatCode(data.response);
    }
});

socket.on('disconnect', () => {
    console.log('Disconnected from WebSocket');
});

document.getElementById('generateAppForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    console.log("Form submitted");

    const prompt = document.getElementById('userPrompt').value;
    if (!prompt) {
        console.log("Prompt is empty");
        return;
    }

    // Disable the button and show the spinner
    const generateButton = document.querySelector('button[type="submit"]');
    generateButton.disabled = true;
    const spinner = document.createElement('div');
    spinner.className = 'spinner';
    generateButton.appendChild(spinner);

    try {
        console.log("Sending fetch request");
        const response = await fetch('/generate-app', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ prompt })
        });

        const result = await response.json();
        console.log("Fetch response received:", result);

        // Process the result to update the UI
        updateAgentStatuses(result);
    } catch (error) {
        console.error("Error generating app:", error);
    } finally {
        // Re-enable the button and remove the spinner
        generateButton.disabled = false;
        generateButton.removeChild(spinner);
    }
});

function updateAgentStatuses(statuses) {
    Object.keys(statuses).forEach(agent => {
        const card = document.getElementById(agent);
        if (card) {
            card.querySelector('.prompt').textContent = statuses[agent].prompt || 'N/A';
            card.querySelector('.response').innerHTML = formatCode(statuses[agent].response);
        }
    });
}

function formatCode(code) {
    if (typeof code === 'string') {
        return `<pre><code>${escapeHtml(code)}</code></pre>`;
    }
    return code;
}

function escapeHtml(unsafe) {
    return unsafe
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;')
        .replace(/'/g, '&#039;');
}
