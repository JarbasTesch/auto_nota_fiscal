<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">


</head>
<body>

<header>
    <h1>AutoNotaFiscal</h1>
</header>

<section>
    <h2>Description</h2>
    <p><strong>AutoNotaFiscal</strong> is an automated script developed using Python and Selenium that simulates the generation of invoices. The script integrates data from an Excel file and automatically enters information into web forms, simulating the entire process of logging into a platform and issuing invoices.</p>
</section>

<section>
    <h2>Features</h2>
    <ul>
        <li><strong>Automated Login</strong>: The script logs into a platform by filling in the username and password from a local HTML file.</li>
        <li><strong>Data Entry</strong>: The script reads invoice data (such as customer details, product description, quantity, and pricing) from an Excel file and fills in the corresponding fields on the web platform.</li>
        <li><strong>File Download Management</strong>: Automatically manages the download directory to save files without prompting the user.</li>
    </ul>
</section>

<section>
    <h2>Requirements</h2>
    <ul>
        <li>Python 3.x</li>
        <li>Selenium</li>
        <li>Chrome WebDriver</li>
        <li>Chrome Browser</li>
        <li><code>pandas</code> library</li>
        <li><code>webdriver-manager</code> library</li>
    </ul>
</section>
<section>
    <h2>Install Requirements</h2>
    <p>To run the script, install the required dependencies using <code>pip</code>:</p>
    <pre><code>pip install --upgrade -r requirements.txt</code></pre>
</section>


<section>
    <h2>How to Use</h2>
    <ol>
        <li>Clone or download the repository.</li>
        <li>Make sure you have Chrome browser installed.</li>
        <li>Ensure that the required <code>login.html</code> and <code>NotasEmitir.xlsx</code> files are available and contain the appropriate data (login credentials accept any input).</li>
        <li>Run the Python script:</li>
        <pre>python main.py</pre>
        <li>The script will log in to the platform and automatically enter invoice data from the Excel file, simulating the process of issuing invoices.</li>
    </ol>
</section>

<section>
    <h2>Files</h2>
    <ul>
        <li><strong>login.html</strong>: HTML file containing the login form (username and password fields).</li>
        <li><strong>NotasEmitir.xlsx</strong>: Excel file containing the details for the invoices to be generated, such as:
            <ul>
                <li>Cliente</li>
                <li>Endereço</li>
                <li>Bairro</li>
                <li>Município</li>
                <li>CEP</li>
                <li>UF</li>
                <li>CPF/CNPJ</li>
                <li>Inscrição Estadual</li>
                <li>Descrição</li>
                <li>Quantidade</li>
                <li>Valor Unitário</li>
                <li>Valor Total</li>
            </ul>
        </li>
    </ul>
</section>

<section>
    <h2>Notes</h2>
    <ul>
        <li>The <strong>NotasEmitir.xlsx</strong> file should be properly formatted with the necessary columns for the invoice generation process.</li>
        <li>When you clone the project, the <code>login.html</code> and <code>NotasEmitir.xlsx</code> files will already be in the project folder. However, if you move or reorganize the project files, you may need to update the paths accordingly.</li>
        <li>Ensure that the <strong>Chrome WebDriver</strong> is properly installed and available on your machine.</li>
    </ul>
</section>

</body>
</html>
