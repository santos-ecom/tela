import os
import glob

# create directory if not exists
os.makedirs('imagens', exist_ok=True)

html = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Galeria de Imagens</title>
    <style>
        body { font-family: Arial, sans-serif; background: #1a202c; color: white; padding: 20px; text-align: center; }
        .gallery { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; max-width: 1200px; margin: 0 auto; }
        .gallery-item { background: #2d3748; padding: 15px; border-radius: 8px; }
        img { max-width: 100%; border-radius: 4px; box-shadow: 0 4px 6px rgba(0,0,0,0.3); }
        h1 { margin-bottom: 40px; }
        p { font-size: 14px; margin-top: 10px; word-break: break-all; color: #a0aec0; }
        .filters { margin-bottom: 30px; }
        button { background: #4a5568; color: white; border: none; padding: 10px 15px; margin: 0 5px; border-radius: 4px; cursor: pointer; }
        button:hover { background: #2b6cb0; }
    </style>
</head>
<body>
    <h1>Galeria de Imagens (/imagens)</h1>
    <div class="filters">
        <button onclick="filter('all')">Todas</button>
        <button onclick="filter('generated')">Geradas por IA (Sem Uploads)</button>
    </div>
    <div class="gallery">
"""

files = glob.glob('imagens-geradas/*.png') + glob.glob('imagens-geradas/*.jpg')

# Sort files by modification time (newest first)
files.sort(key=os.path.getmtime, reverse=True)

for file in files:
    filename = os.path.basename(file)
    cl = 'generated' if not filename.startswith('uploaded_') and 'verification' not in filename and 'check' not in filename else 'other'
    html += f"""
        <div class="gallery-item {cl}">
            <img src="../{file}" loading="lazy">
            <p>{filename}</p>
        </div>
    """

html += """
    </div>
    <script>
        function filter(type) {
            const items = document.querySelectorAll('.gallery-item');
            items.forEach(item => {
                if (type === 'all') {
                    item.style.display = 'block';
                } else if (type === 'generated') {
                    if (item.classList.contains('generated')) {
                        item.style.display = 'block';
                    } else {
                        item.style.display = 'none';
                    }
                }
            });
        }
        // Default to generated
        filter('generated');
    </script>
</body>
</html>
"""

with open('imagens/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
