termux-setup-storage && apt install python -y && pip install --upgrade pip && pip install pafy youtube-dl && cp -r ~/ytdownloader /sdcard && rm /sdcard/ytdownloader/setup.sh && rm /sdcard/ytdownloader/yt.sh && cp ~/ytdownloader/yt.sh ~/yt.sh && chmod +x ~/yt.sh && echo Установка завершена. Для запуска введите ./yt.sh