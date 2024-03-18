const deleteModal = document.getElementById("modal2");
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

/**
 * Geting the deleteing comments model confirm
 */

document.addEventListener('DOMContentLoaded', function() {
  var elems = document.querySelectorAll('.modal');
  var instances = M.Modal.init(elems, preventScrolling=true);
});


for (let button of deleteButtons) {
  button.addEventListener("click", (e) => {
    let jokeId = e.target.getAttribute("joke_id");
    deleteConfirm.href = `delete_joke/${jokeId}`;
    deleteModal.show();
  });
}


/**
 * Materlize drop down for categories
 */
document.addEventListener('DOMContentLoaded', function() {
  var elems = document.querySelectorAll('.dropdown-trigger');
  var instances = M.Dropdown.init(elems);
});