from pathlib import Path

#Variables for relative path to templates directory
BASE_DIR = Path(__file__).resolve().parent.parent 
TEMPLATES_DIR = BASE_DIR / "templates"

#Define function to read the templates
def load_template(name: str) -> str:
    path = TEMPLATES_DIR / name
    with open(path, "r", encoding="utf-8") as f:
        return f.read()
    
#Usage of the function to open the template 
template_text = load_template("template_prod_version.txt") #No need to scale it up at the moment

#Assembling email
def assemble_email(template: str, **kwargs) -> str:
    return template.format(**kwargs)

