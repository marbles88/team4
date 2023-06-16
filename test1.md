Tables:
gpkg_spatial_ref_sys
gpkg_contents
gpkg_geometry_columns
gpkg_extensions
gpkg_data_columns
gpkg_data_column_constraints
gpkg_metadata
sqlite_sequence
gpkg_metadata_reference
gpkg_tile_matrix
gpkg_tile_matrix_set
AISVesselTracks2021
rtree_AISVesselTracks2021_Shape
rtree_AISVesselTracks2021_Shape_rowid
rtree_AISVesselTracks2021_Shape_node
rtree_AISVesselTracks2021_Shape_parent

Table Details:
('table', 'gpkg_spatial_ref_sys', 'gpkg_spatial_ref_sys', 2, 'CREATE TABLE gpkg_spatial_ref_sys (srs_name                  TEXT NOT NULL,srs_id                    INTEGER NOT NULL PRIMARY KEY,organization              TEXT NOT NULL,organization_coordsys_id  INTEGER NOT NULL,definition                TEXT NOT NULL,description               TEXT)')
('table', 'gpkg_contents', 'gpkg_contents', 3, "CREATE TABLE gpkg_contents (table_name   TEXT NOT NULL PRIMARY KEY,data_type    TEXT NOT NULL,identifier   TEXT UNIQUE,description  TEXT DEFAULT '',last_change  DATETIME NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ','now')),min_x        DOUBLE,min_y        DOUBLE,max_x        DOUBLE,max_y        DOUBLE,srs_id       INTEGER,CONSTRAINT fk_gc_r_srs_id FOREIGN KEY (srs_id) REFERENCES gpkg_spatial_ref_sys (srs_id))")
('table', 'gpkg_geometry_columns', 'gpkg_geometry_columns', 6, 'CREATE TABLE gpkg_geometry_columns (table_name  TEXT NOT NULL,column_name TEXT NOT NULL,geometry_type_name          TEXT NOT NULL,srs_id      INTEGER NOT NULL,z           TINYINT NOT NULL,m           TINYINT NOT NULL,CONSTRAINT pk_geom_cols PRIMARY KEY (table_name, column_name),CONSTRAINT uk_gc_table_name UNIQUE (table_name),CONSTRAINT fk_gc_tn FOREIGN KEY (table_name) REFERENCES gpkg_contents (table_name),CONSTRAINT fk_gc_srs FOREIGN KEY (srs_id) REFERENCES gpkg_spatial_ref_sys (srs_id))')
('table', 'gpkg_extensions', 'gpkg_extensions', 9, 'CREATE TABLE gpkg_extensions (table_name      TEXT,column_name     TEXT,extension_name  TEXT NOT NULL,definition      TEXT NOT NULL,scope           TEXT NOT NULL,CONSTRAINT ge_tce UNIQUE (table_name,column_name,extension_name))')
('table', 'gpkg_data_columns', 'gpkg_data_columns', 11, 'CREATE TABLE gpkg_data_columns (table_name      TEXT NOT NULL,column_name     TEXT NOT NULL,name            TEXT,title           TEXT,description     TEXT,mime_type       TEXT,constraint_name TEXT,CONSTRAINT pk_gdc PRIMARY KEY (table_name,column_name),CONSTRAINT fk_gdc_tn FOREIGN KEY (table_name) REFERENCES gpkg_contents (table_name))')
('table', 'gpkg_data_column_constraints', 'gpkg_data_column_constraints', 13, "CREATE TABLE gpkg_data_column_constraints (constraint_name   TEXT NOT NULL,constraint_type   TEXT NOT NULL /* 'range' || 'enum' | 'glob' */,value             TEXT,min               NUMERIC,min_is_inclusive  BOOLEAN,max               NUMERIC,max_is_inclusive  BOOLEAN,description       TEXT,CONSTRAINT gdcc_ntv UNIQUE (constraint_name,constraint_type,value))")
('table', 'gpkg_metadata', 'gpkg_metadata', 15, "CREATE TABLE gpkg_metadata (id                    INTEGER CONSTRAINT m_pk PRIMARY KEY ASC                      AUTOINCREMENT NOT NULL UNIQUE,md_scope              TEXT NOT NULL DEFAULT 'dataset',md_standard_uri       TEXT NOT NULL,mime_type             TEXT NOT NULL DEFAULT 'text/xml',metadata              TEXT NOT NULL)")
('table', 'sqlite_sequence', 'sqlite_sequence', 17, 'CREATE TABLE sqlite_sequence(name,seq)')
('table', 'gpkg_metadata_reference', 'gpkg_metadata_reference', 18, "CREATE TABLE gpkg_metadata_reference (reference_scope  TEXT NOT NULL,table_name       TEXT,column_name      TEXT,row_id_value     INTEGER,timestamp        DATETIME NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ','now')),md_file_id       INTEGER NOT NULL,md_parent_id     INTEGER,CONSTRAINT crmr_mfi_fk FOREIGN KEY (md_file_id) REFERENCES gpkg_metadata(id),CONSTRAINT crmr_mpi_fk FOREIGN KEY (md_parent_id) REFERENCES gpkg_metadata(id))")
('table', 'gpkg_tile_matrix', 'gpkg_tile_matrix', 19, 'CREATE TABLE gpkg_tile_matrix (table_name TEXT NOT NULL,zoom_level INTEGER NOT NULL,matrix_width INTEGER NOT NULL,matrix_height INTEGER NOT NULL,tile_width INTEGER NOT NULL,tile_height INTEGER NOT NULL,pixel_x_size DOUBLE NOT NULL,pixel_y_size DOUBLE NOT NULL,CONSTRAINT pk_ttm PRIMARY KEY (table_name,zoom_level),CONSTRAINT fk_ttm_table_name FOREIGN KEY (table_name) REFERENCES gpkg_contents(table_name))')
('table', 'gpkg_tile_matrix_set', 'gpkg_tile_matrix_set', 23, 'CREATE TABLE gpkg_tile_matrix_set (table_name TEXT NOT NULL PRIMARY KEY,srs_id     INTEGER NOT NULL,min_x      DOUBLE NOT NULL,min_y      DOUBLE NOT NULL,max_x      DOUBLE NOT NULL,max_y      DOUBLE NOT NULL,CONSTRAINT fk_gtms_table_name FOREIGN KEY (table_name) REFERENCES gpkg_contents (table_name),CONSTRAINT fk_gtms_srs FOREIGN KEY (srs_id) REFERENCES gpkg_spatial_ref_sys (srs_id))')
('table', 'AISVesselTracks2021', 'AISVesselTracks2021', 3668719, "CREATE TABLE [AISVesselTracks2021] ([OBJECTID] INTEGER primary key autoincrement not null, [Shape] MULTILINESTRING, [MMSI] MEDIUMINT check((typeof([MMSI]) = 'integer' or typeof([MMSI]) = 'null') and [MMSI] >= -2147483648 and [MMSI] <= 2147483647), [TrackStartTime] DATETIME check((typeof(TrackStartTime) = 'text' or typeof(TrackStartTime) = 'null') and strftime('%Y-%m-%dT%H:%M:%fZ',TrackStartTime)), [TrackEndTime] DATETIME check((typeof(TrackEndTime) = 'text' or typeof(TrackEndTime) = 'null') and strftime('%Y-%m-%dT%H:%M:%fZ',TrackEndTime)), [VesselType] MEDIUMINT check((typeof([VesselType]) = 'integer' or typeof([VesselType]) = 'null') and [VesselType] >= -2147483648 and [VesselType] <= 2147483647), [Length] DOUBLE check(typeof([Length]) = 'real' or typeof([Length]) = 'null'), [Width] DOUBLE check(typeof([Width]) = 'real' or typeof([Width]) = 'null'), [Draft] DOUBLE check(typeof([Draft]) = 'real' or typeof([Draft]) = 'null'), [DurationMinutes] MEDIUMINT check((typeof([DurationMinutes]) = 'integer' or typeof([DurationMinutes]) = 'null') and [DurationMinutes] >= -2147483648 and [DurationMinutes] <= 2147483647), [VesselGroup] TEXT(25) check((typeof([VesselGroup]) = 'text' or typeof([VesselGroup]) = 'null') and not length([VesselGroup]) > 25))")
('table', 'rtree_AISVesselTracks2021_Shape', 'rtree_AISVesselTracks2021_Shape', 0, 'CREATE VIRTUAL TABLE "rtree_AISVesselTracks2021_Shape" USING RTREE (id,minx,maxx,miny,maxy)')
('table', 'rtree_AISVesselTracks2021_Shape_rowid', 'rtree_AISVesselTracks2021_Shape_rowid', 166816, 'CREATE TABLE "rtree_AISVesselTracks2021_Shape_rowid"(rowid INTEGER PRIMARY KEY,nodeno)')
('table', 'rtree_AISVesselTracks2021_Shape_node', 'rtree_AISVesselTracks2021_Shape_node', 166817, 'CREATE TABLE "rtree_AISVesselTracks2021_Shape_node"(nodeno INTEGER PRIMARY KEY,data)')
('table', 'rtree_AISVesselTracks2021_Shape_parent', 'rtree_AISVesselTracks2021_Shape_parent', 166818, 'CREATE TABLE "rtree_AISVesselTracks2021_Shape_parent"(nodeno INTEGER PRIMARY KEY,parentnode)')

Schema for table 'AISVesselTracks2021':
Column name: OBJECTID, Data type: INTEGER
Column name: Shape, Data type: MULTILINESTRING
Column name: MMSI, Data type: MEDIUMINT
Column name: TrackStartTime, Data type: DATETIME
Column name: TrackEndTime, Data type: DATETIME
Column name: VesselType, Data type: MEDIUMINT
Column name: Length, Data type: DOUBLE
Column name: Width, Data type: DOUBLE
Column name: Draft, Data type: DOUBLE
Column name: DurationMinutes, Data type: MEDIUMINT
Column name: VesselGroup, Data type: TEXT(25)