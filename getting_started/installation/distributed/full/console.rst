Console
^^^^^^^

Test 

.. raw:: html

    <script src="https://code.jquery.com/jquery-3.3.1.min.js"></script>
    <script src="https://unpkg.com/jquery.terminal/js/jquery.terminal.min.js"></script>
    <link rel="stylesheet" href="https://unpkg.com/jquery.terminal/css/jquery.terminal.min.css"/>
    <script>
    $('body').terminal({
        title: function(...args) {
            const options = $.terminal.parse_options(args);
            return fetch(options.url || 'https://terminal.jcubic.pl')
                .then(r => r.text())
                .then(html => html.match(/<title>([^>]+)<\/title>/)[1]);
        }
    }, {
        checkArity: false,
        completion: true,
        greetings: 'Welcome to Morpheus\n'
    });
    </script>