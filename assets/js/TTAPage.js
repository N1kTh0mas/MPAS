let selectedGroup = '';
        let ttsText = '';

        document.addEventListener('DOMContentLoaded', function () {
            // Get all dropdown items and the default group
            const dropdownItems = document.querySelectorAll('.dropdown-item');
            const currentGroup = document.getElementById('currentgroup');
            const ttsTextarea = document.getElementById('TTS');
            const sendBtn = document.getElementById('sendBtn');

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

                // Now you can use the selectedGroup and ttsText variables as needed
                console.log('Selected Group:', selectedGroup);
                console.log('Text to Announce:', ttsText);

                // You can use these variables to send a message, make an API call, etc.
            });
        });
