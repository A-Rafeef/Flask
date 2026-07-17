from flask import Flask, render_template, request
import csv
import io

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_csv():
    parsed_data = []
    
    if request.method == 'POST':
        # Check if the file part is present in the request
        if 'csv_file' not in request.files:
            return "No file part in the form", 400
            
        file = request.files['csv_file']
        
        # Check if the user submitted an empty file form
        if file.filename == '':
            return "No selected file", 400

        if file and file.filename.endswith('.csv'):
            # Read the file stream as text stream
            stream = io.StringIO(file.stream.read().decode("UTF8"), newline=None)
            csv_input = csv.reader(stream)
            
            # Loop through rows, print to console, and store for the webpage
            for row in csv_input:
                print(row)  # This prints the CSV rows to your Flask server console
                parsed_data.append(row)

    return render_template('form.html', data=parsed_data)

if __name__ == '__main__':
    app.run(debug=True)