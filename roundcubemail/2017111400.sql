SET @s = (SELECT IF(
    (SELECT COUNT(*)
        FROM INFORMATION_SCHEMA.COLUMNS
        WHERE table_name = 'session'
        AND table_schema = DATABASE()
        AND column_name = 'created'
    ) > 0,
    "SELECT 1",
    "ALTER TABLE session ADD COLUMN created datetime NOT NULL DEFAULT '1970-01-01 00:00:00'"
));

PREPARE stmt FROM @s;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;

