let selectedGroup = '';
let ttsText = '';
let piEndpoints = []; // To store the list of Raspberry Pi IPs

document.addEventListener('DOMContentLoaded', function () {
    // Get all dropdown items and the default group
    const dropdownItems = document.querySelectorAll('.dropdown-item');
    const currentGroup = document.getElementById('currentgroup');
    const ttsTextarea = document.getElementById('TTS');
    const sendBtn = document.getElementById('sendBtn');

    // Fetch the Raspberry Pi IPs from the config.json file
    fetch('/config.json')
        .then(response => {
            if (!response.ok) {
                throw new Error('Failed to load config.json');
            }
            return response.json();
        })
        .then(data => {
            piEndpoints = data.pi_endpoints;
            console.log('Loaded Raspberry Pi Endpoints:', piEndpoints);
        })
        .catch((error) => console.error('Error loading Pi endpoints:', error));

    // Set the default selected group to the first option (All)
    selectedGroup = dropdownItems[0].getAttribute('data-value');
    currentGroup.textContent = `Current selected group: ${selectedGroup}`;

    // Add click event listener to each dropdown item
    dropdownItems.forEach(function (item) {
        item.addEventListener('click', function (event) {
            event.preventDefault(); // Prevent default link behavior

            // Get the selected group's name from the data-value attribute
            selectedGroup = event.target.getAttribute('data-value');

            // Update the <p> element with the selected group's name
            currentGroup.textContent = `Current selected group: ${selectedGroup}`;
        });
    });

    // Add event listener to the Send button to store textarea value and selected group
    sendBtn.addEventListener('click', function () {
        // Store the value of the textarea
        ttsText = ttsTextarea.value;

        // Now you can use the selectedGroup, ttsText, and piEndpoints variables as needed
        console.log('Selected Group:', selectedGroup);
        console.log('Text to Announce:', ttsText);
        console.log('Pi Endpoints:', piEndpoints); // Shows the list of Raspberry Pi IPs

        // Example: Send message to each Raspberry Pi
        piEndpoints.forEach(endpoint => {
            sendMessageToBackend(endpoint, ttsText, selectedGroup);
        });
    });
});

// Function to send the message to the Raspberry Pi backend
function sendMessageToBackend(endpoint, ttsText, selectedGroup) {
    const payload = {
        message: ttsText,
        group: selectedGroup
    };

    fetch(endpoint, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(payload),
    })
    .then(response => response.json())
    .then(data => console.log(`Success on ${endpoint}:`, data))
    .catch((error) => console.error(`Error on ${endpoint}:`, error));
}
