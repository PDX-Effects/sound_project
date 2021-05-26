from i_o import IO
from effects import Effects
from frame import Frame
from time import sleep


audio = IO()
eff = Effects()
info = Frame()


def menu():
    width = 50
    print(width * "-", "80S EFFECTS MENU", width * "-")
    print(width * " ", "Filename: " + info.filename)
    print("1.  Load A File. ")
    print("2.  Create A File. ")
    print("3.  Play A File. ")
    print("4.  Save A File. ")
    print("5.  Apply Chorus Effect. ")
    print("6.  Apply Flang Effect. ")
    print("7.  Apply Phaser Effect. ")
    print("8.  Apply Delay Effect. ")
    print("9.  Apply Clipping Effect. ")
    print("0.  Quit Program. ")
    print((width * 2 + 18) * "-")
    print()


if __name__ == "__main__":
    info.filename = ''
    ctrl = True
    while ctrl:
        menu()
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
            sleep(3)
        elif choice == 2:
            info.filename = input("Enter File Name: ")
            if info.filename != '':
                info = audio.note_gen(info)
            else:
                print("Error: Filename not entered! ")
            sleep(3)
        elif choice == 3:
            if info.samples is None:
                print("Error: File Not Present! ")
            else:
                print("Playing " + info.filename + '! ')
                audio.play_audio(info)
            sleep(3)
        elif choice == 4:
            if info.filename == '':
                print("Error: File Not Present! ")
            elif info.samples is None:
                print("Error: Samples Not Present! ")
            else:
                print("Audio Written to new_" + info.filename + "! ")
                audio.write_audio(info)
            sleep(3)
        elif choice == 5:
            if info.samples is None:
                print("Error: Samples Not Present! ")
            else:
                delay = int(input("Enter Delay in Milliseconds: "))
                if delay > 0:
                    print("Applying: Chorus Effect! ")
                    eff.chorus(info, delay)
                else:
                    print("Error: Improper Delay Value! ")
            sleep(3)
        elif choice == 6:
            if info.samples is None:
                print("Error: Samples Not Present! ")
            else:
                print("Applying: Flang Effect! ")
                eff.flang(info)
            sleep(3)
        elif choice == 7:
            if info.samples is None:
                print("Error: Samples Not Present! ")
            else:
                print("Applying: Phaser Effect! ")
                eff.phaser(info)
            sleep(3)
        elif choice == 8:
            if info.samples is None:
                print("Error: Samples Not Present! ")
            else:
                delay = int(input("Enter Delay in Milliseconds: "))
                if delay > 0:
                    print("Applying: Delay Effect! ")
                    eff.delay(info, delay)
                else:
                    print("Error: Improper Delay Value! ")
            sleep(3)
        elif choice == 9:
            if info.samples is None:
                print("Error: Samples Not Present! ")
            else:
                percent = float(input("Enter % to Clip in Range of 0.1 and 1.00: "))
                if 0.10 <= percent <= 1.00:
                    print("Applying: Clipping Effect! ")
                    eff.clipping(info, percent)
                else:
                    print("Error: Improper Delay Value! ")
            sleep(3)
        elif choice == 0:
            print("Exiting Program! ")
            sleep(3)
            ctrl = False
        else:
            print("Error: Value Out of Bounds! ")
            sleep(3)
