from flask import Flask, render_template, request, redirect, flash
import io
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


@app.route('/hacc', methods=['POST'])
def hacc():
    user_input1 = None

    if request.method == 'POST':
        user_input1 = request.form.get('user_input1')
    plt = model.plot_data_cluster(user_input1)
    plot_data = model.plot_to_img(plt)
    return render_template('hacc.html', plot_data=plot_data)


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


@app.route('/form2')
def hah():
    return render_template('hah.html')


@app.route('/hah', methods=['POST'])
def form2():
    user_input1 = None
    user_input2 = None
    if user_input2 is not None:
        if 'form1_submit' in request.form:
            # Handle form 1 data
            data_from_form1 = request.form['form1_input']
            # Do something with form 1 data
            return f'Form 1 submitted with data: {data_from_form1}'

        elif 'form2_submit' in request.form:
            # Handle form 2 data
            data_from_form2 = request.form['form2_input']
            # Do something with form 2 data
            return f'Form 2 submitted with data: {data_from_form2}'
        if request.method == 'POST':
            user_input1 = request.form.get('user_input1')
            user_input2 = request.form.get('user_input2')

        flash(user_input1, 'info')
        plt = model.plot_against_two(user_input1, user_input2)
        image = model.plot_to_img(plt)

        image_bytes = io.BytesIO()
        image.save(image_bytes, format='PNG')
        image_bytes.seek(0)
        return render_template('hah.html', image=image_bytes)
    else:
        return render_template('hah.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        flash('No file part', 'error')
        return redirect(request.url)

    file = request.files['file']

    if file.filename == '':
        flash('No selected file', 'error')
        return redirect(request.url)

    if file:
        # Save the uploaded file to a desired location (e.g., "uploads" folder)
        file.save('uploads/' + file.filename)

        # Flash a success message
        flash('File uploaded successfully!', 'success')

    return render_template('homepage.html')


@app.route('/index1', methods=['POST'])
def index1():
    header = model.get_header()
    elements = header
    return render_template('index1.html', elements=elements)


if __name__ == '__main__':
    app.run(debug=True)
