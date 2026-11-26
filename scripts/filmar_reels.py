"""Filma um Reels desenhado em HTML (1080x1920) cuja página expõe window.render(t).

Uso:
  python3 scripts/filmar_reels.py <html> <saida.mp4> <segundos_animados> <segundos_parados>
  python3 scripts/filmar_reels.py <html> --quadros 3.0,8.5,12 <pasta>   (só tira fotos para conferir)

A parte animada vira um arquivo; o final parado vira outro (quadro fixo em loop);
os dois são unidos sem recodificar e recebem uma faixa de áudio silenciosa.
"""
import os
import subprocess
import sys
import tempfile

from playwright.sync_api import sync_playwright

FPS = 30
X264 = ["-c:v", "libx264", "-crf", "18", "-preset", "veryfast", "-pix_fmt", "yuv420p", "-r", str(FPS)]


def abrir(p, html):
    browser = p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--no-sandbox"])
    page = browser.new_page(viewport={"width": 1080, "height": 1920}, device_scale_factor=1)
    page.goto(f"file://{os.path.abspath(html)}")
    page.wait_for_timeout(300)
    return browser, page


def quadros(html, tempos, pasta):
    os.makedirs(pasta, exist_ok=True)
    with sync_playwright() as p:
        browser, page = abrir(p, html)
        for t in tempos:
            page.evaluate(f"render({t})")
            caminho = os.path.join(pasta, f"quadro-{t:05.2f}.png")
            page.screenshot(path=caminho)
            print(caminho)
        browser.close()


def filmar(html, saida, animado, parado):
    tmp = tempfile.mkdtemp(prefix="reels-")
    cena1 = os.path.join(tmp, "cena1.mp4")
    cena2 = os.path.join(tmp, "cena2.mp4")
    ultimo = os.path.join(tmp, "ultimo.png")
    n = round(animado * FPS)
    with sync_playwright() as p:
        browser, page = abrir(p, html)
        ff = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "image2pipe", "-framerate", str(FPS),
                               "-c:v", "mjpeg", "-i", "-", *X264, cena1 + ".part.mp4"], stdin=subprocess.PIPE)
        for i in range(n):
            page.evaluate(f"render({i / FPS})")
            ff.stdin.write(page.screenshot(type="jpeg", quality=92))
        ff.stdin.close()
        if ff.wait() != 0:
            sys.exit("ffmpeg falhou na cena animada")
        os.rename(cena1 + ".part.mp4", cena1)
        page.evaluate(f"render({animado})")
        page.screenshot(path=ultimo)
        browser.close()
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", str(FPS), "-i", ultimo,
                    "-vf", f"format=yuv420p,loop=-1:1,trim=duration={parado}", *X264, cena2 + ".part.mp4"], check=True)
    os.rename(cena2 + ".part.mp4", cena2)
    lista = os.path.join(tmp, "lista.txt")
    with open(lista, "w") as f:
        f.write(f"file '{cena1}'\nfile '{cena2}'\n")
    junto = os.path.join(tmp, "junto.mp4")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", lista, "-c", "copy", junto], check=True)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", junto, "-f", "lavfi", "-i", "anullsrc=r=44100:cl=stereo",
                    "-map", "0:v", "-map", "1:a", "-c:v", "copy", "-c:a", "aac", "-b:a", "64k", "-shortest",
                    "-movflags", "+faststart", saida + ".part.mp4"], check=True)
    os.rename(saida + ".part.mp4", saida)
    print("ok", saida)


if __name__ == "__main__":
    if sys.argv[2] == "--quadros":
        quadros(sys.argv[1], [float(x) for x in sys.argv[3].split(",")], sys.argv[4])
    else:
        filmar(sys.argv[1], sys.argv[2], float(sys.argv[3]), float(sys.argv[4]))
