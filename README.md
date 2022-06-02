# Media to anki (python3+)
É um conjunto de scripts que gera um deck anki a partir de algum vídeo com legendas.

## Instalando requisitos
```shell
poetry install
```

## Sintaxe
```
usage: mediatoanki.py [-h] [--padstart seconds] [--padend seconds]              
                      video_source subtitle_source dest                         
                                                                                
Create an anki deck given media and subtitles.                                  
                                                                                
positional arguments:                                                           
  video_source        Video file (.mp4, .mkv)                                   
  subtitle_source     Subtitle file (.vtt, .src, etc)                           
  dest                Destination for files.                                    
                                                                                
optional arguments:                                                             
  -h, --help          show this help message and exit                           
  --padstart seconds  Add more time to the start of the scene from subtitle     
  --padend seconds    Add more time to the end of the scene from subtitle  
```

## Exemplos de uso

### Gerando um deck
```
poetry run python mediatoanki.py mrrobot.mkv mrrobot.vtt decks
```
#### Saida do comando
![img.png](images/img.png)

### Importando o deck para o anki
O deck gerado está em formato .apkg.

#### Método 1: Importando via linha de comando.
```
$ anki deck.apkg 
```

#### Método 2: Importante pela interface gráfica.
Clique no botão File > Import e selecione o arquivo .apkg.

#### Resultado
![img_3.png](images/img_3.png)

### Armazenando os arquivos de media no anki
Após o deck ser importado os arquivos armazenados na pasta media 
devem ser enviados para a pasta `collection.media` do usuário do anki. Caso contrário
os flash-cards ficaram sem as imagens e aúdios.
#### Resultado
![img_4.png](images/img_4.png)

