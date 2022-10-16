# prof.io

## Table of Contents
1. [Overview](#Overview)
1. [Product Spec](#Product-Spec)
1. [Wireframes](#Wireframes)
2. [Schema](#Schema)

## Overview
### Description <br>
Even though there are many websites such as LinkedIn and Handshake for allowing students to find internships, there aren't any comparable platforms for research opportunities. Our vision with prof.io is to enable students to more easily connect with research faculty and professors to outreach to students about their research.

### What it does <br>
The application matches students and professors that share similar research interests. It gives the students recommendations of research opportunities that align with their preferences and helps professors filter out possible mismatches.

## Product Spec

### 1. How we built it <br>
We built the frontend of the mobile application using Swift and used Python with a machine learning library called sklearn to create an K-means clustering model that matches students with professors. The model uses k-elbow method to find the optimal k value, and uses Principal Component Analysis to reduce features dimensions, hence, reduce running time. Furthermore, we set up our database using Firebase to easily store and retrieve data on students and professors. The front, the mobile app connects  to the Google Cloud, and run the python script, and return the computation result back to the mobile app.


### 2. Challenges we ran into <br>
Not everyone on the team had familiarity with Swift and we had to learn along the way. Due to limitations on data that we were able to programmatically generate, the resulting model may not be 100% accurate.


### 3. Accomplishments that we're proud of <br>
Our team was able to apply machine learning to our project and create a working model. We were also able to build a full-stack mobile application with multiple components within 24 hours.

### 4. What we learned <br>
We attempted to follow the traditional software development cycle from ideation to presentation. During the process, we were able to be exposed to various technologies widely used by the industry.

### 5. What's next for prof.io <br>
Organize the structure of the application so that there is a clearer distinction between the frontend and backend, and remodel the user interface to make it more appealing and responsive. We can also improve the machine learning model by analyzing real-world data.

## Wireframes
[Add picture of your hand sketched wireframes in this section]
<img src="https://imgur.com/a/YmeDI2q" width=600>

## Schema 

### Models
| Property |  Type  | Description |
|----------|--------|-------------|
| UserId   | String | unique Id for each user|
| Subject  | String | a subject of the study intended|
| avalibility | Double | number of hours avaliable per week |
| gpa | Double | gpa requirement or current gpa |
| in-person | Boolean | indication of in-person or remote researches |
| internship-month | Double | experiences in working in industry |
| location | String | location of the reseach|
| study | List of Strings | interested topics for research|

* Log-InPage
    * user login (students/professors)
* Candidate List Page
    * (READ/GET) Read data from firebase
    * (Read/GET) Get data from Google Cloud
* Filter Page
    * Data stored locally
* User Info Page
    * (Create) Push data to firebase
* Candidate Detail Page
    * (Create) Push data (application) to firebase


## Video Walkthrough

Here's a walkthrough of implemented user stories:
<img src="http://g.recordit.co/QeqZrFlq89.gif"/>
