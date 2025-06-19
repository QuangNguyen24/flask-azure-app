from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    html = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Flask CI/CD on Azure</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: linear-gradient(to right, #4facfe, #00f2fe);
                color: white;
                text-align: center;
                padding-top: 100px;
            }
            h1 {
                font-size: 3em;
                margin-bottom: 10px;
            }
            p {
                font-size: 1.2em;
            }
            .box {
                background-color: rgba(0, 0, 0, 0.3);
                border-radius: 12px;
                padding: 30px;
                width: 60%;
                margin: auto;
            }
        </style>
    </head>
    <body>
        <div class="box">
            <h1>🚀 Flask App Deployed via GitHub Actions</h1>
            <p>Welcome to your CI/CD deployment on <strong>Microsoft Azure App Service</strong>!</p>
            <p>✓ GitHub Actions ✓ Python ✓ Flask</p>
        </div>
    </body>
    </html>
    '''
    return render_template_string(html)

if __name__ == '__main__':
    app.run()
