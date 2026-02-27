import os
import random

NBA_FACES_DIR = 'graphics/faces/nba'
N_FACES = 10

# Convert to markdown image links
def to_markdown_img(path):
    rel_path = path.replace('\\', '/').replace(os.path.sep, '/')
    return f'![]({rel_path})'

face_paths = []
for team in os.listdir(NBA_FACES_DIR):
    team_dir = os.path.join(NBA_FACES_DIR, team)
    if os.path.isdir(team_dir):
        for fname in os.listdir(team_dir):
            if fname.lower().endswith(('.png', '.jpg', '.jpeg', '.webp', '.gif')):
                face_paths.append(os.path.join(team_dir, fname))


random_faces = random.sample(face_paths, N_FACES)

# Insert faces at the top, after a marker or at the top
marker = '<!-- NBA FACES START -->'
end_marker = '<!-- NBA FACES END -->'
faces_md = '\n'.join([to_markdown_img(f) for f in random_faces])
faces_block = f'{marker}\n{faces_md}\n{end_marker}'
new_content = faces_block

with open("README.md", 'w', encoding='utf-8') as f:
    f.write(new_content)
