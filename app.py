from flask import Flask, render_template
from werkzeug.middleware.proxy_fix import ProxyFix


app = Flask(__name__)

# Informa ao Flask para ler os cabeçalhos X-Forwarded-* enviados pelo Nginx
# Isso faz o url_for() entender que a base da app é /apps/helloworld/
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1)

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == '__main__':
    # host='0.0.0.0' é necessário para o Flask responder fora da interface 127.0.0.1 do próprio container
    app.run(host='0.0.0.0', port=5000, debug=True)