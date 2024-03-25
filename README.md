# DADDJOKES

Dadjokes is not just another website; it's your go-to destination for a guaranteed laugh! Whether you're in the mood for a quick chuckle or eager to share your own comedic gems, Dadjokes promises to leave you amused. With a diverse collection of jokes catering to various tastes and humor styles, there's something for everyone.
As a registered user, you have the power to like, comment on, and rate every joke you come across. Feeling hesitant about sharing your own joke? Fear not! Dadjokes encourages creativity and welcomes contributions from users like you. Plus, you have the flexibility to edit or delete your joke at any time, ensuring that you feel comfortable and in control of your content.

![Am I Responsive](documentation/readme_img/amiresponsive.png)

LIVE LINK HERE

## User Experience

### Project Goals

The goal for DADJOKES was to create an easy-to-navigate site that users can visit when they lie on the couch watching a bad movie or are on the train during a workday morning. It should be a site where users can get away for a little while.

### Agile Methodology

Agile Methodology was used to help prioritize and organize tasks for the hole webpage. I used Project Boards on Github.

* Epics were written containing possible user stories and based on that the website was made.
* User stories were created by looking at epics and added on as the project was advancing.
* Project Board was used to track progression of the task through the Todo, In progress and Done columns

<details>
<summary> Userstories / Project board
</summary>

![userstories.png](documentation/readme_img/userstories.png)
![projectboard.png](documentation/readme_img/projectboard.png)
![issues.png](documentation/readme_img/issues.png)
</details>


To see the Epic and user stroies in full: [project board](https://github.com/users/LindaAPersson/projects/6)

### User Stories

#### First time user

As a first-time user of DADJOKES, I want to easily navigate the website,
so I can quickly find and enjoy a variety of funny jokes and anecdotes.
I also want clear instructions on how to interact with the site,
such as registrer, liking and commenting on jokes,
so I can fully engage with the community and have a positive experience.

#### Registred user

As a registered user of DADJOKES I want to have the ability to like, comment on, and rate jokes, so I can interact with the content and contribute to the community's enjoyment.
Additionally, I want the option to add my own jokes to the platform. I also want to be able to edit and delet my comments and jokes. 

#### Admin user

As an admin user of DADJOKES, I want to have access to backend functionalities,
so I can manage and moderate the content effectively.
I also want the ability to review and approve user-submitted jokes,
so I can ensure the quality and appropriateness of the content on the platform.

## Design

I want DADJOKES to have a positive feeling, and that is reflected in the choice of light and cheerful colors throughout the site. While the current imagery inventory is modest, each selection embodies a playful and goofy spirit, intended to evoke laughter and joy. The site has a clear structure with the jokes on a white background so they are easy to read.

### Color

This palette of colors laid the groundwork for the colors that ended up on the site. However, it's not the exact color codes, as the Materialize color scheme was predominantly used.
![Desktop/Laptop](documentation/readme_img/colors.png)

### Wireframes

While planning this site, I sat down with pen and paper and sketched out the outlines of how I wanted the site to be. Since then, the structure and the number of pages have changed. However, the essence of what I drew is still there.

<details>
<summary> Wireframes
</summary>

![Wireframes1](documentation/readme_img/wireframe1.png)
![Wireframes2](documentation/readme_img/wireframe2.png)
</details>

## Security Features

### User Authentication

* Django Allauth is a popular authentication and authorization library for Django, which provides a set of features for managing user authentication, registration, and account management.

### Login Decorator

* To add, edit, or delete a joke or a comment, users are required to authenticate using the login_required decorator. This ensures that only authenticated users can access these views.

### CSRF Protection

* Django provides built-in protection against Cross-Site Request Forgery (CSRF) attacks. CSRF tokens are generated for each user session, and they are required to submit forms or perform state-changing actions. When a user logs out, the session and associated CSRF token are invalidated, making it difficult for an attacker to forge a valid request using a copied URL.

### Form Validation

* Django Form Validation is a process that ensures the data submitted via HTML forms meets certain criteria. If all validation rules are satisfied, the form is completed. Otherwise, it populates the form with error messages

### Custom error pages

* 404 Error Page, provides user with a button the redirect to home page.
* 500 Error Page, provides user with a button the redirect to home page.

## Features

### Existing Features 

The Home page (index.html) 
* A navigation bar that alters depending on screen size.
* A footer that contains links to social media platforms.

<details>
<summary> Home
</summary>

![home desktop](documentation/readme_img/features/header_desktop.png)
![home mobile](documentation/readme_img/features/header_mobile.png)
</details>

The jokes (the_jokes.html)
* Displays the jokes.
* Displays the creator image. If the user has chosen their own image, that one will appear; otherwise, a placeholder image will appear.
* Options to filter the jokes by categories, age, and labels.
* A button for comments.
* A button to edit the joke (only appears if the joke creator is logged in).
* Average score of the joke.
* A rate box if the user is signed in. The rate box has information that the user can hover over to get more details about how the rating works.

<details>
<summary> The jokes
</summary>

![jokes notlogedin](documentation/readme_img/features/jokesnotlogedin.png)
![jokes](documentation/readme_img/features/jokes.png)
</details>

Add jokes (ad_jokes.html)
* If the user is not logged in, a message with the text 'Log in to add a joke' appears.
* When the user is logged in, a form appears that the user can fill out.

<details>
<summary> Add jokes
</summary>

![addjoke](documentation/readme_img/features/addjoke.png)
</details>

Edit jokes (edit_jokes.html)
* If the user is not logged in, the edit button will not appear.
* When the user is logged in, an edit button will display on their own jokes.
* Clicking on the edit button, a form appears that the user can fill out.

<details>
<summary> Edit jokes
</summary>

![jokes notlogedin](documentation/readme_img/features/editjokebutton.png)
![jokes](documentation/readme_img/features/editjoke.png)
</details>

Jokes Detail (jokes_detail.html)
* If the user is not logged in, the comments will only be readable.
* When the user is logged in:
    * Leave a comment
    * Edit their own comment
    * Delete their own comment
    * Like/unlike a joke

<details>
<summary> Jokes detail
</summary>

![jokesdetail](documentation/readme_img/features/jokesdetail.png)
![editcomment](documentation/readme_img/features/editcomment.png)
</details>

Contact (contact.html)
* Displays a contact form that all visitors can fill out

<details>
<summary> Contact
</summary>

![jokesdetail](documentation/readme_img/features/contact.png)
</details>
