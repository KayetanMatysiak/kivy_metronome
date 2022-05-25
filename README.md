# Kivy Metronome
A simple metronome created with Python and Kivy.<br>
It has tempos ranging from 130 up to 240 (with an increment of 5).<br>

Due to the limitations of Kivy's clock function, I decided to generate rhythm tracks for each tempo. <br>Otherwise, using *Clock.schedule_interval* (or *clock.sleep*), we won't be able to achieve ideal tempo track.<br>

![image](images/screenshot.png)
