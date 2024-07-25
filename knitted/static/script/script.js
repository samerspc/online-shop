document.addEventListener("DOMContentLoaded", function() {
            document.querySelectorAll(".open-popup").forEach(function(element) {
                element.addEventListener("click", function(event) {
                    event.preventDefault();
                    document.querySelector(".layer").style.display = "block";
                    document.body.style.overflow = "hidden";
                    document.querySelector(".panel").style.display = "block";
                    document.querySelector(".panel").style.animation = "animOpen 0.3s ease-in-out";
                    document.querySelector(".layer").style.animation = "animOpen 0.3s ease-in-out";
                });
            });

            document.getElementById("closePanel").addEventListener("click", function(event) {
                event.preventDefault();
                document.querySelector(".panel").style.animation = "animClose 0.3s ease-in-out";
                document.querySelector(".layer").style.animation = "animClose 0.3s ease-in-out";
                setTimeout(() => {
                    document.querySelector(".layer").style.display = "none";
                    document.querySelector(".panel").style.display = "none";
                    document.body.style.overflow = "auto";
                }, 300);
            });

            document.querySelector(".create").addEventListener('click', function(event) {
                event.preventDefault();
                document.querySelector(".create").style.color = "hsla(0, 0%, 0%, 1)";
                document.querySelector(".create").style.fontFamily = "HM";
                document.querySelector(".come").style.color = "hsla(0, 0%, 0%, 0.65)";
                document.querySelector(".come").style.fontFamily = "HL";
                document.getElementById("formAccount").style.display = "block";
                document.getElementById("formInput").style.display = "none";
            });

            document.querySelector(".come").addEventListener('click', function(event) {
                event.preventDefault();
                document.querySelector(".come").style.color = "hsla(0, 0%, 0%, 1)";
                document.querySelector(".come").style.fontFamily = "HM";
                document.querySelector(".create").style.color = "hsla(0, 0%, 0%, 0.65)";
                document.querySelector(".create").style.fontFamily = "HL";
                document.getElementById("formAccount").style.display = "none";
                document.getElementById("formInput").style.display = "block";
            });
        });