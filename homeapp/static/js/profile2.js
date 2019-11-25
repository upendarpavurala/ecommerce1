//<!-- Validation_phoneNo -->

        var reg = /^\(?([0-9]{3})\)?[-. ]?([0-9]{3})[-. ]?([0-9]{4})$/;

        function PhoneValidation(phoneNumber) {
            var OK = reg.exec(phoneNumber.value);
            if (!OK)
                window.alert("phone number isn't  valid");

        }

//<!-- Validation_phoneNo -->