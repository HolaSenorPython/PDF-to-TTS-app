<h1>Note from ME (Elisha)</h1>
<p>Yooooo. Repo name is pretty accurate, but i feel like it wouldn't be right to leave you fighting in the mud. Soooo a GOOD ReadME is coming soon. 
I may or may not have ChatGPT help me draft up an accurate readMe, because these steps were hard for me lol. But this is another project as part of the course,
no aid from the teacher. Here is what ChatGPT has to say about HOW to use this: (btw, I double checked everything myself 🙂‍↕️)</p>


<h2>Project Description</h2>
<p>This Python script converts text from a PDF file into speech using Amazon Polly.
You provide a PDF, it extracts the text, then Polly reads it aloud and saves an mp3 audio file.</p>

<h2>Prerequisites</h2>
<ul>
  <li>Python 3.7+</li>
  <li>AWS account with access keys (AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY)</li>
  <li>Python packages (install via pip):
  <ul>
    <li>boto3</li>
    <li>PyPDF2</li>
    <li>python-dotenv</li>
  </ul>
  </li>
</ul>

<h2>Setup Instructions</h2>
<ul>
  <li>Clone/Download this repo.</li>
  <li>Create an .env file in the ROOT directory (same folder where main.py is) and add your AWS credentials and region:</li>
</ul>

<pre><code>
AWS_ACCESS_KEY_ID=your_access_key_here
AWS_SECRET_ACCESS_KEY=your_secret_key_here
AWS_DEFAULT_REGION=your_region_here
</code></pre>

<ul>
  <li>Install dependencies:</li>
</ul>

<pre><code>pip install -r requirements.txt
</code></pre>

<ul>
  <li>Run the script:</li>
</ul>

<pre><code>python main.py
</code></pre>

<h2>Usage</h2>
<p>The program should prompt you and explain more. You will need name of file (if in root) or absolute file path. Keep under 3000 characters.</p>

<h2>Limitations</h2>
<p>No GUI. All this happens in the console lol. But hey, opening windows mp3 player to listen to it is part of the experience! 😭🙏🏾</p>

<h2>License</h2>
<p>Honestly, I don't really understand this im still learning, but MIT license i guess? Anyone can use this.</p>
