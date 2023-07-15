# Byte Blog
This website is a platform for blogging - it provides a way to ask questions or resolve problems about anything relating to applications, coding, programming, games or game code. 
This website is targeted towards software developers, game enthusiasts and people interested in coding and is suitable for all skill levels.

The website is based on popular sites like Twitter and Reddit but features a simpler UI.

## Features
### Existing Features
* The main page consists of every approved post, ordered by time of creation
  
  ![Main page](https://github.com/meija1/python_battleships_game/assets/109754892/2c422f93-0f16-42c3-b98f-46708bb5f5de)
* Category drop down to select which posts to view - the categories can only be created by admin
 
  ![categories](https://github.com/meija1/python_battleships_game/assets/109754892/fb8fcacd-469d-42c5-b021-536da65f97bc)
* Login and Register options for the website - prompts will be displayed for each action
 
  ![sign in](https://github.com/meija1/python_battleships_game/assets/109754892/29a4ad61-3a39-41dc-bd6e-7beeb09a9d8a)
*  Logout feature with prompt
  
  ![logout](https://github.com/meija1/python_battleships_game/assets/109754892/ec66a82b-dbb7-42b6-bbcc-55a06835abcd)
* Create a post option to submit a new blog post for admin approval - admin approval is required before the post will become available to other users
 
  ![create post](https://github.com/meija1/python_battleships_game/assets/109754892/ba51ac18-5098-4c4a-831b-445783ccf36d)
* New post form
 
  ![create a post form](https://github.com/meija1/python_battleships_game/assets/109754892/ca6607df-9f08-4fa4-b0e9-be3e89bf339e)
* Post detail page with post title, content, comments and likes
 
  ![post details page](https://github.com/meija1/python_battleships_game/assets/109754892/07504873-3b0f-4cda-9fe4-051b2571bc77)
* Form to edit post which will then require admin approval -admin approval is required before the edited post will become available to other users
 
  ![edit post](https://github.com/meija1/python_battleships_game/assets/109754892/a93a8ba4-ff75-4ec9-8049-f11de097ef1c)
* Deleting post option with prompt
 
  ![deliting post](https://github.com/meija1/python_battleships_game/assets/109754892/59d7af43-0aa8-4167-bebc-c72ffcb0805b)

### Features Left to Implement
* Ability to like comments 
* Option for users to edit and delete comments 
* Add additional categories
* Ability to upload images for posts and comments

## Data Model
* Website is based on a database model with Django as the Python web framework
* HTML, CSS and Bootstrap libraries have been used
* PostgreSQL database 
* Git to handle version control
* GitHub to store project
* PIP for installation of tools required
* Heroku for deployment
* Django Crispy Forms to style Django forms

## User Stories
As a ByteBlog website user, I want to:
* Be able to register and create an account
  
  New users are able to create profiles and use the websites features that are provided in the "Existing Features" section above
* Be able to sign in and sign out of the website
  
  Existing users are able to sign in and sign out of the website as shown in the "Existing Features" section above
* Have the ability to create a post
  
  Registered users can create posts consisting of a title, content and category which will then require approval by the admin
* Be able to view posts, read comments and like posts
  
  Users can view the content of posts they select, read the comments left by other users, and like posts by clicking the heart icon
* Be able to leave a comment on any particular post
  
  Users can submit comments on any post which will then require admin approval
* Have the ability to edit and delete posts I have made
  
  Existing users have the ability to edit or delete posts that they have created
* Be able to view posts in the category I have selected
  
  Users can choose which type of posts they want to see on the homepage by selecting a category

## Database Schema

Database schema of how the data is being processed in the app

![Database model](https://github.com/meija1/python_battleships_game/assets/109754892/e3215574-8853-4618-ba6f-ae19045fd933)
Diagram of how the process works when creating and editing posts

![creating post schema](https://github.com/meija1/python_battleships_game/assets/109754892/b23d8854-db87-462d-a8f8-b85828ad5e22)

## Testing
I have tested the website using both manual and automated tests. The website has been viewed successfully on both high and low resolution screens and it also works on desktop and phone screens.

### Automated Tests
I have run automated tests for the following:
* Forms
* Models
* URLs
* Views
  
![blog tests](https://github.com/meija1/python_battleships_game/assets/109754892/2376d845-12a6-4c80-a74d-932b401a003f)

### Manual Tests
For users who have not signed in or registered for an account, the website can only be utilised to view the posts, including the post comments and number of likes. However, they will be unable to create, edit or delete posts, leave comments or like posts. I have tested the process of registering as a new user and creating, editing and deleting posts. The like button on each post appears only when the user is signed in - if the post is liked, the heart will fill with colour and the number next to it will increase. There is a very slight delay in loading this action when the heart icon is clicked. When signing in and out of the website, a prompt will appear above the list of posts. Similarly, a prompt will be displayed when submitting or updating a post.
### Bugs
* An error occurs when trying to check how responsive the website is on third-party sites. This error is caused by restricted access to these sites.
* Loading times vary on different web browsers
### Validator Testing
* PEP8
    * No errors were returned
* W3C CSS
    * No errors were detected
* W3C HTML
    *  Errors only for static Django templates

## Deployment
This project was deployed using Code Institute's mock terminal for Heroku
* Steps for deployment:
    * Create new Heroku app
    * Setup PostgreSQL database
    * Copy database URLs to project
    * Create the requirements.txt file
    * Link the Heroku app to the repository
    * Set x_frame_options to SameOrigin in setting.py file
    * Click on Deploy
## Credits
* Code Institute - provided some of the code used in developing this website
* Creating the Udate and Delete features - assistance found in the following post [DjangoProject](https://docs.djangoproject.com/en/4.2/topics/class-based-views/generic-editing/)
* General errors and issues - solved by reading numerous posts on [StackOverflow](https://stackoverflow.com/)
* Automated testing - support found on Code Institute's Hello Django testing videos and [here](https://www.youtube.com/watch?v=qwypH3YvMKc&list=PLbpAWbHbi5rMF2j5n6imm0enrSD9eQUaM&ab_channel=TheDumbfounds)
* Code Institude tutors


