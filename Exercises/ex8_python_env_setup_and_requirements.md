Python Env Creation:
python -m venv environment_name

Environment Activation:
Linux/Mac
source environment_name/bin/activate

Windows
cd environment_name
.\Scripts\activate

Installation requirements.txt
​​blinker==1.8.2
    # via flask
certifi==2024.6.2
    # via requests
charset-normalizer==3.3.2
    # via requests
click==8.1.7
    # via flask
flask==3.0.3
    # via -r requirements.in
idna==3.7
    # via requests
itsdangerous==2.2.0
    # via flask
jinja2==3.1.4
    # via flask
markupsafe==2.1.5
    # via
    #   jinja2
    #   werkzeug
requests==2.32.3
    # via -r requirements.in
urllib3==2.2.1
    # via requests
werkzeug==3.0.3
