
<h1 align="center">NewsTime</h1> 

NewsTime is for anyone who wants to stay informed and engaged with news from around the world and the latest news from various categories like Politics, Business, Art, Technology, Science, Economy.
NewsTime is responsible for the gathering and broadcasting of news and current affairs around the world.

![NewsTime](AmIResponsive)


## __User Experience (UX)__

### _User Stories_


* **As a Site Admin**


1. News Post Management: As a site Admin I can create, read, update and delete news posts in front-end so that I can manage news content easily.
2. View likes: As a Site Admin I can view the number of likes on each article so that I can see which type of news the audience prefers the most.
3. As a Site Admin I can view comments on an individual articles so that I can read the conversation.
4. Approve comments: As a Site Admin I can approve or delete comments so that I can filter out obnoxious comments.



* **As a Site User**


1. View News List: As a Site User I can view a list of news so that I can select one news to read.
2. View Comments: As a Site User I can view comments on an individual articles so that I can read the conversation.
3. Account Registration: As a Site User I can register an account so that I can comment and like.
4. News Category: As a Site User I can receive news from various category on the page so that I can be informed news from various category.
5. Open News Posts: As a Site User I can click on a post so that I can read the full article.
6. Site Pagination: As a Site User I can view a paginated list of news so that select a news post I want to view.
7. Comment on News Posts: As a Site User I can leave comments on a article so that I can share my thoughts about an article.
8. Like/Unlike: As a Site User I can like or unlike an article so that I can interact with the content.
8. Number of Likes: Number of As a Site User I can view the number of likes on each article so that I can see which type of news the audience prefers the.



### _Design_

* **Colors** 

    * #cf4b1f - Logo, Buttons
    * #db0000 - Warning Text
    * tertiary - Navbar Background


* **Fonts**

    * Racing Sans One 



### _Wireframes_

I created Wireframes to visualize the site's design and act as a template to use when developing the site.

**Home Page**

![NewsTime Home page](./readme/Images/home.jpg)


**Article Page**

![NewsTime Article](./readme/Images/article-w.jpg)


**Sign up page Page**

![NewsTime Sign Up](./readme/Images/signup.jpg)



**Sign In page Page**

![NewsTime Sign In](./readme/Images/signin.jpg)

**Note:** explantion 

### _ERD (Entity Relationship Diagram)_

**Article/ News Post Data Model**

![NewsTime News Post Data Model](./readme/Images/newspost.jpg)

**User Comments Data Model**

![NewsTime User Comments Data Model](./readme/Images/comments.jpg)

**News Categories Data Model**

![NewsTime News Categories Data Model](./readme/Images/category.jpg)

**User Data Model**

Note: I created a user data model and used the Django user model as well. I'll use my custom user model for future implementations.

![NewsTime User Data Model](./readme/Images/user.jpg)



## __Features__

### _Existing Features_

* **Navigation Bar**

    The full responsive navigation bar is featured on all the pages to allow for easy navigation from page to page across all devices. Access is distinct between admins and standard users, with restricted access to standard users.
    On the left side is logo, which can be used as navigation link to the main page, also links to the Home, Add News, Sign Up, SignIn, Sign Out.

    * Site Nav for Admins

        ![NewsTime Navbar for Admins](./readme/Images/admin-nav.jpg)
    
    * Site Nav for First time visitor 

        ![NewsTime Navbar](./readme/Images/nonuser.jpg)

    * Site Nav for Standard User

        ![NewsTime Navbar Standard User](./readme/Images/logged-nav.jpg)

    * Responsive Navbar Admin

        ![NewsTime Responsive Navbar Admin](./readme/Images/responsive-nav-admin.jpg)

    * Responsive Navbar Standard User

        ![NewsTime Responsive Navbar Standard User](./readme/Images/responsive-nav.jpg)

    The navigation bar was created with bootstrap and it's fully responsive across devices.


* **Home Page**

    The home page is the user's first call port and is composed of a list of news post. The feature here is the links to the news posts and its details like: news title, news overview, news category, published date, an eye-catching image of the news which draws the attention of users to open the links and read the article. All this detail makes it possible for users to find their favorite news topic in time.

    ![NewsTime Home page](./readme/Images/home-nonuser.jpg)


* **Article Page**

    The users can read the detail about the news by clicking on the title of the news post.

    ![NewsTime Article page](./readme/Images/article.jpg)

