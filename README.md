# 80s Effect App Sound Project 
Team: 80's Effect App \
Members: Kelsey Larson, kelsey36@pdx.edu; Adam La Fleur, alafleur@pdx.edu; Maeve Hoffer,  dhoffer@pdx.edu

**Contributions** \
==Effects== \
delay - Kelsey \
chorus - Kelsey / Adam \
flang - Adam \
phaser - Maeve \
clipping - Adam \
tremolo - Adam 

==Effects== \
Main/Key_Dict/(Read/Write/Play) - Group \
Song_Gen - Maeve \
Chord_Gen - Maeve 

**what is this project** \
This project serves as a sound editing application, demonstrating an array of effects on the chosen File. This file can be user uploaded or the provided wav files in the repo. Once a file is loaded, the user can apply effects as desired and play the resulting audio.

**How to build and run the project**\
The process to install the requirements is:

pip install -r requirements.txt

The project is intended to run an interface similar to a normal sound editor. A user can load a file provided in the repo, choose effects to apply, and then play back that same file. On the command line:
py .\src\main.py. The user can also a wav file preferably mono to the sound_files folder in src.

From the main menu, first choose a sound file to manipulate (1.File Menu). Once chosen, you are redirected back to the main menu where you can choose a specific effects menu. Finally, head back to the file menu to play the file with the selected effects.

**Testing:** 
\
A component of testing was using Audacity to confirm the waveforms reflect the effects intention and not just make a different noise. Audacity also helped when there was no audible output or confusing output, and you could rely on the visual waveforms to seek out the issue. From the users side, testing was done on the interface itself. Things such as invalid input and path choices were tested and error messages were added to guide users to the correct implementation of the project.  
 
**What worked?**\
An object oriented architecture with isolated effect applications was the most straightforward design. It was also important for us to decide on which data format to use during IO. At its most raw form, bytes-like objects are used to represent wav files. However, there are more available methods through scipy.io if you work with 16 bit integer arrays.

**What didn't work for us/ issues along the way:**\
It proved difficult to use different data sizes and structures for manipulation of raw audio data throughout the project. For example, translating from 32 bit floats to 16 bit integers  and vice versa was a lot more involved than expected. This is most likely due to assumptions being made about the step sizes, length, and overall sizing being unaffected by these changes. It was easier to keep the same format throughout the entire project, even within private functions where data could be reformatted, modified, and formatted back to its original structure. 

It was difficult to find resources on creating effects and not having to rely solely on examples or other people's code. Although we can cite other people's work and ideas, it is necessary to have your own approach.

**future implementation:**\
This project had a stretch goal of creating a frontend UI . This would be fun to do once the project was properly tested and documented. We also sought out to make this app 80s themed, creating effects that reflect the distinct style of that time in synthesizer production. Creating working effects on their own took most of the project time, so fine tuning the style would also be an improvement. 
Another future improvement is having effects occur at the same time. This would be more involved as the effects/objects would need to be aware of one another while manipulating the same copy of a signal. Issues of unrecognizable or garbage output would be heightened and there would most likely need to be a modulation order.

\
The group is mostly satisfied with the result, and believe it's a good start to the introduction of the complexity of these kinds of applications. It is not perfect, but we have learned much from its implementation.
