import os
import subprocess

import yt_dlp
from flask import Flask, flash, redirect, render_template, request

app = Flask(__name__)
app.secret_key = 'segredo'

DOWNLOAD_DIR = os.path.join(os.path.dirname(__file__), 'downloads')
os.makedirs(DOWNLOAD_DIR, exist_ok=True)


def ffmpeg_instalado():
    try:
        subprocess.run(['ffmpeg', '-version'], stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE, check=True)
        return True
    except Exception:
        return False


def download_with_ytdlp(url, mode):
    ydl_opts = {
        'outtmpl': os.path.join(DOWNLOAD_DIR, '%(title)s.%(ext)s'),
        'noplaylist': mode != 'playlist',
    }

    if mode == 'audio':
        if ffmpeg_instalado():
            ydl_opts.update({
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }]
            })
        else:
            raise RuntimeError(
                "FFmpeg não está disponível para conversão de áudio.")
    elif mode == 'video':
        if ffmpeg_instalado():
            ydl_opts.update({'format': 'bestvideo+bestaudio/best'})
        else:
            # fallback para uma stream única com vídeo + áudio combinados
            ydl_opts.update({'format': 'best'})
    elif mode == 'playlist':
        ydl_opts.update({'format': 'best'})

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form.get('url')
        tipo = request.form.get('download_type')

        try:
            download_with_ytdlp(url, tipo)
            flash('Download concluído com sucesso!', 'success')
        except Exception as e:
            flash(f'Erro: {e}', 'danger')

        return redirect('/')

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
