// mon catalogue (metric = le prix en DH)
const catalogItems = [
  {
    id: 1,
    title: "PlayStation 5",
    category: "Console de salon",
    image: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSFN9bV0AT4AibzZIX6JmD4JetxLnlbJ_l7gns4rwdR5uT-z68A6i10Cg-U&s=10",
    metric: 6499,
    shortDescription: "La console de Sony avec SSD ultra rapide et manette DualSense.",
    fullDetails: "Sortie en 2020. Jeux en 4K, chargements quasi instantanés grâce au SSD, retour haptique et gâchettes adaptatives sur la manette DualSense. Compatible avec la plupart des jeux PS4."
  },
  {
    id: 2,
    title: "Xbox Series X",
    category: "Console de salon",
    image: "https://media.wired.com/photos/5fa5dc3dba670daaf8e97a8d/master/pass/games_gear_series-x.jpg",
    metric: 6299,
    shortDescription: "La Xbox la plus puissante, idéale avec le Game Pass.",
    fullDetails: "Sortie en 2020. Lecteur Blu-ray 4K, jeux jusqu'à 120 images par seconde et Quick Resume pour passer d'un jeu à l'autre. Compatible avec les anciennes générations de Xbox."
  },
  {
    id: 3,
    title: "Xbox Series S",
    category: "Console de salon",
    image: "https://commons.wikimedia.org/wiki/Special:FilePath/Xbox_Series_S_with_controller.jpg?width=600",
    metric: 3499,
    shortDescription: "Petite, blanche et 100 % numérique, parfaite pour commencer.",
    fullDetails: "Sortie en 2020. Version compacte sans lecteur de disque, pensée pour le jeu dématérialisé. Même catalogue que la Series X avec une résolution plus basse."
  },
  {
    id: 4,
    title: "Nintendo Switch",
    category: "Console portable",
    image: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSKOZ4w01yIih297IngqCFtBQr0SIK5j-BqGfIQA8mnYQ&s=10",
    metric: 3299,
    shortDescription: "Console hybride qui se joue sur la télé ou en mode portable.",
    fullDetails: "Sortie en 2017. Les manettes Joy-Con se détachent pour jouer à deux. Accès aux grandes licences Nintendo : Mario, Zelda, Pokémon."
  },
  {
    id: 5,
    title: "Steam Deck",
    category: "Console portable",
    image: "https://i5.walmartimages.com/seo/Valve-s-Steam-Deck-512-GB-US-Plug-V004287-30_721dfd3a-0133-45e5-bacf-7882301c009b.754435869c0cecb85fa90d1a136062a9.jpeg",
    metric: 4999,
    shortDescription: "Un vrai PC portable de poche pour jouer à ta bibliothèque Steam.",
    fullDetails: "Sortie en 2022 par Valve. Écran tactile, deux pavés tactiles et SteamOS. Se branche aussi sur un écran pour jouer comme sur un PC de bureau."
  },
  {
    id: 6,
    title: "PC Gamer Starter",
    category: "PC Gamer",
    image: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQGwqDNEdiGUOI3ijziqO229dlFAa-i_8xV2VmlW_00vuabct9tC0RuBVtb&s=10",
    metric: 8990,
    shortDescription: "Une tour équilibrée pour jouer en 1080p sans se ruiner.",
    fullDetails: "Processeur 6 cœurs, 16 Go de RAM, SSD 1 To et carte graphique milieu de gamme. Idéal pour les jeux compétitifs comme Valorant ou Fortnite."
  },
  {
    id: 7,
    title: "PC Gamer RGB Blue",
    category: "PC Gamer",
    image: "https://images.unsplash.com/photo-1658673640999-fd012da64ba4?w=800&q=60&auto=format&fit=crop",
    metric: 14500,
    shortDescription: "Une config puissante avec éclairage RGB bleu pour le 1440p.",
    fullDetails: "Processeur 8 cœurs, 32 Go de RAM, SSD 2 To et refroidissement liquide. Fait tourner les jeux récents en haute qualité."
  },
  {
    id: 8,
    title: "PC Gamer Ultra",
    category: "PC Gamer",
    image: "https://images.unsplash.com/photo-1660855551570-dd44e0ab800c?w=800&q=60&auto=format&fit=crop",
    metric: 22900,
    shortDescription: "Le haut de gamme pour jouer en 4K et streamer en même temps.",
    fullDetails: "Processeur 16 cœurs, 64 Go de RAM, SSD 4 To et carte graphique haut de gamme. Pensé pour la 4K, le streaming et le montage vidéo."
  },
  {
    id: 9,
    title: "Nintendo NES",
    category: "Console RETRO",
    image: "https://commons.wikimedia.org/wiki/Special:FilePath/NES-Console-Set.jpg?width=600",
    metric: 1200,
    shortDescription: "La console 8 bits culte qui a lancé Super Mario Bros.",
    fullDetails: "Sortie en 1985 en Occident. Console d'occasion testée et nettoyée, livrée avec une manette. Fonctionne avec les cartouches d'origine."
  },
  {
    id: 10,
    title: "Nintendo GameCube",
    category: "Console RETRO", 
    image: "https://upload.wikimedia.org/wikipedia/commons/2/2b/GameCube-Console-Set.png?utm_source=fr.wikipedia.org&utm_campaign=index&utm_content=original",
    metric: 1500,
    shortDescription: "Le petit cube violet de Nintendo et sa manette mythique.",
    fullDetails: "Sortie en 2001. Console d'occasion avec manette et carte mémoire. Célèbre pour Super Smash Bros. Melee et Mario Kart: Double Dash."
  },
  {
    id: 11,
    title: "Game Boy",
    category: "Console RETRO",
    image: "https://thumb.wikimedia.org/wikipedia/commons/thumb/8/8f/Game-Boy-Original.jpg/960px-Game-Boy-Original.jpg?utm_source=fr.wikipedia.org&utm_campaign=index&utm_content=thumbnail",
    metric: 800,
    shortDescription: "La première console portable de Nintendo, indestructible.",
    fullDetails: "Sortie en 1989. Écran monochrome vert, fonctionne avec 4 piles AA. Exemplaire d'occasion vérifié, parfait pour Tetris et Pokémon Rouge."
  },
  {
    id: 12,
    title: "Xbox originale",
    category: "Console RETRO",
    image: "https://commons.wikimedia.org/wiki/Special:FilePath/Xbox-console.jpg?width=600",
    metric: 900,
    shortDescription: "La toute première Xbox, celle qui a fait découvrir Halo.",
    fullDetails: "Sortie en 2001. Console d'occasion avec manette S. Disque dur intégré, ce qui était une première pour une console de salon."
  }
];
