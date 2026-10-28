// on récupère les éléments de la page
const grille = document.getElementById("cards-grid");
const messageVide = document.getElementById("NoElement");
const champRecherche = document.getElementById("recherche");
const boutons = document.querySelectorAll(".btn-categorie");
const selectTri = document.getElementById("tri");
const fenetre = document.getElementById("fenetre");
const contenuFenetre = document.getElementById("contenu-fenetre");
const boutonFermer = document.getElementById("fermer");

// les choix de l'utilisateur
let recherche = "";
let categorie = "Tous";
let tri = "";


// affiche les cartes
function renderItems(data) {
  grille.innerHTML = ""; // on vide d'abord

  data.forEach(function (item) {
    const carte = document.createElement("article");
    carte.classList.add("card");
    carte.innerHTML = `
      <img class="card-img" src="${item.image}" alt="${item.title}">
      <span class="card-category">${item.category}</span>
      <h2 class="card-name">${item.title}</h2>
      <p class="card-prix">${item.metric} DH</p>
      <p class="card-desc">${item.shortDescription}</p>
    `;

    carte.addEventListener("click", function () {
      ouvrirFiche(item);
    });

    grille.appendChild(carte);
  });

  // si y'a rien on affiche le message
  if (data.length === 0) {
    messageVide.hidden = false;
  } else {
    messageVide.hidden = true;
  }
}


// filtre + recherche + tri en même temps
function updateDisplay() {
  const texte = recherche.toLowerCase();

  const resultat = catalogItems.filter(function (item) {
    const bonneCategorie = categorie === "Tous" || item.category === categorie;
    const bonneRecherche = item.title.toLowerCase().includes(texte) || item.shortDescription.toLowerCase().includes(texte);
    return bonneCategorie && bonneRecherche;
  });

  // filter fait déjà une copie donc le catalogue reste intact
  if (tri === "A-Z") {
    resultat.sort(function (a, b) { return a.title.localeCompare(b.title); });
  } else if (tri === "Z-A") {
    resultat.sort(function (a, b) { return b.title.localeCompare(a.title); });
  } else if (tri === "croissant") {
    resultat.sort(function (a, b) { return a.metric - b.metric; });
  } else if (tri === "decroissant") {
    resultat.sort(function (a, b) { return b.metric - a.metric; });
  }

  renderItems(resultat);
}


// recherche en direct
champRecherche.addEventListener("input", function () {
  recherche = champRecherche.value.trim();
  updateDisplay();
});

// boutons catégorie
boutons.forEach(function (bouton) {
  bouton.addEventListener("click", function () {
    categorie = bouton.dataset.category;

    boutons.forEach(function (b) {
      b.classList.remove("actif");
    });
    bouton.classList.add("actif");

    updateDisplay();
  });
});

// tri
selectTri.addEventListener("change", function () {
  tri = selectTri.value;
  updateDisplay();
});


// ouvre la fiche avec toutes les infos
function ouvrirFiche(item) {
  contenuFenetre.innerHTML = `
    <img class="fiche-img" src="${item.image}" alt="${item.title}">
    <span class="card-category">${item.category}</span>
    <h2>${item.title}</h2>
    <p class="card-prix">${item.metric} DH</p>
    <p>${item.shortDescription}</p>
    <p>${item.fullDetails}</p>
  `;
  fenetre.showModal();
}

// fermer avec le bouton
boutonFermer.addEventListener("click", function () {
  fenetre.close();
});

// fermer en cliquant sur le fond
fenetre.addEventListener("click", function (e) {
  if (e.target === fenetre) {
    fenetre.close();
  }
});

// fermer avec Echap
document.addEventListener("keydown", function (e) {
  if (e.key === "Escape" && fenetre.open) {
    fenetre.close();
  }
});


// premier affichage
updateDisplay();
