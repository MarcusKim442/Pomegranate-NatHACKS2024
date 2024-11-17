function showReaction(isPositive) {
  const container = document.querySelector(".icon-container");
  container.innerHTML = ""; // Clear the previous icon

  const icon = document.createElement("div");
  icon.classList.add("icon-animation");
  icon.style.fontSize = "100px"; // Set the size of the emoji or icon
  if (isPositive) {
    icon.innerText = "❤️";
    likeButtonPommed();
  } else {
    icon.innerText = "💔";
    negativePostSlide();

    setTimeout(() => {
      const div = document.querySelector(".post-id-holder");
      const next_post_id = div.getAttribute("next_post_id");
      // Demonstration mockup: only 6 posts exist
      if (next_post_id < 6) {
        window.location.href = `/pomapp/post/${next_post_id}`;
      }
    }, 3000);
  }

  container.appendChild(icon);

  // Remove the icon after the animation completes (2 seconds)
  setTimeout(() => {
    container.innerHTML = "";
  }, 2000);
}

function likeButtonPommed() {
  // Get the button with the class "like"
  const button = document.querySelector(".like");

  // Check if the button exists to avoid errors
  if (button) {
    // Add the "like-added" class to the button
    button.className = "like like-pommed";

    // Change the button text
    button.textContent = "🤍 Pommed!";
  } else {
    console.error('Button with class "like" not found');
  }
}

function negativePostSlide() {
  // Get the button with the class "like"
  const container = document.querySelector(".post-container");

  // Check if the button exists to avoid errors
  if (container) {
    // Add the "like-added" class to the button
    container.className = "post-container post-negative-animation";
  } else {
    console.error("Container not found");
  }
}

function removePomegranalyzing() {
  const div = document.querySelector("#pomegranalyzing");
  if (div) {
    div.classList.add("display-none");
  } else {
    console.error("div not found");
  }
}

// Fetch data based on page trigger, rather than on a timer
async function sendDataTrigger() {
  var response = await fetch("/begin-collection");
  response = await response.json();
  console.log(response.data);
  if (response.data === 0) {
    // Negative
    showReaction(false);
  }
  if (response.data === 2) {
    // Positive
    showReaction(true);
  }
  removePomegranalyzing();
}

sendDataTrigger();
