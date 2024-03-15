const editButtons = document.getElementsByClassName("btn-edit");
const jokeText = document.getElementById("joke_text");
const jokeForm = document.getElementById("EditJokeForm");
const submitButton = document.getElementById("submitButton");


for (let button of editButtons) {
  button.addEventListener("click", (e) => {
    let jokeId = e.target.getAttribute("joke_id");
    let jokeContent = document.getElementById(`joke${jokeId}`).innerText;
    jokeText.value = jokeContent;
    submitButton.innerText = "Update";
    jokeForm.setAttribute("action", `edit_joke/${jokeId}`);
  });
}