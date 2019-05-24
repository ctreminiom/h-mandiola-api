/*=============================================================

VERSION:     1.0.0
DATE:        20/05/2019 00:22
SERVER:      (local)
DATABASE:    

	SCHEMAS:
		dbo, guest, db_owner, db_accessadmin, db_securityadmin, db_ddladmin, db_backupoperator, db_datareader, db_datawriter, db_denydatareader, db_denydatawriter, dba
	TABLES:
		roles, grants, users, activities, consecutives_types, clients, consecutives, rooms, rooms_types, products, products_types


=============================================================*/
BEGIN TRAN
GO

-- Create schema [dba]
Print 'Create schema [dba]'
GO
CREATE SCHEMA [dba]
	AUTHORIZATION [dbo]
GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
SET ANSI_NULLS ON
SET QUOTED_IDENTIFIER ON

GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
-- Create table [dba].[consecutives_types]
Print 'Create table [dba].[consecutives_types]'
GO
CREATE TABLE [dba].[consecutives_types] (
		[ID]       [varchar](1700) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		[name]     [varchar](8000) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		CONSTRAINT [consecutives_types_PK]
		PRIMARY KEY
		NONCLUSTERED
		([ID])
)
GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
ALTER TABLE [dba].[consecutives_types] SET (LOCK_ESCALATION = TABLE)
GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
SET ANSI_NULLS ON
SET QUOTED_IDENTIFIER ON

GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
-- Create table [dba].[products_types]
Print 'Create table [dba].[products_types]'
GO
CREATE TABLE [dba].[products_types] (
		[ID]       [varchar](1700) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		[name]     [varchar](8000) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		CONSTRAINT [products_types_PK]
		PRIMARY KEY
		NONCLUSTERED
		([ID])
)
GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
ALTER TABLE [dba].[products_types] SET (LOCK_ESCALATION = TABLE)
GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
SET ANSI_NULLS ON
SET QUOTED_IDENTIFIER ON

GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
-- Create table [dba].[roles]
Print 'Create table [dba].[roles]'
GO
CREATE TABLE [dba].[roles] (
		[ID]       [varchar](1700) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		[name]     [varchar](8000) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		CONSTRAINT [roles_PK]
		PRIMARY KEY
		NONCLUSTERED
		([ID])
)
GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
ALTER TABLE [dba].[roles] SET (LOCK_ESCALATION = TABLE)
GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
SET ANSI_NULLS ON
SET QUOTED_IDENTIFIER ON

GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
-- Create table [dba].[rooms_types]
Print 'Create table [dba].[rooms_types]'
GO
CREATE TABLE [dba].[rooms_types] (
		[ID]              [varchar](1700) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		[name]            [varchar](8000) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		[description]     [varchar](8000) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		CONSTRAINT [rooms_types_PK]
		PRIMARY KEY
		NONCLUSTERED
		([ID])
)
GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
ALTER TABLE [dba].[rooms_types] SET (LOCK_ESCALATION = TABLE)
GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
SET ANSI_NULLS ON
SET QUOTED_IDENTIFIER ON

GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
-- Create table [dba].[users]
Print 'Create table [dba].[users]'
GO
CREATE TABLE [dba].[users] (
		[ID]                    [varchar](1700) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		[username]              [varchar](8000) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		[email]                 [varchar](8000) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		[password]              [varchar](8000) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		[security_question]     [varchar](8000) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		[security_answer]       [varchar](8000) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		CONSTRAINT [users_PK]
		PRIMARY KEY
		NONCLUSTERED
		([ID])
)
GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
-- Create index username_AK on [dba].[users]
Print 'Create index username_AK on [dba].[users]'
GO
CREATE UNIQUE NONCLUSTERED INDEX [username_AK]
	ON [dba].[users] ([username])
GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
-- Create index email_AK on [dba].[users]
Print 'Create index email_AK on [dba].[users]'
GO
CREATE UNIQUE NONCLUSTERED INDEX [email_AK]
	ON [dba].[users] ([email])
GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
ALTER TABLE [dba].[users] SET (LOCK_ESCALATION = TABLE)
GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
SET ANSI_NULLS ON
SET QUOTED_IDENTIFIER ON

GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
-- Create table [dba].[consecutives]
Print 'Create table [dba].[consecutives]'
GO
CREATE TABLE [dba].[consecutives] (
		[ID]              [varchar](1700) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		[type]            [varchar](1700) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		[description]     [varchar](8000) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		[has_prefix]      [varchar](8000) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		[prefix]          [varchar](8000) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		[has_range]       [varchar](8000) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		[initial]         [varchar](8000) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		[final]           [varchar](8000) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		[consecutive]     [varchar](8000) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		CONSTRAINT [consecutives_PK]
		PRIMARY KEY
		NONCLUSTERED
		([ID])
)
GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
ALTER TABLE [dba].[consecutives] SET (LOCK_ESCALATION = TABLE)
GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
SET ANSI_NULLS ON
SET QUOTED_IDENTIFIER ON

GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
-- Create table [dba].[grants]
Print 'Create table [dba].[grants]'
GO
CREATE TABLE [dba].[grants] (
		[ID]       [varchar](1700) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		[userID]     [varchar](1700) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		[roleID]     [varchar](1700) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		CONSTRAINT [grants_PK]
		PRIMARY KEY
		NONCLUSTERED
		([ID])
)
GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
ALTER TABLE [dba].[grants] SET (LOCK_ESCALATION = TABLE)
GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
SET ANSI_NULLS ON
SET QUOTED_IDENTIFIER ON

GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
-- Create table [dba].[activities]
Print 'Create table [dba].[activities]'
GO
CREATE TABLE [dba].[activities] (
		[ID]              [varchar](1700) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		[consecutive]     [varchar](1700) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		[name]            [varchar](8000) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		[description]     [varchar](8000) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		[image_path]      [varchar](8000) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		CONSTRAINT [activities_PK]
		PRIMARY KEY
		NONCLUSTERED
		([ID])
)
GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
ALTER TABLE [dba].[activities] SET (LOCK_ESCALATION = TABLE)
GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
SET ANSI_NULLS ON
SET QUOTED_IDENTIFIER ON

GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
-- Create table [dba].[clients]
Print 'Create table [dba].[clients]'
GO
CREATE TABLE [dba].[clients] (
		[ID]              [varchar](1700) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		[consecutive]     [varchar](1700) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		[first_name]      [varchar](8000) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		[last_names]      [varchar](8000) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		[email]           [varchar](8000) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		[username]        [varchar](8000) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		[password]        [varchar](8000) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		[oauth_token]     [varchar](8000) COLLATE Latin1_General_CI_AS_KS_WS NULL,
		CONSTRAINT [clients_PK]
		PRIMARY KEY
		NONCLUSTERED
		([ID])
)
GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
-- Create index email_AK on [dba].[clients]
Print 'Create index email_AK on [dba].[clients]'
GO
CREATE UNIQUE NONCLUSTERED INDEX [email_AK]
	ON [dba].[clients] ([email])
GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
-- Create index username_AK on [dba].[clients]
Print 'Create index username_AK on [dba].[clients]'
GO
CREATE UNIQUE NONCLUSTERED INDEX [username_AK]
	ON [dba].[clients] ([username])
GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
ALTER TABLE [dba].[clients] SET (LOCK_ESCALATION = TABLE)
GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
SET ANSI_NULLS ON
SET QUOTED_IDENTIFIER ON

GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
-- Create table [dba].[products]
Print 'Create table [dba].[products]'
GO
CREATE TABLE [dba].[products] (
		[ID]              [varchar](1700) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		[consecutive]     [varchar](1700) COLLATE Latin1_General_CI_AS_KS_WS NULL,
		[type]            [varchar](1700) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		[name]            [varchar](8000) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		[descrption]      [varchar](8000) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		[price]           [varchar](8000) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		[inventory]       [varchar](8000) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		CONSTRAINT [productos_PK]
		PRIMARY KEY
		NONCLUSTERED
		([ID])
)
GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
ALTER TABLE [dba].[products] SET (LOCK_ESCALATION = TABLE)
GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
SET ANSI_NULLS ON
SET QUOTED_IDENTIFIER ON

GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
-- Create table [dba].[rooms]
Print 'Create table [dba].[rooms]'
GO
CREATE TABLE [dba].[rooms] (
		[ID]              [varchar](1700) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		[consecutive]     [varchar](1700) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		[type]            [varchar](1700) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		[number]          [varchar](8000) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		[description]     [varchar](8000) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		[image_path]      [varchar](8000) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		[available]       [varchar](8000) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		CONSTRAINT [rooms_PK]
		PRIMARY KEY
		NONCLUSTERED
		([ID])
)
GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
ALTER TABLE [dba].[rooms] SET (LOCK_ESCALATION = TABLE)
GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
-- Create foreign key activities_consecutives_FK on [dba].[activities]
Print 'Create foreign key activities_consecutives_FK on [dba].[activities]'
GO
ALTER TABLE [dba].[activities]
	WITH CHECK
	ADD CONSTRAINT [activities_consecutives_FK]
	FOREIGN KEY ([consecutive]) REFERENCES [dba].[consecutives] ([ID])
