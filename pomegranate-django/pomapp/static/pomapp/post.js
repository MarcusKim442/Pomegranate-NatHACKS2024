function showReaction(isPositive) {
    const container = document.querySelector('.icon-container');
    container.innerHTML = ''; // Clear the previous icon

    const icon = document.createElement('i');
    icon.classList.add('icon-animation');
    icon.style.fontSize = '500px'; // Set the size of the emoji or icon
    if (isPositive) {
        icon.innerText = '❤️';
    } else {
        icon.innerText = '💔';
    }

    container.appendChild(icon);

    // Remove the icon after the animation completes (2 seconds)
    setTimeout(() => {
        container.innerHTML = '';
    }, 2000);
}