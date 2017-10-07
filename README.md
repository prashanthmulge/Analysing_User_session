# Analysing_User_session
Coding challenge: analyzing user sessions

In this exercise we will provide you a web server access log, and ask you to find the most active users. There's also an exciting twist: your program must work even when the dataset does not fit in memory.
Input

In the file "access.log.gz" you'll see an access log from the web server of an imaginary web site. It has a bunch of lines with three columns: timestamp, userid, and path. The line "1436911100008,50215,/item/36993" means that user id 50215 accessed "/item/36993" at t = 1436911100008.

It's up to you if you want your program to read the access.log.gz directly, or if you want to unzip it yourself and have your program read the plain text version.

The input file is here: http://static.imply.io/takehome/access.log.gz
Output

Your challenge is to write a program that reads the access log and finds all userids that visited at least N distinct paths (provided as a command line argument). Your program should write the list of userids to a file on disk, one per line. They don't have to be in any particular order, but each one should appear only once.

Your program should write its output file, as well as any scratch files you may need, to its working directory.
Memory constraints

Even though the sample access.log is small enough to fit into memory, your program should work if the input and output files are too big to fit into memory. So, you should avoid reading the entire input file into memory at once. You should also avoid buffering the entire output file in memory at once.
Evaluation

Please send us a .zip or .tar.gz file with your program and a writeup about how your program works. This challenge is meant to take no more than a few hours, but you won't be judged on how long you wait before sending us your solution.

It is much more important to have a working program than the best possible program. There's no need to over-generalize or over-optimize your program. An ideal, awesome solution would have a basic working program and a short, yet thoughtful writeup about how it could be improved.

You can use any language you like. We'll be looking at the high-level approach you take and won't be paying attention to low-level optimizations. The most important thing is that your approach should work on a larger-than-memory dataset in a reasonable amount of time.

Your program can use any of its language's builtin in-memory data structures and algorithms, but if you need any disk-backed data structures, you should write the code yourself.

Feel free to use any outside resources, although any code you write should be your own!

In the writeup, we're hoping that you include:

    A short description of how to build and run your program
    The general approach you're taking, and why you chose it
    Any alternate approaches you considered, and why you didn't choose them
    A brief analysis of the resource needs and performance of your chosen approach
    Any assumptions you made about the properties of the dataset
    Any improvements you could make in the future

The writeup does not need to be very long: a few notes for each point should be enough.
