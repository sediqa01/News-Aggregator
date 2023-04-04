
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

![NewsTime Article](./readme/Images/article.jpg)


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

        ![NewsTime Navbar Standard Userl](./readme/Images/logged-nav.jpg)

    * Responsive Navbar Admin

        ![NewsTime Navbar Standard Userl](./readme/Images/responsive-nav-admin.jpg.jpg)

    * Responsive Navbar Standard User

        ![NewsTime Navbar Standard Userl](./readme/Images/responsive-nav.jpg.jpg)


* **Home Page**




 
        