const counter = document.querySelector("#counter");
const increaseButton = document.querySelector("#increase-button");
const decreaseButton = document.querySelector("#decrease-button");

increaseButton.addEventListener("click", () => {
    counter.textContent = Number(counter.textContent) + 1;
});

decreaseButton.addEventListener("click", () => {
    if (Number(counter.textContent) > 0) {
        counter.textContent = Number(counter.textContent) - 1;
    }
});
