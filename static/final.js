window.addEventListener("load", () => {
    const card = document.querySelector(".card");
    if(!card) return;

    card.style.opacity = "0";
    card.style.transform = "translateY(40px)";

    setTimeout(() => {
        card.style.transition = "1s ease";
        card.style.opacity = "1";
        card.style.transform = "translateY(0)";
    }, 200);
});



const inputs = document.querySelectorAll("input, select");

inputs.forEach(input => {
    input.addEventListener("focus", () => {
        input.style.boxShadow = "0 0 12px #0b1d3a";
        input.style.transform = "scale(1.05)";
    });

    input.addEventListener("blur", () => {
        input.style.boxShadow = "none";
        input.style.transform = "scale(1)";
    });
});

const form = document.querySelector("form");
const button = document.querySelector("button");

if(form){
form.addEventListener("submit", function () {
    button.innerHTML = "⏳ Predicting...";
    button.style.opacity = "0.7";
    button.style.pointerEvents = "none";
});
}



const card = document.querySelector(".card");

document.addEventListener("mousemove", (e) => {
    if(!card) return;

    let x = (window.innerWidth / 2 - e.pageX) / 40;
    let y = (window.innerHeight / 2 - e.pageY) / 40;

    card.style.transform = `rotateY(${x}deg) rotateX(${y}deg)`;
});



const alertBox = document.querySelector(".alert");

if (alertBox) {
    alertBox.style.opacity = "0";
    alertBox.style.transform = "translateY(20px)";

    setTimeout(() => {
        alertBox.style.transition = "0.6s";
        alertBox.style.opacity = "1";
        alertBox.style.transform = "translateY(0)";
    }, 300);
}
