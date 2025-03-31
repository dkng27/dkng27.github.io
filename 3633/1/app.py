# app.py
from flask import Flask, request, render_template_string
import time

app = Flask(__name__)

FLAG = "what{R3DaCT_d}"
names = ["william", "ivan", "peter", "eason", "jacky", "marco", "hoard", "qwerty", FLAG]

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>COMP4321 enjoyer</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; }
        .container { max-width: 800px; margin: 0 auto; }
        input[type="text"] { padding: 8px; width: 300px; }
        button { padding: 8px 16px; }
        .timing { color: #888; font-size: 0.9em; }
    </style>
</head>
<body>
    <div class="container">
        <h1>List of names search</h1>
        <form action="/" method="GET">
            <label for="query">Search Query:</label>
            <input type="text" id="query" name="query" value="{{ query|default('') }}" required>
            <button type="submit">Search</button>
        </form>
        
        {% if query %}
            <h2>Search Results for "{{ query }}":</h2>
            
            {% if results %}
                <ul>
                    {% for result in results %}
                        <li>{{ result }}</li>
                    {% endfor %}
                </ul>
            {% else %}
                <p>No results found.</p>
            {% endif %}

            
            <p class="timing">Search completed in {{ time_taken }}ms</p>
        {% endif %}
    </div>
</body>
</html>
'''

@app.route('/', methods=['GET'])
def index():
    query = request.args.get('query', '')
    
    if not query:
        return render_template_string(HTML_TEMPLATE)
    
    results = []
    start_time = time.time()
    
    for item in names:
        if query.lower() in item.lower():
            results.append(item)
    
    if FLAG in results:
        # make sure the flag is not leaked, i am so smort
        for _ in range(650):
            try:
                results.remove(FLAG)
            except ValueError:
                print("Flag removed")

    elapsed = time.time() - start_time
    
    return render_template_string(
        HTML_TEMPLATE, 
        results=results, 
        query=query,
        time_taken=round(elapsed * 1000, 2)
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)