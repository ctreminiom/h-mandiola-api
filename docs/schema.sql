/*=============================================================

VERSION:     1.0.0
DATE:        20/05/2019 00:22
SERVER:      (local)
DATABASE:    

	SCHEMAS:
		dbo, guest, db_owner, db_accessadmin, db_securityadmin, db_ddladmin, db_backupoperator, db_datareader, db_datawriter, db_denydatareader, db_denydatawriter, dev
	TABLES:
		roles, grants, users, activities, consecutives_types, clients, consecutives, rooms, rooms_types, products, products_types


=============================================================*/
BEGIN TRAN
GO

-- Create schema [dev]
Print 'Create schema [dev]'
GO
CREATE SCHEMA [dev]
	AUTHORIZATION [dbo]
GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
SET ANSI_NULLS ON
SET QUOTED_IDENTIFIER ON

GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
-- Create table [dev].[consecutives_types]
Print 'Create table [dev].[consecutives_types]'
GO
CREATE TABLE [dev].[consecutives_types] (
		[ID]       [varchar](50) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		[name]     [varchar](4000) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		CONSTRAINT [consecutives_types_PK]
		PRIMARY KEY
		NONCLUSTERED
		([ID])
)
GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
ALTER TABLE [dev].[consecutives_types] SET (LOCK_ESCALATION = TABLE)
GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
SET ANSI_NULLS ON
SET QUOTED_IDENTIFIER ON

GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
-- Create table [dev].[products_types]
Print 'Create table [dev].[products_types]'
GO
CREATE TABLE [dev].[products_types] (
		[ID]       [varchar](50) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		[name]     [varchar](4000) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		CONSTRAINT [products_types_PK]
		PRIMARY KEY
		NONCLUSTERED
		([ID])
)
GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
ALTER TABLE [dev].[products_types] SET (LOCK_ESCALATION = TABLE)
GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
SET ANSI_NULLS ON
SET QUOTED_IDENTIFIER ON

GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
-- Create table [dev].[roles]
Print 'Create table [dev].[roles]'
GO
CREATE TABLE [dev].[roles] (
		[ID]       [varchar](50) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		[name]     [varchar](4000) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		CONSTRAINT [roles_PK]
		PRIMARY KEY
		NONCLUSTERED
		([ID])
)
GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
ALTER TABLE [dev].[roles] SET (LOCK_ESCALATION = TABLE)
GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
SET ANSI_NULLS ON
SET QUOTED_IDENTIFIER ON

GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
-- Create table [dev].[rooms_types]
Print 'Create table [dev].[rooms_types]'
GO
CREATE TABLE [dev].[rooms_types] (
		[ID]              [varchar](50) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		[name]            [varchar](4000) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		[description]     [varchar](4000) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		CONSTRAINT [rooms_types_PK]
		PRIMARY KEY
		NONCLUSTERED
		([ID])
)
GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
ALTER TABLE [dev].[rooms_types] SET (LOCK_ESCALATION = TABLE)
GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
SET ANSI_NULLS ON
SET QUOTED_IDENTIFIER ON

GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
-- Create table [dev].[users]
Print 'Create table [dev].[users]'
GO
CREATE TABLE [dev].[users] (
		[ID]                    [varchar](50) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		[username]              [varchar](4000) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		[email]                 [varchar](4000) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		[password]              [varchar](4000) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		[security_question]     [varchar](4000) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		[security_answer]       [varchar](4000) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		CONSTRAINT [users_PK]
		PRIMARY KEY
		NONCLUSTERED
		([ID])
)
GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
-- Create index username_AK on [dev].[users]
Print 'Create index username_AK on [dev].[users]'
GO
CREATE UNIQUE NONCLUSTERED INDEX [username_AK]
	ON [dev].[users] ([username])
GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
-- Create index email_AK on [dev].[users]
Print 'Create index email_AK on [dev].[users]'
GO
CREATE UNIQUE NONCLUSTERED INDEX [email_AK]
	ON [dev].[users] ([email])
GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
ALTER TABLE [dev].[users] SET (LOCK_ESCALATION = TABLE)
GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
SET ANSI_NULLS ON
SET QUOTED_IDENTIFIER ON

GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
-- Create table [dev].[consecutives]
Print 'Create table [dev].[consecutives]'
GO
CREATE TABLE [dev].[consecutives] (
		[ID]              [varchar](50) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		[type]            [varchar](50) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		[description]     [varchar](4000) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		[has_prefix]      [varchar](4000) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		[prefix]          [varchar](4000) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		[has_range]       [varchar](4000) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		[initial]         [varchar](4000) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		[final]           [varchar](4000) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		[consecutive]     [varchar](4000) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		CONSTRAINT [consecutives_PK]
		PRIMARY KEY
		NONCLUSTERED
		([ID])
)
GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
ALTER TABLE [dev].[consecutives] SET (LOCK_ESCALATION = TABLE)
GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
SET ANSI_NULLS ON
SET QUOTED_IDENTIFIER ON

GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
-- Create table [dev].[grants]
Print 'Create table [dev].[grants]'
GO
CREATE TABLE [dev].[grants] (
		[ID]       [varchar](50) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		[user]     [varchar](50) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		[role]     [varchar](50) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		CONSTRAINT [grants_PK]
		PRIMARY KEY
		NONCLUSTERED
		([ID])
)
GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
ALTER TABLE [dev].[grants] SET (LOCK_ESCALATION = TABLE)
GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
SET ANSI_NULLS ON
SET QUOTED_IDENTIFIER ON

GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
-- Create table [dev].[activities]
Print 'Create table [dev].[activities]'
GO
CREATE TABLE [dev].[activities] (
		[ID]              [varchar](50) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		[consecutive]     [varchar](50) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		[name]            [varchar](4000) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		[description]     [varchar](4000) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		[image_path]      [varchar](4000) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		CONSTRAINT [activities_PK]
		PRIMARY KEY
		NONCLUSTERED
		([ID])
)
GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
ALTER TABLE [dev].[activities] SET (LOCK_ESCALATION = TABLE)
GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
SET ANSI_NULLS ON
SET QUOTED_IDENTIFIER ON

GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
-- Create table [dev].[clients]
Print 'Create table [dev].[clients]'
GO
CREATE TABLE [dev].[clients] (
		[ID]              [varchar](50) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		[consecutive]     [varchar](50) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		[first_name]      [varchar](4000) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		[last_names]      [varchar](4000) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		[email]           [varchar](4000) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		[username]        [varchar](4000) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		[password]        [varchar](4000) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		[oauth_token]     [varchar](4000) COLLATE Latin1_General_CI_AS_KS_WS NULL,
		CONSTRAINT [clients_PK]
		PRIMARY KEY
		NONCLUSTERED
		([ID])
)
GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
-- Create index email_AK on [dev].[clients]
Print 'Create index email_AK on [dev].[clients]'
GO
CREATE UNIQUE NONCLUSTERED INDEX [email_AK]
	ON [dev].[clients] ([email])
GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
-- Create index username_AK on [dev].[clients]
Print 'Create index username_AK on [dev].[clients]'
GO
CREATE UNIQUE NONCLUSTERED INDEX [username_AK]
	ON [dev].[clients] ([username])
GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
ALTER TABLE [dev].[clients] SET (LOCK_ESCALATION = TABLE)
GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
SET ANSI_NULLS ON
SET QUOTED_IDENTIFIER ON

GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
-- Create table [dev].[products]
Print 'Create table [dev].[products]'
GO
CREATE TABLE [dev].[products] (
		[ID]              [varchar](50) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		[consecutive]     [varchar](50) COLLATE Latin1_General_CI_AS_KS_WS NULL,
		[type]            [varchar](50) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		[name]            [varchar](4000) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		[descrption]      [varchar](4000) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		[price]           [varchar](4000) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		[inventory]       [varchar](4000) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		CONSTRAINT [productos_PK]
		PRIMARY KEY
		NONCLUSTERED
		([ID])
)
GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
ALTER TABLE [dev].[products] SET (LOCK_ESCALATION = TABLE)
GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
SET ANSI_NULLS ON
SET QUOTED_IDENTIFIER ON

GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
-- Create table [dev].[rooms]
Print 'Create table [dev].[rooms]'
GO
CREATE TABLE [dev].[rooms] (
		[ID]              [varchar](50) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		[consecutive]     [varchar](50) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		[type]            [varchar](50) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		[number]          [varchar](4000) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		[description]     [varchar](4000) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		[image_path]      [varchar](4000) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		[available]       [varchar](4000) COLLATE Latin1_General_CI_AS_KS_WS NOT NULL,
		CONSTRAINT [rooms_PK]
		PRIMARY KEY
		NONCLUSTERED
		([ID])
)
GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
ALTER TABLE [dev].[rooms] SET (LOCK_ESCALATION = TABLE)
GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
-- Create foreign key activities_consecutives_FK on [dev].[activities]
Print 'Create foreign key activities_consecutives_FK on [dev].[activities]'
GO
ALTER TABLE [dev].[activities]
	WITH CHECK
	ADD CONSTRAINT [activities_consecutives_FK]
	FOREIGN KEY ([consecutive]) REFERENCES [dev].[consecutives] ([ID])
