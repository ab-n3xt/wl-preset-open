# W.L. Presets
This is the open-source repository of my mod-hosting website for the adult game [Wild Life](https://candyvalleynetwork.com/projects/wildlife-an-adult-rpg/).

It was implemented using Django, SQLite, and Bootstrap earlier in 2023.

Feel free to make pull requests to add code or ask for suggestions. Thank you all!

# Building from Source
Requires latest version of [Python](https://www.python.org/).

```bash
# Clone project
git clone https://github.com/ab-n3xt/wl-preset-open.git

# Enter into the project directory
cd wl-preset-open

# Create a Python virtual environment
python -m venv env

# Activate the environment
# As my machine is on Windows 10, I use the following command
.\env\Scripts\activate

# Install Python dependencies
python -m pip -r requirements.txt

# Go into website directory
cd website/

# Run database migrations (and take a look at all of my awful changes to the db model)
python manage.py makemigrations

# Finally, start the server
python manage.py runserver
```
