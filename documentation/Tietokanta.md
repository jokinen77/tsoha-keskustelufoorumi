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

## Sovelluksen käyttämiä tietokantakyselyitä

* Sisäänkirjautuminen
```
SELECT account.id AS account_id, account.username AS account_username, account.date_created AS account_date_created, account.name AS account_name, account.email AS account_email, account.password AS account_password, account.usertype_id AS account_usertype_id 
FROM account 
WHERE account.username = ? AND account.password = ?
```

* Foorumien hakeminen
```
# Haetaan käyttäjän käyttäjäryhmät
SELECT usergroup.id AS usergroup_id, usergroup.name AS usergroup_name, usergroup.description AS usergroup_description 
FROM usergroup, usergroup_account 
WHERE ? = usergroup_account.account_id AND usergroup.id = usergroup_account.usergroup_id

# Haetaan käyttäjäryhmiin liitetyt foorumit
SELECT forum.id AS forum_id, forum.date_created AS forum_date_created, forum.name AS forum_name, forum.usergroup_id AS forum_usergroup_id 
FROM forum 
WHERE ? = forum.usergroup_id
```

* Foorumin viestien hakeminen
```
SELECT message.id AS message_id, message.date AS message_date, message.content AS message_content, message.user_id AS message_user_id, message.forum_id AS message_forum_id 
FROM message
WHERE message.forum_id = ? 
ORDER BY message.date
```

* Käyttäjien hakeminen
```
SELECT account.id AS account_id, account.username AS account_username, account.date_created AS account_date_created, account.name AS account_name, account.email AS account_email, account.password AS account_password, account.usertype_id AS account_usertype_id 
FROM account ORDER BY account.username
```

* Käyttäjätyyppien hakeminen
```
SELECT usertype.id AS usertype_id, usertype.name AS usertype_name, usertype.value AS usertype_value 
FROM usertype 
WHERE usertype.id = ?
```

* Käyttäjäryhmien hakeminen
```
SELECT usergroup.id AS usergroup_id, usergroup.name AS usergroup_name, usergroup.description AS usergroup_description 
FROM usergroup
```

* Käyttäjän luominen
```
INSERT INTO account (username, date_created, name, email, password, usertype_id) 
VALUES (?, CURRENT_TIMESTAMP, ?, ?, ?, ?)
```

* Foorumin luominen
```
INSERT INTO forum (date_created, name, usergroup_id) VALUES (CURRENT_TIMESTAMP, ?, ?)
```

* Viestin lähettäminen
```
INSERT INTO message (date, content, user_id, forum_id) VALUES (CURRENT_TIMESTAMP, ?, ?, ?)
```

* Käyttäjien lähettämien viestien lukumäärän laskeminen:
```{sql}
SELECT COUNT(message.id) FROM account 
LEFT JOIN message ON message.user_id = account.id 
WHERE (account.id = ?) 
GROUP BY account.id
```

