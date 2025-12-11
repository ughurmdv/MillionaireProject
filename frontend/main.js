// =============================================================
//  Millionaire Game - Clean Frontend Logic
// =============================================================

console.log("MAIN.JS LOADED");

const API_BASE = "http://127.0.0.1:8000";

// -------------------------------------------------------------
// Helper utils
// -------------------------------------------------------------

function playSound(id) {
    const el = document.getElementById(id);
    if (!el) return;
    el.currentTime = 0;
    el.play().catch(() => {});
}

function showOverlay(title, html, onClose) {
    const old = document.getElementById("game-overlay");
    if (old) old.remove();

    const overlay = document.createElement("div");
    overlay.id = "game-overlay";
    overlay.style.position = "fixed";
    overlay.style.inset = "0";
    overlay.style.background = "rgba(0,0,0,0.7)";
    overlay.style.display = "flex";
    overlay.style.alignItems = "center";
    overlay.style.justifyContent = "center";
    overlay.style.zIndex = "9999";

    const box = document.createElement("div");
    box.style.background = "linear-gradient(145deg,#070726,#10104a)";
    box.style.borderRadius = "18px";
    box.style.border = "2px solid #f7b500";
    box.style.padding = "24px 30px 26px";
    box.style.minWidth = "320px";
    box.style.maxWidth = "480px";
    box.style.textAlign = "center";
    box.style.color = "#f5f5ff";
    box.style.boxShadow = "0 0 30px rgba(0,0,0,0.8)";

    const h = document.createElement("h3");
    h.textContent = title;
    h.style.marginTop = "0";
    h.style.marginBottom = "12px";
    h.style.color = "#ffdf6b";

    const p = document.createElement("div");
    p.innerHTML = html;
    p.style.fontSize = "15px";
    p.style.lineHeight = "1.5";

    const btn = document.createElement("button");
    btn.textContent = "OK";
    btn.type = "button";
    btn.style.marginTop = "20px";
    btn.style.padding = "8px 26px";
    btn.style.border = "2px solid #f7b500";
    btn.style.borderRadius = "999px";
    btn.style.background = "#182072";
    btn.style.color = "#ffffff";
    btn.style.fontWeight = "600";
    btn.style.cursor = "pointer";
    btn.style.fontSize = "15px";

    btn.onclick = () => {
        overlay.remove();
        if (onClose) onClose();
    };

    box.appendChild(h);
    box.appendChild(p);
    box.appendChild(btn);
    overlay.appendChild(box);
    document.body.appendChild(overlay);
}

function logout() {
    localStorage.removeItem("player");
    window.location = "index.html";
}
window.logout = logout;

// -------------------------------------------------------------
// Auth
// -------------------------------------------------------------

function signup() {
    const u = document.getElementById("signup-username");
    const p = document.getElementById("signup-password");
    if (!u || !p) return;

    const username = u.value.trim();
    const password = p.value.trim();
    if (!username || !password) {
        alert("Please enter username and password");
        return;
    }

    fetch(API_BASE + "/signup", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, password })
    })
        .then(r => r.json().then(d => ({ ok: r.ok, d })))
        .then(({ ok, d }) => {
            if (!ok) {
                alert(d.detail || "Signup failed");
            } else {
                alert("Signup successful. You can log in now.");
                window.location = "login.html";
            }
        })
        .catch(err => {
            console.error("Signup error:", err);
            alert("Signup failed (see console).");
        });
}

function login() {
    const u = document.getElementById("login-username");
    const p = document.getElementById("login-password");
    if (!u || !p) return;

    const username = u.value.trim();
    const password = p.value.trim();
    if (!username || !password) {
        alert("Please enter username and password");
        return;
    }

    fetch(API_BASE + "/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, password })
    })
        .then(r => r.json().then(d => ({ ok: r.ok, d })))
        .then(({ ok, d }) => {
            if (!ok || !d.username) {
                alert(d.detail || "Login failed");
            } else {
                localStorage.setItem("player", d.username);
                window.location = "home.html";
            }
        })
        .catch(err => {
            console.error("Login error:", err);
            alert("Login failed (see console).");
        });
}

