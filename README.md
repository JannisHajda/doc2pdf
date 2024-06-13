# doc2pdf

A simple docker application to convert doc, docx, ppt and pptx files to pdf.

<img src="docker.gif" alt="kobayashi" height="130"/> <img src="kobayashi.gif" alt="kobayashi" width="200"/>

## Instructions

1. Make sure you have docker and docker-compose installed on your system
2. Place your doc/docx/ppt/pptx files inside the `./input` and create folder `./output`
3. Put fonts that used in your doc/docx/ppt/pptx into `./fonts`
4. Run `docker-compose up` and enjoy your converted files! (They are available inside the /src/output directory)
