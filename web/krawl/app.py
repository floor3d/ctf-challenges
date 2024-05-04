from flask import Flask, render_template_string, abort
import os

app = Flask(__name__)


@app.route('/')
def index():
    # Redirect to the /f1 route
    return """
    The bunny has scattered a bunch of files. One of them has something... There are enough so that you simply won't find it manually. Make a script to do it!
    <br />
    <a href=/file1>hop... hop... hop...</a>
    <br />
    If you want starter code, look below!
    <br />

    <br />
    <br />
    <br />
    <br />
    <br />
    <br />
    <br />
    <br />
    <br />
    <br />
    <br />
    <br />
    <br />
    <br />
    <br />
    [THIS CODE WILL BE USEFUL]
    <br />
<pre>
import requests

def retrieve_letters(base_url, num_files):

    for i in range(1, num_files + 1):
        # fix the file URL! what should it look like?
        file_url = f"{base_url}/idk?????"
        response = requests.get(file_url).text
        # what now? the flag definitely has "CTF" in it ...

    return None

#put the base url here
base_url = "put the base url here"
# guess... how many files? to be safe, put a decently large number. hint: it's more than 100
num_files = 0

message = retrieve_letters(base_url, num_files)
print(message)
</pre>
"""


@app.route('/file<int:file_number>')
def show_file(file_number):
    file_path = f"files/file{file_number}"
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            flag = file.readline()
        return render_template_string("<html><h2>{{ flag }}</h2></html>", flag=flag)
    else:
        abort(404)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