ALTER TABLE [dev].[activities]
	CHECK CONSTRAINT [activities_consecutives_FK]

GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
-- Create foreign key clients_consecutives_FK on [dev].[clients]
Print 'Create foreign key clients_consecutives_FK on [dev].[clients]'
GO
ALTER TABLE [dev].[clients]
	WITH CHECK
	ADD CONSTRAINT [clients_consecutives_FK]
	FOREIGN KEY ([consecutive]) REFERENCES [dev].[consecutives] ([ID])
ALTER TABLE [dev].[clients]
	CHECK CONSTRAINT [clients_consecutives_FK]

GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
-- Create foreign key consecutives_consecutives_types_FK on [dev].[consecutives]
Print 'Create foreign key consecutives_consecutives_types_FK on [dev].[consecutives]'
GO
ALTER TABLE [dev].[consecutives]
	WITH CHECK
	ADD CONSTRAINT [consecutives_consecutives_types_FK]
	FOREIGN KEY ([type]) REFERENCES [dev].[consecutives_types] ([ID])
ALTER TABLE [dev].[consecutives]
	CHECK CONSTRAINT [consecutives_consecutives_types_FK]

GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
-- Create foreign key grants_users_FK on [dev].[grants]
Print 'Create foreign key grants_users_FK on [dev].[grants]'
GO
ALTER TABLE [dev].[grants]
	WITH CHECK
	ADD CONSTRAINT [grants_users_FK]
	FOREIGN KEY ([user]) REFERENCES [dev].[users] ([ID])
ALTER TABLE [dev].[grants]
	CHECK CONSTRAINT [grants_users_FK]

GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
-- Create foreign key grants_roles_FK on [dev].[grants]
Print 'Create foreign key grants_roles_FK on [dev].[grants]'
GO
ALTER TABLE [dev].[grants]
	WITH CHECK
	ADD CONSTRAINT [grants_roles_FK]
	FOREIGN KEY ([role]) REFERENCES [dev].[roles] ([ID])
ALTER TABLE [dev].[grants]
	CHECK CONSTRAINT [grants_roles_FK]

GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
-- Create foreign key productos_consecutives_FK on [dev].[products]
Print 'Create foreign key productos_consecutives_FK on [dev].[products]'
GO
ALTER TABLE [dev].[products]
	WITH CHECK
	ADD CONSTRAINT [productos_consecutives_FK]
	FOREIGN KEY ([consecutive]) REFERENCES [dev].[consecutives] ([ID])
ALTER TABLE [dev].[products]
	CHECK CONSTRAINT [productos_consecutives_FK]

GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
-- Create foreign key products_products_types_FK on [dev].[products]
Print 'Create foreign key products_products_types_FK on [dev].[products]'
GO
ALTER TABLE [dev].[products]
	WITH CHECK
	ADD CONSTRAINT [products_products_types_FK]
	FOREIGN KEY ([type]) REFERENCES [dev].[products_types] ([ID])
ALTER TABLE [dev].[products]
	CHECK CONSTRAINT [products_products_types_FK]

GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
-- Create foreign key rooms_consecutives_FK on [dev].[rooms]
Print 'Create foreign key rooms_consecutives_FK on [dev].[rooms]'
GO
ALTER TABLE [dev].[rooms]
	WITH CHECK
	ADD CONSTRAINT [rooms_consecutives_FK]
	FOREIGN KEY ([consecutive]) REFERENCES [dev].[consecutives] ([ID])
ALTER TABLE [dev].[rooms]
	CHECK CONSTRAINT [rooms_consecutives_FK]

GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO
-- Create foreign key rooms_rooms_types_FK on [dev].[rooms]
Print 'Create foreign key rooms_rooms_types_FK on [dev].[rooms]'
GO
ALTER TABLE [dev].[rooms]
	WITH CHECK
	ADD CONSTRAINT [rooms_rooms_types_FK]
	FOREIGN KEY ([type]) REFERENCES [dev].[rooms_types] ([ID])
ALTER TABLE [dev].[rooms]
	CHECK CONSTRAINT [rooms_rooms_types_FK]

GO

IF @@ERROR<>0 OR @@TRANCOUNT=0 BEGIN IF @@TRANCOUNT>0 ROLLBACK SET NOEXEC ON END
GO

IF @@TRANCOUNT>0
	COMMIT

SET NOEXEC OFF
GO

