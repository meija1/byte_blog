# Byte Blog
Website made for bloging and forums, asking questions or resolving problems about anything relating applications, coding, programming, games or game codes.
This website is targeted towards software developers, game enthusiasts and people interested in coding. It's great for new comers and people learning to code.

The website is based on popular sites like twitter and reddit with a more easier and simpler UI.

## Features
### Existing Features
* The main page consists of all the posts from every user ordered in the date and time they were created in
  ![Main page](https://github.com/meija1/python_battleships_game/assets/109754892/2c422f93-0f16-42c3-b98f-46708bb5f5de)
* Categories to select type of post to look at
 
  ![categories](https://github.com/meija1/python_battleships_game/assets/109754892/fb8fcacd-469d-42c5-b021-536da65f97bc)
* Sign in, Register and Log out options for the website
 
  ![sign in](https://github.com/meija1/python_battleships_game/assets/109754892/29a4ad61-3a39-41dc-bd6e-7beeb09a9d8a)
*  Logout feature with prompt
  
  ![logout](https://github.com/meija1/python_battleships_game/assets/109754892/ec66a82b-dbb7-42b6-bbcc-55a06835abcd)
* Create a post option to submit a new blog post
 
  ![create post](https://github.com/meija1/python_battleships_game/assets/109754892/ba51ac18-5098-4c4a-831b-445783ccf36d)
* New post form
 
  ![create a post form](https://github.com/meija1/python_battleships_game/assets/109754892/ca6607df-9f08-4fa4-b0e9-be3e89bf339e)
* Post detail page with post title, content, comments and likes
 
  ![post details page](https://github.com/meija1/python_battleships_game/assets/109754892/07504873-3b0f-4cda-9fe4-051b2571bc77)
* Edit post feature with a form
 
  ![edit post](https://github.com/meija1/python_battleships_game/assets/109754892/a93a8ba4-ff75-4ec9-8049-f11de097ef1c)
* Deleting post option with a prompt
 
  ![deliting post](https://github.com/meija1/python_battleships_game/assets/109754892/59d7af43-0aa8-4167-bebc-c72ffcb0805b)

### Features Left to Implement
* Adding likes to post comments in the future
* Edit and delete comments option for users
* Add new categories which can easily be added by the admin if users request
* Ability to upload images for posts and comments, to be approved by admin

## Data Model
* Website is based on database model with django as python web framework
* HTML, CSS and Bootstrap libraries have been used
* PostgreSQL database 
* Git to handle version control.
* GitHub to store project
* PIP for installation of tools needed in this project.
* Heroku for deployment
* Django Crispy Forms to style django forms.

## User Stories
As a ByteBlog website user, I want to:
* Be able to register to the website
  New users are able to create profiles and use the websites features that are provided in the Existing Features section above
* Be able to sign in and sign out of the website
  Existing users are able to sign in and sign out of the website
* Have the ability to create a post
  Registered users can create post of their liking with title, content and category that fits it to be approved by the admin
* Be able to view, read and like posts
  Users can see the post content that they choose, read the posts contents and it's comments left by other users and like posts by clicking the heart icon
* Be able to leave a comment on any particular post
  Users can submit comments on any post that will need to be approved by the admin
* Have the ability to edit and delete posts I have made
  Existing users have the ability to edit or delete posts that they have created
* Be able to see posts in the category I have selected
  Users can choose which posts they want to see in the website view by selecting a category

## Database Schema
Database schema of how the data is being processed in the app
![Database model](https://github.com/meija1/python_battleships_game/assets/109754892/e3215574-8853-4618-ba6f-ae19045fd933)
Diagram of how process works in creating a post
![creating post schema](https://github.com/meija1/python_battleships_game/assets/109754892/b23d8854-db87-462d-a8f8-b85828ad5e22)

## Testing
I have tested the website in manual and automated tests
The website has been viewed in high and low resolution screens, it works on desktop screens and phone screens

### Automated Tests
I have ran automated tests for applicatons:
* Forms
* Models
* Urls
* Views
![blog tests](https://github.com/meija1/python_battleships_game/assets/109754892/2376d845-12a6-4c80-a74d-932b401a003f)

### Manual Tests
The website can be viewed as a non user to see the post lists on the main page and seeing the post details with comments and number of likes, but can not create a post or leave a comment as well as like, edit or delete them. I have tested registering as a new user and creating, editing and deleting posts. The like button on each post appears only when the user is signed in, if the post is liked the heart will fill with color and number next to it will go up. Clicking the heart icon has a very slight delay in loading the action. Signing in and out gives promts above the post lists, same as submiting or updating the forms.
### Bugs
* The copied website link doesn't seem to be working in some of the sites to check how responsive the app is, due to error that heroku has restricted the access
* Loading times differ on different web browsers
### Validator Testing
* PEP8
    * No errors were returned from PEP8
* W3C CSS
    * No errors detected
* W3C HTML
    *  Errors only for static django templates

## Deployment
This project was deployed using Code Institute's mock terminal for Heroku
* Steps for deployment
    * Create new Heroku app
    * Setup PostgreSQL database
    * Copy database urls to project
    * Create the requirements.txt file
    * Link the Heroku app to the repository
    * Set x_frame_options to SameOrigin in setting.py file
    * Click on Deploy
## Credits
* Code Institute for some of the code
* Udate and Delete post was helped by this post [DjangoProject](https://docs.djangoproject.com/en/4.2/topics/class-based-views/generic-editing/)
* Most of the errors and issues where solved by going through many posts on [StackOverflow](https://stackoverflow.com/)
* The automated testing help was found on Code Institute's Hello Django testing videos and videos [here](https://www.youtube.com/watch?v=qwypH3YvMKc&list=PLbpAWbHbi5rMF2j5n6imm0enrSD9eQUaM&ab_channel=TheDumbfounds) 


