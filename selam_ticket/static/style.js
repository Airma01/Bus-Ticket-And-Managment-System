const text = "Hello We Are Selam Bus Thanks For Your Choice"

let i = 0;
function typewriter() {
    if (i < text.length) {
        document.getElementById("typed").innerHTML += text.charAt(i);
        i++;
        setTimeout(typewriter, 70);
    }
}

window.onload = typewriter;


