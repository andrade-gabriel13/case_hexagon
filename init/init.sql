-- Executa o comando de restauração da lista de arquivos
RESTORE FILELISTONLY FROM DISK = '/var/opt/mssql/backup/base_data.bak';
GO

-- Restaura o banco de dados usando os nomes lógicos dos arquivos
RESTORE DATABASE AdventureWorksLT2022
FROM DISK = '/var/opt/mssql/backup/base_data.bak'
WITH MOVE 'AdventureWorksLT2022_Data' TO '/var/opt/mssql/data/AdventureWorksLT2022.mdf',
     MOVE 'AdventureWorksLT2022_Log' TO '/var/opt/mssql/data/AdventureWorksLT2022_log.ldf';
GO
