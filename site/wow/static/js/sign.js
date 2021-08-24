 function valid()
            {
                var a = document.validation.FirstName.value;
                if(a = "" || a.length <= 3 || a.length >= 20)
                    {
                        alert("input name is invalid.");
                        return false;
                    }

                var b = document.validation.pass.value;
                var c = document.validation.word.value;
                if(b != c)
                {
                    alert("Password didn't match");
                    return false;
                }



            }