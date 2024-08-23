// Function to show a modal with a message
function showModal(message) {
    const modalMessageContent = document.getElementById('modalMessage');
    modalMessageContent.innerHTML = message;
    const messageModal = new bootstrap.Modal(document.getElementById('messageModal'), {
        backdrop: 'static',
        keyboard: false
    });
    messageModal.show();
}

// Connect to the WebSocket server to listen for new messages
if (typeof io !== 'undefined') {  // Check if io is available
    var socket = io();  // Only call io() if it exists
    socket.on('new_message', function(data) {
        showModal(data.message);
    });
} else {
    console.error("Socket.IO not loaded");
}
