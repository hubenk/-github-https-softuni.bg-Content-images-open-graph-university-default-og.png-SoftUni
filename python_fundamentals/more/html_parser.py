some_text = input()
title_regex = r"(?<=<title>)[\w\s]+(?=</title>)"
body_regex = r"(?<=<body>)[\a-zA-Z]+(?=</body>)"
body_clear_regex = r""