window.signup = signup;
window.login = login;

// -------------------------------------------------------------
// Game state
// -------------------------------------------------------------

const MONEY_LADDER = [
    100, 200, 300, 500,
    1000, 2000, 4000, 8000,
    16000, 32000, 64000, 1000000
];
const QUESTION_TIME = 30;

const gameState = {
    status: "idle",   // idle | playing | finished
    questions: [],
    index: 0,
    earned: 0,
    timeLeft: QUESTION_TIME,
    timerId: null,
    used: {
        audience: false,
        phone: false,
        fifty: false,
        change: false
    },
    finishedOnce: false
};

// -------------------------------------------------------------
// Page init
// -------------------------------------------------------------

document.addEventListener("DOMContentLoaded", () => {
    // Home page
    const homeName = document.getElementById("home-player-name");
    if (homeName) {
        const p = localStorage.getItem("player");
        if (!p) {
            window.location = "login.html";
            return;
        }
        homeName.textContent = p;

        const startBtn = document.getElementById("start-btn");
        if (startBtn) startBtn.onclick = () => window.location = "game.html";

        const lbBtn = document.getElementById("home-leaderboard-btn");
        if (lbBtn) lbBtn.onclick = () => window.location = "leaderboard.html";
    }

    // Game page
    if (document.getElementById("question-text")) {
        initGamePage();
    }

    // Leaderboard page
    if (document.getElementById("leaderboard-list")) {
        loadLeaderboard();
    }
});

// -------------------------------------------------------------
// Game init
// -------------------------------------------------------------

function initGamePage() {
    const player = localStorage.getItem("player");
    if (!player) {
        alert("You must login first.");
        window.location = "login.html";
        return;
    }
    const nameEl = document.getElementById("player-name");
    if (nameEl) nameEl.textContent = player;

    drawLadder();
    resetGameState();
    fetchQuestionsAndStart();

    const bAud = document.getElementById("btn-audience");
    if (bAud) bAud.onclick = lifelineAudience;

    const bPhone = document.getElementById("btn-phone");
    if (bPhone) bPhone.onclick = lifelinePhone;

    const b50 = document.getElementById("btn-5050");
    if (b50) b50.onclick = lifeline5050;

    const bChange = document.getElementById("btn-change");
    if (bChange) bChange.onclick = lifelineChange;
}

function resetGameState() {
    gameState.status = "idle";
    gameState.questions = [];
    gameState.index = 0;
    gameState.earned = 0;
    gameState.timeLeft = QUESTION_TIME;
    gameState.finishedOnce = false;
    gameState.used = { audience: false, phone: false, fifty: false, change: false };
    if (gameState.timerId) {
        clearInterval(gameState.timerId);
        gameState.timerId = null;
    }
    const winEl = document.getElementById("current-earnings");
    if (winEl) winEl.textContent = "0";

    ["btn-audience","btn-phone","btn-5050","btn-change"].forEach(id => {
        const el = document.getElementById(id);
        if (el) {
            el.disabled = false;
            el.classList.remove("used");
        }
    });
}

function fetchQuestionsAndStart() {
    fetch(API_BASE + "/questions")
        .then(r => r.json())
        .then(qs => {
            gameState.questions = qs || [];
            if (!gameState.questions.length) {
                alert("No questions from server.");
                return;
            }
            gameState.status = "playing";
            gameState.index = 0;
            showQuestion();
        })
        .catch(err => {
            console.error("Question fetch error:", err);
            alert("Could not load questions.");
        });
}

// -------------------------------------------------------------
// Show question
// -------------------------------------------------------------

function showQuestion() {
    if (gameState.status !== "playing") return;

    const q = gameState.questions[gameState.index];
    if (!q) {
        finishGame("You answered all questions!");
        return;
    }

    const qText = document.getElementById("question-text");
    const grid = document.getElementById("answers-grid");
    if (!qText || !grid) return;

    qText.textContent = q.q;
    grid.innerHTML = "";

    q.a.forEach(ans => {
        const div = document.createElement("div");
        div.className = "answer";
        div.textContent = ans;
        div.onclick = () => onAnswerClick(div, ans);
        grid.appendChild(div);
    });

    highlightLadder();
    startTimer();
}

