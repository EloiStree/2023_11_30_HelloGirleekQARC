## Exercice du jour

**Pour les étudiants orientés logique :**
- Créez un script qui modifie un système de particules.
- Créez un script qui crée un objet du niveau derrière la voiture.
- *Niveau intermédiaire :* Affichez sur la voiture une jauge d'informations :
  - Vitesse, nombre de collisions,
  - Distance avec des objets devant (voir Raycast).

**Pour les étudiants orientés couleur :**
- Utilisez Shader Graph pour personnaliser les couleurs de votre équipe ou de votre voiture.
  - *Niveau débutant :* Suivez un tutoriel sur Shader Graph pour créer le shader.
  - *Niveau intermédiaire :* Téléchargez des shaders depuis l'Asset Store et transformez-les pour URP.

*Optionnel, pour un expert :*
- Utilisez la clé Bluetooth sous Python pour communiquer avec la Xbox via le Brook.
- Utilisez un port série avec le TTL sous Python pour activer des relais Arduino.

# Qu'est-ce qu'un script ?

Un logiciel est constitué de millions de lignes de texte qui permettent de communiquer avec la machine. On appelle cela du code. Et quand il est massif, on appelle ça une architecture logicielle.

Pour permettre aux développeurs de travailler avec les game designers et les artistes, Unity3D a créé des scripts que l'on appelle des MonoBehaviour.

Ces scripts permettent :
- Aux développeurs juniors de commencer facilement sur Unity3D.
- Aux développeurs experts de prototyper rapidement.
- Aux designers de modifier les éléments du jeu sans devoir coder.
- Aux designers avec une connaissance du code de pouvoir adapter le jeu.
- ...

Dans cet atelier, je vais vous montrer comment, à l'aide de scripts, on peut affecter des particules et des objets dans Unity pour que vous personnalisiez votre modèle.

# Qu'est-ce que Shader Graph ?

Comme nous l'avons vu dans l'atelier précédent, les artistes peuvent créer des objets 3D et des objets 2D. Mais pour créer l'interaction de la lumière sur les triangles de l'objet, on a besoin de shaders. Avant, ce travail était celui d'un développeur, mais avec le no-code, c'est devenu un travail de graphiste.

Shader Graph est un outil fourni par Unity3D qui permet de très facilement fabriquer des effets complexes dans nos jeux sans connaître de code.

Dans cet atelier, je vais vous montrer les bases pour que vous puissiez créer vos propres shaders pour votre modèle 3D.
