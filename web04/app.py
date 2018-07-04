from flask import *
from mongoengine import *
from models.video import Video
from youtube_dl import YoutubeDL
import mlab

app = Flask(__name__)
app.secret_key = "linhcute"
mlab.connect()

@app.route('/')
def index():
    videos = Video.objects()
    return render_template('index.html',videos = videos)

@app.route('/admin',methods = ["GET","POST"])
def admin():
    if request.method == "GET":
        videos = Video.objects()
        return render_template('admin.html',videos = videos)
    elif request.method == "POST":
        form = request.form
        link = form['link']

        ydl = YoutubeDL()
        data = ydl.extract_info(link, download=False)

        title = data['title']
        thumbnail = data['thumbnail']
        views = data['view_count']
        youtubeid = data['id']

        new_video = Video(
            title = title,
            thumbnail = thumbnail,
            views = views,
            link = link,
            youtubeid = youtubeid
        )

        new_video.save()
        
        return redirect(url_for('admin'))

@app.route('/detail/<youtubeid>')
def detail(youtubeid):
    return render_template('detail.html',youtubeid = youtubeid)

if __name__ == '__main__':
  app.run(debug=True)