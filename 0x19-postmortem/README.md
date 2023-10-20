# Postmortem Report

## 504 Error while accessing a given URL

#### Summary

On September 11th, 2018 at midnight the server access went down resulting in 504 error for anyone trying to access a website. Background on the server being based on a LAMP stack.

#### Timeline

- **00:00 GMT** - 500 error for users trying to access the site
- **00:05 GMT** - Ensuring Apache and MySQL are running
- **00:10 GMT** - Problems with the website loading
- **00:12 GMT** - After quick Apache restart the server returned a status of 200 and was OK
- **00:18 GMT** - Reviewing Error Logs to search for the cause of the problem
- **00:25 GMT** - Check /var/log to see that the apache server was being prematurely shut down
- **00:30 GMT** - Checking php.ini found out error logging was off so turned it on
- **00:32 GMT** - Restarting Apache
- **00:34 GMT** - Reviewing error logs again revelead a mistyped file resulting for the error
- **00:38 GMT** - Fixing file name and restarting Apache server
- **00:40 GMT** - Server is now running normally

#### Root Cause And Solution

The issue was connected with a wrong file name. The error was raised when trying to curl to the server, once the error logs were checked the problem was discovered and fixed by changing the file extension through Puppet

#### Corrective and Preventive Measures

All servers and sites should have error logging turned on to easily identify errors
