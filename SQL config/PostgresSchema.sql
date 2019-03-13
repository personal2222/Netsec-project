CREATE TABLE dns_records(
	zone TEXT NOT NULL,
	host TEXT NOT NULL,
	ttl INT NOT NULL,
	type TEXT NOT NULL,
	mx_priority INT NULL,
	data TEXT NOT NULL,
	resp_person TEXT NULL,
	serial INT NOT NULL,
	refresh INT NOT NULL,
	retry INT NOT NULL,
	expire INT NOT NULL,
	minimum int NOT NULL
	);
	
	CREATE INDEX host_index ON dns_records USING btree (host);
	CREATE INDEX type_index ON dns_records USING btree (type);
	CREATE INDEX zone_index ON dns_records USING btree (zone);