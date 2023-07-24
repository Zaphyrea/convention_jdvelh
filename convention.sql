-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Hôte : db
-- Généré le : lun. 24 juil. 2023 à 12:20
-- Version du serveur : 8.0.33
-- Version de PHP : 8.1.19

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `convention`
--

-- --------------------------------------------------------

--
-- Structure de la table `animes`
--

CREATE TABLE `animes` (
  `id_anime` int DEFAULT NULL,
  `Titre` varchar(53) DEFAULT NULL,
  `Resume` varchar(86) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Déchargement des données de la table `animes`
--

INSERT INTO `animes` (`id_anime`, `Titre`, `Resume`) VALUES
(1, 'One Slice - À la Recherche de la Part de Pizza Perdue', 'Un équipage de pirates à la recherche d\'une part de pizza aux pouvoirs mystiques !'),
(2, 'My Hérisson Academia - Les Héros à Épines', 'Des hérissons dotés de pouvoirs étranges intègrent une académie secrète !'),
(3, 'Attack on Snacks - La Quête des Collations', 'Des adolescents affamés cherchent à trouver les meilleures collations du monde !'),
(4, 'Dearth Note - Le Cahier des Courses Mortelles', 'Un carnet magique permet de commander toutes sortes de plats, mais à quel prix ?'),
(5, 'Tokyo Ghoulfriend - Monstres de la Cuisine', 'Un lycéen rencontre une fille qui le transforme en créature dévoreuse de desserts !'),
(6, 'Sailor Spoon - La Guerrière de la Cuillère', 'Une adolescente maladroite devient une guerrière culinaire contre les repas fades !'),
(7, 'Dragon Ball Zzz - Les Guerriers des Siestes Épiques', 'Goku et ses amis se battent contre l\'ennui pour rester éveillés pendant les combats !'),
(8, 'Fullmetal Al\'chimiste - L\'Alchimie de la Malbouffe', 'Deux frères alchimistes recherchent le fast-food ultime dans un monde parallèle !'),
(9, 'Hunter X Buffet - Les Chasseurs de Buffets à Volonté', 'Des chasseurs d\'élite partent en quête de buffets à volonté à travers le monde !'),
(10, 'Sword Art Abridged - L\'Épée du Raccourci', 'Un joueur de réalité virtuelle recherche la quête la plus courte pour sauver sa sœur !');

-- --------------------------------------------------------

--
-- Structure de la table `celebrites`
--

CREATE TABLE `celebrites` (
  `id_celebrity` int DEFAULT NULL,
  `Nom` varchar(17) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Déchargement des données de la table `celebrites`
--

INSERT INTO `celebrites` (`id_celebrity`, `Nom`) VALUES
(1, 'Hayao Miyazaki'),
(2, 'Masashi Kishimoto'),
(3, 'Akira Toriyama'),
(4, 'Naoko Takeuchi'),
(5, 'Eiichiro Oda'),
(6, 'Makoto Shinkai'),
(7, 'Hiromu Arakawa'),
(8, 'Rumiko Takahashi'),
(9, 'Osamu Tezuka'),
(10, 'Yoshihiro Togashi');

-- --------------------------------------------------------

--
-- Structure de la table `goodies`
--

CREATE TABLE `goodies` (
  `id_goodies` int DEFAULT NULL,
  `Goodie` varchar(26) DEFAULT NULL,
  `Charisme` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Déchargement des données de la table `goodies`
--

INSERT INTO `goodies` (`id_goodies`, `Goodie`, `Charisme`) VALUES
(1, 'Tenue Sailor Moon', 9),
(2, 'Peluche pikouai', 5),
(3, 'T-shirt Star Wars', 7),
(4, 'Figurine Sangohan', 8),
(5, 'Perruque Raiponce', 10),
(6, 'Boussole steampunk', 6),
(7, 'Poster bulbizarre', 6),
(8, 'Pin\\\'s Yoshi', 7),
(9, 'Bouclier hylien', 8),
(10, 'Statuette de Gladeulfheura', 10);

-- --------------------------------------------------------

--
-- Structure de la table `goodies_moches`
--

CREATE TABLE `goodies_moches` (
  `id_goodies` int DEFAULT NULL,
  `Goodie` varchar(61) DEFAULT NULL,
  `Perte charisme` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Déchargement des données de la table `goodies_moches`
--

INSERT INTO `goodies_moches` (`id_goodies`, `Goodie`, `Perte charisme`) VALUES
(1, 'Chapeau en forme de hot-dog', 5),
(2, 'Chaussettes avec des motifs de cornichons', 4),
(3, 'Casquette fluorescente \'Je suis bizarre\'', 5),
(4, 'Mouchoirs en papier imprimés de cafards', 9),
(5, 'T-shirt \'J\'aime les légumes\' avec des dessins d\'épinards', 5),
(6, 'Porte-clés en forme de limace', 8),
(7, 'Autocollants géants pour ongles avec des motifs de moustaches', 10),
(8, 'Coque de téléphone en plastique imitation bois', 6),
(9, 'Porte-monnaie en forme de poisson pourri', 7),
(10, 'Lunettes de soleil avec des yeux exorbités', 11),
(11, 'Sweat-shirt Je suis beauf', 30);

-- --------------------------------------------------------

--
-- Structure de la table `goodies_rares`
--

CREATE TABLE `goodies_rares` (
  `id_goodies_rares` int DEFAULT NULL,
  `Goodie` varchar(44) DEFAULT NULL,
  `Charisme` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Déchargement des données de la table `goodies_rares`
--

INSERT INTO `goodies_rares` (`id_goodies_rares`, `Goodie`, `Charisme`) VALUES
(1, 'Figurine cristal Link ', 16),
(2, 'Épée Excalibur en ébène', 20),
(3, 'T-shirt brodé Final Fantasy', 19),
(4, 'Statue marbre Saitama', 25),
(5, 'Montre Triforce nacrée', 21),
(6, 'Cartes éditions limitées Pokémon', 22),
(7, 'Figurine articulée platine Dark Vador', 20),
(8, 'Statuette bronze Gandalf You shall not pass!', 24),
(9, 'Maquette Chateau ambulant en verre poli', 25),
(10, 'Scultpure Bob l’éponge en vraie éponge', 50);

-- --------------------------------------------------------

--
-- Structure de la table `jeux_vr`
--

CREATE TABLE `jeux_vr` (
  `id_game` int DEFAULT NULL,
  `Titre` varchar(67) DEFAULT NULL,
  `Resume` varchar(99) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Déchargement des données de la table `jeux_vr`
--

INSERT INTO `jeux_vr` (`id_game`, `Titre`, `Resume`) VALUES
(1, 'Beat That Saber - Le Jeu de Danse Absurde', 'Dansez sur des chansons loufoques et faites exploser des blocs de pudding !'),
(2, 'The Elder Malls - Le Shopping Magique', 'Devenez le meilleur acheteur en utilisant des sorts farfelus pour trouver les meilleures affaires !'),
(3, 'Resident Sneevil - Les Farces Mortelles', 'Incarnez un farceur qui embête les résidents d\'une maison hantée en réalité virtuelle !'),
(4, 'Fruit Snacks - La Guerre des Fruits', 'Combattez pour les fruits les plus délirants dans une arène virtuelle remplie de pépins !'),
(5, 'Job Simulator - La Simulation du Délire Professionnel', 'Expérimentez les emplois les plus loufoques et hilarants dans un monde virtuel déjanté !'),
(6, 'Fruit Ninja\'s Revenge - La Vengeance des Fruits', 'Les fruits reviennent pour se venger des joueurs qui les ont découpés dans un jeu plein de jus !'),
(7, 'Resident Raccoon - Les Farces des Ratons Laveurs', 'Explorez une ville infestée de ratons laveurs farceurs dans ce jeu d\'action en VR !'),
(8, 'The Legend of Zelda: Link\'s Unwakening - Le Sommeil des Aventuriers', 'Link s\'endort à chaque fois qu\'il rencontre un ennemi, mais il doit quand même sauver Hyrule !'),
(9, 'Doomed VR - Le Shooter de Farce', 'Affrontez des monstres farceurs dans des niveaux délirants remplis de rires en réalité virtuelle !'),
(10, 'Starcraft: Super Starprank - Les Farces Interstellaires', 'Préparez des pièges farfelus pour les Zergs et Protoss dans cet épisode déjanté !');

-- --------------------------------------------------------

--
-- Structure de la table `musiques`
--

CREATE TABLE `musiques` (
  `id_music` int DEFAULT NULL,
  `Titre` varchar(33) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Déchargement des données de la table `musiques`
--

INSERT INTO `musiques` (`id_music`, `Titre`) VALUES
(1, 'Epic Pizza Quest'),
(2, 'Kawaii Chaos Dance'),
(3, 'Noodle Nation Anthem'),
(4, 'Funky Food Wars'),
(5, 'Otaku Groove Revolution'),
(6, 'Chibi Chaos Symphony'),
(7, 'Ramen Rap Battle'),
(8, 'Epic Quest for the Remote Control'),
(9, 'Chopstick Champions'),
(10, 'Yokai Dance Delight');

-- --------------------------------------------------------

--
-- Structure de la table `vendeurs`
--

CREATE TABLE `vendeurs` (
  `id_vendor` int DEFAULT NULL,
  `Vendeur` varchar(16) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Déchargement des données de la table `vendeurs`
--

INSERT INTO `vendeurs` (`id_vendor`, `Vendeur`) VALUES
(1, 'Ninj\'Abracadabra'),
(2, 'Kawaiizilla'),
(3, 'OtakuFolie'),
(4, 'MechaLoufoque'),
(5, 'YokaiYoghourt'),
(6, 'MangaMistigri'),
(7, 'SamouraïSourire'),
(8, 'KawaiiChaos'),
(9, 'DessinsDélirium'),
(10, 'YokaiYogini');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
