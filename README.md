# basehttpserver-base64-webshell
A self-serving Python 2.7 HTTP GET/POST Web Shell

## Trivia
Some days ago `sid` and me were writing a mod_python webshell to perform some Penetration Testing activity. You can access the code of [modpython-base64-webshell|https://github.com/siddolo/modpython-base64-webshell].

Today I noticed that the customer is instead using `mod_wsgi` so our code was not fit for his infrastructure.

I just rewrote it to serve itself and killed the apache thread :)

## How to run
The `port` parameter is optional and default to `80`.
```
./shell.py [port]
```

## How to connect
Set the endpoint URL in the client and run it. The `method` parameter is optional, defaults to `POST`, accepted values are `POST` or `GET`.
```
./client [method]
```
