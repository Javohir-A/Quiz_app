def dict_questions():
    
    questions = [
        {
            "id": 1,
            "question": "Docker containers and images are included in Plesk Backup and migrated by Plesk Migrator.",
            "answers": {
                "answer_a": "True",
                "answer_b": "False"
            },
            "correct_answer": "False",
            "answered": False

        },
        {
            "id": 2,
            "question": "The SQL keyword BETWEEN is used?",
            "answers": {
                "answer_a": "To Limit The Columns Displayed",
                "answer_b": "None Of The Above",
                "answer_c": "For Ranges",
                "answer_d": "As A Wildcard"
            },
            "correct_answer": "As A Wildcard",
            "answered": False

        },
        {
            "id": 3,
            "question": "In Linux, the priority of a running process can be changed using which command?",
            "answers": {
                "answer_a": "priority",
                "answer_b": "renice",
                "answer_c": "ps -A",
                "answer_d": "passwd"
            },
            "correct_answer": "renice",
            "answered": False
        },
        {
            "id": 4,
            "question": "How can we end a session?",
            "answers": {
                "answer_a": "session_destroy();",
                "answer_b": "session_close().",
                "answer_c": "session_end().",
                "answer_d": "session_write_end().",
                "answer_e": "session_destroy_now();"
            },
            "correct_answer": "session_destroy();",
            "answered": False
        },
        {
            "id": 5,
            "question": "Referential integrity is directly related to",
            "answers": {
                "answer_a": "Relation Key",
                "answer_b": "Foreign Key",
                "answer_c": "Unique Key",
                "answer_d": "Primary Key"
            },
            "correct_answer": "Foreign Key",
            "answered": False
        },
        {
            "id": 6,
            "question": "How can we propagate a session id?",
            "answers": {
                "answer_a": "You can propagate a session id via cookies or URL parameters.",
                "answer_b": "You can propagate a session id via headers and routing."
            },
            "correct_answer": "You can propagate a session id via cookies or URL parameters.",
            "answered": False
        },
        {
            "id": 7,
            "question": "Which arithmetic operator you can not use?",
            "answers": {
                "answer_a": "+",
                "answer_b": "-",
                "answer_c": "*",
                "answer_d": "\\",
                "answer_e": "%"
            },
            "correct_answer": "\\",
            "answered": False
        },
        {
            "id": 8,
            "question": "Which of the following function returns a text in title case from a variable?",
            "answers": {
                "answer_a": "ucwords($var)",
                "answer_b": ".ucword($var)",
                "answer_c": "toupper($var)",
                "answer_d": ".upper($var)"
            },
            "correct_answer": "ucwords($var)",
            "answered": False
        },
        {
            "id": 9,
            "question": "Select all true statements for a node in Kubernetes?",
            "answers": {
                "answer_a": "A node is a worker machine in Kubernetes, previously known as a minion",
                "answer_b": "Each node contains the services necessary to run pods and is managed by the master components",
                "answer_c": "A node may be a VM or physical machine, depending on the cluster.",
                "answer_d": "There is only one node in each Kubernetes cluster"
            },
            "correct_answer": "A node is a worker machine in Kubernetes, previously known as a minion",
            "answered": False
        },
        {
            "id": 10,
            "question": "Which command can be used to know the terminal type?",
            "answers": {
                "answer_a": "tty",
                "answer_b": "pts",
                "answer_c": "who",
                "answer_d": "terminal"
            },
            "correct_answer": "tty",
            "answered": False
        },
        {
            "id": 11,
            "question": "Which one of these variables has an illegal name?",
            "answers": {
                "answer_a": "$myVar",
                "answer_b": "$my_Var",
                "answer_c": "$my-Var",
                "answer_d": "$MyVar"
            },
            "correct_answer": "$my-Var",
            "answered": False
        },
        {
            "id": 12,
            "question": "How to pull the Apache HTTP server image.",
            "answers": {
                "answer_a": "$ docker pull http img",
                "answer_b": "$ docker pull httpd img",
                "answer_c": "$ docker pull httpd"
            },
            "correct_answer": "$ docker pull httpd",
            "answered": False
        },
        {
            "id": 13,
            "question": "DML is included into SQL language of:",
            "answers": {
                "answer_a": "managing users",
                "answer_b": "managing transactions",
                "answer_c": "description data",
                "answer_d": "managing data"
            },
            "correct_answer": "managing data",
            "answered": False
        },
        {
            "id": 14,
            "question": "What does the /etc/hosts file contains?",
            "answers": {
                "answer_a": "Hostnames of all devices on the network segment",
                "answer_b": "The IP address of the default gateway",
                "answer_c": "CPU and memory info",
                "answer_d": "IP addresses to hostnames mappings"
            },
            "correct_answer": "IP addresses to hostnames mappings",
            "answered": False
        },
        {
            "id": 15,
            "question": "What is the correct HTML for inserting a background image?",
            "answers": {
                "answer_a": "<background img=\"background.gif\">",
                "answer_b": "<body bg=\"background.gif\">",
                "answer_c": "<body style=\"background-image:url(background.gif)\">",
                "answer_d": "<background style img=\"background.gif\">"
            },
            "correct_answer": "<body style=\"background-image:url(background.gif)\">",
            "answered": False
        },
        {
            "id": 16,
            "question": "Which of the following is NOT available in MySQL:",
            "answers": {
                "answer_a": "REVOKE",
                "answer_b": "JOIN",
                "answer_c": "LIKE",
                "answer_d": "FETCH"
            },
            "correct_answer": "REVOKE",
            "answered": False
        },
        {
            "id": 17,
            "question": "Which of these is a valid call to a function (watch The Spaces Carefully!)",
            "answers": {
                "answer_a": "CONCAT( A , B )",
                "answer_b": "CONCAT( \"A\" . \"B\" )",
                "answer_c": "CONCAT ( \"A\" , \"B\" )",
                "answer_d": "CONCAT ( A , B )"
            },
            "correct_answer": "CONCAT ( \"A\" , \"B\" )",
            "answered": False
        },
        {
            "id": 18,
            "question": "Which command will you use to display the first user?",
            "answers": {
                "answer_a": "kubectl config view -o jsonpath='{.usersname[]}'",
                "answer_b": "kubectl config view -o jsonpath='{.users[].name}'",
                "answer_c": "kubectl config view user 1",
                "answer_d": "kubectl config view -o jsonpath='{.users[*].name}'"
            },
            "correct_answer": "kubectl config view -o jsonpath='{.users[].name}'",
            "answered": False
        },
        {
            "id": 19,
            "question": "How is the ternary conditional operator used in PHP?",
            "answers": {
                "answer_a": "Expression_1?Expression_2 : Expression_3;",
                "answer_b": "Expression_1:Expression_2 : Expression_3;"
            },
            "correct_answer": "Expression_1?Expression_2 : Expression_3;",
            "answered": False
        },
        {
            "id": 20,
            "question": "How can we destroy a PHP session:",
            "answers": {
                "answer_a": "session_destroy()",
                "answer_b": "destroy_session()",
                "answer_c": "session()",
                "answer_d": "startD()",
                "answer_e": "sessionDestroy()",
                "answer_f": "destroySession()"
            },
            "correct_answer": "session_destroy()",
            "answered": False
        },
        {}
    ]
    return questions