ALTER TABLE [dba].[activities]
	CHECK CONSTRAINT [activities_consecutives_FK]

GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
-- Create foreign key clients_consecutives_FK on [dba].[clients]
Print 'Create foreign key clients_consecutives_FK on [dba].[clients]'
GO
ALTER TABLE [dba].[clients]
	WITH CHECK
	ADD CONSTRAINT [clients_consecutives_FK]
	FOREIGN KEY ([consecutive]) REFERENCES [dba].[consecutives] ([ID])
ALTER TABLE [dba].[clients]
	CHECK CONSTRAINT [clients_consecutives_FK]

GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
-- Create foreign key consecutives_consecutives_types_FK on [dba].[consecutives]
Print 'Create foreign key consecutives_consecutives_types_FK on [dba].[consecutives]'
GO
ALTER TABLE [dba].[consecutives]
	WITH CHECK
	ADD CONSTRAINT [consecutives_consecutives_types_FK]
	FOREIGN KEY ([type]) REFERENCES [dba].[consecutives_types] ([ID])
ALTER TABLE [dba].[consecutives]
	CHECK CONSTRAINT [consecutives_consecutives_types_FK]

GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
-- Create foreign key grants_users_FK on [dba].[grants]
Print 'Create foreign key grants_users_FK on [dba].[grants]'
GO
ALTER TABLE [dba].[grants]
	WITH CHECK
	ADD CONSTRAINT [grants_users_FK]
	FOREIGN KEY ([userID]) REFERENCES [dba].[users] ([ID])
ALTER TABLE [dba].[grants]
	CHECK CONSTRAINT [grants_users_FK]

GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
-- Create foreign key grants_roles_FK on [dba].[grants]
Print 'Create foreign key grants_roles_FK on [dba].[grants]'
GO
ALTER TABLE [dba].[grants]
	WITH CHECK
	ADD CONSTRAINT [grants_roles_FK]
	FOREIGN KEY ([roleID]) REFERENCES [dba].[roles] ([ID])
ALTER TABLE [dba].[grants]
	CHECK CONSTRAINT [grants_roles_FK]

GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
-- Create foreign key productos_consecutives_FK on [dba].[products]
Print 'Create foreign key productos_consecutives_FK on [dba].[products]'
GO
ALTER TABLE [dba].[products]
	WITH CHECK
	ADD CONSTRAINT [productos_consecutives_FK]
	FOREIGN KEY ([consecutive]) REFERENCES [dba].[consecutives] ([ID])
ALTER TABLE [dba].[products]
	CHECK CONSTRAINT [productos_consecutives_FK]

GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
-- Create foreign key products_products_types_FK on [dba].[products]
Print 'Create foreign key products_products_types_FK on [dba].[products]'
GO
ALTER TABLE [dba].[products]
	WITH CHECK
	ADD CONSTRAINT [products_products_types_FK]
	FOREIGN KEY ([type]) REFERENCES [dba].[products_types] ([ID])
ALTER TABLE [dba].[products]
	CHECK CONSTRAINT [products_products_types_FK]

GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
-- Create foreign key rooms_consecutives_FK on [dba].[rooms]
Print 'Create foreign key rooms_consecutives_FK on [dba].[rooms]'
GO
ALTER TABLE [dba].[rooms]
	WITH CHECK
	ADD CONSTRAINT [rooms_consecutives_FK]
	FOREIGN KEY ([consecutive]) REFERENCES [dba].[consecutives] ([ID])
ALTER TABLE [dba].[rooms]
	CHECK CONSTRAINT [rooms_consecutives_FK]

GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
-- Create foreign key rooms_rooms_types_FK on [dba].[rooms]
Print 'Create foreign key rooms_rooms_types_FK on [dba].[rooms]'
GO
ALTER TABLE [dba].[rooms]
	WITH CHECK
	ADD CONSTRAINT [rooms_rooms_types_FK]
	FOREIGN KEY ([type]) REFERENCES [dba].[rooms_types] ([ID])
ALTER TABLE [dba].[rooms]
	CHECK CONSTRAINT [rooms_rooms_types_FK]

GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO

IF @@TRANCOUNT>0
	COMMIT

SET NOEXEC OFF
GO

