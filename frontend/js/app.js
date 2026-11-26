// O endereço é calculado a partir deste arquivo para funcionar em todas as páginas.
const raizSite = new URL("../../", document.currentScript.src);

let usuario = null;
let paises = [];
let visitas = [];
let codigoSelecionado = "";
let idEmEdicao = null;
let documentoMapa = null;
let salvando = false;

const formularioVisita = document.getElementById("form-visita");
const seletorPais = document.getElementById("seletor-pais");

function endereco(caminho) {
  return new URL(caminho, raizSite).href;
}

function mostrarMensagem(texto, tipo = "sucesso") {
  const mensagem = document.getElementById("mensagem");
  mensagem.textContent = texto;
  mensagem.dataset.tipo = tipo;
}

async function consultarAPI(caminho, metodo = "GET", dados) {
  const opcoes = { method: metodo, credentials: "same-origin", cache: "no-store" };
  if (dados !== undefined) {
    opcoes.headers = { "Content-Type": "application/json" };
    opcoes.body = JSON.stringify(dados);
  }

  let resposta;
  try {
    resposta = await fetch(endereco(caminho), opcoes);
  } catch {
    throw new Error("Não foi possível conectar. Confira se o Flask e o banco estão ligados.");
  }
  if (resposta.status === 204) {
    return null;
  }
  if (!resposta.headers.get("content-type")?.includes("application/json")) {
    throw new Error("Abra o site pelo Flask em http://127.0.0.1:5000 para acessar o sistema.");
  }

  const resultado = await resposta.json();
  if (!resposta.ok) {
    const erro = new Error(resultado.erro || "Não foi possível concluir a operação.");
    erro.status = resposta.status;
    throw erro;
  }
  return resultado;
}

function formatarData(valor) {
  if (!valor) {
    return "Não informada";
  }
  const partes = valor.slice(0, 10).split("-");
  return partes.length === 3 ? partes.reverse().join("/") : valor;
}

function atualizarMapa() {
  if (!documentoMapa) {
    return;
  }
  const visitados = new Set(visitas.map(visita => visita.codigo_mapa));
  for (const elemento of documentoMapa.querySelectorAll("[data-pais]")) {
    const codigo = elemento.dataset.pais;
    const visitado = visitados.has(codigo);
    const pais = paises.find(item => item.codigo_mapa === codigo);
    elemento.classList.toggle("visitado", visitado);
    elemento.classList.toggle("selecionado", codigo === codigoSelecionado);
    elemento.setAttribute("aria-pressed", String(codigo === codigoSelecionado));
    if (pais) {
      elemento.setAttribute("aria-label", pais.nome + (visitado ? ", visitado" : ""));
    }
  }
}

function registrarEventosMapa() {
  const objeto = document.getElementById("mapa-svg");
  if (!objeto) {
    return;
  }
  function prepararMapa() {
    const documento = objeto.contentDocument;
    if (!documento?.querySelector("[data-pais]") || documento === documentoMapa) {
      return;
    }
    documentoMapa = documento;
    for (const elemento of documento.querySelectorAll("[data-pais]")) {
      elemento.addEventListener("click", () => selecionarPais(elemento.dataset.pais));
      elemento.addEventListener("keydown", evento => {
        if (evento.key === "Enter" || evento.key === " ") {
          evento.preventDefault();
          selecionarPais(elemento.dataset.pais);
        }
      });
    }
    atualizarMapa();
  }
  objeto.addEventListener("load", prepararMapa);
  prepararMapa();
}

function atualizarBotaoVisita() {
  if (!formularioVisita) {
    return;
  }
  const botao = document.getElementById("btn-salvar-visita");
  botao.disabled = salvando || !usuario || !codigoSelecionado;
  botao.textContent = salvando ? "Salvando…" : (idEmEdicao ? "Atualizar viagem" : "Salvar viagem");
  document.getElementById("titulo-form-visita").textContent = idEmEdicao ? "Editar viagem" : "Registrar viagem";
  document.getElementById("btn-cancelar-edicao").hidden = !idEmEdicao;
  document.getElementById("aviso-visita").textContent = usuario
    ? "Preencha a data de início e os dados que deseja guardar."
    : "Entre na sua conta para salvar uma viagem.";
}

