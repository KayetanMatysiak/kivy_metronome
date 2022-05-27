


# Kivy Metronome
>A simple metronome created with Python and Kivy.<br>

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Screenshots](#screenshots)
* [Project Status](#project-status)
* [Room for Improvement](#room-for-improvement)
<!-- * [License](#license) -->


## General Information
- It has tempos ranging from 130 up to 240 (with an increment of 5).<br>
- Due to the limitations of Kivy's clock function, I decided to generate rhythm tracks for each tempo. <br>Otherwise, using *Clock.schedule_interval* (or *clock.sleep*), we  won't be able to achieve ideal tempo track.<br>


## Technologies Used
- Python
- Kivy
- Pygame

## Features
- Loud and hear clicks
- Accent on the first beat
- Fast and responsive

## Screenshots
<img src="images/screenshot.png" width="400">

## Project Status
Project is: _in progress_.

## Room for Improvement
- Finding alternative to playing pre-recorded tempos and being able to generate on-the-fly

