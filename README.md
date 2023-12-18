# gemini-ai-telegram
<p align=center>
<img src="https://github.com/AbhiTheModder/gemini-ai-telegram/assets/85984486/710e32e6-3751-4cc9-b846-f17367076962" width=500 height=300>

   **Pyrogram(Pyrofork) Based Python script for Telegram Userbots and Bots**
</p>


# Requirements:
- Python >=3.9
- Get [Obtain an API key from AI Studio](https://makersuite.google.com/app/apikey)
- pyrofork : `pip install pyrofork`
- google-generativeai : `pip install google-generativeai`
- PIL : `pip install Pillow` `# Only if you want to use 'aimage.py/google-pro-vision' model`

## Note: Users in termux may face issue with installation of `google-generativeai`
- To fix it install  these libraries first:
- `pkg update && pkg upgrade -y`
- `pkg install python`
- `pkg install openssl zlib c-ares -y`
- Install `grpcio` through below command:
 ```
GRPC_PYTHON_DISABLE_LIBC_COMPATIBILITY=1 GRPC_PYTHON_BUILD_SYSTEM_OPENSSL=1 GRPC_PYTHON_BUILD_SYSTEM_ZLIB=1 GRPC_PYTHON_BUILD_SYSTEM_CARES=1 CFLAGS+=" -U__ANDROID_API__ -D__ANDROID_API__=33 -include unistd.h" LDFLAGS+=" -llog" pip install grpcio
```
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
  `You can alslo use `botmerge` if you want to integrate both models to your bot
