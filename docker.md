**Suppose for this example you need to run `botai.py` so for it to run via docker:**

- Enter `gemini-ai-telegram` directory;
```shell
cd gemini-ai-telegram
```

- Now use nano to edit that file and put your vars like api id,hash etc in it:
```shell
nano botai.py
```

- After that's done use nano again to edit Dockerfile:
```shell
nano Dockerfile
```

**In that you don't have to edit anything only last line where file name of your python is suppose you ever wanted to run other files then put that's name there**

- Now after that's done run below command:
```shell
docker build . gemini:latest
```
This will build you docker image

- Now to run in background:
```shell
docker run -d gemini:latest
```
