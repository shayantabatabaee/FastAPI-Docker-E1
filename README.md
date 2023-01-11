[![Python](https://img.shields.io/badge/python-3.7-green)](https://www.python.org/downloads/release/python-370/)
<h1>FastAPI Docker Exercise 1</h1>
<h2> Build using docker</h2>
	<ul>
		<li>
			To build docker image use the following command:
			<pre><code>docker build -t myimage .</code></pre>
		</li>
        <li>
			To create container and run:
			<pre><code>docker run -d --name mycontainer -p 8080:8080 myimage</code></pre>
		</li>
        or using docker compose:
        <pre><code>docker compose up</code></pre>
	</ul>

<h2> Installation </h2>
<ul>
	<li> Install requirements: 
		<ol type="a">
			<li> Install <b> "python3.7" </b> </li>
			<li>  Install <b> "virtualenv" </b>
        			<pre><code>pip install virtualenv</code></pre> 
			</li>
			<li>
        			Create the virtual environment using following command:
        			<pre><code>virtualenv .env</code></pre>
    			</li>
			<li> Active virtualenv:
				<ul>
					<li> For linux: 
       						<pre><code>source .env/bin/activate</code></pre>
					</li>
					<li> For windows:
       						<pre><code>.\.env\Scripts\activate</code></pre>
					</li>					
				</ul>	
    			</li>
			<li> Now you can install libraries and dependencies listed in requirements file:
        			<ul>
                        <pre><code>pip install -r requirements.txt</code></pre>
                    </ul>
            </li>
            <li>
                You can exit from virtual environment using following command:
                <pre><code>deactivate</code></pre>
            </li>
		</ol>
	</li>

</ul>

<h2> Running the app </h2>
	<ul>
		<li>Set environment variable:
			<ul>
			    <pre><code>DEFAULT_PORT=5000</code></pre>
                * if DEFAULT_PORT is not set, it will be 8080
                <li> For development: 
                        <pre><code>FAST_API_ENV=development</code></pre>
                </li>
                <li> For production:
                       <pre><code>FAST_API_ENV=production</code></pre>
                </li>					
            </ul>
		</li>
		<li>Run the app:
		    <ul>
                <pre><code>python asgi.py</code></pre>					
            </ul>
		</li>
	</ul>
<h2> Documentation</h2>
You can see APIDoc after that server is started using following link:
<pre><code>http://localhost:8080/redoc</code></pre>