function selecionarPais(codigo) {
  if (salvando) {
    return;
  }
  const pais = paises.find(item => item.codigo_mapa === codigo);
  codigoSelecionado = pais?.codigo_mapa || "";
  idEmEdicao = null;
  formularioVisita.reset();
  formularioVisita.elements.codigo_mapa.value = codigoSelecionado;
  seletorPais.value = codigoSelecionado;
  document.getElementById("nome-pais").textContent = pais?.nome || "Selecione uma localidade";
  document.getElementById("capital-pais").textContent = pais?.capital || "—";
  atualizarMapa();
  atualizarBotaoVisita();
  exibirViagens(document.getElementById("lista-visitas"), visitas.filter(visita => visita.codigo_mapa === codigoSelecionado));
}

function editarViagem(visita) {
  if (!formularioVisita) {
    window.location.assign(endereco("index.html?visita=" + visita.id_visita));
    return;
  }
  if (salvando) {
    return;
  }
  selecionarPais(visita.codigo_mapa);
  idEmEdicao = visita.id_visita;
  for (const elemento of formularioVisita.elements) {
    if (elemento.name && Object.hasOwn(visita, elemento.name)) {
      elemento.value = visita[elemento.name] ?? "";
    }
  }
  atualizarBotaoVisita();
  formularioVisita.querySelector("details").open = true;
  formularioVisita.scrollIntoView({ behavior: "smooth", block: "start" });
  formularioVisita.elements.data_inicio.focus({ preventScroll: true });
}

function exibirViagens(lista, registros) {
  if (!lista) {
    return;
  }
  lista.replaceChildren();
  if (registros.length === 0) {
    const item = document.createElement("li");
    item.textContent = usuario ? "Nenhuma viagem registrada." : "Entre na sua conta para consultar suas viagens.";
    lista.append(item);
    return;
  }

  const campos = {
    cidade_principal: "Cidade", motivo_viagem: "Motivo", meio_transporte: "Transporte",
    avaliacao: "Avaliação", custo_estimado: "Custo estimado", moeda: "Moeda", observacao: "Observação"
  };
  for (const visita of registros) {
    const item = document.createElement("li");
    item.className = "viagem";
    const titulo = document.createElement("strong");
    titulo.textContent = visita.nome_pais + " • " + formatarData(visita.data_inicio);
    item.append(titulo);
    if (visita.data_fim) {
      const fim = document.createElement("p");
      fim.textContent = "Até " + formatarData(visita.data_fim);
      item.append(fim);
    }
    for (const [campo, rotulo] of Object.entries(campos)) {
      if (visita[campo] !== null && visita[campo] !== "") {
        const linha = document.createElement("p");
        linha.textContent = rotulo + ": " + visita[campo];
        item.append(linha);
      }
    }
    const editar = document.createElement("button");
    editar.type = "button";
    editar.className = "botao secundario";
    editar.textContent = "Editar viagem";
    editar.setAttribute("aria-label", "Editar viagem para " + visita.nome_pais + " de " + formatarData(visita.data_inicio));
    editar.addEventListener("click", () => editarViagem(visita));
    item.append(editar);
    lista.append(item);
  }
}

function atualizarPerfil() {
  const campos = {
    "conta-nome": usuario?.nome,
    "conta-usuario": usuario?.nome_usuario,
    "conta-email": usuario?.email,
    "conta-biografia": usuario?.biografia || (usuario ? "Sem biografia cadastrada." : null),
    "conta-data-cadastro": usuario ? formatarData(usuario.data_cadastro) : null
  };
  for (const [id, valor] of Object.entries(campos)) {
    const elemento = document.getElementById(id);
    if (elemento) {
      elemento.textContent = valor || "—";
    }
  }
  const aviso = document.getElementById("conta-sem-sessao");
  const sair = document.getElementById("btn-sair");
  if (aviso) aviso.hidden = Boolean(usuario);
  if (sair) sair.hidden = !usuario;
  for (const link of document.querySelectorAll("[data-publico]")) {
    link.hidden = Boolean(usuario);
  }
}

function atualizarListas() {
  const doPais = visitas.filter(visita => visita.codigo_mapa === codigoSelecionado);
  exibirViagens(document.getElementById("lista-visitas"), doPais);
  exibirViagens(document.getElementById("lista-viagens-conta"), visitas);
  atualizarMapa();
  atualizarPerfil();
  atualizarBotaoVisita();
}

