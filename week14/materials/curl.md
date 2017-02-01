# HTTP Client with curl

`curl` is a very helpful and useful tool when you have to deal with HTTP calls.

Since it may not be available in your distro, make sure that you install it:

```
$ sudo apt-get install curl
```

## Making GET requests

The simplest thing you can do with `curl` is to make a GET request to a URL

```
$ curl https://hackbulgaria.com/

<some html here>
```

If you want to see the response headers, you can call curl with `-I`:

```
$ curl -I https://hackbulgaria.com/
HTTP/1.1 200 OK
Server: nginx/1.8.0
Date: Wed, 10 Feb 2016 12:03:57 GMT
Content-Type: text/html; charset=utf-8
Connection: keep-alive
X-Frame-Options: SAMEORIGIN
Content-Language: bg
Vary: Accept-Language, Cookie
```

This is very helpful in order to debug things.

If you want to see request headers, you can do the following things:


1. Start a netcat server at some port: `$ nc -l 8000`
2. Execute: `$ curl https://localhost:8000`
3. On the `nc` tab you will see the **request headers**

```
GET / HTTP/1.1
User-Agent: curl/7.37.1
Host: localhost:8000
Accept: */*
```


The other way is to execute:

```
$ curl -vs https://hackbulgaria.com > /dev/null

... some output ...
> GET / HTTP/1.1
> User-Agent: curl/7.37.1
> Host: hackbulgaria.com
> Accept: */*
>
< HTTP/1.1 200 OK
* Server nginx/1.8.0 is not blacklisted
< Server: nginx/1.8.0
< Date: Wed, 10 Feb 2016 12:06:01 GMT
< Content-Type: text/html; charset=utf-8
< Transfer-Encoding: chunked
< Connection: keep-alive
< X-Frame-Options: SAMEORIGIN
< Content-Language: bg
< Vary: Accept-Language, Cookie
<
```

`-vs` means `verbose` and `silent` and we redirect the HTML output to `/dev/null`
