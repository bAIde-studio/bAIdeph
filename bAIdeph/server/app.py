from flask import Flask, render_template

# app = Flask(__name__)
app = Flask(__name__, template_folder='../templates', static_folder='../bAIde/web')


@app.route('/')
def hello_world():
    return 'Hello, from Flask!'

@app.route('/<path:page_path>')
def render_page(page_path):
    return render_template(f'pages/{page_path}')

if __name__ == '__main__':
    print('Visit the online IDE at http://127.0.0.1')
    app.run(debug=True)
