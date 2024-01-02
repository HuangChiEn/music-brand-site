# Music Blog Site
Welcome to Music Blog Site! This repository provide a simple music blog backended by django framework.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)


## Features
The key feature of music blog are as follows:
- Contains multi-media (video, podcast) on the main page.
- Blog contains Image gallery, pop-up video, quick menu navigation.
- The admin interface allow the user add the new video, podcast.
- Structured template easily reflect update of video and podcast.


## Installation
```bash
# Clone the repository
git clone https://github.com/yourusername/your-music-blog.git

# Change directory
cd personal_homepage

# Install dependencies
pip install -r requirement.txt
```

## Usage 
### Run the server with debug mode
user@:/personal_homepage/$ python manage.py runserver $PORT
> we'll omit the path in the later examples

### Further deploy the server by ngrok
1. Open `personal_homepage/settings` and turn `DEBUG` flag to False.

2. Copy the staticfile to the `STATIC_ROOT`
`python manage.py collections`

3. Run the server with whitenoise middleware (for easily deployment)
> if you have setup apache/nginx, it would be better to server the service via staticfile cache, ..., etc.
`python manage.py runserver $PORT`

4. Forward your local service online via ngrok
> Suppose you have ngrok account and the secret key yaml file properly setup in local. 
`ngrok https $PORT`

## License
please check the LICENSE under this project.