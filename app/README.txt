

++++ venv installed libraries ++++++

pip install : 
    -Flask
    -requests
    -pymongo
    -pymongo[srv]
    -beautifulsoup4
    -aiohttp
    -aiofiles
    -aiodns
    -validators
    -fastapi
    -uvicorn[standard]
    -jinja2


+++++build docker container+++++++++

    docker build -t web_scrapper ./

++++++run docker container based on fastapi++++++++++++++

    docker run  --name web_scrapper -p 80:80 web_scrapper


+++++++docker pull command +++++++++

docker pull duftcola/web_scrapper:latest