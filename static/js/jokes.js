const deleteModal = document.getElementById("modal2");
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

/**
 * Geting the deleteing comments model confirm
 */

document.addEventListener('DOMContentLoaded', function () {
  var elems = document.querySelectorAll('.modal');
  var instances = M.Modal.init(elems, preventScrolling = true);
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
document.addEventListener('DOMContentLoaded', function () {
  var elems = document.querySelectorAll('.dropdown-trigger');
  var instances = M.Dropdown.init(elems);
});

/**
 * Materlize drop down in add jokes
 */
document.addEventListener('DOMContentLoaded', function () {
  var elems = document.querySelectorAll('select');
  var instances = M.FormSelect.init(elems,);
});

/**
 * Materlize tooltip, "comments above the buttons"
 */
document.addEventListener('DOMContentLoaded', function () {
  var elems = document.querySelectorAll('.tooltipped');
  var instances = M.Tooltip.init(elems);
});

/**
 * Rating"
 */
document.querySelectorAll('.rate-star').forEach(star => {
  star.addEventListener('click', function() {
      const rating = parseInt(this.getAttribute('data-rating'));
      const jokeId = parseInt(this.getAttribute('data-joke-id'));
      console.log(`Rating: ${rating}, Joke ID: ${jokeId}`);
      rate(rating, jokeId);
  });
});

const rate = (user_rating, jokeId) => {
  console.log('Sending rating request...');
  fetch(`/rate/${jokeId}/${user_rating}/`, {
      method: 'GET',
      headers: {
          'Content-Type': 'application/json'
      }
  }).then(response => {
      console.log('Response received:', response);
      if (response.status === 200) {
          console.log('Rating successful, reloading page...');
          window.location.reload();
      } else {
          console.error('Failed to rate joke:', response.statusText);
      }
  }).catch(error => {
      console.error('Error rating joke:', error);
  });
};