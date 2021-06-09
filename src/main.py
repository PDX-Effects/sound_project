# Python Imports
import matplotlib.pyplot as plt
import numpy as np
import os

# Project Imports
from i_o import IO
from effects import Effects
from frame import Frame
from time import sleep

g_sleep = 1
path = os.path.realpath(__file__).replace("main.py", '') + "sound_files"


def print_filename(info, width):
    file_name = " Filename: " + info.filename + " "
    half_file = int((width - len(file_name)) / 2) - 1
    print(half_file * " " + file_name + half_file * " ")


def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')


def main_menu(info, audio, eff, width):
    ctrl = True
    title = " 80S EFFECTS MENU "
    half = int((width - len(title)) / 2) - 1
    while ctrl:
        clear()
        print(half * "-" + title + half * "-")
        print_filename(info, width)
        print("1.  File Menu. ")
        print("2.  Modulation Effects Menu. ")
        print("3.  Time-Based Effects Menu. ")
        print("4.  Spectral Effects Menu. ")
        print("5.  Dynamic Effects Menu. ")
        print("6.  Filters Menu. ")
        print("0.  Quit Program. ")
        print((width - 2) * "-")
        print()
        try:
            choice = int(input("Enter Choice: "))
        except ValueError:
            print("Error: Incorrect Value!")
            choice = -1
        if choice == 1:
            info = file_menu(info, audio, width)
        elif choice == 2:
            info = mod_menu(info, eff, width)
        elif choice == 3:
            info = time_menu(info, eff, width)
        elif choice == 4:
            info = spec_menu(info, eff, width)
        elif choice == 5:
            info = dynamic_menu(info, eff, width)
        elif choice == 6:
            info = filter_menu(info, eff, width)
        elif choice == 0:
            print("Exiting Program! ")
            ctrl = False
        else:
            print("Error: Value Out of Bounds! ")
        sleep(g_sleep)
    return info


def view_wave(info):
    times = np.arange(len(info.samples)) / info.framerate
    plt.axis([None, None, -1.0, 1.0])
    plt.ylabel("Amplitude (Float32)")
    plt.plot(times, info.samples)
    plt.xlabel("Time (s)")
    plt.title(info.filename)
    plt.show()


def file_menu(info, audio, width):
    clear()
    sounds = list()
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".wav"):
                sounds.append(file.replace('.wav', ''))

    title = " 80S FILE MENU "
    half = int((width - len(title)) / 2) - 1
    print(half * "-" + title + (half + 1) * "-")
    print_filename(info, width)

    print("1.  Load A File. ")
    print("2.  Create A File. ")
    print("3.  Play A File. ")
    print("4.  View A File. ")
    print("5.  Save A File. ")
    print("6.  Append A File. ")
    print((width - 2) * "-")
    print()
    try:
        choice = int(input("Enter Choice: "))
    except ValueError:
        print("Error: Incorrect Value!")
        choice = -1

    if choice == 1:
        print("\nList of Files in Sound Directory: ")
        for s in sounds:
            print(s)
        print()
        info.filename = input("Enter File Name: ")
        if info.filename != '':
            info = audio.read_audio(info, path)
            if info.samples is None:
                print("Error: File Not Present! ")
        else:
            print("Error: Filename not entered! ")
    elif choice == 2:
        info.filename = input("Enter File Name: ")
        print("https://www.inspiredacoustics.com/en/MIDI_note_numbers_and_center_frequencies")
        song = input("Enter Song Line as Notes: ")
        time = input("Enter duration in seconds (e.g. 5.0): ")
        if info.filename != '':
            info = audio.song_gen(info, song, float(time))
        else:
            print("Error: Filename not entered! ")
    elif choice == 3:
        if info.samples is None:
            print("Error: File Not Present! ")
        else:
            print("Playing " + info.filename + '! ')
            audio.play_audio(info)
    elif choice == 4:
        if info.samples is None:
            print("Error: File Not Present! ")
        else:
            print("Viewing " + info.filename + '! ')
            view_wave(info)
    elif choice == 5:
        if info.filename == '':
            print("Error: File Not Present! ")
        elif info.samples is None:
            print("Error: Samples Not Present! ")
        else:
            filename = input("Enter Name for File: ")
            print(filename == info.filename)
            over = True
            if info.filename == filename:
                dec = input("Overwrite Original File? (Y or N):")
                if dec == 'N':
                    over = False
            if over:
                info.filename = filename
                print("Audio Written to " + info.filename + "! ")
                audio.write_audio(info, path)
    elif choice == 6:
        if info.filename == '':
            print("Error: File Not Present! ")
        elif info.samples is None:
            print("Error: Samples Not Present! ")
        else:
            times = input("Enter How Many Times to Append: ")
            info = audio.audio_append(info, info.samples, int(times))
    return info


