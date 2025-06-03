const form = document.getElementById("downloadForm");
const historyCard = document.getElementById("historyCard");
const historyList = document.getElementById("historyList");
const pagination = document.getElementById("pagination");

async function getYouTubeTitle(url) {
  try {
    const videoId = new URL(url).searchParams.get("v");
    if (!videoId) return "Título indisponível";

    const res = await fetch(
      `https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=${videoId}&format=json`,
    );
    if (!res.ok) throw new Error("Não foi possível obter o título.");
    const data = await res.json();
    return data.title;
  } catch {
    return "Título indisponível";
  }
}

function truncate(str, max = 200) {
  return str.length > max ? str.slice(0, max) + "..." : str;
}

function loadHistory() {
  let history = JSON.parse(localStorage.getItem("downloadHistory")) || [];

  if (history.length === 0) {
    historyCard.style.display = "none";
    return;
  }

  // Remover duplicatas, mantendo a entrada mais recente
  const uniqueHistory = Object.values(
    history.reduce((acc, item) => {
      if (
        !acc[item.url] ||
        new Date(item.date) > new Date(acc[item.url].date)
      ) {
        acc[item.url] = item;
      }
      return acc;
    }, {}),
  );

  historyCard.style.display = "block";
  const itemsPerPage = 10;
  let currentPage = 1;

  function renderPage(page) {
    const start = (page - 1) * itemsPerPage;
    const end = start + itemsPerPage;
    const items = uniqueHistory.slice().reverse().slice(start, end);

    historyList.innerHTML = items
      .map(
        (item) => `
          <div class="history-item">
            <div class="history-title" title="${item.name}">
              ${truncate(item.name)}
            </div>
            <div class="history-meta">
              <span>${item.date}</span>
              <a href="${item.url}" target="_blank">Abrir link</a>
            </div>
          </div>
        `,
      )
      .join("");

    renderPagination(page);
  }

  function renderPagination(current) {
    const totalPages = Math.ceil(uniqueHistory.length / itemsPerPage);
    pagination.innerHTML = "";
    for (let i = 1; i <= totalPages; i++) {
      const btn = document.createElement("button");
      btn.textContent = i;
      btn.className = i === current ? "active" : "";
      btn.onclick = () => renderPage(i);
      pagination.appendChild(btn);
    }
  }

  renderPage(currentPage);
}

form.addEventListener("submit", async (e) => {
  e.preventDefault();
  document.getElementById("overlay").style.display = "flex";

  const url = document.getElementById("url").value;
  const type = document.getElementById("download_type").value;
  const history = JSON.parse(localStorage.getItem("downloadHistory")) || [];
  const now = new Date();

  const title = await getYouTubeTitle(url);

  const entry = {
    name: title,
    url,
    type,
    date: now.toLocaleString(),
  };

  history.push(entry);
  localStorage.setItem("downloadHistory", JSON.stringify(history));

  form.submit();
});

loadHistory();
