from flask import Flask, request
import subprocess

app = Flask(__name__)

def run_command(cmd):
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()  
    #This makes the wait possible
    p_status = p.wait()
    return str(output).split(" ")

def get_crontab():
    return run_command("crontab -l | grep -v -E \"^#|^;\"")



@app.route("/")
def default():
    output =  """
    <form method="post" action="/syncnow">
    <div class="form-group">
      <label for="user">Benutzername</label>
      <input type="text" class="form-control" id="user" name="user" placeholder="uwe" value="Uwe">
    </div>

    <div class="form-group">
      <label for="host">Zielhost</label>
      <input type="text" class="form-control" id="host" name="host" placeholder="hasenbalg.org" value="192.168.1.127">
    </div>

    <div class="form-group">
      <label for="port">Port</label>
      <input type="text" class="form-control" id="port" name="port" placeholder="22" value="22">
    </div>

    <div class="form-group">
      <label for="source">Quellordner</label>
      <input type="text" class="form-control" id="source" name="source" placeholder="/huhu/hehe/" value="/huhu">
    </div>
    <div class="form-group">
        <label for="destination">Zielordner</label>
        <input type="text" class="form-control" id="destination" name="destination" placeholder="/hihi/hoho/" value="/hihi">
      </div>
    <button type="submit" class="btn btn-default">Rsync starten</button>
  </form>
    """

    return output + get_crontab()[2]


@app.route("/syncnow",  methods=['GET', 'POST'])
def sync_now():
    if request.method == 'POST':
        user = request.form.get('user')
        print(user)

        host = request.form.get('host')
        print(host)

        port = request.form.get('port')
        print(port)

        source = request.form.get('source')
        print(source)

        destination = request.form.get('destination')
        print(destination)
        
        print("syncing")
        return "rsync -v -e ssh -p" + port + " " + source +" " + user + "@" + host + ":"+ destination


if __name__ == "__main__":
    app.run(debug=True)
