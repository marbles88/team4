Tables:
st_spatial_reference_systems
st_aux_spatial_reference_systems
sqlite_sequence
st_geometry_columns
st_vtspindex_interface
AISVesselTracks2022
st_spindexAISVesselTracks2022_Shape
st_spindexAISVesselTracks2022_Shape_rowid
st_spindexAISVesselTracks2022_Shape_node
st_spindexAISVesselTracks2022_Shape_parent

Table Details:
('table', 'st_spatial_reference_systems', 'st_spatial_reference_systems', 0, 'CREATE VIRTUAL TABLE st_spatial_reference_systems USING VSRS()')
('table', 'st_aux_spatial_reference_systems', 'st_aux_spatial_reference_systems', 2, 'CREATE TABLE st_aux_spatial_reference_systems (srid           INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, auth_name      text(256), auth_srid      int32, srtext         text(2048), falsex         float64 NOT NULL, falsey         float64 NOT NULL, xyunits        float64 NOT NULL, falsez         float64 DEFAULT 0.0, zunits         float64 DEFAULT 1.0, falsem         float64 DEFAULT 0.0, munits         float64 DEFAULT 1.0, xycluster_tol  float64, zcluster_tol   float64, mcluster_tol   float64, object_flags   int32 DEFAULT 1)')
('table', 'sqlite_sequence', 'sqlite_sequence', 3, 'CREATE TABLE sqlite_sequence(name,seq)')
('table', 'st_geometry_columns', 'st_geometry_columns', 4, 'CREATE TABLE st_geometry_columns (gcid               INTEGER PRIMARY KEY AUTOINCREMENT, f_table_name       clob NOT NULL, f_geometry_column  clob NOT NULL, geometry_type      int32, coord_dimension    int32, srid               int32 NOT NULL, spatial_index_type clob,CONSTRAINT gc_uk UNIQUE (f_table_name,f_geometry_column))')
('table', 'st_vtspindex_interface', 'st_vtspindex_interface', 0, 'CREATE VIRTUAL TABLE st_vtspindex_interface USING VTSpindex()')
('table', 'AISVesselTracks2022', 'AISVesselTracks2022', 6, "CREATE TABLE [AISVesselTracks2022] (OBJECTID integer primary key autoincrement not null, Shape geometryblob check((typeof(Shape) = 'blob' and length(Shape) >= 18 and cast(hex(substr(Shape,1,1)) as integer) = 64) or typeof(Shape) = 'null'), MMSI int32 check((typeof(MMSI) = 'integer' or typeof(MMSI) = 'null') and MMSI >= -2147483648 and MMSI <= 2147483647), TrackStartTime realdate check((typeof(TrackStartTime) = 'real' or typeof(TrackStartTime) = 'null') and TrackStartTime >= 0.0), TrackEndTime realdate check((typeof(TrackEndTime) = 'real' or typeof(TrackEndTime) = 'null') and TrackEndTime >= 0.0), VesselType int32 check((typeof(VesselType) = 'integer' or typeof(VesselType) = 'null') and VesselType >= -2147483648 and VesselType <= 2147483647), Length float64 check(typeof(Length) = 'real' or typeof(Length) = 'null'), Width float64 check(typeof(Width) = 'real' or typeof(Width) = 'null'), Draft float64 check(typeof(Draft) = 'real' or typeof(Draft) = 'null'), DurationMinutes int32 check((typeof(DurationMinutes) = 'integer' or typeof(DurationMinutes) = 'null') and DurationMinutes >= -2147483648 and DurationMinutes <= 2147483647), VesselGroup text(25) check((typeof(VesselGroup) = 'text' or typeof(VesselGroup) = 'null') and not length(VesselGroup) > 25))")
('table', 'st_spindex__AISVesselTracks2022_Shape', 'st_spindex__AISVesselTracks2022_Shape', 0, 'CREATE VIRTUAL TABLE [st_spindex__AISVesselTracks2022_Shape] USING RTREE (pkid,minx,maxx,miny,maxy)')
('table', 'st_spindex__AISVesselTracks2022_Shape_rowid', 'st_spindex__AISVesselTracks2022_Shape_rowid', 1703165, 'CREATE TABLE "st_spindex__AISVesselTracks2022_Shape_rowid"(rowid INTEGER PRIMARY KEY,nodeno)')
('table', 'st_spindex__AISVesselTracks2022_Shape_node', 'st_spindex__AISVesselTracks2022_Shape_node', 1703166, 'CREATE TABLE "st_spindex__AISVesselTracks2022_Shape_node"(nodeno INTEGER PRIMARY KEY,data)')
('table', 'st_spindex__AISVesselTracks2022_Shape_parent', 'st_spindex__AISVesselTracks2022_Shape_parent', 1703167, 'CREATE TABLE "st_spindex__AISVesselTracks2022_Shape_parent"(nodeno INTEGER PRIMARY KEY,parentnode)')


