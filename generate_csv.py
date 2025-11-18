import os

# Change this if you want a different folder name or root
folder_in_repo = "images"  

with open('image_urls.csv', 'w') as f:
    f.write('filename,raw_url\n')
    for filename in sorted(os.listdir(folder_in_repo)):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.png', '.gif', '.webp')):
            url = f"https://media.githubusercontent.com/media/DhruvPatel9924/img/main/{folder_in_repo}/{filename}"
            f.write(f"{filename},{url}\n")

print("CSV created successfully: image_urls.csv")
