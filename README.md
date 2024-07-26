<body>

<h1>DiscordTokenChecker</h1>

<p>A robust token checker that works with every Discord token and avoids rate limits. This tool verifies the validity of Discord tokens by making requests to the Discord API and identifying valid tokens.</p>

<h2>Features</h2>
<ul>
  <li><strong>Rate Limit Handling</strong>: Designed to avoid hitting Discord's rate limits.</li>
  <li><strong>Batch Processing</strong>: Efficiently checks a list of tokens.</li>
  <li><strong>Valid Token Identification</strong>: Saves valid tokens to a separate file.</li>
</ul>

<h2>Requirements</h2>
<ul>
  <li>Python 3.x</li>
  <li><code>requests</code> library</li>
</ul>

<p>You can install the required library using pip:</p>
<pre><code>pip install requests</code></pre>

<h2>Usage</h2>
<ol>
  <li><strong>Clone the repository</strong>:</li>
  <pre><code>git clone https://github.com/jordanbardella/DiscordTokenChecker.git
cd DiscordTokenChecker</code></pre>
  <li><strong>Prepare your tokens</strong>:</li>
  <p>Create a file named <code>tokens.txt</code> in the repository directory. This file should contain one token per line.</p>
  <li><strong>Run the script</strong>:</li>
  <pre><code>python checker.py</code></pre>
  <li><strong>Check the results</strong>:</li>
  <p>After the script has run, valid tokens will be saved in <code>valid_tokens.txt</code>.</p>
</ol>

<h2>Script Details</h2>
<p>The script reads tokens from <code>tokens.txt</code>, checks each token's validity by making a request to the Discord API, and then saves the valid tokens to <code>valid_tokens.txt</code>.</p>

<h3>Example <code>tokens.txt</code> format:</h3>
<pre><code>token1
token2
token3
...</code></pre>

<h2>Disclaimer</h2>
<p>This tool is intended for educational purposes only. Ensure you have permission to use and verify the tokens. Unauthorized use of tokens may violate Discord's terms of service.</p>

<h2>License</h2>
<p>This project is licensed under the MIT License. See the <code>LICENSE</code> file for details.</p>

</body>
