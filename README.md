# python-website
This is a short example on how you can use Python to create a simple HTTP Web Server.

It uses Flask which is a light weight library for building web applications.

When this example is running, you can open a Web Browser and point it to port 5000 on your machine, e.g.

> http://localhost:5000/index.html

To use the Python script on Windows, you can run python3.exe as illustrated:

```
C:\Users\stephenquan\Documents>python3 python-website.py
 * Serving Flask app "python-website" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
127.0.0.1 - - [30/Apr/2020 16:44:20] "GET /home-32.svg HTTP/1.1" 304 -
127.0.0.1 - - [30/Apr/2020 16:44:21] "GET /favicon.ico HTTP/1.1" 404 -
```
