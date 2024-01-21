from flask import Flask, render_template, request, jsonify
import model

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set a secret key for flash messages


@app.route('/')
def homepage():
    return render_template('homepage.html')


@app.route('/homepage')
def home():
    return render_template('homepage.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/price')
def price():
    return render_template('price.html')


@app.route('/sidebar')
def sidebar():
    return render_template('sidebar.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/splash')
def splash():
    return render_template('splash.html')


@app.route('/form1', methods=['POST'])
def form1():
    user_input1 = None
    user_input2 = None

    if request.method == 'POST':
        user_input1 = request.form.get('user_input1')
        user_input2 = request.form.get('user_input2')
    plt = model.plot_against_two(user_input1, user_input2)
    plot_data = model.plot_to_img(plt)
    return render_template('hah.html', plot_data=plot_data)


@app.route('/hac')
def hac():
    return render_template('hac.html')


@app.route('/ic')
def ic():
    plt = model.indi_cluster()
    plot_data = model.plot_to_img(plt)
    return render_template('ic.html', plot_data=plot_data)


@app.route('/threed')
def threed():
    plt = model.plot_3dcluster()
    plot_data = model.plot_to_img(plt)
    return render_template('threed.html', plot_data=plot_data)


@app.route('/started')
def started():
    return 0


@app.route('/hah')
def hah():
    return render_template('hah.html')


@app.route('/form2', methods=['POST'])
def form2():
    user_input1 = None
    user_input2 = None

    if request.method == 'POST':
        user_input1 = request.form.get('user_input1')
        user_input2 = request.form.get('user_input2')
    plt = model.plot_against_two(user_input1, user_input2)


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'

    file = request.files['file']

    if file.filename == '':
        return 'No selected file'

    # Save the file to a desired location
    file.save('uploads/' + file.filename)
    model.uploaded_file(file.filename)


@app.route('/index1', methods=['POST'])
def index1():
    header = model.get_header()
    elements = header
    return render_template('index1.html', elements=elements)


if __name__ == '__main__':
    app.run(debug=True)
