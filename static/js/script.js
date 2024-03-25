/* navbar on mobil size screens **/
document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.sidenav');
    var instances = M.Sidenav.init(elems);
});


document.addEventListener('DOMContentLoaded', function () {
    // Parse the JSON data passed from Django template
    const messages = JSON.parse('{{ messages_json|escapejs }}');

    // Initialize index for the while loop
    let i = 0;

    // Loop until the end of the messages array
    while (i < messages.length) {
        // Display toast message for the current message
        M.toast({ html: messages[i].html, classes: messages[i].tags });
        // Increment the index
        i++;
    }
});


