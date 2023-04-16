# Napptive X WeMakeDevs Cloud Native Hackathon Project By Code-Up Team
cloud native app project created for <a href="https://wemakedevs.org/events/hackathons/napptive" target="blank">Napptive X WeMakeDev Hackathon</a>

<h1><b>Flask Blog</b></h1>
This is a simple Flask blog application that retrieves blog posts from an external API and displays them on the homepage. Users can click on a post to view its details, or navigate to the about page.

<h2><b>Installation</b></h2>

- Clone the repository
- Install the required packages using the command pip install -r requirements.txt
- Run the application using the command python app.py

<h2><b>Usage</b></h2>
- Once the application is running, visit http://localhost:3000 to view the homepage. From there, you can navigate to individual blog posts or the about page.

To send a message through the contact form, fill out the form fields and click "Send". The message will be sent to the email address configured in the email API endpoint.

<h2><b>API Endpoints</b></h2>

- / - Returns the homepage with a list of blog posts
- /post/<int:index> - Returns the details for the blog post with the specified index
- /about - Returns the about page
- /contact - Accepts POST requests with form data to send a message via email

Credits
This project was developed by [Prathamesh Mandavkar :
<a href="https://github.com/Pmking27" target="blank">Pmking27</a> | Suraj Bhosale : <a href="https://github.com/SurajBhosale003" target="blank">SurajBhosale003</a>].