def mod_menu(info, eff, width):
    clear()
    title = " 80S MODULATION MENU "
    half = int((width - len(title)) / 2) - 1
    print(half * "-" + title + (half + 1) * "-")
    print_filename(info, width)
    print("1.  Apply Chorus Effect. ")
    print("2.  Apply Tremolo Effect. ")
    print("3.  Apply Flanger Effect. ")
    print("4.  Apply Phaser Effect. ")
    print((width - 2) * "-")
    print()
    try:
        choice = int(input("Enter Choice: "))
    except ValueError:
        print("Error: Incorrect Value!")
        choice = -1
    if choice == 1:
        if info.samples is None:
            print("Error: Samples Not Present! ")
        else:
            dec = input("Load Defaults? (Y or N): ")
            if dec == 'Y':
                info = eff.chorus(info)
                print("Applying: Chorus Effect! ")
            elif dec == 'N':
                freq = int(input("Enter Frequency (Hz): "))
                dry = float(input("Enter Dry Value: "))
                wet = float(input("Enter Wet Value: "))
                delay = float(input("Enter Delay Value: "))
                depth = float(input("Enter Depth Value: "))
                phase = float(input("Enter Phase Value: "))
                info = eff.chorus(info, freq, dry, wet, delay, depth, phase)
                print("Applying: Chorus Effect! ")
    elif choice == 2:
        if info.samples is None:
            print("Error: Samples Not Present! ")
        else:
            dec = input("Load Defaults? (Y or N): ")
            if dec == 'Y':
                info = eff.tremolo(info)
                print("Applying: Tremolo Effect! ")
            elif dec == 'N':
                freq = int(input("Enter Frequency (Hz): "))
                dry = float(input("Enter Dry Value: "))
                wet = float(input("Enter Wet Value: "))
                info = eff.tremolo(info, freq, dry, wet)
                print("Applying: Tremolo Effect! ")
    elif choice == 3:
        if info.samples is None:
            print("Error: Samples Not Present! ")
        else:
            dec = input("Load Defaults? (Y or N): ")
            if dec == 'Y':
                info = eff.flang(info)
                print("Applying: Flanger Effect! ")
            elif dec == 'N':
                freq = int(input("Enter Frequency (Hz): "))
                dry = float(input("Enter Dry Value: "))
                wet = float(input("Enter Wet Value: "))
                delay = float(input("Enter Delay Value: "))
                depth = float(input("Enter Depth Value: "))
                phase = float(input("Enter Phase Value: "))
                info = eff.flang(info, freq, dry, wet, delay, depth, phase)
                print("Applying: Flanger Effect! ")
    elif choice == 4:
        if info.samples is None:
            print("Error: Samples Not Present! ")
        else:
            dec = input("Load Defaults? (Y or N): ")
            if dec == 'Y':
                info = eff.phaser(info)
                print("Applying: Phaser Effect! ")
            elif dec == 'N':
                info = eff.phaser(info)
                print("Applying: Flanger Effect! ")
    return info


def time_menu(info, eff, width):
    clear()
    title = " 80S TIME-BASED MENU "
    half = int((width - len(title)) / 2) - 1
    print(half * "-" + title + (half + 1) * "-")
    print_filename(info, width)
    print("1.  Dropped: Apply Reverb Effect. ")
    print("2.  Apply Echo/Delay Effect. ")
    print((width - 2) * "-")
    print()
    try:
        choice = int(input("Enter Choice: "))
    except ValueError:
        print("Error: Incorrect Value!")
        choice = -1
    if choice == 1:
        if info.samples is None:
            print("Error: Samples Not Present! ")
        else:
            print("Dropped: Reverb Effect! ")
    if choice == 2:
        if info.samples is None:
            print("Error: Samples Not Present! ")
        else:
            dec = input("Load Defaults? (Y or N): ")
            if dec == 'Y':
                info = eff.delay(info)
                print("Applying: Echo/Delay Effect! ")
            elif dec == 'N':
                delay = int(input("Enter Delay in Milliseconds: "))
                if delay > 0:
                    info = eff.delay(info, delay)
                    print("Applying: Echo/Delay Effect! ")
                else:
                    print("Error: Improper Delay Value! ")
    return info


