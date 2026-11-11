-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 09/11/2026 às 17:43
-- Versão do servidor: 10.4.32-MariaDB
-- Versão do PHP: 8.1.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `passaporte_sulamericano`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `pais`
--

CREATE TABLE `pais` (
  `id_pais` int(11) NOT NULL,
  `nome` varchar(80) NOT NULL,
  `codigo_iso2` char(2) NOT NULL,
  `codigo_iso3` char(3) NOT NULL,
  `capital` varchar(100) DEFAULT NULL,
  `tipo_localidade` varchar(20) NOT NULL,
  `latitude_referencia` decimal(9,6) DEFAULT NULL,
  `longitude_referencia` decimal(9,6) DEFAULT NULL,
  `bandeira_url` varchar(500) DEFAULT NULL,
  `codigo_mapa` varchar(20) NOT NULL,
  `ativo` tinyint(1) NOT NULL DEFAULT 1,
  `cadastrado_em` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `pais`
--

INSERT INTO `pais` (`id_pais`, `nome`, `codigo_iso2`, `codigo_iso3`, `capital`, `tipo_localidade`, `latitude_referencia`, `longitude_referencia`, `bandeira_url`, `codigo_mapa`, `ativo`, `cadastrado_em`) VALUES
(1, 'Argentina', 'AR', 'ARG', 'Buenos Aires', 'PAIS', -34.603700, -58.381600, NULL, 'ARG', 1, '2026-11-09 13:42:52'),
(2, 'Bolívia', 'BO', 'BOL', 'Sucre', 'PAIS', -19.019600, -65.261900, NULL, 'BOL', 1, '2026-11-09 13:42:52'),
(3, 'Brasil', 'BR', 'BRA', 'Brasília', 'PAIS', -15.793900, -47.882800, NULL, 'BRA', 1, '2026-11-09 13:42:52'),
(4, 'Chile', 'CL', 'CHL', 'Santiago', 'PAIS', -33.448900, -70.669300, NULL, 'CHL', 1, '2026-11-09 13:42:52'),
(5, 'Colômbia', 'CO', 'COL', 'Bogotá', 'PAIS', 4.711000, -74.072100, NULL, 'COL', 1, '2026-11-09 13:42:52'),
(6, 'Equador', 'EC', 'ECU', 'Quito', 'PAIS', -0.180700, -78.467800, NULL, 'ECU', 1, '2026-11-09 13:42:52'),
(7, 'Guiana', 'GY', 'GUY', 'Georgetown', 'PAIS', 6.801300, -58.155100, NULL, 'GUY', 1, '2026-11-09 13:42:52'),
(8, 'Paraguai', 'PY', 'PRY', 'Assunção', 'PAIS', -25.263700, -57.575900, NULL, 'PRY', 1, '2026-11-09 13:42:52'),
(9, 'Peru', 'PE', 'PER', 'Lima', 'PAIS', -12.046400, -77.042800, NULL, 'PER', 1, '2026-11-09 13:42:52'),
(10, 'Suriname', 'SR', 'SUR', 'Paramaribo', 'PAIS', 5.852000, -55.203800, NULL, 'SUR', 1, '2026-11-09 13:42:52'),
(11, 'Uruguai', 'UY', 'URY', 'Montevidéu', 'PAIS', -34.901100, -56.164500, NULL, 'URY', 1, '2026-11-09 13:42:52'),
(12, 'Venezuela', 'VE', 'VEN', 'Caracas', 'PAIS', 10.480600, -66.903600, NULL, 'VEN', 1, '2026-11-09 13:42:52'),
(13, 'Guiana Francesa', 'GF', 'GUF', 'Caiena', 'TERRITORIO', 4.922400, -52.313500, NULL, 'GUF', 1, '2026-11-09 13:42:52');

-- --------------------------------------------------------

--
-- Estrutura para tabela `usuario`
--

CREATE TABLE `usuario` (
  `id_usuario` int(11) NOT NULL,
  `nome` varchar(100) NOT NULL,
  `nome_usuario` varchar(40) NOT NULL,
  `email` varchar(150) NOT NULL,
  `senha_hash` varchar(255) NOT NULL,
  `foto_perfil_url` varchar(500) DEFAULT NULL,
  `biografia` varchar(300) DEFAULT NULL,
  `data_cadastro` datetime NOT NULL DEFAULT current_timestamp(),
  `ultimo_acesso` datetime DEFAULT NULL,
  `ativo` tinyint(1) NOT NULL DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `visita`
--

CREATE TABLE `visita` (
  `id_visita` int(11) NOT NULL,
  `id_usuario` int(11) NOT NULL,
  `id_pais` int(11) NOT NULL,
  `data_inicio` date NOT NULL,
  `data_fim` date DEFAULT NULL,
  `cidade_principal` varchar(100) DEFAULT NULL,
  `motivo_viagem` varchar(60) DEFAULT NULL,
  `meio_transporte` varchar(40) DEFAULT NULL,
  `avaliacao` tinyint(4) DEFAULT NULL,
  `observacao` varchar(500) DEFAULT NULL,
  `custo_estimado` decimal(10,2) DEFAULT NULL,
  `moeda` char(3) DEFAULT NULL,
  `criada_em` datetime NOT NULL DEFAULT current_timestamp(),
  `atualizada_em` datetime NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `pais`
--
ALTER TABLE `pais`
  ADD PRIMARY KEY (`id_pais`),
  ADD UNIQUE KEY `codigo_iso2` (`codigo_iso2`),
  ADD UNIQUE KEY `codigo_iso3` (`codigo_iso3`),
  ADD UNIQUE KEY `codigo_mapa` (`codigo_mapa`);

--
-- Índices de tabela `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`id_usuario`),
  ADD UNIQUE KEY `nome_usuario` (`nome_usuario`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Índices de tabela `visita`
--
ALTER TABLE `visita`
  ADD PRIMARY KEY (`id_visita`),
  ADD KEY `fk_visita_usuario` (`id_usuario`),
  ADD KEY `fk_visita_pais` (`id_pais`);

--
-- AUTO_INCREMENT para tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `pais`
--
ALTER TABLE `pais`
  MODIFY `id_pais` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT de tabela `usuario`
--
ALTER TABLE `usuario`
  MODIFY `id_usuario` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `visita`
--
ALTER TABLE `visita`
  MODIFY `id_visita` int(11) NOT NULL AUTO_INCREMENT;

--
-- Restrições para tabelas despejadas
--

--
-- Restrições para tabelas `visita`
--
ALTER TABLE `visita`
  ADD CONSTRAINT `fk_visita_pais` FOREIGN KEY (`id_pais`) REFERENCES `pais` (`id_pais`),
  ADD CONSTRAINT `fk_visita_usuario` FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id_usuario`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
