#!/usr/bin/node

const request = require('request');

// Get movie ID from first positional argument
const movieId = process.argv[2];

// validate input
if (!movieId) {
	console.error('Please provide a Movie ID');
	process.exit(1);
}

// define endpoint for the films
const filmUrl = `https://swapi.dev/api/films/${movieId}/`;

request(filmUrl, (error, response, body) => {
	if (error) {
		console.log('Error making the request:', error);
		return;
	}

	if (response.statusCode !== 200) {
		console.error('Failed to retrieve data:', response.statusCode);
		return;
	}

	// parse response body
	const filmData = JSON.parse(body);

	// extract characters array from the film data
	const characters = filmData.characters;

	// fetch & print each character name
	const fetchCharacterName = (url) => {
		return new Promise((resolve, reject) => {
			request(url, (error, response, body) => {
				if (error) {
					reject(error);
					return;
				}

				if (response.statusCode !== 200) {
					reject(`Failed to retrieve data: ${response.statusCode}`);
					return;
				}

				// parse character data
				const characterData = JSON.parse(body);
				resolve(characterData.name);
			});
		});
	};

	// loop through chars array & retrieve each name
	const characterPromises = characters.map(fetchCharacterName);

	Promise.all(characterPromises)
		.then((names) => {
			names.forEach(name => console.log(name));
		})
		.catch((error) => {
			console.error('Error fetching character names:', error);
		});
});
