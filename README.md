# gemini-ai-telegram
<p align=center>
<img src="https://github.com/AbhiTheModder/gemini-ai-telegram/assets/85984486/710e32e6-3751-4cc9-b846-f17367076962" width=500 height=300>

![GitHub Repo stars](https://img.shields.io/github/stars/AbhiTheModder/gemini-ai-telegram)

   **Pyrogram(Pyrofork) Based Python script for Telegram Userbots and Bots**
</p>

### 📹 You can checkout the demo video:
- Using for bots: [Here](https://x.com/Qbtaumai/status/1736681149047726176?s=20)
- Using as UserBot: [Here](https://x.com/Qbtaumai/status/1736681423703351629?s=20)

# 🚀 Demo
**Try it Out in Telegram:** [Here](https://t.me/gemini_testbot)

## ☁️ Cloud Host:

<a href="https://app.koyeb.com/deploy?type=git&repository=github.com/AbhiTheModder/gemini-ai-telegram&branch=main&name=gemini"><img src="https://www.koyeb.com/static/images/deploy/button.svg">

## 🐋 Docker:
**[Instructions](docker.md)**

## 📦 Requirements:
- Python >=3.9 [Best if >=python3.11]
- Get API_KEY : [Obtain an API key from AI Studio](https://makersuite.google.com/app/apikey)
- Get BOT_TOKEN of your bot from [@BotFather](https://t.me/botfather)
- Get API_ID and API_HASH from my.telegram.org -> `Api development tools` option
- pyrofork : `pip install pyrofork`
- google-generativeai : `pip install google-generativeai`
- PIL : `pip install Pillow` `# Only if you want to use 'aimage.py/google-pro-vision' model`

## 🗒️ Note:
 **Users in termux may face issue with installation of `google-generativeai`**
- To fix it install  these libraries first:
- `pkg update && pkg upgrade -y`
- `pkg install python`
- `pkg install openssl zlib c-ares -y`
- Install `grpcio` through below command:
 ```
GRPC_PYTHON_DISABLE_LIBC_COMPATIBILITY=1 GRPC_PYTHON_BUILD_SYSTEM_OPENSSL=1 GRPC_PYTHON_BUILD_SYSTEM_ZLIB=1 GRPC_PYTHON_BUILD_SYSTEM_CARES=1 CFLAGS+=" -U__ANDROID_API__ -D__ANDROID_API__={YOUR API LEVEL} -include unistd.h" LDFLAGS+=" -llog" pip install grpcio
```
**🗒️Note:** Make sure to put your own `ANDROID_API` to which your device/android OS version sdk is on(based)
- OR If you're too lzy to compile yourself and your API LEVEL is 33(Android OS: 13), Lucky You because I've pushed release of compiled wheels in [releases](https://github.com/AbhiTheModder/gemini-ai-telegram/releases/) section of this repo :D

- Now install `google-generativeai`:
  ```
  pip install google-generativeai
  ```

# 🏃 Usage:
- Except for Termux users simply `pip install -r requirements.txt` is enough
- AGAIN make sure to get your api keys :D
- **Userbots:**
  Use files starting with `ub`, Fill the keys and you're good to go
- **Simple Bots:**
  Use files starting with `bot`, Fill the keys and you're good to go

  - You can also use `botmerged.py` if you want to integrate both models to your bot
- **Group Bot**
  Use file starting with `botmrg_grp.py`
  - It has feature of allowing use in private also and without commands allowing user to interact like chatting with someone

## 💖 Like my work?
This project needs a ⭐ from you. Don't forget to leave a ⭐.    

## 👨‍💻 CREDITS:
- [Pyrofork](https://github.com/Mayuri-Chan/pyrofork/)
- [GeminiAi](https://blog.google/technology/ai/google-gemini-ai/)
- Myself :D
