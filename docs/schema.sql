/*=============================================================

VERSION:     1.0.0
DATE:        20/05/2019 00:22
SERVER:      (local)
DATABASE:    

	SCHEMAS:
		dbo, guest, db_owner, db_accessadmin, db_securityadmin, db_ddladmin, db_backupoperator, db_datareader, db_datawriter, db_denydatareader, db_denydatawriter, dev2
	TABLES:
		roles, grants, users, activities, consecutives_types, clients, consecutives, rooms, rooms_types, products, products_types


=============================================================*/
BEGIN TRAN
GO

-- Create schema [dev2]
Print 'Create schema [dev2]'
GO
CREATE SCHEMA [dev2]
	AUTHORIZATION [dbo]
GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
SET ANSI_NULLS ON
SET QUOTED_IDENTIFIER ON

GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
-- Create table [dev2].[consecutives_types]
Print 'Create table [dev2].[consecutives_types]'
GO
CREATE TABLE [dev2].[consecutives_types] (
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
ALTER TABLE [dev2].[consecutives_types] SET (LOCK_ESCALATION = TABLE)
GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
SET ANSI_NULLS ON
SET QUOTED_IDENTIFIER ON

GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
-- Create table [dev2].[products_types]
Print 'Create table [dev2].[products_types]'
GO
CREATE TABLE [dev2].[products_types] (
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
ALTER TABLE [dev2].[products_types] SET (LOCK_ESCALATION = TABLE)
GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
SET ANSI_NULLS ON
SET QUOTED_IDENTIFIER ON

GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
-- Create table [dev2].[roles]
Print 'Create table [dev2].[roles]'
GO
CREATE TABLE [dev2].[roles] (
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
ALTER TABLE [dev2].[roles] SET (LOCK_ESCALATION = TABLE)
GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
SET ANSI_NULLS ON
SET QUOTED_IDENTIFIER ON

GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
-- Create table [dev2].[rooms_types]
Print 'Create table [dev2].[rooms_types]'
GO
CREATE TABLE [dev2].[rooms_types] (
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
ALTER TABLE [dev2].[rooms_types] SET (LOCK_ESCALATION = TABLE)
GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
SET ANSI_NULLS ON
SET QUOTED_IDENTIFIER ON

GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
-- Create table [dev2].[users]
Print 'Create table [dev2].[users]'
GO
CREATE TABLE [dev2].[users] (
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
-- Create index username_AK on [dev2].[users]
Print 'Create index username_AK on [dev2].[users]'
GO
CREATE UNIQUE NONCLUSTERED INDEX [username_AK]
	ON [dev2].[users] ([username])
GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
-- Create index email_AK on [dev2].[users]
Print 'Create index email_AK on [dev2].[users]'
GO
CREATE UNIQUE NONCLUSTERED INDEX [email_AK]
	ON [dev2].[users] ([email])
GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
ALTER TABLE [dev2].[users] SET (LOCK_ESCALATION = TABLE)
GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
SET ANSI_NULLS ON
SET QUOTED_IDENTIFIER ON

GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
-- Create table [dev2].[consecutives]
Print 'Create table [dev2].[consecutives]'
GO
CREATE TABLE [dev2].[consecutives] (
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
ALTER TABLE [dev2].[consecutives] SET (LOCK_ESCALATION = TABLE)
GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
SET ANSI_NULLS ON
SET QUOTED_IDENTIFIER ON

GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
-- Create table [dev2].[grants]
Print 'Create table [dev2].[grants]'
GO
CREATE TABLE [dev2].[grants] (
		[ID]       [varchar](1700) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		[user]     [varchar](1700) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		[role]     [varchar](1700) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		CONSTRAINT [grants_PK]
		PRIMARY KEY
		NONCLUSTERED
		([ID])
)
GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
ALTER TABLE [dev2].[grants] SET (LOCK_ESCALATION = TABLE)
GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
SET ANSI_NULLS ON
SET QUOTED_IDENTIFIER ON

GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
-- Create table [dev2].[activities]
Print 'Create table [dev2].[activities]'
GO
CREATE TABLE [dev2].[activities] (
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
ALTER TABLE [dev2].[activities] SET (LOCK_ESCALATION = TABLE)
GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
SET ANSI_NULLS ON
SET QUOTED_IDENTIFIER ON

GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
-- Create table [dev2].[clients]
Print 'Create table [dev2].[clients]'
GO
CREATE TABLE [dev2].[clients] (
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
-- Create index email_AK on [dev2].[clients]
Print 'Create index email_AK on [dev2].[clients]'
GO
CREATE UNIQUE NONCLUSTERED INDEX [email_AK]
	ON [dev2].[clients] ([email])
GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
-- Create index username_AK on [dev2].[clients]
Print 'Create index username_AK on [dev2].[clients]'
GO
CREATE UNIQUE NONCLUSTERED INDEX [username_AK]
	ON [dev2].[clients] ([username])
GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
ALTER TABLE [dev2].[clients] SET (LOCK_ESCALATION = TABLE)
GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
SET ANSI_NULLS ON
SET QUOTED_IDENTIFIER ON

GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
-- Create table [dev2].[products]
Print 'Create table [dev2].[products]'
GO
CREATE TABLE [dev2].[products] (
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
ALTER TABLE [dev2].[products] SET (LOCK_ESCALATION = TABLE)
GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
SET ANSI_NULLS ON
SET QUOTED_IDENTIFIER ON

GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
-- Create table [dev2].[rooms]
Print 'Create table [dev2].[rooms]'
GO
CREATE TABLE [dev2].[rooms] (
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
ALTER TABLE [dev2].[rooms] SET (LOCK_ESCALATION = TABLE)
GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
-- Create foreign key activities_consecutives_FK on [dev2].[activities]
Print 'Create foreign key activities_consecutives_FK on [dev2].[activities]'
GO
ALTER TABLE [dev2].[activities]
	WITH CHECK
	ADD CONSTRAINT [activities_consecutives_FK]
	FOREIGN KEY ([consecutive]) REFERENCES [dev2].[consecutives] ([ID])
ALTER TABLE [dev2].[activities]
	CHECK CONSTRAINT [activities_consecutives_FK]

GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
-- Create foreign key clients_consecutives_FK on [dev2].[clients]
Print 'Create foreign key clients_consecutives_FK on [dev2].[clients]'
GO
ALTER TABLE [dev2].[clients]
	WITH CHECK
	ADD CONSTRAINT [clients_consecutives_FK]
	FOREIGN KEY ([consecutive]) REFERENCES [dev2].[consecutives] ([ID])
ALTER TABLE [dev2].[clients]
	CHECK CONSTRAINT [clients_consecutives_FK]

GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
-- Create foreign key consecutives_consecutives_types_FK on [dev2].[consecutives]
Print 'Create foreign key consecutives_consecutives_types_FK on [dev2].[consecutives]'
GO
ALTER TABLE [dev2].[consecutives]
	WITH CHECK
	ADD CONSTRAINT [consecutives_consecutives_types_FK]
	FOREIGN KEY ([type]) REFERENCES [dev2].[consecutives_types] ([ID])
ALTER TABLE [dev2].[consecutives]
	CHECK CONSTRAINT [consecutives_consecutives_types_FK]

GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
-- Create foreign key grants_users_FK on [dev2].[grants]
Print 'Create foreign key grants_users_FK on [dev2].[grants]'
GO
ALTER TABLE [dev2].[grants]
	WITH CHECK
	ADD CONSTRAINT [grants_users_FK]
	FOREIGN KEY ([user]) REFERENCES [dev2].[users] ([ID])
ALTER TABLE [dev2].[grants]
	CHECK CONSTRAINT [grants_users_FK]

GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
-- Create foreign key grants_roles_FK on [dev2].[grants]
Print 'Create foreign key grants_roles_FK on [dev2].[grants]'
GO
ALTER TABLE [dev2].[grants]
	WITH CHECK
	ADD CONSTRAINT [grants_roles_FK]
	FOREIGN KEY ([role]) REFERENCES [dev2].[roles] ([ID])
ALTER TABLE [dev2].[grants]
	CHECK CONSTRAINT [grants_roles_FK]

GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
-- Create foreign key productos_consecutives_FK on [dev2].[products]
Print 'Create foreign key productos_consecutives_FK on [dev2].[products]'
GO
ALTER TABLE [dev2].[products]
	WITH CHECK
	ADD CONSTRAINT [productos_consecutives_FK]
	FOREIGN KEY ([consecutive]) REFERENCES [dev2].[consecutives] ([ID])
ALTER TABLE [dev2].[products]
	CHECK CONSTRAINT [productos_consecutives_FK]

GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
-- Create foreign key products_products_types_FK on [dev2].[products]
Print 'Create foreign key products_products_types_FK on [dev2].[products]'
GO
ALTER TABLE [dev2].[products]
	WITH CHECK
	ADD CONSTRAINT [products_products_types_FK]
	FOREIGN KEY ([type]) REFERENCES [dev2].[products_types] ([ID])
ALTER TABLE [dev2].[products]
	CHECK CONSTRAINT [products_products_types_FK]

GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
-- Create foreign key rooms_consecutives_FK on [dev2].[rooms]
Print 'Create foreign key rooms_consecutives_FK on [dev2].[rooms]'
GO
ALTER TABLE [dev2].[rooms]
	WITH CHECK
	ADD CONSTRAINT [rooms_consecutives_FK]
	FOREIGN KEY ([consecutive]) REFERENCES [dev2].[consecutives] ([ID])
ALTER TABLE [dev2].[rooms]
	CHECK CONSTRAINT [rooms_consecutives_FK]

GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
-- Create foreign key rooms_rooms_types_FK on [dev2].[rooms]
Print 'Create foreign key rooms_rooms_types_FK on [dev2].[rooms]'
GO
ALTER TABLE [dev2].[rooms]
	WITH CHECK
	ADD CONSTRAINT [rooms_rooms_types_FK]
	FOREIGN KEY ([type]) REFERENCES [dev2].[rooms_types] ([ID])
ALTER TABLE [dev2].[rooms]
	CHECK CONSTRAINT [rooms_rooms_types_FK]

GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO

IF @@TRANCOUNT>0
	COMMIT

SET NOEXEC OFF
GO

