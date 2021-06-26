
<h1 align="center">FITNESS WELLNESS</h1>
<h1 align="center"><img src="readme/mockup/home.png" /></h1>

-[Live Website](https://ms4-fitnesswellness.herokuapp.com/)

-[GitHub Repository](https://github.com/RubySrivastava/ms4-fitnesswellness)

## About

This project is made for the gym owner(admin) and users of the gym. It will be used by the users who wants to know more about gym and want to join program of the gym.
This is designed for the business purpose of the owner who wants to grow his business by his programs and products. 
The goal of this project was to allow the user to create an account and make a purchase of products with Stripe.
Although the majority of the admin activities is done through the Django admin site.
This project also provides more common tasks such as adding, editing and deleting products through the web app's UI. 
Because of sensitivity involved in handling customer details I had to approach development from a security conscious perspective. 
For site owners it will be utility to increase their presence over the internet which lead to increase their business by adding and selling more products.
It is designed to be responsive on all devices and easy to navigate for users and owner.


## Table of Contents

[User Experience (UX)](#UX)

[Features](#features)

[Design](#design)

[Technologies Used](#technologies)

[Testing](#testing)

[Deployment](#deployment)

[Known Bugs](#bugs)

[Credits](#credits)

<a name="UX"></a>
## User Experience (UX)

### User Stories

This website gives the information about different recipe with cooking method posted by site owner and other users. 
Any food lover who wants to come and explore different taste then this website is perfect for him.
In this website he gets the information about different recipe based on category and can also post his recipe.
This site also provides to create your own account and post recipe.

- #### Generic User
    1. I want to easily understand the purpose and the layout of the site without additional instructions needed.
    1. I want to intuitively navigate through the site to browse the content.
    1. I want the site is responsive on all device as I usually use phone for doing all such type of stuff.
    1. I want to be able to use the website on any device so I can keep it handy.
    1. I want to use the navigation at all times and have it readily available so I can quickly navigate from one page to another.

- ####  Admin/Site Owner
    1. As a site owner I want to check all gym program and merchandise so that I can update those if it is required for business.
    1. As a site owner I want to add, edit and delete the products and programs plans.
    1. As a site owner I want to manage products by adding, deleting and removing if required.
    1. As a site owner I should be able to display testimonials of my users.
    1. As a site owner I have to secure user's sensitivity data.

- #### User who wants to know about gym program and products
    1. I want to check the products without login or sign up on site.
    1. I want to get products by search option.
    1. I want filter option for the products so that I can see only what I want.
    1. I want to contact the site owner by sending message without login or sign up.
    1. I want to request the site owner for newsletter without login or sign up.
    1. I want to look the contact details on contact page and map of address.
    1. I want to check any offers which should be on landing page and I can find easily.
    1. I want to know about gym what program they offer.
    1. I want to know about merchandise and detail description..
    1. I want to know about price details to check the price for different products.

- #### User who wants to be member of gym and/or buy the merchandise.
    1. I want to create my profile by sign up.
    1. I want to easliy login and check my page.
    1. I want to easily add products in my cart.
    1. I want to update my cart if I want to do.
    1. I want to be secure about my all personal data.
    1. I should be able to do the secure payment for purchasing.
    1. I want to get confirmation mail of my order.
    1. I want to save my all purchase in my profile.
    1. I want to request the site owner for newsletter
    1. I want to contact the admin for any query.

<a name="features"></a>
## Features

### Existing Features

- #### Common Features Across All Pages

    - Header allows user to easily navigate across all pages
      - The header itself is positioned to always be visible (positioned absolutely using Bootstrap 'fixed-top' class) at the top of the screen (mobile and desktop) which allows visitors to find it quickly.
      - There are two header on page. One is main navigation menu and other is mobile top header. 
      - The brand logo is positioned on the left and a search box. Both are visible on all pages .
      - Navigation is included in the header to let the user intuitively locate it.
      - Main navigation links collapse in a home menu when viewed on mobile device.
      - Mobile top header is visible on all device.
    
    - Accessibility
      - All Pages have a description in case the image link breaks as well as helps screen readers.
      - The home menu has aria-label added to let users with screen readers know where the toggleable menu is.
    
    - Buttons/Links
      - All buttons are styled in the way to provide consistency across the page.
      - All links have a hover effect.
      - All external links open in a new tab to allow the user to easily navigate back to the page. 
    
    - Toast messages
      - Messages displayed at the right corner of the page to provide the user confirmation of actions like sign out, adding or editing products etc.

    - Responsiveness
      - All Pages are responsive on different viewport size.

    - Footer
      - Footer has been designed to be at the bottom of the page, regardless of the amount of content. This aids the overall user experience.
      - All content has been spaced out and aligned to the center.
      - There are social links and when hovered over, it changed the color.

- #### Specific to Pages

    - Home Page
        - This page has header, footer and search box. This page has subsciber link for newsletter. This page has special offer link which directs to train page.Page contains testimonials of users with their names too. The header has navigation bar and footer has copyright and social links.The image brings the user's attention and inviting the user to explore the website.
    
    - About Page
        - This page contains the information of gym.

    - Train Page
        - This page contains the list of programs based on category with image and price. Page has pagination and back to top button.

    -Shop Page
        - This page contains the list of products based on category with image and price. Page has pagination and back to top button.

    - Contact Page
        - This page contains a form where users can give feedback and ask questions. This Page has map and address details.

    - Register Page
        - This page has signup form. After registration user will reach on home page.

    - Login Page 
        - This page has login form. After login user will reach on home page.

    - Product Management Page
        - Only admin can access this page. In this page admin can manage products.

    - My Profile 
        - This page consist of user details like address and order details of respective user.

    - Logout Page
        - This page has logout form with confirmation button to logout.

    - Product Description Page
        - This page displays product description of selected product with add to cart and continue pruchase link.

    - Bag Page
        - This page has list of all products added to cart with secure checkout and continue purchase link.

    - Checkout Page
        - This page has form for user address deatils and other is for order summary. This page use for payment through stripe. This page adjust to cart and complete order link.

    - Checkout Success Page
        - This page has confirmation message of your payment for order. This page also contains orders and user deatils.

### Future Features
  - Create a way for the user to rate the website without having to type up feedback.
  - A page where people can write and read review of product.