* **Comments & Like**

    The Comments and Likes feature is restricted access to standard users. Users who are registered in NewsTime could leave a comment or Like an article.

    ![NewsTime Comments & Like section](./readme/Images/comment-like.jpg)


* **Comment List**

    For those who aren't registered in Newstime, Can only read the comments on the article page.
    
    ![NewsTime Comment list](./readme/Images/comment-list.jpg)

* **Sign Up Page**

    ![NewsTime Sign Up Page](./readme/Images/signup-p.jpg)

* **Sign In Page**

    ![NewsTime Sign Up Page](./readme/Images/signin-p.jpg)

* **Sign Out page**

    ![NewsTime Sign Up Page](./readme/Images/signout-p.jpg)

* **Footer**

    The footer section is consistent on all pages and includes links to the relevant social media sites and follows the same style as the navigation bar, and appears in the same format on all pages - this allows for consistency throughout the site.

    ![NewsTime Article page](./readme/Images/footer.jpg)

    * The links will open in a separate tab in a browser to allow easy navigation for the users.
    * The footer is useful for users to get connected with the community for socialization through social networks.



* **Admin Home Page**

    The Admin page is only accessible for Admin users specifically. This page informs the superuser how to add, edit and delete news posts.

    ![NewsTime Admin Home page](./readme/Images/home-admin.jpg)

    * **Add Post - Admin page**

        The Add Song page is only accessible for Admin. This page consists of a form to be completed in order to add a news post, with title, news overview, news content input fields, featured image, news category and pulished status selector.
        The Add News Post form is fully responsive across all devices.

    ![NewsTime Admin Add News page](./readme/Images/admin-addnews.jpg)
        

    * **Update/Edit News Post - Admin page**

        This page consists of a form with pre filled content. Update a news post form includes: title, news overview, news content input fields, featured image, news category and pulished status selector.
        The Update News Post form is fully responsive across all devices.

    ![NewsTime Admin Add News page](./readme/Images/edit-admin.jpg)


    * **Delete News Post - Admin page**

        The feature for this page is an eye-catching Warning text with exclamation font awesome icon, confirm buton and cancel button.

    ![NewsTime Admin Delete News page](./readme/Images/admin-delete-post.jpg)



### _Future Implementations_

* Social Sharing Button
* Popular News Post Section
* User Profile
* Contact Form


## __Technologies Used__

**1. Languages**

* HTML5
* CSS3
* JavaScript
* Python


**2. Frameworks, Libraries & Programs**

* **Django:** The Django web framework was used to create the full-stack web application.
* **PostgreSQL:** was used as the object-relational database system.
* **ElephantSQL:** ElephantSQL was used to host the database.
* **Bootstrap:** Bootstrap was used through the project to style the project and create responsive elements/layouts.
* **Git:** Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
* **GitHub:** GitHub is used to store the projects code after being pushed from Git.
* **Heroku:** Heroku was used for the deployed application.
* **Balsamiq:** Balsamiq was used to create the wireframes during the design process.
* **Chrome DevTools:** Chrome DevTools was used to consistently check the site in terms of responsivity,
 performance, accessibility, best practice and SEO.
* **Font Awesome:** Font Awesome was used on all pages throughout the website to add icons for UX purposes.
* **Font Awesome Favicon Generator** Font Awesome Favicon Generator was used to reproduce a favicon.

**3. Python Modules and Packages**

* **cloudinary:** Used for the post Image Model field, Image upload and deletion.
* **django-crispy-forms:** Used to format form elements and layout.
* **crispy-bootstrap5:** Used to style form using Bootstrap5.
* **dj-database-url:** Allows the use of 'DATABASE_URL' environmental variable in the Django project settings file to 
 connect to a PostgreSQL database.
* **dj3-cloudinary-storage:** Facilitates integration with Cloudinary by implementing Django Storage API.
* **django-allauth:** Set of Django application used for account registration, management and authentication.
* **django-filter:** Application that allows dynamic QuerySet filtering from URL parameters.
* **django-model-utils:** Easily add choices to a django model field.
* **django-summernote:** Allows easy use of the Summernote WYSIWYG editor in Django projects.
* **gunicorn:** Python WSGI HTTP Server.
* **psycopg2:** Python PostgreSQL database adapter.






 
        