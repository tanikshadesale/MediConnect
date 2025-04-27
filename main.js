// CHATBOT FUNCTION
async function sendMessage() {
    const userMessage = document.getElementById("userInput").value;
    const response = await fetch("http://localhost:5000/chatbot1.html", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ message: userMessage }),
    });
    const data = await response.json();
    document.getElementById("chatArea").innerText = data.reply;
}

// EMERGENCY MODE
let countdownInterval;
let secondsLeft = 5;

function activateEmergencyMode() {
    const existingBox = document.getElementById("emergencyBox");
    if (existingBox) existingBox.remove(); // Remove if already there

    const emergencyBox = document.createElement("div");
    emergencyBox.id = "emergencyBox";
    emergencyBox.innerHTML = `
    <div style="
      position:fixed;
      bottom:20px;
      right:20px;
      z-index:9999;
      background:red;
      color:white;
      padding:1rem;
      border-radius:10px;
    ">
      <p id="countdownText">Calling in 5 seconds...</p>
      <button onclick="cancelEmergency()" style="margin-top:5px;">Cancel</button>
    </div>
  `;

    document.body.appendChild(emergencyBox);

    secondsLeft = 5;
    countdownInterval = setInterval(() => {
        secondsLeft--;
        const text = document.getElementById("countdownText");
        if (text) text.innerText = `Calling in ${secondsLeft} seconds...`;

        if (secondsLeft === 0) {
            clearInterval(countdownInterval);
            window.location.href = "tel:112"; // or your emergency number
        }
    }, 1000);
}


function cancelEmergency() {
    clearInterval(countdownInterval);

    const textBox = document.getElementById("countdownText");
    if (textBox) {
        textBox.innerText = "Emergency cancelled.";
    }

    // Delay removal of the box
    setTimeout(() => {
        const emergencyBox = document.getElementById("emergencyBox");
        if (emergencyBox) {
            emergencyBox.remove();
        }
    }, 1000); // Show "cancelled" for 2 seconds, then remove box
}

// Navbar Toggle Functionality
$(document).ready(function(){
    // Toggle navbar on click
    $('.fa-bars').click(function(){
        $(this).toggleClass('fa-times');
        $('.navbar').toggleClass('nav-toggle');
    });

    // Scroll event to change header style
    $(window).on('scroll load', function(){
        $('.fa-bars').removeClass('fa-times');
        $('.navbar').removeClass('nav-toggle');

        // Add/remove active class based on scroll position
        if($(window).scrollTop() > 30) {
            $('header').addClass('header-active');
        } else {
            $('header').removeClass('header-active');
        }
    });
});