// -------------------------------------------------------------
// Answer handling
// -------------------------------------------------------------

function onAnswerClick(el, selected) {
    if (gameState.status !== "playing") return;

    stopTimer();
    playSound("sound-select");

    const q = gameState.questions[gameState.index];
    const all = document.querySelectorAll(".answer");

    // Disable all answers instantly
    all.forEach(a => (a.onclick = null));

    // Mark selected answer for suspense
    el.classList.add("selected");

    // Wait 2 seconds before revealing truth
    setTimeout(() => {

        el.classList.remove("selected");  // remove suspense highlight

        // ----------------------------
        // CASE 1 – CORRECT ANSWER
        // ----------------------------
        if (selected === q.correct) {
            el.classList.add("correct");
            playSound("sound-correct");

            gameState.earned = MONEY_LADDER[gameState.index];
            const wEl = document.getElementById("current-earnings");
            if (wEl) wEl.textContent = String(gameState.earned);

            // Last question
            if (gameState.index === gameState.questions.length - 1) {
                gameState.status = "finished";
                setTimeout(() => {
                    finishGame("🎉 Congratulations! You reached 1,000,000 $!");
                }, 1500);
                return;
            }

            // Next question
            setTimeout(() => {
                if (gameState.status !== "playing") return;
                gameState.index++;
                showQuestion();
            }, 1500);
        }

        // ----------------------------
        // CASE 2 – WRONG ANSWER
        // ----------------------------
        else {
            el.classList.add("wrong");
            playSound("sound-wrong");

            // reveal correct one
            all.forEach(a => {
                if (a.textContent === q.correct) a.classList.add("correct");
            });

            gameState.status = "finished";

            const msg = `
                ❌ Wrong answer!<br><br>
                Correct answer was: <strong>${q.correct}</strong><br>
                You leave with: <strong>$${gameState.earned.toLocaleString()}</strong>
            `;

            setTimeout(() => finishGame(msg), 2000);
        }

    }, 2000); // <-- 2-second suspense delay before revealing correct/wrong
}

function stopSound(id) {
    const el = document.getElementById(id);
    if (!el) return;
    el.pause();
    el.currentTime = 0;
}

// -------------------------------------------------------------
// Timer
// -------------------------------------------------------------

function startTimer() {
    stopTimer();
    gameState.timeLeft = QUESTION_TIME;
    updateTimerUI();

    gameState.timerId = setInterval(() => {
        if (gameState.status !== "playing") {
            stopTimer();
            return;
        }
        gameState.timeLeft -= 1;
        if (gameState.timeLeft < 0) gameState.timeLeft = 0;
        updateTimerUI();

        if (gameState.timeLeft <= 0) {
            stopTimer();
            gameState.status = "finished";
            playSound("sound-timesup");
            finishGame("⏳ Time is up!");
        } else if (gameState.timeLeft <= 10) {
            playSound("sound-tick");
        }
    }, 1000);
}

function stopTimer() {
    if (gameState.timerId) {
        clearInterval(gameState.timerId);
        gameState.timerId = null;
    }
}

function updateTimerUI() {
    const t = document.getElementById("timer");
    if (t) t.textContent = String(gameState.timeLeft);
}

// -------------------------------------------------------------
// Lifelines (jokers) – with fade
// -------------------------------------------------------------

function markLifelineUsed(id) {
    const el = document.getElementById(id);
    if (el) {
        el.disabled = true;
        el.classList.add("used"); // CSS will fade it
    }
}

function lifelineAudience() {
    if (gameState.status !== "playing" || gameState.used.audience) return;
    gameState.used.audience = true;
    markLifelineUsed("btn-audience");

    const q = gameState.questions[gameState.index];
    showOverlay("📊 Audience Poll", `Audience majority votes for:<br><strong>${q.correct}</strong>`);
}

