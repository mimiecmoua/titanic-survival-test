document.addEventListener("DOMContentLoaded", function() {
    console.log("JS Loaded 🚀");

    // 🔹 Sélection des boutons Man/Woman
    const btnWoman = document.getElementById("btn-woman");
    const btnMan = document.getElementById("btn-man");

    let selectedGender = null; // Variable pour stocker le genre sélectionné

    // ✅ Ajouter un event listener sur chaque bouton
    btnWoman.addEventListener("click", function () {
        selectedGender = "female";
        btnWoman.classList.add("active", "btn-light");
        btnMan.classList.remove("active", "btn-light");
    });

    btnMan.addEventListener("click", function () {
        selectedGender = "male";
        btnMan.classList.add("active", "btn-light");
        btnWoman.classList.remove("active", "btn-light");
    });

    // 🔹 Sélection du bouton "Go!"
    const goButton = document.querySelector(".btn-heartbeat");

    goButton.addEventListener("click", async function () {
        // 🔹 1. Récupérer les valeurs des inputs
        const age = document.getElementById("input-age").value;
        const classe = document.getElementById("select-classe").value;

        // ✅ Vérifier si l'utilisateur a bien rempli tout
        if (!selectedGender || !age || !classe) {
            alert("Please fill in all the fields! 🙏");
            return;
        }

        // ✅ Créer l'objet avec les données
        const data = {
            sexe: selectedGender,
            age: parseInt(age),
            classe: parseInt(classe)
        };

        console.log("Sending data to API:", data);

        try {
            // 🔹 2. Envoyer la requête POST à Flask
            const response = await fetch("https://titanic-api-6g6t.onrender.com/predict", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(data)
            });

            // 🔹 3. Récupérer la réponse JSON
            const result = await response.json();
            console.log("Response from API:", result);

            // 🔹 4. Afficher le message de réponse sur la page
            document.getElementById("result-message").textContent = result.message;
            document.getElementById("result-message").style.display = "block";

        } catch (error) {
            console.error("Error:", error);
            alert("Oops! Something went wrong. 😢");
        }
    });
});


