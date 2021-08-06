<!--
*** This README markdown is built from the following repo
*** https://github.com/othneildrew/Best-README-Template
-->



<!-- PROJECT SHIELDS -->
<!--
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />


  <h3 align="center">Virtual Painter</h3>

  <p align="left">
    Use your webcam to virtually paint using python and OpenCV
    
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]]

In this project we will develop virtual air painter using Python and real time webcam feed

We can divide the project into the following tasks:
* Capture frames from webcam using `OpenCV` framework
* Detect hand landmarks using google `Mediapipe` package
* `fingers_module` and `hand_tracking_module` tracks landmarks of both index and middle fingers 
* Using these landmarks, and the `OpenCv` methods the movement of your hand in the air is translated into drawings


### Built With

main frameworks and libraries used in building this project

* [OpenCV](https://opencv.org)
* [MediaPipe](https://mediapipe.dev)



<!-- GETTING STARTED -->
## Getting Started

You need to install the following dependencies in order to run the project
### Dependencies
- OpenCV
- Mediapipe


### Prerequisites

Install the following python packages to your env/vevn using the shell/bash.
* pip
  ```sh
  pip install opencv-python
  pip install mediapipe
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/SamirGouda/Virtual_Painter.git
   ```
   
2. Run the python file using from your terminal
   ```shell
   python ai_virtual_painter.py
   ```



<!-- USAGE EXAMPLES -->
## Usage

- to toggle paint mode you should have only your index finger up
- to toggle selection mode open up both you index and middle fingers
- the distance between index and middle fingers changes the brush thickness

<!-- CONTACT -->
## Contact

Samir Gouda - [https://www.linkedin.com/in/samirgouda](https://www.linkedin.com/in/samirgouda) 

email: [samiir.ahmedd@gmail.com](mailto:samiir.ahmedd@gmail.com)

Project Link: [https://github.com/SamirGouda/Virtual_Painter](https://github.com/SamirGouda/Virtual_Painter)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* [othneildrew](https://github.com/othneildrew/) for his README template
* [murtazahassan](https://github.com/murtazahassan) for his computer vision course  




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/samirgouda/
[product-screenshot]: images/1.png
