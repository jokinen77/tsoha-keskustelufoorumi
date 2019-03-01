# Tietokanta

## Tietokantakaavio

<img width="1000" src="https://github.com/jokinen77/tsoha-keskustelufoorumi/blob/master/documentation/db_diagram-20190301.png">

## Create table -komennot

```{sql}
CREATE TABLE usergroup (
	id INTEGER NOT NULL, 
	name VARCHAR NOT NULL, 
	description VARCHAR(500), 
	PRIMARY KEY (id), 
	UNIQUE (name)
);
CREATE TABLE usertype (
	id INTEGER NOT NULL, 
	name VARCHAR(255) NOT NULL, 
	value FLOAT, 
	PRIMARY KEY (id), 
	UNIQUE (name)
);
CREATE TABLE account (
	id INTEGER NOT NULL, 
	username VARCHAR(255), 
	date_created DATETIME, 
	name VARCHAR(255) NOT NULL, 
	email VARCHAR(255), 
	password VARCHAR(255) NOT NULL, 
	usertype_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (username), 
	FOREIGN KEY(usertype_id) REFERENCES usertype (id)
);
CREATE TABLE usergroup_account (
	account_id INTEGER, 
	usergroup_id INTEGER, 
	FOREIGN KEY(account_id) REFERENCES account (id), 
	FOREIGN KEY(usergroup_id) REFERENCES usergroup (id)
);
CREATE TABLE forum (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	name VARCHAR(255) NOT NULL, 
	usergroup_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(usergroup_id) REFERENCES usergroup (id)
);
CREATE TABLE message (
	id INTEGER NOT NULL, 
	date DATETIME, 
	content VARCHAR(1000), 
	user_id INTEGER, 
	forum_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(user_id) REFERENCES account (id) ON DELETE CASCADE, 
	FOREIGN KEY(forum_id) REFERENCES forum (id)
);
```

## Sovelluksen käyttämiä yhteenvetokyselyitä

* Käyttäjien lähettämien viestien lukumäärä selvitetään yhteenvetokyselyllä (:id kohdalle sijoitetaan kyseisen käyttäjän id):
```{sql}
SELECT COUNT(message.id) FROM account 
	LEFT JOIN message ON message.user_id = account.id 
	WHERE (account.id = :id) 
	GROUP BY account.id;
```
