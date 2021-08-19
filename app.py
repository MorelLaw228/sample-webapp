from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index():
    # load current count
    #  We open ht file "count.txt" in read mode with (r)
    f = open("count.txt","r")
    # We read the content of the file with "f.read()" and we cast the value to the integer with int()
    count = int(f.read())
    # We close the file with  "f.close()"
    f.close()

    # Increment the count
    count += 1

    # Now , we open the file "count.txt" in overwrite mode(w) and write the value of the new count
    # Overwrite the count
    f = open("count.txt","w")
    f.write(str(count))
    f.close()

    # render HTML with count variable
    return render_template("index.html",count=count)


if __name__ == '__main__':
    app.run(port=5001,debug=True)
