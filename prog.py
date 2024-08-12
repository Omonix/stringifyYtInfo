from pytube import YouTube
import json

def viewser(views):
    tab_letter = ['', 'K', 'M', 'Md']
    count_letter = 0
    while views > 1:
        views = views / 1000
        count_letter += 1
    return [tab_letter[count_letter - 1], views]

def allYtInfo(yt):
    to_json = []
    for url in yt:
        the_video = YouTube(url)
        views = the_video.views
        to_json.append({'title': the_video.title, 'author': the_video.author, 'url_channel': the_video.channel_url, 'views': round(viewser(views)[1] * 1000, 1), 'number_views': viewser(views)[0], 'duration': round(the_video.length / 60, 2), 'publish_date': f'{the_video.publish_date}', 'age_restricted': the_video.age_restricted})
        print(f'\n\033[1;32mTitle : \033[1;35m{the_video.title}\n\033[1;32mAuthor : \033[1;35m{the_video.author}\n\033[1;32mChannel URL : \033[1;35m{the_video.channel_url}\n\033[1;32mViews : \033[1;35m{round(viewser(views)[1] * 1000, 1)}{viewser(views)[0]}\n\033[1;32mDuration : \033[1;35m{round(the_video.length / 60, 2)}min\n\033[1;32mPublish date : \033[1;35m{the_video.publish_date}\n\033[1;32mAge restricted : \033[1;35m{the_video.age_restricted}\033[0m\n')
    return to_json
i = int(input('\033[1;33mHow many videos have you ? '))
z = 0
videos = []
while z < i:
    videos.append(input(f'\033[1;36mURL video n°{z + 1} : '))
    z += 1
compacting = input('\033[1;33mCompact in json file ? [y/n]')
if compacting == 'y':
    create_file = input('\033[1;33mFile path : ')
    file = open(create_file, "w")
    file.write(json.dumps(allYtInfo(videos)))
    file.close()
else:
    allYtInfo(videos)