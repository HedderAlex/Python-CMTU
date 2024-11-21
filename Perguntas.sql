--top 5 perguntas mais erradas
SELECT 
    TEXTO, 
    ERRO 
FROM 
    ATIVIDADE
ORDER BY 
    ERRO DESC 
LIMIT 5;

--top 5 perguntas mais acertadas
SELECT
    TEXTO, 
    ACERTO 
FROM 
    ATIVIDADE
ORDER BY 
    ACERTO DESC 
LIMIT 5;

--porcentagem de pessoas que conseguiu o certificado
SELECT 
    COUNT(*) AS Quantidade de usuarios
FROM 
    USUARIO
WHERE 
    STATUS = TRUE;

SELECT 
    COUNT(*) AS Quantidade de certificados
FROM 
    CERTIFICADO
WHERE 
    STATUS = TRUE;

--média das notas
SELECT 
    PORCENTAGEM_CONCLUIDO
FROM 
    USUARIO_MODULO
WHERE 
    STATUS = TRUE;

--porcentagem de módulos iniciados
SELECT
    COUNT(*) as Iniciado_modulos
FROM
    USUARIO_MODULO
WHERE
    STATUS = TRUE AND INICIADO = TRUE;

SELECT
    COUNT(*) as Total_modulos
FROM
    USUARIO_MODULO
WHERE
    STATUS = TRUE;