# Important notes for Django Projects

1. Open terminal and create a folder to store the project (e.g. Code/SDGKU/blog)
2. Move to the respective folder (make sure you are on the right location)
3. Create a virtual environment (Windows: python -m venv venv | Mac: python3 -m venv venv)
4. Activate venv (Windows: venv\Scripts\activate | Mac: source venv/bin/activate)
5. Install django (pip install django)
6. Save packages into requirements.txt file (pip freeze > requirements.txt)
7. Create the project (django-admin startproject config .)
8. Finish the structure:
   - Create the static, templates, img, css and js folders
   - Create the .gitignore, README.md (optional) files
9. link everything to the settings.py


# Important notes for DTL - Jinja
{% %} - basic structure for all tags
{% block NAME_OF_THE_BLOCK %}{% endblock %} - portion of code
{% load static %} - load static files
{% extends 'filename' %} - Inheritance through htmls
{% include 'filename' %} - Insert html code into the desired one
{% static 'PATH_FOR_THE_FILE' %} - Load any static file (css, js, img)
{% url 'NAME_OF_THE_URL' %} - Travel through htmls