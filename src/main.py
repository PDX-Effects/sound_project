from i_o import IO
from effects import Effects
from frame import Frame
from time import sleep
import matplotlib.pyplot as plt

audio = IO()
eff = Effects()
info = Frame()
info.filename = "gc.wav"
info = audio.read_audio(info)

def view_wave(info):
    plt.ylabel("Amplitude (Float32)")
    plt.plot(info.samples)
    plt.xlabel("Time (Rate * Duration)")
    plt.title(info.filename)
    plt.show()

def main_menu(info, width=50):
    ctrl = True
    while ctrl:
        print(width * "-", "80S EFFECTS MENU", width * "-")
        print(width * " ", "Filename: " + info.filename)
        print("1.  File Menu. ")
        print("2.  Modulation Effects Menu. ")
        print("3.  Time-Based Effects Menu. ")
        print("4.  Spectral Effects Menu. ")
        print("5.  Dynamic Effects Menu. ")
        print("6.  Filters Menu. ")
        print("0.  Quit Program. ")
        print((width * 2 + 18) * "-")
        print()
        try:
            choice = int(input("Enter Choice: "))
        except ValueError:
            print("Error: Incorrect Value!")
            choice = -1
        if choice == 1:
            info = file_menu(info, width)
        elif choice == 2:
            info = mod_menu(info, width)
        elif choice == 3:
            info = time_menu(info, width)
        elif choice == 4:
            info = spec_menu(info, width)
        elif choice == 5:
            info = dynamic_menu(info, width)
        elif choice == 6:
            info = filter_menu(info, width)
        elif choice == 0:
            print("Exiting Program! ")
            ctrl = False
        else:
            print("Error: Value Out of Bounds! ")
        sleep(3)
    return info


def file_menu(info, width):
    print(width * "-", "80S File MENU", (width + 3) * "-")
    print(width * " ", "Filename: " + info.filename)
    print("1.  Load A File. ")
    print("2.  Create A File. ")
    print("3.  Play A File. ")
    print("4.  View A File. ")
    print("5.  Save A File. ")
    print((width * 2 + 18) * "-")
    print()
    try:
        choice = int(input("Enter Choice: "))
    except ValueError:
        print("Error: Incorrect Value!")
        choice = -1

    if choice == 1:
        info.filename = input("Enter File Name: ")
        if info.filename != '':
            info = audio.read_audio(info)
            if info.samples is None:
                info.filename = ''
                print("Error: File Not Present! ")
        else:
            print("Error: Filename not entered! ")
    elif choice == 2:
        info.filename = input("Enter File Name: ")
        print("https://www.inspiredacoustics.com/en/MIDI_note_numbers_and_center_frequencies")
        song = input("Enter Song Line as Notes: ")
        time = 1.0
        if info.filename != '':
            info = audio.song_gen(info, song, time)
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
            print("Audio Written to new_" + info.filename + "! ")
            audio.write_audio(info)
    return info


def mod_menu(info, width):
    print(width * "-", "80S MODULATION MENU", (width - 3) * "-")
    print(width * " ", "Filename: " + info.filename)
    print("1.  Apply Chorus Effect. ")
    print("2.  Apply Tremolo Effect. ")
    print("3.  Apply Flanger Effect. ")
    print("4.  Apply Phaser Effect. ")
    print((width * 2 + 18) * "-")
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
            delay = int(input("Enter Delay in Milliseconds: "))
            if delay > 0:
                print("Applying: Chorus Effect! ")
                eff.chorus(info, delay)
            else:
                print("Error: Improper Delay Value! ")
    elif choice == 2:
        if info.samples is None:
            print("Error: Samples Not Present! ")
        else:
            print("Applying: Tremolo Effect! ")
            eff.tremolo(info)
    elif choice == 3:
        if info.samples is None:
            print("Error: Samples Not Present! ")
        else:
            print("Applying: Flang Effect! ")
            eff.flang(info)
    elif choice == 4:
        if info.samples is None:
            print("Error: Samples Not Present! ")
        else:
            print("Applying: Phaser Effect! ")
            eff.phaser(info)
    return info


def time_menu(info, width):
    print(width * "-", "80S TIME-BASED MENU", (width - 3) * "-")
    print(width * " ", "Filename: " + info.filename)
    print("1.  Planned: Apply Reverb Effect. ")
    print("2.  Apply Delay Effect. ")
    print("3.  Planned: Apply Echo Effect. ")
    print((width * 2 + 18) * "-")
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
            print("Planned: Reverb Effect! ")
    elif choice == 2:
        if info.samples is None:
            print("Error: Samples Not Present! ")
        else:
            delay = int(input("Enter Delay in Milliseconds: "))
            if delay > 0:
                print("Applying: Delay Effect! ")
                eff.delay(info, delay)
            else:
                print("Error: Improper Delay Value! ")
    elif choice == 3:
        if info.samples is None:
            print("Error: Samples Not Present! ")
        else:
            print("Planned: Echo Effect! ")
    return info


def spec_menu(info, width):
    print(width * "-", "80S SPECTRAL MENU", (width - 1) * "-")
    print(width * " ", "Filename: " + info.filename)
    print("1.  Planned: Apply EQ Effect. ")
    print("2.  Planned: Apply Panning Effect. ")
    print((width * 2 + 18) * "-")
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
            print("Planned: EQ Effect! ")
    elif choice == 2:
        if info.samples is None:
            print("Error: Samples Not Present! ")
        else:
            print("Planned: Panning Effect! ")
    return info


def dynamic_menu(info, width):
    print(width * "-", "80S DYNAMIC MENU", width * "-")
    print(width * " ", "Filename: " + info.filename)
    print("1.  Planned: Apply Compression Effect. ")
    print("2.  Planned: Apply Distortion Effect. ")
    print("3.  Apply Clipping Effect. ")
    print("4.  Apply Gain Effect. ")
    print((width * 2 + 18) * "-")
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
            print("Planned: Compression Effect! ")
    elif choice == 2:
        if info.samples is None:
            print("Error: Samples Not Present! ")
        else:
            print("Planned: Distortion Effect! ")
    elif choice == 3:
        if info.samples is None:
            print("Error: Samples Not Present! ")
        else:
            percent = float(input("Enter % to Clip in Range of 0.1 and 1.00: "))
            if 0.10 <= percent <= 1.00:
                print("Applying: Clipping Effect! ")
                eff.clipping(info, percent)
            else:
                print("Error: Improper Delay Value! ")
    elif choice == 4:
        if info.samples is None:
            print("Error: Samples Not Present! ")
        else:
            gain = float(input("Enter % to Gain in Range of 1.00+: "))
            if 1.00 <= gain:
                print("Applying: Gain Effect! ")
                eff.boost(info, gain)
            else:
                print("Error: Improper Gain Value! ")
    return info


def filter_menu(info, width):
    print(width * "-", "80S FILTERS MENU", width * "-")
    print(width * " ", "Filename: " + info.filename)
    print((width * 2 + 18) * "-")
    print()
    try:
        choice = int(input("Enter Choice: "))
    except ValueError:
        print("Error: Incorrect Value!")
        choice = -1
    return info


if __name__ == "__main__":
    main_menu(info)
