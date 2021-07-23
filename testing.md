<h1 align="center">FITNESS WELLNESS</h1>

- Back To [Readme](README.md)

## Testing

### Functionality Testing
  - #### Navigation bar
     - The navigation bar stays at the top of the page on all screen sizes.
            - When the nav links clicks it opens the relevent page in same window with same header footer.
  - #### Footer
     - Footer is located at the bottom of the page regardless of the content amount.
     - When the social links are clicked, they open the relevant social media page in a new tab.
  
  - All external links is tested to make sure they open up the correct pages in new tabs.
  - All internal links is tested to make sure that all pages are correctly connected.
    
## Validator

### CSS3 validator 
Validate by direct input 
    [CSS Validator](https://jigsaw.w3.org/css-validator/)
  - Test result : No Error 

### HTML5 validator
Vaidate by direct input 
    [HTML5 Validator](https://validator.w3.org/#validate_by_input)
  - Test result : On all pages there are some error as I used django framework to create the pages.

### JavaScript validator
Validate by direct input
    [JavaScript Validator](https://jshint.com/)
  - Test result : No Error Found But Warning

### Python Validator
Validate by direct input
    [Pyhton Validator](http://pep8online.com/)
  - Test result : Some error which is already created. Pass result for self created

### Usability Testing
  - This website is shared on slack channel to get the feedback.This is also shared with friends to check on different device and accessbility.

### Compatibility Testing
  - #### Browser Compatibility
    - Tested on Chrome, Firefox, Opera, Microsoft Edge, Safari.
  - #### OS Compatibility
    - Tested on iOS , Android 10 and Windows 10.
  - #### Tested for responsivness on [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools). 

### Performance Testing
  - #### Tested on Developer Tools Lighthouse.
    - To run a report

        1. Download Google Chrome for Desktop.
        2. In Google Chrome, go to the URL you want to audit. You can audit any URL on the web.
        3. Open Chrome DevTools.
        4. Click the Audits tab.
        5. To the left is the viewport of the page that will be audited. To the right is the Audits panel of Chrome DevTools, which is now powered by Lighthouse.
        6. Click Perform an audit. DevTools shows you a list of audit categories. Leave them all enabled.
        7. Click Run audit. After 30 to 60 seconds, Lighthouse gives you a report on the page.

  - #### A Lighthouse report in Chrome DevTools
    - Home Page Desktop and Mobile

     <img src="readme/lighthouse/home-desk.png" height="120px"/>
     <img src="readme/lighthouse/home-mob.png" height="120px"/>

    - Subscribe Page Desktop and Mobile

     <img src="readme/lighthouse/subscribe-desk.png" height="120px"/>
     <img src="readme/lighthouse/subscribe-mob.png" height="120px"/> 

    - About Page Desktop and Mobile

     <img src="readme/lighthouse/about-desk.png" height="120px"/>
     <img src="readme/lighthouse/about-mob.png" height="120px"/>

    - Train/Shop Page Desktop and Mobile

      <img src="readme/lighthouse/products-desk.png" height="120px"/>
      <img src="readme/lighthouse/products-mob.png" height="120px"/>

    - Product Description Desktop and Mobile

      <img src="readme/lighthouse/productdesc-desk.png" height="120px"/>
      <img src="readme/lighthouse/productdesc-mob.png" height="120px"/>
    
    - Bag Page Desktop and Mobile
   
      <img src="readme/lighthouse/bag-desk.png" height="120px" />
      <img src="readme/lighthouse/bag-mob.png" height="120px" />

    - Checkout Page Desktop and Mobile
   
      <img src="readme/lighthouse/checkout-desk.png" height="120px" />
      <img src="readme/lighthouse/checkout-mob.png" height="120px" />

    - Checkout Success Page Desktop and Mobile
   
      <img src="readme/lighthouse/Scheckout-desk.png" height="120px" />
      <img src="readme/lighthouse/Scheckout-mob.png" height="120px" />

    - Product Management Desktop and Mobile

      <img src="readme/lighthouse/editproduct-desk.png" height="120px"/>
      <img src="readme/lighthouse/editproduct-mob.png" height="120px"/>

    - Contact Page Desktop and Mobile

      <img src="readme/lighthouse/contact-desk.png" height="120px"/>
      <img src="readme/lighthouse/contact-mob.png" height="120px"/>

    - Sign Up Page Desktop and Mobile
   
      <img src="readme/lighthouse/signup-desk.png" height="120px" />
      <img src="readme/lighthouse/signup-mob.png" height="120px" />

    - Login Page Desktop and Mobile
   
      <img src="readme/lighthouse/login-desk.png" height="120px" />
      <img src="readme/lighthouse/login-mob.png" height="120px" />
    
    - My Profile Page Desktop and Mobile
   
      <img src="readme/lighthouse/myprofile-desk.png" height="120px" />
      <img src="readme/lighthouse/myprofile-mob.png" height="120px" />

### Testing User Stories 
- #### Generic User
    - I easily understand the purpose and the layout of the site without additional instructions needed.
    - The landing page is simple and clear with a search box. 
    - All pages of website has navigation bar, suscribe link, search box and footer. 
    - With navigation bar I can easily access diiferent page and go anywhere from present page and come back.
    - Footer has social link. If I click on link it open the relevant page on different tab so I can easily check the social activity.
    - I am able to use the website on any device so I can keep it handy.
    - I can access external links and be able to learn more about each page.
        - Home Page
            - Home page provides the search box to search the specific product.I can get subscribe link to subscribe for newsletter. I can see all testimonial of users.
        - About Page
            - About page provides me information of gym.
        - Train Page
            - In this page I get all program of gym with pagination and filtering.
        - Shop Page
            - In this page I get all merchandise of gym with pagination and filtering.
        - Product Description Page
            - In this page I can see product description of specific product.
        - Bag Page
            - In this page I can see all by products which I added for purchase with secure checkout and adjust bag link.
        - Checkout Page
            - In this page I can enter the address and do the secure payment by entering the form.
        - Checkout Success Page
           - This page provides me confirmation of my purchase with my order details.
        - Contact Page
            - In this page I can get address and map. I can contact through contact form.
        - Signup Page    
            - In this page I can signup on website.
        - Login Page
            - In this page I can login to my profile.
        - My Profile Page
            - In profile page I can see my address details which I can update and my old orders detials.
        - Manage Product Page
            - This page can be accessed by only admin. In this page admin can manage products.

- #### Admin/Site Owner 
    - As a site owner I can check all gym program and merchandise so that I can update those if it is required for business.
    - As a site owner I can add, edit and delete the products and programs plans.
    - As a site owner I can manage products by adding, deleting and removing if required.
    - As a site owner I am able to display testimonials of my users.
    - As a site owner I could secure user's sensitivity data.

- #### User who wants to know about gym program and products
    - I can check the products without login or sign up on site.
    - I can get products by search option.
    - I can use filter option for the products so that I can see only what I want.
    - I can contact the site owner by sending message without login or sign up.
    - I can request the site owner for newsletter without login or sign up.
    - I can look the contact details on contact page and map of address.
    - I can check offers which is on landing page and I find easily.
    - I can know about gym what program they offer.
    - I can know about merchandise and detail description..
    - I can know about price details to check the price for different products.
    
- #### User who wants to be member of gym and/or buy the merchandise.
    - I can create my profile by sign up.
    - I can easliy login and check my page.
    - I can easily add products in my cart.
    - I can update my cart if I want to do.
    - I can be secure about my all personal data.
    - I am able to do the secure payment for purchasing.
    - I can get confirmation mail of my order.
    - I can save my all purchase in my profile.
    - I can request the site owner for newsletter
    - I can contact the admin for any query.