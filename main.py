import inquirer
import os
from colorama import *
from moviepy.editor import VideoFileClip, AudioFileClip, vfx, afx
import pystyle
from rich.console import Console
from rich.theme import Theme

text_theme = Theme(
    {
        'info': 'dim cyan',
        'warning': 'magenta',
        'danger': 'bold red'
    }
)

thankyou = f"""
████████╗██╗  ██╗ █████╗ ███╗   ██╗██╗  ██╗    ██╗   ██╗ ██████╗ ██╗   ██╗
╚══██╔══╝██║  ██║██╔══██╗████╗  ██║██║ ██╔╝    ╚██╗ ██╔╝██╔═══██╗██║   ██║
   ██║   ███████║███████║██╔██╗ ██║█████╔╝      ╚████╔╝ ██║   ██║██║   ██║
   ██║   ██╔══██║██╔══██║██║╚██╗██║██╔═██╗       ╚██╔╝  ██║   ██║██║   ██║
   ██║   ██║  ██║██║  ██║██║ ╚████║██║  ██╗       ██║   ╚██████╔╝╚██████╔╝
   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝       ╚═╝    ╚═════╝  ╚═════╝ 
"""

console = Console(highlight=False)

################################# MAIN MENU ###################################
def edit_tool():
    while True:
        os.system('cls')
        os.system('clear')
        banner = f"""
        ███████╗██████╗ ██╗████████╗  ██╗   ██╗██╗██████╗ ███████╗ █████╗ 
        ██╔════╝██╔══██╗██║╚══██╔══╝  ██║   ██║██║██╔══██╗██╔════╝██╔══██╗
        █████╗  ██║  ██║██║   ██║     ╚██╗ ██╔╝██║██║  ██║█████╗  ██║  ██║
        ██╔══╝  ██║  ██║██║   ██║      ╚████╔╝ ██║██║  ██║██╔══╝  ██║  ██║
        ███████╗██████╔╝██║   ██║       ╚██╔╝  ██║██████╔╝███████╗╚█████╔╝
        ╚══════╝╚═════╝ ╚═╝   ╚═╝        ╚═╝   ╚═╝╚═════╝ ╚══════╝ ╚════╝ 
        """
        console.print(pystyle.Center.XCenter(banner), style='cyan')
        console.print(pystyle.Box.DoubleCube('Use arrow key to select the options'), style='bold green')
        questions = [
        inquirer.List('tool',
                        message="What size do you need?",
                        choices=['Mirror', 'Speed', 'Add music', 'Quit'],
                    ),
        ]
        answers = inquirer.prompt(questions)

        if answers['tool'] == 'Mirror':
            mirror()
            break
        elif answers['tool'] == 'Speed':
            speed()
            break
        elif answers['tool'] == 'Add music':
            addmusic()
            break
        else:
            os.system('cls')
            os.system('clear')
            console.print(pystyle.Center.XCenter(thankyou), style='cyan')
            break

################################# GET FILE PATH ###################################
def get_file_path_in(text):
    file_name = input(text)
    current_dir = os.path.abspath(os.getcwd())
    if os.path.isabs(file_name):
        return file_name
    else:
        if os.path.exists(os.path.join(current_dir, file_name)):
            return file_name
        else:
            return "File not found in the current directory. Please enter an absolute path."
        

def get_file_path_out(text):
    file_name = input(text)
    current_dir = os.path.abspath(os.getcwd())
    if os.path.isabs(file_name):
        return file_name
    else:
        return os.path.join(current_dir, file_name)
################################# MIRROR VIDEO ####################################
def mirror():
    def flip(input, output):
        #print(path_name_list)
        clip = VideoFileClip(input)
        #audio = AudioFileClip(input)
        clip = clip.fx(vfx.mirror_x)
        name = clip.filename
        clip.write_videofile(output, verbose=False, codec='libx264', audio_codec="aac") #, logger=None
        clip.close()

    while True:
        os.system('cls')
        os.system('clear')

        banner = f"""
        ███╗   ███╗██╗██████╗ ██████╗  ██████╗ ██████╗ 
        ████╗ ████║██║██╔══██╗██╔══██╗██╔═══██╗██╔══██╗
        ██╔████╔██║██║██████╔╝██████╔╝██║   ██║██████╔╝
        ██║╚██╔╝██║██║██╔══██╗██╔══██╗██║   ██║██╔══██╗
        ██║ ╚═╝ ██║██║██║  ██║██║  ██║╚██████╔╝██║  ██║
        ╚═╝     ╚═╝╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝
        """
        console.print(pystyle.Center.XCenter(banner), style='cyan')
        console.print(pystyle.Box.DoubleCube('Example: C:/Users/Name/Desktop/Folder/Video/test.mp4 if video file not in current directory \nor     : test.mp4 if video is in current directory'), style='bold green')
        video_path = get_file_path_in(f'{Fore.YELLOW}Please enter video path: {Fore.WHITE}')
        out_path = get_file_path_out(f'{Fore.YELLOW}Please enter where to save: {Fore.WHITE}')
        flip(video_path, out_path)
        break

    os.system('cls')
    os.system('clear')
    console.print(pystyle.Center.XCenter(banner), style='cyan')
    questions = [
    inquirer.List('choice',
                    message="Do you want to mirror another video?",
                    choices=['Yes', 'Go to Main Menu', 'Quit'],
                ),
    ]
    answers = inquirer.prompt(questions)

    if answers['choice'] == 'Go to Main Menu':
        edit_tool()
    elif answers['choice'] == 'Yes':
        mirror()
    else:
        os.system('cls')
        os.system('clear')
        console.print(pystyle.Center.XCenter(thankyou), style='cyan')