async function carregarSessao() {
  usuario = null;
  visitas = [];
  try {
    usuario = await consultarAPI("api/conta");
    visitas = await consultarAPI("api/visitas");
  } catch (erro) {
    if (erro.status === 401) {
      usuario = null;
    } else {
      throw erro;
    }
  } finally {
    atualizarListas();
  }
}

function prepararFormularioConta(id, rota, proximaPagina) {
  const formulario = document.getElementById(id);
  if (!formulario) {
    return;
  }
  const botao = formulario.querySelector("button[type=submit]");
  botao.disabled = false;
  formulario.addEventListener("submit", async evento => {
    evento.preventDefault();
    if (botao.disabled) return;
    botao.disabled = true;
    mostrarMensagem("Enviando…");
    try {
      await consultarAPI(rota, "POST", Object.fromEntries(new FormData(formulario)));
      window.location.assign(endereco(proximaPagina));
    } catch (erro) {
      mostrarMensagem(erro.message, "erro");
    } finally {
      botao.disabled = false;
    }
  });
}

async function salvarViagem(evento) {
  evento.preventDefault();
  if (salvando || !usuario || !codigoSelecionado) {
    return;
  }
  const dados = Object.fromEntries(new FormData(formularioVisita));
  if (dados.data_fim && dados.data_fim < dados.data_inicio) {
    mostrarMensagem("A data de fim deve ser igual ou posterior à de início.", "erro");
    return;
  }
  const editando = idEmEdicao !== null;
  const rota = editando ? "api/visitas/" + idEmEdicao : "api/visitas";
  salvando = true;
  for (const elemento of formularioVisita.elements) elemento.disabled = true;
  seletorPais.disabled = true;
  atualizarBotaoVisita();
  try {
    await consultarAPI(rota, editando ? "PUT" : "POST", dados);
    formularioVisita.reset();
    formularioVisita.elements.codigo_mapa.value = codigoSelecionado;
    idEmEdicao = null;
    try {
      visitas = await consultarAPI("api/visitas");
      mostrarMensagem(editando ? "Viagem atualizada." : "Viagem registrada.");
    } catch {
      mostrarMensagem("A viagem foi salva. Recarregue a página para atualizar o mapa e o histórico.", "erro");
    }
    atualizarListas();
  } catch (erro) {
    if (erro.status === 401) {
      usuario = null;
      visitas = [];
      atualizarListas();
    }
    mostrarMensagem(erro.message, "erro");
  } finally {
    salvando = false;
    for (const elemento of formularioVisita.elements) elemento.disabled = false;
    seletorPais.disabled = false;
    atualizarBotaoVisita();
  }
}

async function iniciar() {
  prepararFormularioConta("form-login", "api/login", "index.html");
 prepararFormularioConta(
  "form-cadastro",
  "api/usuarios",
  "frontend/pages/entrar.html?cadastro=ok"
);

  const sair = document.getElementById("btn-sair");
  sair?.addEventListener("click", async () => {
    sair.disabled = true;
    try {
      await consultarAPI("api/logout", "POST", {});
      usuario = null;
      visitas = [];
      atualizarListas();
      window.location.assign(endereco("index.html"));
    } catch (erro) {
      mostrarMensagem(erro.message, "erro");
    } finally {
      sair.disabled = false;
    }
  });

  if (formularioVisita) {
    formularioVisita.addEventListener("submit", salvarViagem);
    seletorPais.addEventListener("change", () => selecionarPais(seletorPais.value));
    document.getElementById("btn-cancelar-edicao").addEventListener("click", () => selecionarPais(codigoSelecionado));
    paises = await consultarAPI("api/paises");
  }
  await carregarSessao();
  const parametros = new URLSearchParams(window.location.search);
  if (parametros.get("cadastro") === "ok") {
    mostrarMensagem("Conta criada. Entre com seu nome de usuário e senha.");
  }
  if (formularioVisita && parametros.has("visita")) {
    const visita = visitas.find(item => item.id_visita === Number(parametros.get("visita")));
    if (visita) editarViagem(visita);
    else mostrarMensagem("Entre na conta que registrou essa viagem para editá-la.", "erro");
  }
}


window.addEventListener("pageshow", evento => {
  if (evento.persisted) {
    carregarSessao().catch(erro => mostrarMensagem(erro.message, "erro"));
  }
});

iniciar().catch(erro => mostrarMensagem(erro.message, "erro"));
