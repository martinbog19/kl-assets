import os
import random

NBA_FACES_DIR = 'graphics/faces/nba'
N_FACES = 10

# Convert to markdown image links
def to_markdown_img(path, size=60):
    rel_path = path.replace('\\', '/').replace(os.path.sep, '/')
    return f'<img src="{rel_path}" height="{size}" />'

face_paths = []
team_dirs = sorted(os.listdir(NBA_FACES_DIR))
for team in team_dirs:
    team_dir = os.path.join(NBA_FACES_DIR, team)
    if os.path.isdir(team_dir):
        team_faces = [f for f in os.listdir(team_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp', '.gif'))]
        random_face = random.sample(team_faces, 1)
        face_paths.append(os.path.join(team_dir, random_face[0]))

# Insert faces at the top, after a marker or at the top
marker = '<!-- NBA FACES START -->'
end_marker = '<!-- NBA FACES END -->'
faces_md = ' '.join([to_markdown_img(f) for f in face_paths])
faces_block = f'{marker}\n{faces_md}\n{end_marker}'
new_content = faces_block

with open("README.md", 'w', encoding='utf-8') as f:
    f.write(new_content)
