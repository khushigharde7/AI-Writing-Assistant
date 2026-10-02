def format_output(output, content_type):

    print("\n")
    print("=" * 70)

    if content_type == "blog":
        print("GENERATED BLOG")
    elif content_type == "email":
        print("GENERATED EMAIL")
    elif content_type == "code":
        print("CODE EXPLANATION")
    elif content_type == "social":
        print("SOCIAL MEDIA POST")
    else:
        print("GENERATED CONTENT")

    print("=" * 70)

    print(output)

    print("=" * 70)