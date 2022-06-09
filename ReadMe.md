# Simple Chat
## This is a chat between two users (dialogue)
To run it, download the project, open it in the PyCharm IDE, run the server, and tap the link in the terminal.
```sh
python manage.py runserver
```
## /admin

Login: admin
Password: 12345678

## Structure

The application consists 6 url (endpoints):

- ['/'] - main page
- ['/create'] - here you can create new chat
- ['/'str_thread''] - list of user's chats
- ['/str_messages'] - list of messages
- ['/mark'] - read marks
- ['/unread'] - number of unread messages



