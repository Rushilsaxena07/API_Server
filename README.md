# API_Server
This is a fake API server which will fetch the json data and present it.
## Getting all the Posts
Simply run the main.py file: Command: **python main.py**, follow the link provided and all the posts will be listed.

<hr>

## Getting a particular post from postId
Follow the above mention steps, and add `/resource/<any postId number>`, and you will be able to see only that specific post.
<hr>

## Getting comments from a post
Add `/resource/<postIdNumber>/comments` or `/resource/comments?postId=<postId-Number>`.
