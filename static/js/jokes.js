const editButtons = document.getElementsByClassName("btn-edit");
const jokeText = document.getElementById("joke_text");
const jokeForm = document.getElementById("jokeForm");
const submitButton = document.getElementById("submitButton");

/**
* Initializes edit functionality for the provided edit buttons.
* 
* For each button in the `editButtons` collection:
* - Retrieves the associated comment's ID upon click.
* - Fetches the content of the corresponding comment.
* - Populates the `commentText` input/textarea with the comment's content for editing.
* - Updates the submit button's text to "Update".
* - Sets the form's action attribute to the `edit_comment/{commentId}` endpoint.
*/
for (let button of editButtons) {
  button.addEventListener("click", (e) => {
    let jokeId = e.target.getAttribute("joke_id");
    let jokeContent = document.getElementById(`joke${jokeId}`).innerText;
    jokeText.value = jokeContent;
    submitButton.innerText = "Update";
    jokeForm.setAttribute("action", `edit_joke/${jokeId}`);
  });
}