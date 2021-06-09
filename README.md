# MY BLOG
Application where favorite pictures are shared.
Application URL: https://my-blog1357.herokuapp.com/
## Design
<img width="1349" alt="Screen Shot 2021-06-08 at 20 31 20" src="https://user-images.githubusercontent.com/77530003/121177619-95dffa00-c898-11eb-88c9-816d89cdaaff.png">

### what users can do with the application
    ・Login and Logout
    ・Post blogs
    ・Edit blogs
## Reauirements
Below are some demonstrations for understanding project requirements.

### Code oraganization
Code organization helps the whole program to be compact and easily readable. At this juncture, I feel my skill should be improved more to decrease repeated parts in the program code. 

On the below bunch of codes, there could be organized parts and those should be more organized. The organized part is that both of two router methods use the same HTML form, which could be saving of data memory of application. And the opposite part is that there are completely same sentences. The part might be solved to set a new function that generate the same result of the sentence.

<img width="774" alt="Screen Shot 2021-06-08 at 19 58 34" src="https://user-images.githubusercontent.com/77530003/121174507-f4a37480-c894-11eb-930f-f951a0c5770b.png">

### Documentation
I learned it's important to provide commented-out sentences for people who read for the first time to understand programs. The below bunch of codes has some green comments that tells the aim of execution of the following codes. 

<img width="710" alt="Screen Shot 2021-06-08 at 19 51 04" src="https://user-images.githubusercontent.com/77530003/121172705-ee13fd80-c892-11eb-9b3e-537696c704aa.png">

### Variabale, conditions, and loops.
Variable provides a memory location to values. On the screenshot below, two variables 'status' and 'post_title' hold values, and they are pulled in arguments of render_template method that generates HTML output.

<img width="816" alt="Screen Shot 2021-06-08 at 19 18 41" src="https://user-images.githubusercontent.com/77530003/121170070-afc90f00-c88f-11eb-9aee-27acead093fa.png">

If statement defined as conditional statement is used to generate different conputations depending on whether the condition evaluates true or false. Looking at the above screenshot again, if statement evaluates whether a user is logged in.

Loop is repeated execution of a program block under specified condition. The below is a loop that repeates generating Html block with a list of information of Post instances.

<img width="684" alt="Screen Shot 2021-06-08 at 19 32 29" src="https://user-images.githubusercontent.com/77530003/121170831-b4da8e00-c890-11eb-9f00-e9dbce24156f.png">

### Collections (list and dictionary)
Collections are useful to store data and tranmit multiple data in a bunched form. This application uses two types of collection: List and Dictionary.

On the screenshots below, posts is a list that pulls every Post instances stored in database. Its form is like [post, post, post, post, ....].
And For loop is useful to approach each instance in the list.

<img width="373" alt="Screen Shot 2021-06-08 at 17 31 33" src="https://user-images.githubusercontent.com/77530003/121152641-59080900-c880-11eb-8ed2-23d8209c2189.png">

<img width="655" alt="Screen Shot 2021-06-08 at 17 42 02" src="https://user-images.githubusercontent.com/77530003/121153629-2e6a8000-c881-11eb-938d-0c471060f4f2.png">

Dictionary stores each item with a key, and Session object exploits the utility to hold consistent information on running application. The screenshot below shows that Session object holds user information with a key 'user_name' while User object is logged in.

<img width="626" alt="Screen Shot 2021-06-08 at 17 52 18" src="https://user-images.githubusercontent.com/77530003/121155141-82299900-c882-11eb-8ea2-897ac422ce78.png">

### Functions, parameters, arguments, default parameters, and named arguments
In views.py, there are some important functions for the application to carry out HTTP communication that provides web pages, recieves request from user and deal with the reauest for the following behavior.

When looking at the function that transfers to top page, it has default parameters, named arguments and parameters that are generated with content of named arguments to transmit necessary components to build a top page template:

<img width="813" alt="Screen Shot 2021-06-08 at 17 15 55" src="https://user-images.githubusercontent.com/77530003/121150173-41c81c00-c87e-11eb-87f1-09873733a468.png">


### Simple classes, attributes and methods
There are two classes dealed with in this application: User and Post. And  the both are simple.
Each of the two has some attributes as seen on the screen shot below, and the attributes are initialized by __init__ method when generated.

<img width="708" alt="Screen Shot 2021-06-08 at 17 05 35" src="https://user-images.githubusercontent.com/77530003/121147395-cbc2b580-c87b-11eb-8b41-81c7196848d0.png">

Their attributes of Post can be updated by inserting new data into an instance previously generated.

<img width="690" alt="Screen Shot 2021-06-08 at 17 08 09" src="https://user-images.githubusercontent.com/77530003/121148464-c31eaf00-c87c-11eb-92f6-fc992b1932c8.png">

### User IO, and validations
This application always provieds user opportunity to input/output because the program needs request of user for behaving through HTTP communication. Focusing on the Sign up behavior, there is manifest points where input and output occurs. 

As an example of input,  a user should go through inputing some info in a form and send request(submit) to sign up.
As an example of output. a computer recieves the request with the user’s info, generates data of the user, and transfer to the other page to show the user that the request has been dealt with.

Example of I/O:

<img width="717" alt="Screen Shot 2021-06-08 at 16 54 58" src="https://user-images.githubusercontent.com/77530003/121146880-52c35e00-c87b-11eb-9de8-97e2f8976aab.png">


### Test
Test file: https://github.com/kenstratton/my_blog/blob/main/db.py

Test result: 

<img width="401" alt="Screen Shot 2021-06-08 at 14 57 18" src="https://user-images.githubusercontent.com/77530003/121142221-bdbe6600-c876-11eb-8eca-bd8a2843c743.png">

As seen on the picture, the whole test is executed with one method. Also, each test is built with error handling methods try and except.

The first and second results are same because the second info results from User instance stored in database which has been generated at the first test.

The third one tests whether a method of the User instance refelcts an expected value.

The fourth and fifth tests generation and storation of Post instance and whether the instance can be pulled from database.

The sixth tests whether Post instance can be updated with new data.

Finally, the last test demonstrates deletion of Post instance from database.