Schema for table 'st_aux_spatial_reference_systems':
Column name: srid, Data type: INTEGER
Column name: auth_name, Data type: text(256)
Column name: auth_srid, Data type: int32
Column name: srtext, Data type: text(2048)
Column name: falsex, Data type: float64
Column name: falsey, Data type: float64
Column name: xyunits, Data type: float64
Column name: falsez, Data type: float64
Column name: zunits, Data type: float64
Column name: falsem, Data type: float64
Column name: munits, Data type: float64
Column name: xycluster_tol, Data type: float64
Column name: zcluster_tol, Data type: float64
Column name: mcluster_tol, Data type: float64
Column name: object_flags, Data type: int32

Schema for table 'sqlite_sequence':
Column name: name, Data type: 
Column name: seq, Data type: 

Schema for table 'st_geometry_columns':
Column name: gcid, Data type: INTEGER
Column name: f_table_name, Data type: clob
Column name: f_geometry_column, Data type: clob
Column name: geometry_type, Data type: int32
Column name: coord_dimension, Data type: int32
Column name: srid, Data type: int32
Column name: spatial_index_type, Data type: clob

Schema for table 'AISVesselTracks2022':
Column name: OBJECTID, Data type: INTEGER
Column name: Shape, Data type: geometryblob
Column name: MMSI, Data type: int32
Column name: TrackStartTime, Data type: realdate
Column name: TrackEndTime, Data type: realdate
Column name: VesselType, Data type: int32
Column name: Length, Data type: float64
Column name: Width, Data type: float64
Column name: Draft, Data type: float64
Column name: DurationMinutes, Data type: int32
Column name: VesselGroup, Data type: text(25)

## bl_vessel_dates_2022

[    [319133800, [        ('2022-01-01', '21:48:20'),        ('2022-01-02', '02:37:39'),        ('2022-01-02', '03:11:50'),        ('2022-01-02', '04:01:10'),        ('2022-01-02', '04:58:59'),        ('2022-01-02', '06:11:10'),        ('2022-01-02', '09:19:50'),        ('2022-01-02', '09:59:39'),        ('2022-03-10', '22:48:01'),        ('2022-03-10', '22:55:37'),        ('2022-03-10', '23:13:37'),        ('2022-03-11', '13:06:07')    ]],
    [477237100, [        ('2022-12-26', '02:43:40'),        ('2022-12-26', '05:31:40'),        ('2022-12-26', '10:51:39'),        ('2022-12-26', '11:17:10'),        ('2022-12-27', '06:04:59'),        ('2022-12-27', '06:37:20'),        ('2022-12-27', '07:07:39'),        ('2022-12-27', '07:28:00'),        ('2022-12-27', '08:01:59'),        ('2022-12-27', '08:38:19'),        ('2022-12-27', '08:56:00'),        ('2022-12-27', '09:54:50'),        ('2022-12-27', '10:08:33'),        ('2022-12-27', '11:10:01'),        ('2022-12-27', '13:07:00'),        ('2022-12-27', '13:32:19'),        ('2022-12-27', '14:17:50'),        ('2022-12-27', '15:04:29'),        ('2022-12-27', '18:51:16'),        ('2022-12-27', '19:15:59'),        ('2022-12-27', '20:45:36'),        ('2022-12-27', '21:37:53'),        ('2022-12-28', '00:16:19'),        ('2022-12-28', '01:03:30')    ]]
]
