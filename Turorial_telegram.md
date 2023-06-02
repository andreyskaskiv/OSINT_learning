#  Turorial telegram

```bash
 pip install --upgrade pip
 pip install -r requirements.txt
 ```
~~~shell
$ pip freeze > requirements.txt
~~~


1. [snscrape](https://github.com/bellingcat/snscrape)

    Console:
    ```text
    snscrape --max-results 10 vkontakte-user username > vk-@username.txt
    snscrape --max-results 10 --jsonl vkontakte-user username > vk-@username_jsonl.txt
    snscrape --max-results 10 --jsonl vkontakte-user group_name > vk-@group_name_jsonl.txt
    snscrape --max-results 10 --jsonl --progress telegram-channel python2day > telegram-@channel_name_jsonl.txt 
    snscrape --max-results 10 --jsonl instagram-user username > instagram-@username_jsonl.txt
    ```

2. [telegram_parser.py](Telegram%2Ftelegram_parser.py)


