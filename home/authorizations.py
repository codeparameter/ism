def authorize():

    for app in (
        'users',
        'mines',
        'factories',
    ):            
        exec(f"from {app}.authorizations import authorize as au")
        exec("au()")