def spec_menu(info, eff, width):
    clear()
    title = " 80S SPECTRAL MENU "
    half = int((width - len(title)) / 2) - 1
    print(half * "-" + title + (half + 1) * "-")
    print_filename(info, width)
    print("1.  Dropped: Apply EQ Effect. ")
    print("2.  Dropped: Apply Panning Effect. ")
    print((width - 2) * "-")
    print()
    try:
        choice = int(input("Enter Choice: "))
    except ValueError:
        print("Error: Incorrect Value!")
        choice = -1
    if choice == 1:
        if info.samples is None:
            print("Error: Samples Not Present! ")
        else:
            print("Dropped: EQ Effect! ")
    elif choice == 2:
        if info.samples is None:
            print("Error: Samples Not Present! ")
        else:
            print("Dropped: Panning Effect! ")
    return info


def dynamic_menu(info, eff, width):
    clear()
    title = " 80S DYNAMIC MENU "
    half = int((width - len(title)) / 2) - 1
    print(half * "-" + title + half * "-")
    print_filename(info, width)
    print("1.  Dropped: Apply Compression Effect. ")
    print("2.  Dropped: Apply Distortion Effect. ")
    print("3.  Apply Clipping Effect. ")
    print("4.  Apply Gain Effect. ")
    print("5.  Apply Loss Effect. ")
    print((width - 2) * "-")
    print()
    try:
        choice = int(input("Enter Choice: "))
    except ValueError:
        print("Error: Incorrect Value!")
        choice = -1
    if choice == 1:
        if info.samples is None:
            print("Error: Samples Not Present! ")
        else:
            print("Dropped: Compression Effect! ")
    elif choice == 2:
        if info.samples is None:
            print("Error: Samples Not Present! ")
        else:
            print("Dropped: Distortion Effect! ")
    elif choice == 3:
        if info.samples is None:
            print("Error: Samples Not Present! ")
        else:
            percent = float(input("Enter % to Clip in Range of 0.1 and 1.00: "))
            if 0.10 <= percent <= 1.00:
                print("Applying: Clipping Effect! ")
                info = eff.clipping(info, percent)
            else:
                print("Error: Improper Delay Value! ")
    elif choice == 4:
        if info.samples is None:
            print("Error: Samples Not Present! ")
        else:
            gain = float(input("Enter % to Gain in Range of 1.00+: "))
            if 1.00 <= gain:
                print("Applying: Gain Effect! ")
                info = eff.change_amp_rate(info, gain)
            else:
                print("Error: Improper Gain Value! ")
    elif choice == 5:
        if info.samples is None:
            print("Error: Samples Not Present! ")
        else:
            loss = float(input("Enter % to Lose in Range of 0.0 to 1.00: "))
            if 0.0 < loss <= 1.0:
                print("Applying: Gain Effect! ")
                info = eff.change_amp_rate(info, loss)
            else:
                print("Error: Improper Loss Value! ")
    return info


def filter_menu(info, eff, width):
    clear()
    title = " 80S FILTERS MENU "
    half = int((width - len(title)) / 2) - 1
    print(half * "-" + title + half * "-")
    print_filename(info, width)
    print("1.   ")
    print("2.   ")
    print("3.   ")
    print("4.   ")
    print((width - 2) * "-")
    print()
    try:
        choice = int(input("Enter Choice: "))
    except ValueError:
        print("Error: Incorrect Value!")
        choice = -1
    return info


if __name__ == "__main__":
    try:
        t_size = os.get_terminal_size()
    except OSError:
        t_size = [50, 50]
    except ValueError:
        t_size = [50, 50]
    # Initialize Objects
    info_master = Frame()
    audio_master = IO()
    eff_master = Effects()

    # Place Code Here to Specifically Test Effect


    # End Of Testing Area
    main_menu(info_master, audio_master, eff_master, t_size[0])
