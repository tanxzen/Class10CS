const text = "Class 10 CS Study Guide";
const target = document.getElementById("typewriter");

let index = 0;
let isDeleting = false;

function typeWriterLoop() {
  if (!isDeleting) {
    target.textContent += text.charAt(index);
    index++;
    if (index < text.length) {
      setTimeout(typeWriterLoop, 100); // typing speed
    } else {
      setTimeout(() => {
        isDeleting = true;
        typeWriterLoop();
      }, 3000); // pause before deleting
    }
  } else {
    target.textContent = text.substring(0, index - 1);
    index--;
    if (index > 0) {
      setTimeout(typeWriterLoop, 100); // deleting speed
    } else {
      isDeleting = false;
      setTimeout(typeWriterLoop, 1000); // pause before typing again
    }
  }
}

window.onload = typeWriterLoop;