################################# SPEED VIDEO ####################################
def speed():
    def speed_video(input, output, speed_factor):
        # Load video
        clip = VideoFileClip(input)
        # Speed up video
        clip = clip.fx(vfx.speedx, speed_factor)
        # Write it to a file
        clip.write_videofile(output, verbose=False, codec='libx264', audio_codec="aac")
        clip.close()

    while True:
        os.system('cls')
        os.system('clear')

        banner = f"""
        ███████╗██████╗ ███████╗███████╗██████╗ 
        ██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗
        ███████╗██████╔╝█████╗  █████╗  ██║  ██║
        ╚════██║██╔═══╝ ██╔══╝  ██╔══╝  ██║  ██║
        ███████║██║     ███████╗███████╗██████╔╝
        ╚══════╝╚═╝     ╚══════╝╚══════╝╚═════╝ 
        """
        console.print(pystyle.Center.XCenter(banner), style='cyan')
        console.print(pystyle.Box.DoubleCube('Example: C:/Users/Name/Desktop/Folder/Video/test.mp4 if video file not in current directory \nor     : test.mp4 if video is in current directory'), style='bold green')
        video_path = get_file_path_in(f'{Fore.YELLOW}Please enter video path: {Fore.WHITE}')
        out_path = get_file_path_out(f'{Fore.YELLOW}Please enter where to save: {Fore.WHITE}')
        speed_factor = float(input(f'{Fore.YELLOW}Please enter speed factor: {Fore.WHITE}'))
        speed_video(video_path, out_path, speed_factor)
        break

    os.system('cls')
    os.system('clear')
    console.print(pystyle.Center.XCenter(banner), style='cyan')
    questions = [
    inquirer.List('choice',
                    message="Do you want to do it again?",
                    choices=['Yes', 'Go to Main Menu', 'Quit'],
                ),
    ]
    answers = inquirer.prompt(questions)

    if answers['choice'] == 'Go to Main Menu':
        edit_tool()
    elif answers['choice'] == 'Yes':
        speed()
    else:
        os.system('cls')
        os.system('clear')
        console.print(pystyle.Center.XCenter(thankyou), style='cyan')

################################# ADD MUSIC ####################################
def addmusic():
    # add background music
    def addbackgroundmusic(input, music, output):
        videoclip = VideoFileClip(input)
        clip_duration = videoclip.duration
        audioclip = AudioFileClip(music)#.set_duration(clip_duration)
        # new_audioclip = CompositeAudioClip([audioclip])
        new_audioclip = afx.audio_loop(audioclip, duration=clip_duration)
        clip = videoclip.set_audio(new_audioclip)
        clip.write_videofile(output, verbose=False, codec='libx264', audio_codec="aac")
        clip.close()

    while True:
        os.system('cls')
        os.system('clear')

        banner = f"""
         █████╗ ██████╗ ██████╗     ███╗   ███╗██╗   ██╗███████╗██╗ ██████╗
        ██╔══██╗██╔══██╗██╔══██╗    ████╗ ████║██║   ██║██╔════╝██║██╔════╝
        ███████║██║  ██║██║  ██║    ██╔████╔██║██║   ██║███████╗██║██║     
        ██╔══██║██║  ██║██║  ██║    ██║╚██╔╝██║██║   ██║╚════██║██║██║     
        ██║  ██║██████╔╝██████╔╝    ██║ ╚═╝ ██║╚██████╔╝███████║██║╚██████╗
        ╚═╝  ╚═╝╚═════╝ ╚═════╝     ╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝ ╚═════╝ 
        """
        console.print(pystyle.Center.XCenter(banner), style='cyan')
        console.print(pystyle.Box.DoubleCube('Example: C:/Users/Name/Desktop/Folder/Video/test.mp4 if video file not in current directory \nor     : test.mp4 if video is in current directory'), style='bold green')
        video_path = get_file_path_in(f'{Fore.YELLOW}Please enter video path: {Fore.WHITE}')
        audio_path = get_file_path_in(f'{Fore.YELLOW}Please enter music path: {Fore.WHITE}')
        out_path = get_file_path_out(f'{Fore.YELLOW}Please enter where to save: {Fore.WHITE}')
        addbackgroundmusic(video_path, audio_path, out_path)
        break

    os.system('cls')
    os.system('clear')
    console.print(pystyle.Center.XCenter(banner), style='cyan')
    questions = [
    inquirer.List('choice',
                    message="Do you want to do it again?",
                    choices=['Yes', 'Go to Main Menu', 'Quit'],
                ),
    ]
    answers = inquirer.prompt(questions)

    if answers['choice'] == 'Go to Main Menu':
        edit_tool()
    elif answers['choice'] == 'Yes':
        addmusic()
    else:
        os.system('cls')
        os.system('clear')
        console.print(pystyle.Center.XCenter(thankyou), style='cyan')

if __name__ == '__main__':
    edit_tool()