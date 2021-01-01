import pafy, time, os, sys
def out_red(text):
    print("\033[31m {} \033[0m" .format(text))
def out_green(text):
	print("\033[32m {} \033[0m" .format(text))
def out_blue(text):
	print("\033[34m {} \033[0m" .format(text))
banner = """
 ____________________________
|                            |
| YouTube Video Downloader   |
| Author: ilya1391           |
| Version: 1.1               |
| Status: Stable             |
|____________________________|
"""
out_blue(banner)
print("")
out_blue("Для загрузки видео/аудио с Youtube вставьте ссылку ниже")
url = input("\033[34mСсылка на видео:\033[0m ")
out_blue("Для загрузки видео введите 1, для загрузки аудио введите 2")
choice = input("\033[34mВведите цифру:\033[0m ")
def download(choice):
    try:
        v = pafy.new(url)
        if choice == "1":
            streams = v.streams
        elif choice == "2":
            streams = v.audiostreams
        else:
            out_red("unknown command. programm closed")
        out_blue("Выберите качество загружаемого видео. Например: 1 : ") if choice == "1" else print("Выберите качество загружаемого аудио. Например: 2 : ")
        available_streams = {}
        count = 1
        for stream in streams:
            available_streams[count] = stream
            print(f"{count}: {stream}")
            count += 1
        stream_count = int(input("Введите номер: "))
        d = streams[stream_count - 1].download()
        if choice == "2":
            audio_extension = str(available_streams[stream_count])
            audio_extension = audio_extension.split("@")[0].split(":")[1]
            file_name = v.title
            music_file = f"{file_name}.{audio_extension}"
            base = os.path.splitext(music_file)[0]
            os.rename(music_file, base + ".mp3")
        out_green("Загрузка завершена!")
        out_green("Ваше видео/аудио лежит во внутреней памяти в папке ytdownloader")
    except:
        out_red("unknown command. programm closed")
download(choice)