function lifelinePhone() {
    if (gameState.status !== "playing" || gameState.used.phone) return;
    gameState.used.phone = true;
    markLifelineUsed("btn-phone");

    const q = gameState.questions[gameState.index];
    showOverlay("📞 Phone a Friend", `Your friend thinks the answer is:<br><strong>${q.correct}</strong>`);
}

function lifeline5050() {
    if (gameState.status !== "playing" || gameState.used.fifty) return;
    gameState.used.fifty = true;
    markLifelineUsed("btn-5050");

    const q = gameState.questions[gameState.index];
    const wrong = q.a.filter(a => a !== q.correct);
    const toHide = wrong.slice(0, 2);

    document.querySelectorAll(".answer").forEach(a => {
        if (toHide.includes(a.textContent)) a.style.visibility = "hidden";
    });
}

function lifelineChange() {
    if (gameState.status !== "playing" || gameState.used.change) return;
    if (gameState.index < 7) {
        showOverlay("Unavailable", "You can use 'Change Question' only from question 8 onwards.");
        return;
    }
    gameState.used.change = true;
    markLifelineUsed("btn-change");

    const q = gameState.questions[gameState.index];
    const difficulty = q.difficulty || "medium";

    fetch(`${API_BASE}/question_new/${difficulty}`)
        .then(r => r.json())
        .then(newQ => {
            gameState.questions[gameState.index] = newQ;
            showQuestion();
        })
        .catch(err => {
            console.error("Change question error:", err);
            showOverlay("Error", "Could not change question.");
        });
}

// -------------------------------------------------------------
// Ladder
// -------------------------------------------------------------

function drawLadder() {
    const ladder = document.getElementById("ladder");
    if (!ladder) return;

    ladder.innerHTML = "";
    for (let i = MONEY_LADDER.length - 1; i >= 0; i--) {
        const row = document.createElement("div");
        row.className = "ladder-row";
        row.dataset.index = i;
        row.innerHTML = `<span>${i + 1}</span><span>${MONEY_LADDER[i].toLocaleString()} $</span>`;
        ladder.appendChild(row);
    }
}

function highlightLadder() {
    const rows = document.querySelectorAll(".ladder-row");
    rows.forEach(r => r.classList.remove("current"));
    const idxFromTop = MONEY_LADDER.length - 1 - gameState.index;
    if (rows[idxFromTop]) rows[idxFromTop].classList.add("current");
}

// -------------------------------------------------------------
// Finish game
// -------------------------------------------------------------

function finishGame(reasonHtml) {
    if (gameState.finishedOnce) return;
    gameState.finishedOnce = true;
    stopTimer();

    const player = localStorage.getItem("player");
    const finalEarned = gameState.earned;

    const showEnd = () => {
        showOverlay(
            "Game Over",
            `${reasonHtml}<br><br>You earned: <strong>$${finalEarned.toLocaleString()}</strong>`,
            () => { window.location = "home.html"; }
        );
    };

    if (!player) {
        showEnd();
        return;
    }

    fetch(API_BASE + "/score", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username: player, earned: finalEarned })
    })
        .catch(err => console.error("Score save error:", err))
        .finally(showEnd);
}

// -------------------------------------------------------------
// Leaderboard
// -------------------------------------------------------------

function loadLeaderboard() {
    fetch(API_BASE + "/leaderboard")
        .then(r => r.json())
        .then(users => {
            const list = document.getElementById("leaderboard-list");
            if (!list) return;

            if (!users.length) {
                list.innerHTML = "<p>No players yet.</p>";
                return;
            }

            list.innerHTML = "";
            users.forEach((u, idx) => {
                const div = document.createElement("div");
                div.className = "leaderboard-item";
                div.innerHTML = `<span>#${idx + 1} ${u.username}</span><span>$${u.total_money}</span>`;
                list.appendChild(div);
            });
        })
        .catch(err => {
            console.error("Leaderboard error:", err);
            const list = document.getElementById("leaderboard-list");
            if (list) list.innerHTML = "<p>Error loading leaderboard.</p>";
        });
}
