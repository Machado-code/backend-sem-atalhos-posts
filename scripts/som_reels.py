"""Coloca efeitos sonoros (sem voz) num Reels filmado com filmar_reels.py.

Uso:
  python3 scripts/som_reels.py <html> <video.mp4> <saida.mp4>

O HTML expõe window.eventosSom(), que devolve [[segundo, tipo], ...].
Tipos: tecla, enter, tique, taque, erro, blip, risco, acerto, virada.
Tudo é sintetizado aqui (numpy), então não há direito autoral de terceiros.
"""
import os
import subprocess
import sys
import tempfile
import wave

import numpy as np
from playwright.sync_api import sync_playwright
from scipy.signal import butter, lfilter

SR = 44100
rng = np.random.default_rng(7)


def env(n, ataque=0.002, queda=0.03):
    t = np.arange(n) / SR
    a = np.minimum(1, t / max(ataque, 1e-4))
    return a * np.exp(-t / queda)


def banda(x, lo, hi):
    b, a = butter(2, [lo / (SR / 2), hi / (SR / 2)], btype="band")
    return lfilter(b, a, x)


def seno(f, dur, queda):
    n = int(dur * SR)
    t = np.arange(n) / SR
    return np.sin(2 * np.pi * f * t) * env(n, 0.003, queda)


def tecla():
    n = int(0.035 * SR)
    clique = banda(rng.standard_normal(n), 1800, 6500) * env(n, 0.0005, 0.006)
    corpo = seno(rng.uniform(170, 230), 0.035, 0.01) * 0.5
    return (clique * 0.9 + corpo) * rng.uniform(0.4, 0.7)


def enter():
    return tecla() * 1.3 + np.pad(seno(120, 0.06, 0.02), (0, 0))[: int(0.035 * SR)] * 0.6


def tique(f=1900):
    return seno(f, 0.05, 0.012) * 0.9


def erro():
    partes = []
    for f in (196, 147):
        n = int(0.13 * SR)
        t = np.arange(n) / SR
        onda = np.sign(np.sin(2 * np.pi * f * t)) * 0.35 + np.sin(2 * np.pi * f * t) * 0.4
        partes.append(banda(onda, 80, 2500) * env(n, 0.004, 0.09))
    return np.concatenate(partes) * 0.8


def blip():
    return seno(1046, 0.08, 0.03) * 0.5 + seno(1568, 0.08, 0.02) * 0.2


def risco():
    n = int(0.7 * SR)
    t = np.arange(n) / SR
    ruido = banda(rng.standard_normal(n), 2500, 7000)
    mod = 0.55 + 0.45 * np.sin(2 * np.pi * 9 * t)
    janela = np.sin(np.pi * t / t[-1])
    return ruido * mod * janela * 0.22


def acerto():
    a = seno(880, 0.6, 0.25) + seno(1760, 0.6, 0.12) * 0.3
    b = seno(1318.5, 0.9, 0.35) + seno(2637, 0.9, 0.15) * 0.3
    out = np.zeros(int(1.2 * SR))
    out[: len(a)] += a * 0.5
    d = int(0.11 * SR)
    out[d : d + len(b)] += b * 0.55
    return out


def virada():
    n = int(0.45 * SR)
    t = np.arange(n) / SR
    ruido = rng.standard_normal(n)
    b, a = butter(2, 900 / (SR / 2), btype="low")
    return lfilter(b, a, ruido) * np.sin(np.pi * t / t[-1]) ** 2 * 0.5


SONS = {"tecla": tecla, "enter": enter, "tique": tique, "taque": lambda: tique(1450),
        "erro": erro, "blip": blip, "risco": risco, "acerto": acerto, "virada": virada}


def duracao(video):
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", video],
                         capture_output=True, text=True, check=True).stdout
    return float(out.strip())


def main(html, video, saida):
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--no-sandbox"])
        page = browser.new_page(viewport={"width": 1080, "height": 1920})
        page.goto(f"file://{os.path.abspath(html)}")
        eventos = page.evaluate("eventosSom()")
        browser.close()
    total = duracao(video)
    mix = np.zeros(int(total * SR) + SR)
    for t, tipo in eventos:
        s = SONS[tipo]()
        i = int(t * SR)
        mix[i : i + len(s)] += s[: max(0, len(mix) - i)]
    mix = mix[: int(total * SR)]
    mix *= 0.7 / max(1e-9, np.abs(mix).max())          # pico em cerca de -3 dB
    est = np.stack([mix, mix], axis=1)
    pcm = (est * 32767).astype("<i2")
    wav = os.path.join(tempfile.mkdtemp(prefix="som-"), "som.wav")
    with wave.open(wav, "wb") as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(pcm.tobytes())
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", video, "-i", wav, "-map", "0:v", "-map", "1:a",
                    "-c:v", "copy", "-c:a", "aac", "-b:a", "128k", "-shortest", "-movflags", "+faststart",
                    saida + ".part.mp4"], check=True)
    os.rename(saida + ".part.mp4", saida)
    print("ok", saida, f"{len(eventos)} efeitos")


if __name__ == "__main__":
    main(*sys.argv[1:4])
