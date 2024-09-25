document.getElementById('start-btn').addEventListener('click', () => {
    const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
    
    recognition.onresult = (event) => {
        const transcript = event.results[0][0].transcript;
        document.getElementById('response').innerText = `You said: ${transcript}`;
        
        // Send the transcript to the backend (Python code)
        sendToBackend(transcript);
    };
    
    recognition.start();
});

document.getElementById('send-btn').addEventListener('click', () => {
    const text = document.getElementById('text-input').value;
    document.getElementById('response').innerText = `You typed: ${text}`;
    
    // Send the text input to the backend
    sendToBackend(text);
});

function sendToBackend(command) {
    // Here you would typically make an AJAX call to your Python backend
    console.log(`Sending command to backend: ${command}`);

    // Example using fetch (assuming you have a backend API to handle this)
    // fetch('http://localhost:5000/command', {
    //     method: 'POST',
    //     headers: {
    //         'Content-Type': 'application/json'
    //     },
    //     body: JSON.stringify({ command: command })
    // })
    // .then(response => response.json())
    // .then(data => {
    //     console.log(data.response);
    //     document.getElementById('response').innerText += `\nAssistant: ${data.response}`;
    // })
    // .catch(error => console.error('Error:', error));
}
