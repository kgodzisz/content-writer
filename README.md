<p>One of my main tasks in my professional work is writing technical texts related to cybersecurity and other IT-related topics. Very often, I need to check how many words and characters with spaces are in the material I have written. In connection with my recent efforts related to the Python language, I decided to write a simple script that:<p>
<ul>
<li>counts the number of words in a file;</li>
<li>counts the number of characters with spaces in a file;</li>
<li>counts the number of characters without spaces in a file;</li>
<li>counts the number of punctuation marks in a file;</li> 
</ul>
<p>I need the first three options for most of my text. I added the last one just for fun. The script outputs these values in .docx files. As in the previous cases, I create a Docker image that I use. However, if you want, I also provide the script itself. Therefore, you can run it using Python installed on your local system. The script is located in the Github repository.</p><br />

<p><strong>To download files from Github:</strong></p>
<p><code>git clone https://github.com/kgodzisz/content-counter.git</code></p><br />

<p><strong>Create your own image in your local repository:</p>
<p><code>docker build -t content-counter .</code></p><br />

<p><strong>Run the tool:</strong></p>
<p><code>docker run --rm -v /path/to/folder:/app content-counter file-name</code></p><br />

<p><strong>The second way is to download the prepared file from the Docker Hub repository:</strong></p>
<p><code>docker run --rm -v /path/to/folder:/app kgodzisz/content-counter file-name</code></p><br />

<p><strong>Description of the options used in the commands:</strong></p>
<p><code>--rm - the container will be automatically removed after exiting; </code></p>
<p><code>-v - path to the folder where the files for which you want to count the number of lines of code are located;</code></p>
<p><code>content-counter - the name of the created Docker image that we want to use;</code></p>
<p><code>kgodzisz/content-counter - the address to the image on DockerHub platform;</code></p>
<p><code>file-name - you provide the name of the file along with its extension.</code></p><br />

<p><strong>Github</strong>: <a href="https://github.com/kgodzisz/content-counter" target="_blank">https://github.com/kgodzisz/content-counter</a>.</p>
<p><strong>Blog</strong>: <a href="https://dockeryzacjaswiata.pl" target="_blank">https://dockeryzacjaswiata.pl.</a></p>
