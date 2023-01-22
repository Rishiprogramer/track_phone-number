def track():
    import phonenumbers

    from phonenumbers import geocoder
    number = input("Enter the phnober: ")
    ch_number = phonenumbers.parse(number, "CH")
    print(geocoder.description_for_number(ch_number, "en"))

    from phonenumbers import carrier

    service = phonenumbers.parse(number, "RO")
    print(carrier.name_for_number(service, "en"))
