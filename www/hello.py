# hello.py


def application(environ, start_response):
    res = '''
    <html>
<head>
  <title>Hello</title>
  <style>
    h1 {
      color: #333333;
      font-size: 48px;
      text-shadow: 3px 3px 3px #666666;
    }
  </style>
  <script>
    function change() {
      document.getElementsByTagName('h1')[0].style.color = '#ff0000';
    }
  </script>
</head>
<body>
  <h1 onclick="change()">Hello, %s!</h1>
</body>
</html>
    '''% (environ['PATH_INFO'][1:]or'web')
    
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [res.encode('utf-8')] #[b'<h1>Hello, web!</h1>']
