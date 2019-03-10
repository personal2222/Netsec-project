
DROP TABLE IF EXISTS dns_records;
CREATE TABLE dns_records (
    zone text,
    host text,
    ttl integer,
    type text,
    mx_priority integer,
    data text,
    resp_person text,
    serial integer,
    refresh integer,
    retry integer,
    expire integer,
    minimum integer
);
CREATE INDEX host_index on dns_records (host);
CREATE INDEX type_index on dns_records (type);
CREATE INDEX zone_index on dns_records (zone);
