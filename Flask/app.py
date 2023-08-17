from flask import Flask, render_template, request, send_from_directory
from utils import process_multiple_pages
import os

app = Flask(__name__)

# Get the directory where the script is located
script_directory = os.path.dirname(os.path.abspath(__file__))

# Define the route for the homepage
@app.route('/', methods=['GET', 'POST'])

if request.method == 'POST':
    start_url = request.form['start_url']
    output_filename = 'combined-output.docx'
    save_path = os.path.join(script_directory, output_filename)
    process_multiple_pages(start_url, save_path)
    render_template('index.html', download_link=output_filename)
render_template('index.html', download_link=None)

@app.route('/download/<filename>')
send_from_directory(script_directory, filename, as_attachment=True)
#if __name__ == '__main__':
 #   app.run(debug=True)
