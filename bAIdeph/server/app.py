from flask import Flask, render_template, send_from_directory

# app = Flask(__name__)
app = Flask(__name__, template_folder='../templates', static_folder='../bAIde/web')


@app.route('/<path:path>')  # Specific path for Flutter app
def send_flutter(path):
    return send_from_directory('../bAIde/web', path)

@app.route('/')  # Root of your Flutter app
def send_flutter_index():
    return send_from_directory('../bAIde/web', 'index.html')

@app.route('/<path:page_path>')
def render_page(page_path):
    return render_template(f'pages/{page_path}')

if __name__ == '__main__':
    print('Visit the online IDE at http://127.0.0.1:5000')
    app.run(debug=True)
