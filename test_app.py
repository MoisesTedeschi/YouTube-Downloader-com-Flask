from unittest import mock

import pytest

from app import app, download_with_ytdlp, ffmpeg_instalado


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_ffmpeg_instalado_true():
    with mock.patch('subprocess.run') as mocked_run:
        mocked_run.return_value.returncode = 0
        assert ffmpeg_instalado() is True


def test_ffmpeg_instalado_false():
    with mock.patch('subprocess.run', side_effect=Exception("Erro")):
        assert ffmpeg_instalado() is False


@mock.patch('app.ffmpeg_instalado', return_value=True)
@mock.patch('app.yt_dlp.YoutubeDL')
def test_download_with_ytdlp_video(mock_yt, mock_ffmpeg):
    download_with_ytdlp("https://youtube.com/fake", "video")
    mock_yt.assert_called_once()
    mock_yt.return_value.__enter__.return_value.download.assert_called_once()


@mock.patch('app.ffmpeg_instalado', return_value=False)
@mock.patch('app.yt_dlp.YoutubeDL')
def test_download_with_ytdlp_video_fallback(mock_yt, mock_ffmpeg):
    download_with_ytdlp("https://youtube.com/fake", "video")
    mock_yt.assert_called_once()
    mock_yt.return_value.__enter__.return_value.download.assert_called_once()


@mock.patch('app.ffmpeg_instalado', return_value=False)
def test_download_with_ytdlp_audio_without_ffmpeg(mock_ffmpeg):
    with pytest.raises(RuntimeError):
        download_with_ytdlp("https://youtube.com/fake", "audio")


@mock.patch('app.download_with_ytdlp')
def test_index_post_success(mock_download, client):
    response = client.post('/', data={
        'url': 'https://youtube.com/fake',
        'download_type': 'video'
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b'Download conclu' in response.data


@mock.patch('app.download_with_ytdlp', side_effect=Exception("Erro ao baixar"))
def test_index_post_error(mock_download, client):
    response = client.post('/', data={
        'url': 'https://youtube.com/fake',
        'download_type': 'video'
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b'Erro: Erro ao baixar' in response.data


def test_index_get(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'YouTube Downloader' in response.data
