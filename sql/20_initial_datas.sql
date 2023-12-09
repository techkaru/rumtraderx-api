INSERT INTO production_method_detail (id, name) VALUES
    (1,'Coffey Still'),
    (2,'20hl Copper Pot Still'),
    (3,'Single Retort Pot Still'),
    (4,'Double Retort Pot Still'),
    (5,'Savalle Still'),
    (6,'Blair Column Still'),
    (7,'John Dore Pot Still'),
    (8,'Vendome Double Retort Still'),
    (9,'Müller Copper Pot Still'),
    (10,'Wooden Continuous Still'),
    (11,'Column Still'),
    (12,'Metal Coffey Still'),
    (13,'Creole Column Still'),
    (14,'Savalle Column Still'),
    (15,'Continuous Blair Still'),
    (16,'Wooden Single Pot Still'),
    (17,'Four-column Still'),
    (18,'Two-column Still'),
    (19,'Two-column Wooden Coffey Still'),
    (20,'Forsyths Pot Still'),
    (21,'Double Wooden Pot Still'),
    (22,'Pot & Column Still'),
    (23,'See Lot Description'),
    (24,'Five-column Still'),
    (25,'Wooden Pot Still'),
    (26,'French Savalle Still'),
    (27,'Batch Kettle Still'),
    (28,'Barbet Column Still'),
    (29,'Three-column Still'),
    (30,'Single Pot Still'),
    (31,'Hybrid Column Still'),
    (32,'Wooden Continuous Coffee Still'),
    (33,'Multi-column Still'),
    (34,'Gregg Pot Still'),
    (35,'Greg Pot Still & Column Still'),
    (36,'Bain-marie Müller Copper Pot Still'),
    (37,'Inox Pot Still'),
    (38,'Four-column Savalle Still'),
    (39,'Copper Pot Still'),
    (40,'Wooden Coffey Still'),
    (41,'Pot Still'),
    (42,'Single Wooden Pot Still');

INSERT INTO bottler (id, name, description, country, region) VALUES
    (1, 'LMDW', 'La Maison Du Whisky', 'gp', 'Marie-Galante'),
    (2, 'Velier', 'Embouteilleur Velier', 'gp', 'Marie-Galante');

INSERT INTO canne_type (id, name, description) VALUES
    (1, 'Blue canne', 'Canne bleue'),
    (2, 'Red Canne', 'Canne rouge');

INSERT INTO distillery (id, name, description, creation_date, is_alive, closure_date, country, region) VALUES
    (1, 'Bielle', 'Distillerie de Grand-Bourg', '2023-01-01', true, null, 'gp', 'Marie-Galante'),
    (2, 'Damoiseau', 'Distillerie du Moule', '1942-01-01', true, null, 'gp', 'Marie-Galante');

INSERT INTO brand (id, name, description, country, region) VALUES
    (1, 'Damoiseau', 'Damoiseau brand description', 'gp', 'Marie-Galante'),
    (2, 'Bielle', 'Description Bielle', 'gp', 'Marie-Galante');

INSERT INTO product (id, is_active, category, sku, name, slug, description, made_from, distillation_type, aging_climate, aging_type, batch, abv, size, bottled_year, year, age, total_bottles, created_date, main_picture, is_single_cask, cask_number, is_bio, is_parcellaire, is_approved, is_discontinued, updated_date, production_method_detail_id, brand_id, distillery_id, bottler_id, canne_type_id, region, production_method, country, min_ask_price, max_bid_price) VALUES
    (1, true, 'Old rum', null, 'Bielle 2016', 'bielle-2016', 'Brut de Fût de 7ans 2016', 'Molasse', 'distillation_type', 'tropical', 'aging_type', 1, 54.6, 70, 2009, 2016, 7, 5000, '2023-11-09', 'http://test', false, null, false, false, true, false, '2023-11-09', 1, 1, 1, 1, 1, 'Marie-Galante', 'Column Still', 'gp', 70, 90); 