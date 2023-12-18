# gemini-ai-telegram
<p align=center>
<img src="https://github.com/AbhiTheModder/gemini-ai-telegram/assets/85984486/710e32e6-3751-4cc9-b846-f17367076962" width=500 height=300>

   **Pyrogram(Pyrofork) Based Python script for Telegram Userbots and Bots**
</p>

**Try it Out in Telegram:** [Here](https://t.me/gemini_testbot)

# Requirements:
- Python >=3.9
- Get [Obtain an API key from AI Studio](https://makersuite.google.com/app/apikey)
- pyrofork : `pip install pyrofork`
- google-generativeai : `pip install google-generativeai`
- PIL : `pip install Pillow` `# Only if you want to use 'aimage.py/google-pro-vision' model`

# Note:
 **Users in termux may face issue with installation of `google-generativeai`**
- To fix it install  these libraries first:
- `pkg update && pkg upgrade -y`
- `pkg install python`
- `pkg install openssl zlib c-ares -y`
- Install `grpcio` through below command:
 ```
GRPC_PYTHON_DISABLE_LIBC_COMPATIBILITY=1 GRPC_PYTHON_BUILD_SYSTEM_OPENSSL=1 GRPC_PYTHON_BUILD_SYSTEM_ZLIB=1 GRPC_PYTHON_BUILD_SYSTEM_CARES=1 CFLAGS+=" -U__ANDROID_API__ -D__ANDROID_API__=33 -include unistd.h" LDFLAGS+=" -llog" pip install grpcio
```
- OR If you're too lzy to cpmile yourself and your API LEVEL is 33(Android OS: 13), Lucky You because i've pushed release of compiled wheels in [releases](https://github.com/AbhiTheModder/gemini-ai-telegram/releases/) section of this repo :D

- Now install `google-generativeai`:
  ```
  pip install google-generativeai
  ```
**Note:** Make sure to put your own `ANDROID_API` to which your device/android OS version sdk is on(based)

# Usage:
- Except for Termux users simply `pip install -r requirements.txt` is enough
- AGAIN make sure to get your api keys :D
- **Userbots:**
  Use files starting with `ub`, Fill the keys and you're good to go
- **Simple Bots:**
  Use files starting with `bot`, Fill the keys and you're good to go

  - You can also use `botmerged.py` if you want to integrate both models to your bot
  - FURTHER If you want to host through any cloud service provider like koyeb,back4app,heroku etc you can use files from [cloud-host](https://github.com/AbhiTheModder/cloud-host-gemini-tg) repo

## CREDITS:
- [Pyrofork](https://github.com/Mayuri-Chan/pyrofork/)
- [GeminiAi](https://blog.google/technology/ai/google-gemini-ai/)
- Myself :D
