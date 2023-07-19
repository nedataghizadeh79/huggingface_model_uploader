!pip install huggingface_hub
from huggingface_hub import notebook_login
notebook_login()


from huggingface_hub import Repository


!git config --global user.email "nedath1378@gmail.com"
!git config --global user.name "NedaTaghizadeh"



repo = Repository("wordClassification", clone_from="NedaTaghizadeh/wordClassification")

pipe.save_pretrained("wordClassification")
repo.push_to_hub()


from transformers import pipeline
classifier = pipeline("text-classification", model="NedaTaghizadeh/wordClassification")
pipeline("text-classification", model="NedaTaghizadeh/wordClassification")